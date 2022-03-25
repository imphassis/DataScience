import json
import pprint
from collections import defaultdict

pp = pprint.PrettyPrinter(indent=4)

salaries_and_tenures = [
    (83000, 8.7),
    (88000, 8.1),
    (48000, 0.7),
    (76000, 6),
    (69000, 6.5),
    (76000, 7.5),
    (60000, 2.5),
    (83000, 10),
    (48000, 1.9),
    (63000, 4.2),
]


salary_by_tenure = defaultdict(list)


for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# pprint.pprint((salary_by_tenure))


def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"


salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)


# pp.pprint(dict(salary_by_tenure_bucket))


average_salary = defaultdict(list)

# for category, salaries in salary_by_tenure_bucket.items():
#     average = round(sum(salaries)/len(salaries), 2)
#     average_salary[category] = average


# pp.pprint(dict(average_salary))


average_salary = {
    tenure_bucket: round(sum(salaries)/len(salaries), 2)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

pp.pprint(average_salary)
