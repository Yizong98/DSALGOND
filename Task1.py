"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
record = [elem[0] for elem in texts] + [elem[1] for elem in texts] + [elem[0] for elem in calls] + [elem[1] for elem in calls]
cnt = len(set(record))

print("There are {} different telephone numbers in the records.".format(cnt))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
