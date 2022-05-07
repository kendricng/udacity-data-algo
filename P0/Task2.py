"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
if __name__ == "__main__":
    durations = {}
    for call in calls:
        # assume the caller didn't call themselves
        caller = call[0]
        callee = call[1]

        if caller in durations:
            durations[caller] += int(call[3])
        else:
            durations[caller] = int(call[3])

        if callee in durations:
            durations[callee] += int(call[3])
        else:
            durations[callee] = int(call[3])

    longest_call = max(durations, key=durations.get)

    print(f"{longest_call}", end="")
    print(f" spent the longest time, {durations[longest_call]} seconds,"
          f" on the phone during September 2016.")
