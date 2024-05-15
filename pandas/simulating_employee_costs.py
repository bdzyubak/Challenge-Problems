import numpy as np
import pandas as pd
import seaborn as sns


pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

number_of_work_hours_per_year = 2080
match_401k = 0.03
bonus = 0.075
stock = 0.075
soc_sec_tax = 0.062
medicare = 0.0145

overhead_rate_total = match_401k + bonus + stock + soc_sec_tax + medicare
print(f"The overhead percentage is {overhead_rate_total}, see flat below")  # 25%
# The overhead percentage is 0.2565, see flat below

health_insurance = 2500 * 12  # 30000
federal_ui = 420
state_ui = 427
worker_comp = 420
short_long_term_disability_insurance = 400 * 12  # 5000
life_insurance = 400

overhead_flat_total = (
        health_insurance + federal_ui + state_ui + worker_comp + short_long_term_disability_insurance +
        life_insurance)
print(f"The overhead flat amount is {overhead_flat_total}")
# The overhead flat amount is 36467


def main():
    salary_range = np.array([170, 180, 190, 200]) * 1000  # Range for Senior AI engineer with my skillset/experience

    employer_cost_range = get_employer_cost(salary_range=salary_range)
    print(employer_cost_range)
    print(f"Total overhead in $: {(employer_cost_range - salary_range)}")
    # Total overhead in $: [80072 82637 85202 87767]
    print(f"Total overhead in percent: {((employer_cost_range - salary_range) / salary_range * 100).astype(int)}")
    # Total overhead in percent: [47 45 44 43]

    fte_range = np.array([0.5, 0.6, 0.7, 0.8, 0.9, 1])
    annual_income = salary_range[1]
    rows_list = list()
    for fte in fte_range:
        employee_income_fte = int(annual_income * fte)
        employer_cost_fte = get_employer_cost(salary_range=annual_income * fte)
        employer_overhead_percent = int(round((employer_cost_fte - employee_income_fte) / employer_cost_fte * 100))
        hourly_amount = round(employer_cost_fte / (number_of_work_hours_per_year * fte), 1)
        row = {'FTE': fte, 'Employee Gross Income': employee_income_fte, 'Employer Cost': employer_cost_fte,
               'Hourly Amount': hourly_amount,
               'Employer Inefficiency (%)': employer_overhead_percent}
        # row = {'FTE': fte, 'Employee Gross Income': employee_income_fte,
        #        'Hourly Amount': hourly_amount}
        rows_list.append(row)

    salary_fte = pd.DataFrame(rows_list, columns=list(rows_list[0].keys()))

    wages_comp_list = np.interp(np.append(fte_range, 0.1), [0.5, 1], [190, 140])[:-1]
    salary_fte['Hourly Amount Comp'] = wages_comp_list
    salary_fte['Employer Annual Cost Comp'] = get_employer_annual_from_wage(fte_range, wages_comp_list)
    salary_fte['Employee Gross Income Comp'] = get_employee_amount(fte_range=fte_range, wage_range=wages_comp_list)
    print(salary_fte)

    fte_range_breakpoints = np.array([0.8, 0.6, 0.5])
    wages_comp_list = np.array([150, 175, 190])
    print(f"Employer costs: {get_employer_annual_from_wage(fte_range_breakpoints, wages_comp_list)}")
    print(f"Employee gross income: {get_employee_amount(fte_range_breakpoints, wages_comp_list)}")


def get_employer_annual_from_wage(fte_range, wages_comp_list):
    return np.round(wages_comp_list * (number_of_work_hours_per_year * fte_range)).astype(int)


def get_employer_cost(salary_range):
    employer_cost_range = np.round(salary_range * (1 + overhead_rate_total) + overhead_flat_total).astype(int)
    return employer_cost_range


def get_employee_amount(fte_range, wage_range):
    wage_total_per_year = wage_range * (number_of_work_hours_per_year * fte_range)
    income_total_per_year = wage_total_per_year * (1 - overhead_rate_total) - overhead_flat_total
    income_total_per_year = np.round(income_total_per_year / 1000) * 1000
    gross_income = np.round(income_total_per_year).astype(int)
    return gross_income


if __name__ == '__main__':
    main()
