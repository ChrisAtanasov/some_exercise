#Write a program which calculate daily salary by given input.

worked_days_in_month=int(input())
earned_money_per_day=float(input())
dollar_exchange_rate=float(input())

monthly_salary=int(worked_days_in_month*earned_money_per_day)

anual_salary=monthly_salary*12+monthly_salary*2.5

salary_after_taxes=anual_salary*0.75

salary_in_leva=salary_after_taxes*dollar_exchange_rate

average_anual_dayly_salary=salary_in_leva/365



print("{:.2f}".format(average_anual_dayly_salary))

#after all calculations we have calculated the clear salary per day after taxes










