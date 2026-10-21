#access_check.py
# برنامج لفحص صلاحيات الدخول الأمني بناءً على المدخلات   

MAX_FAILED = 5
role = input("Role: ")
MFA = input("MFA passed (yes/no):")
failed =int(input("Failed attempts: "))
mfa_ok = MFA == "yes" 
is_privileged = role == "root" or role == "admin"
can_log_in =  (mfa_ok) and (failed < MAX_FAILED) 
print(f"MFA OK: {mfa_ok}\nPrivileged role: {is_privileged}\nCan log in: {can_log_in}")