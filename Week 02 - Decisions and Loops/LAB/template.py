"""
RECORD CHECK  -  my version
===========================

Name  : Jemel
Lane  :   Cyber    
Date  : 28.10.2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



source_ip = input("Enter Source IP: ")     
failed_logins = float (input(" Enter failed logins: "))  
total_attemps= float (input("Enter total attemps: "))    



difference = total_attemps - failed_logins # 
percent = (failed_logins / total_attemps) * 100    

if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else :
    status = "OK" 


print()
print("=" * 38)
print(f"  RECORD CHECK  -  {source_ip}")
print("=" * 38)
print(f" {'Used':<12}:  {failed_logins:>10.2f} ")
print(f" {'Total':<12}: {total_attemps:>10.2f} ")
print(f" {'Free':<12}:  {difference:>10.2f}")
print(f" {'Percent':<12}: {percent:>10.2f} %")
print(f" {'Status':<12}: {status:>10}")
print("=" * 38)
print()


