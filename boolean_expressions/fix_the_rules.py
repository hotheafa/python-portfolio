# fix_the_rules.py
# This program checks a connection against three rules.

role = input("Role: ")
# int() الخطأ هنا عدم وضع التحويل الى رقم صيحيح
port = int(input("Port: "))
#adminالخطأ هنا هو  كتابة المساواة واسناد قيمة بدل المقارنه وهو خطأ منطقي لانه سيطبع دائما 
is_admin = role =="admin"
#الخطأ هنا فقط في كتابة الاشارة بالمقلوب 
is_system_port = port <= 1023
#  443  مش   port == 443 الخطأ هنا هو انه لازم نحط
is_web_port = port == 80 or 443
print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")
