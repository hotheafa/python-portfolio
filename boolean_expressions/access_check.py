#access_check.py
# برنامج لفحص صلاحيات الدخول الأمني بناءً على المدخلات   

MAX_FAILED = 5
role = input("Enter a role: ")
MFA = input("Did you pass the MAF?:")
failed =int(input("Number of failed attempts = "))
mfa_ok = MFA == "yes" 
is_privileged = role == "root"
can_log_in =  (mfa_ok == True ) and (failed < MAX_FAILED) 
print (f"MFA OK: {mfa_ok}\nPrivileged role: {is_privileged}\nCan log in: {can_log_in}")