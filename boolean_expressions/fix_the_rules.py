# fix_the_rules.py
# This program checks a connection against three rules.

role = input("Role: ")
# (Runtime Error))int() الخطأ هنا عدم وضع التحويل الى رقم صيحيح
port = int(input("Port: "))
#(Semantic Error) adminالخطأ هنا هو  كتابة المساواة واسناد قيمة بدل المقارنه وهو خطأ منطقي لانه سيطبع دائما 
is_admin = role =="admin"
#(Syntax Error)الخطأ هنا فقط في كتابة الاشارة بالمقلوب 
is_system_port = port <= 1023
# (Semantic Error) 443  مش   port == 443 الخطأ هنا هو انه لازم نحط
is_web_port = port == 80 or port == 443
print(f"Admin: {is_admin}")
print(f"System port: {is_system_port}")
print(f"Web port: {is_web_port}")
