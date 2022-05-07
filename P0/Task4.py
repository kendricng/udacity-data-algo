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
if __name__ == "__main__":
    # Criteria 1: outgoing calls
    one = set([call[0] for call in calls])

    # Criteria 2: not send texts, receive texts, or receive incoming calls
    calls_to = set([call[1] for call in calls])
    texts_from = set([text[0] for text in texts])
    texts_to = set([text[1] for text in texts])

    two = calls_to | texts_from | texts_to

    # Both criteria one and two
    # i.e. remove numbers from one that are in two
    not_likely_telemarketers = one & two
    likely_telemarketers = one - not_likely_telemarketers

    print("These numbers could be telemarketers: ")
    for number in sorted(list(likely_telemarketers)):
        print(number)
