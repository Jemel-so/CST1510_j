"""
RECORD CHECK  -  my version
===========================

Name  : Jemel
Lane  :  AI     (delete two)
Date  : 28.10.2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Returns the usage status based on the ratio of value to limit."""
        pct = (self.value / self.limit) * 100
        if pct >= 100:
            return "OVER LIMIT"
        elif pct >= 90:
            return "WARNING"
        else:
            return "OK"

records = [
    Record("R-001", 64, 100),
    Record("R-002", 120, 100),
    Record("R-003", 93, 100)
]



for record in records:
    print("-" * 30)
    print(f"Label:  {record.label}")
    print(f"Value:  {record.value}")
    print(f"Limit:  {record.limit}")
    print(f"Status: {record.status()}")
print("-" * 30)
