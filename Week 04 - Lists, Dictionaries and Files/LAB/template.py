"""
RECORD CHECK  -  my version
===========================

Name  : Jemel
Lane  :   Cyber
Date  : 29.10.2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

def check_record(value, limit):
    """Calculates the difference, percentage, and breach status for a record."""
    difference = limit - value
    percent = (value / limit) * 100
    
    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"
        
    return difference, percent, status


def check_record(value, limit):
    """Calculates the difference, percentage, and breach status for a record."""
    difference = limit - value
    percent = (value / limit) * 100
    
    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"
        
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Formats and prints the report details for a single record on one line."""
    print(f"{label:<12} | Value: {value:<5} | Limit: {limit:<5} | Diff: {difference:<5} | {percent:>5.1f}% | Status: {status}")


def load_records(path):
    """Reads label, value, limit lines from a file and returns a list of dicts."""
    records_list = []
    with open(path, 'r') as file:
        for line in file:
            cleaned_line = line.strip()
            if not cleaned_line:
                continue  # Skip empty lines
                
            parts = cleaned_line.split(',')
            if len(parts) == 3:
                # We use pop(0) to cleanly extract each item one after the other
                item_label = parts.pop(0).strip()
                item_value = int(parts.pop(0).strip())
                item_limit = int(parts.pop(0).strip())
                
                records_list.append({
                    "label": item_label,
                    "value": item_value,
                    "limit": item_limit
                })
    return records_list


# ======================================================================= STORE

# Make a file called records.txt in your folder containing data like:
#10.0.0.5,85,100
#7.0.3.4,120,100
#10.1.2.0,45,100

records = load_records('Week 04 - Lists, Dictionaries and Files/LAB/records.txt')


# ======================================================================= PROCESS + OUTPUT

# 3. Loop over records. For each one, call check_record and print_report.
for rec in records:
    # Unpack calculations
    diff, pct, stat = check_record(rec["value"], rec["limit"])
    
    # Send all details to print_report
    print_report(rec["label"], rec["value"], rec["limit"], diff, pct, stat)
