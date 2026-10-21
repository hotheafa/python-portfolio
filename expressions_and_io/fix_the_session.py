# fix_the_session.py
# يقوم هذا الملف بإصلاح الأخطاء البرمجية والمنطقية في تقرير وقت الجلسة.

username = input("Username: ")
# (runtime error) int() الخطأ هو انه تم ادخال الثواني ك نص وهذا غير منطقي يجب اضافة التحويل الى عدد صحيح باستخدام
total_seconds = int(input("Session length in seconds: "))
# (semantic error)(//)الخطأ هنا هو انه تم استخدام القسمة العادية لحساب النتائج بالدقائق لكن الناتج سكون عدد غير صحيح يعني معاه باقي لذا يجب استخدام
minutes = total_seconds // 60
seconds = total_seconds % 60

print("=" * 30)
#(semantic error) (f-strings) f الخطأ هنا هو نسيان حرف 
print(f"User: {username}")
#(runtime error) لان اداة الربط تستعمل فقط للربط بين النصصوص فقط   str()الخطأ هنا عدم تحويل الدقائق الىنص باستخدام 
print("Session: " + str(minutes) + " min " + str(seconds) + " s")
print("=" * 30)
