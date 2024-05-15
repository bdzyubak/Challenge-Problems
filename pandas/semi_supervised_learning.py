import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import datasets
import seaborn as sns
import matplotlib.pyplot as plt

# This is a numpy array, not pandas dataset. df['data'] contains 178 examples by 13 features
# df['target'] contains 178 lables in range(0,3) corresponding to wine names. Which are actually just class_n
df_orig = datasets.load_wine()
X = df_orig['data']
y = df_orig['target']

class_names = df_orig['target_names']

# Split includes random shuffle made reproducible by setting the state
X_train_labeled, X_test, y_train_labeled, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1)
# Split train data in labeled and (simulated) unlabeled
X_train_labeled, X_unl, y_train_labeled, y_unl = train_test_split(
    X_train_labeled, y_train_labeled, test_size=0.7, random_state=1)

print(f"The split is: {X_train_labeled.shape} labeled training cases, {X_unl.shape} unlabeled training cases, and "
      f"{X_test.shape} test cases.")

clf = svm.SVC(kernel='linear', probability=True, C=1).fit(X_train_labeled, y_train_labeled)
print(f"The prediction score on labeled data is {round(clf.score(X_test, y_test), 2)}")

X_unl_pred_prob = clf.predict_proba(X_unl)
X_unl_pred_class = clf.predict(X_unl)

df = pd.DataFrame(X_unl_pred_prob, columns=class_names)
for class_ind, column in enumerate(class_names):
    df['pred' + column] = X_unl_pred_prob[:, class_ind]

df['pred_max_prob'] = df[class_names].max(axis=1)  # Prediction confidence
# plt.figure()
# plt.rcParams.update({'font.size': 22})  # must set in top
# figManager = plt.get_current_fig_manager()
# figManager.window.showMaximized()
# df['pred_max_prob'].plot.hist()
df['pred_class'] = X_unl_pred_class

# Which cutoff to use is a hyperparamter. Optimize a value once in a train set, and use as default for similar data
conf_cutoffs = [round(cutoff, 2) for cutoff in np.arange(0.45, 1, 0.05)]

iterations = 5
acc_test_ignore = round(clf.score(X_test, y_test), 3)

print(f"The prediction on test cases without using semi-supervised learning is: {acc_test_ignore}")
iteration_names = [f"Iter_{name}_acc" for name in range(1, iterations + 1)]
df_test_results = pd.DataFrame(index=conf_cutoffs, columns=iteration_names)

for cutoff in conf_cutoffs:
    acc = list()
    X_train_labeled_iter = X_train_labeled.copy()
    y_train_labeled_iter = y_train_labeled.copy()
    X_train_unlabeled_iter = X_unl.copy()
    y_train_unlabeled_iter = y_unl.copy()
    X_unl_pred_prob_iter = X_unl_pred_prob.copy()
    for iter_name in iteration_names:
        # print(f'Iteration {labeling_iter}: cutoff {cutoff}')
        # conf_ind = df["pred_max_prob"] > cutoff
        conf_ind = np.max(X_unl_pred_prob_iter, axis=1) > cutoff
        # TODO: iteratively add only new examples above threshold
        X_train_labeled_iter = np.append(X_train_labeled_iter, X_train_unlabeled_iter[conf_ind, :], axis=0)
        y_train_labeled_iter = np.append(y_train_labeled_iter, y_train_unlabeled_iter[conf_ind])
        X_train_unlabeled_iter = X_train_unlabeled_iter[~conf_ind, :]
        y_train_unlabeled_iter = y_train_unlabeled_iter[~conf_ind]

        print(f"{iter_name} with cutoff {cutoff}. Train cases:  "
              f"{X_train_labeled_iter.shape[0]}, including {X_train_labeled_iter.shape[0] - X_train_labeled.shape[0]}"
              f" model-labeled cases. There are {X_train_unlabeled_iter.shape[0]} more unlabeled cases.")
        if X_train_unlabeled_iter.shape[0] == 0:
            break

        clf = svm.SVC(kernel='linear', probability=True).fit(X_train_labeled_iter, y_train_labeled_iter)
        acc_iter = round(clf.score(X_test, y_test), 5)
        print(f"The accuracy for this iteration is {acc_iter}")
        acc.append(acc_iter)
        X_unl_pred_prob_iter = clf.predict_proba(X_train_unlabeled_iter)

    if not acc:
        acc = [0] * iterations
    if len(acc) < iterations:
        acc += [acc[-1]] * (iterations - len(acc))
    df_test_results.loc[[cutoff]] = acc

# series_no_relabel = pd.Series([acc_test_ignore] * df_test_results.shape[1], name='no_relabel')
df_test_results.loc[['no_relabel']] = [acc_test_ignore] * iterations
    # acc['no_relabel'] = acc_test_ignore
# df_test_results.loc[len(df_test_results)] = acc_test_ignore

plt.hist(acc)
