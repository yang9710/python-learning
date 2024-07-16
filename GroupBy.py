rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2024'},
    {'address': '5148 N CLARK', 'date': '07/04/2024'},
    {'address': '5800 E 58TH', 'date': '07/02/2024'},
    {'address': '2122 N CLARK', 'date': '07/03/2024'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2024'},
    {'address': '1060 W ADDISON', 'date': '07/02/2024'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2024'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2024'},
]

from operator import itemgetter
from itertools import groupby

# Sort by the desired field first
rows.sort(key=itemgetter('date'))
# Iterate in groups
# for date, items in groupby(rows, key=itemgetter('date')):
#     print(date)
#     for i in items:
#         print(' ', i)


from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

print(rows_by_date)

for date in rows_by_date:
    print(date)
    for row in rows_by_date[date]:
        print(' ', row)