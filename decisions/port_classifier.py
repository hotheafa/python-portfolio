#port_classifier.py
# برنامج للتحقق من صحة أرقام المنافذ وتصنيفها حسب نطاقات إيانا والخدمات المحددة

port = int(input("Port: "))
if port < 0 or port > 65535:
    print("Invalid port: use a number from 0 to 65535.")
#تصنيف النطاق (للمنافذ الصالحة) بحيث  يطبع النطاق الذي ينتمي إليه المنفذ
else:
    if port <= 1023:
       print("Range: system")
    elif port <= 49151:
       print("Range: user")
    else:
       print("Range: dynamic or private")
#تحديد الخدمة للمنافذ 22 و 80 و 443 فقط
if port == 22:
    print("Service: ssh")
if port == 80:
    print("Service: http")
if port == 443:
    print("Service: https")
