import sys

file_name, production_hours, rate_hour, premium = sys.argv


def salary_function(production_hours, rate_hour, premium):
    return production_hours * rate_hour + premium


print(salary_function(int(production_hours), int(rate_hour), int(premium)))
