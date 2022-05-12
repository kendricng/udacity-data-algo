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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
if __name__ == "__main__":
    #
    # ---------- PART A ----------
    #
    calls_from_bangalore = [call[1] for call in calls if
                            call[0].startswith('(080)', 0, 5)]

    callees = set()
    chars = [' ', '(', ')']
    mobile_prefixes = ['7', '8', '9']

    for c in calls_from_bangalore:
        # telemarketers
        if not any(char in c for char in chars) and c.startswith('140', 0, 3):
            callees.add('140')

        # mobile numbers
        elif ' ' in c and c[0] in mobile_prefixes:
            callees.add(c[0:4])

        # fixed lines
        elif c[0] == '(' and ')' in c:
            idx1 = c.index("(")
            idx2 = c.index(")")
            callees.add(c[idx1 + 1: idx2])

        else:
            pass

    callees_sorted = sorted(list(callees))

    print("The numbers called by people in Bangalore have codes:")
    for callee in callees_sorted:
        print(callee)

    #
    # ---------- PART B ----------
    #
    num_calls_from_bangalore = len(calls_from_bangalore)
    num_calls_to_and_from_bangalore = 0

    for call in calls_from_bangalore:
        if call.startswith('(080)', 0, 5):
            num_calls_to_and_from_bangalore += 1

    pct_calls_to_and_from_banglore = (num_calls_to_and_from_bangalore /
                                      num_calls_from_bangalore) * 100

    print(f"{pct_calls_to_and_from_banglore:.2f}"
          " percent of calls from fixed lines in Bangalore are calls to other"
          " fixed lines in Bangalore.")
