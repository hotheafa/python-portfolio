#login_report.py
# يحسب هذا البرنامج محاولات الدخول المتبقية ويعرض تقريراً منسقاً للمستخدم.
 
MAX_LOGIN_ATTEMPTS = 5
username = input("Enter username: ")
failed = int(input("Number of failed attempts: "))
remaining_attempts = MAX_LOGIN_ATTEMPTS - failed 
line = "*"*30
messge = f"\nUsername: {username}\nRemaining attempts = {remaining_attempts} \nNumber of failed attempts = {failed}"
print (line)
print ("         LOGIN REPORT")
print (line)
print (messge)