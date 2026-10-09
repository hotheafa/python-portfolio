# fix_the_record.py
# This program prints a short record about a network device.
  
device_name = "edge-router"
#   (syntax error) الخطأ هو البدء باسم المتغير ب رقم 2 
end_ip = "192.0.2.1"
#  (syntax error)  الخطأ هو استخدام اسم المتغير  بقيمة محجوزة للغة 
device_type= "router"
#   (runtime error)  الخطأ هو تحويل نص مكون الى حروف رقم و النظام لا يمكنه ذلك      
port = int("22")
#(runtime error)  الخطأ هو عدم كتابة اسم المتغير كامل              
print("Device:", device_name)
#الخطأ هو عدم تغير اسم المتغير بعد تعديله 
print("Backup IP:", end_ip)
print("Type:", device_type)
print("Port:", port)
# يكتشف بايثون الأخطاء القواعدية 
# Syntax Errors أولاً قبل تشغيل أي سطر كود لأنه يفحص بنية الملف كاملة قبل التنفيذ