#login_report.py
# يحسب هذا البرنامج محاولات الدخول المتبقية ويعرض تقريراً منسقاً للمستخدم.
 
MAX_LOGIN_ATTEMPTS = 5
username = input("Enter username: ")
failed = int(input("Number of failed attempts: "))
remaining_attempts = MAX_LOGIN_ATTEMPTS - failed 
line = "="*30
messge = f"\nUser:\t\t{username}\nfailed:\t\t{failed}\nAttempts left:\t{remaining_attempts}"
print (line)
print ("LOGIN REPORT")
print (line)
print (messge)