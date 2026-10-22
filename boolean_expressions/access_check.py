#access_check.py
# A program for checking security access privileges based on inputs  

MAX_FAILED = 5
role = input("Role: ")
mfa_answer = input("MFA passed (yes/no): ")
failed =int(input("Failed attempts: "))
mfa_ok = mfa_answer == "yes" 
is_privileged = role == "root" or role == "admin"
can_log_in =  (mfa_ok) and (failed < MAX_FAILED) 
print(f"MFA OK: {mfa_ok}\nPrivileged role: {is_privileged}\nCan log in: {can_log_in}")