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


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
if __name__ == "__main__":
    records = texts + calls
    records_from = [record[0] for record in records]
    records_to = [record[1] for record in records]
    records_count = len(set(records_from + records_to))

    print(f"There are {records_count} different telephone numbers in the "
          f"records.")
