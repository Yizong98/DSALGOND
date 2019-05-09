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
send_txt = list(set(elem[0] for elem in texts))
recived_txt = list(set(elem[1] for elem in texts))
recived_call = list(set(elem[1] for elem in calls))
send_call = set(elem[0] for elem in calls)
total = set(send_txt+recived_txt+recived_call)
possible_tele = send_call - total
print("These numbers could be telemarketers: ")
for elem in sorted(possible_tele):
	print(elem)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

