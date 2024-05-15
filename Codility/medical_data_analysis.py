# Check if variable is potentially a cause of death
# Treat int64 as categorial, perform chi-squared
# For numerical, shapiro-Wilk

# Round all p_values to 4 decimal places
import pandas as pd
from pandas.api.types import is_numeric_dtype
from scipy import stats


def _append_test_result(test_result_list: list, feature: str, p_value: float):
    test_result_list.append((feature, round(p_value, 4)))  # Updated in dict due to pass-by-reference


def perform_tests(data: pd.DataFrame) -> dict:
    features = data.columns
    features = [name for name in features if name != 'death']
    data_target = data['death']
    test_results = {'mann_whitney': list(), 'ttest': list(), 'chi_square': list(), 'shapiro_wilk': list()}

    for feature in features:
        data_feature = data[feature]
        if data_feature.dtype.name in ['int64', 'category', 'object']:
            if pd.Categorical(data_feature).dtype.name != ['int64']:
                data_feature = data_feature.astype('int64')

            contingency_table = pd.crosstab(data_feature, data['death'])
            p_value = stats.chi2_contingency(contingency_table)[1]
            _append_test_result(test_results['chi_square'], feature=feature, p_value=p_value)

        elif is_numeric_dtype(data_feature):
            feature_pos = data_feature[data_target == 0]
            feature_neg = data_feature[data_target == 1]
            # Index into the second tuple entry to get p-value and threshold
            shapiro_p_val_pos = stats.shapiro(feature_pos)[1]
            shapiro_p_val_neg = stats.shapiro(feature_neg)[1]
            shapiro_worst_p_value = min(shapiro_p_val_pos, shapiro_p_val_neg)
            # Get the worst of two p_values
            test_results['shapiro_wilk'].append((feature, (round(shapiro_p_val_pos, 4), round(shapiro_p_val_neg, 4))))

            if shapiro_worst_p_value > 0.05:
                # Both normal
                p_value = stats.ttest_ind(feature_pos, feature_neg, equal_var=False)[1]
                _append_test_result(test_results['ttest'], feature=feature, p_value=p_value)
            else:
                # Both non-normal
                p_value = stats.mannwhitneyu(feature_pos, feature_neg)[1]
                _append_test_result(test_results['mann_whitney'], feature=feature, p_value=p_value)
        else:
            raise NotImplementedError(f'The datatype {data[feature].dtype} is not '
                                      f'supported at this time. ')

    return test_results


try:
    test_file_path = r"D:\data\ML\medical_data\medical_data.csv"
    data = pd.read_csv(test_file_path)

    print(data.dtypes)
    # All columns are either int64 (categorical) or float64 (numeric). Still, attempt to handle other datatypes and
    # adapt code as they come up
    example_data = data[["death", "Na+", "DBP", "PLT", "ivabradine", "MRA"]]
    example_data.head()
    # Confirmed looks like example

    example_results = perform_tests(example_data)
    print(example_results)

    # Check correct test types performed
    test_type = 'mann_whitney'
    test_features = [name[0] for name in example_results[test_type]]
    assert test_features.sort() == ['Na+'].sort()

    test_type = 'ttest'
    test_features = [name[0] for name in example_results[test_type]]
    assert test_features.sort() == ['DBP', 'PLT'].sort()

    test_type = 'chi_square'
    test_features = [name[0] for name in example_results[test_type]]
    assert test_features.sort() == ['ivabradine', 'MRA'].sort()

    test_type = 'shapiro_wilk'
    test_features = [name[0] for name in example_results[test_type]]
    assert test_features.sort() == ['Na+', 'DBP', 'PLT', ].sort()

    # Check correct p-values obtained
    test_type = 'mann_whitney'
    assert sorted(example_results[test_type], key=lambda x: x[0]) == sorted([('Na+', 0.2143)], key=lambda x: x[
        0]), f'{test_type} yields wrong p-value'

    test_type = 'ttest'
    assert sorted(example_results[test_type], key=lambda x: x[0]) == sorted([('DBP', 0.0), ('PLT', 0.4739)],
                                                                            key=lambda x: x[
                                                                                0]), f'{test_type} yields wrong p-value'

    test_type = 'chi_square'
    assert sorted(example_results[test_type], key=lambda x: x[0]) == sorted([('ivabradine', 0.0144), ('MRA', 0.2884)],
                                                                            key=lambda x: x[
                                                                                0]), f'{test_type} yields wrong p-value'

    test_type = 'shapiro_wilk'
    assert sorted(example_results[test_type], key=lambda x: x[0]) == sorted(
        [('Na+', (0.0, 0.0071)), ('PLT', (0.2361, 0.6935)),
         ('DBP', (0.5272, 0.3715))], key=lambda x: x[0]), f'{test_type} yields wrong p-value'
except Exception:
    raise OSError('Local data not found.')


data_results = perform_tests(data)
print(data_results)
