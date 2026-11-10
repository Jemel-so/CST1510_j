"""
RECORD CHECK  -  my version
===========================

Name  : Jemel
Lane  :  Cyber
Date  : 28.10.2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def status_of(percent):
    """Return the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """ to calculate the difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    print()
    print("=" * 40)
    print(f" RECORD CHECK - {label}")
    print("=" * 40)
    print(f"{'Used':<12}: {value:>10.2f}")
    print(f"{'Total':<12}: {limit:>10.2f}")
    print(f"{'Free':<12}: {difference:>10.2f}")
    print(f"{'Percent':<12}: {percent:>9.2f} %")
    print(f"{'Status':<12}: {status:>10}")
    print("=" * 40)
over_limit_count = 0

while True:
    label = input("\nEnter Source IP (or 'quit' to stop): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter failed logins: "))
    limit = float(input("Enter total attempts: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1

print()
print(f"Records OVER LIMIT: {over_limit_count}")