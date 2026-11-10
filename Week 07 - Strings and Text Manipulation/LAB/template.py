"""
RECORD CHECK  -  my version
===========================

Name  : jemel
Lane  :  Cyber
Date  : 11.10.2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def parse_line(raw_line):
    """Cleans and parses a raw log string into a dictionary of key-value pairs."""
    record = {}
    for item in raw_line.split(","):
        if "=" in item:
            key, value = item.split("=", 1)
            key = key.strip().lower()
            value = value.strip()
            
            # Convert numeric values to integer if applicable
            if value.isdigit():
                value = int(value)
                
            record[key] = value
    return record


def status_of(record):
    """Determines security status (FLAGGED or OK) based on failed attempts or result."""
    if record.get("result") == "FAILED" or record.get("attempts", 0) >= 10:
        return "FLAGGED"
    return "OK"


raw_records = [
    "SRC=10.0.0.5 , ATTEMPTS=12 , RESULT=FAILED",
    "src=192.168.1.10, attempts=2, result=SUCCESS",
    " SRC=172.16.0.4 , attempts=15 , result=failed ",
    "src=10.0.0.12, ATTEMPTS=0, RESULT=SUCCESS ",
    "  SRC=192.168.1.50 , attempts=8 , result=FAILED  "
]




for raw_record in raw_records:
    parsed_record = parse_line(raw_record)
    status = status_of(parsed_record)
    print(parsed_record, status)