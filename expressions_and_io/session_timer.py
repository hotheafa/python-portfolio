# session_timer.py
# يقوم هذا البرنامج بتحويل طول الجلسة من الثواني إلى دقائق وثواني متبقية.

time_seconds = int(input("Enter the session duration in seconds: "))
time_minutes = time_seconds // 60
remaining_seconds = time_seconds % 60 
messge = f"Session duration = {time_minutes}m and {remaining_seconds}s"
print (messge)
# 15m and 5s = عندما المستخدم يدخل وقت الجلسة يساوي 905 ثواني 
#  1m and 0s = عندما المستخدم يدخل وقت الجلسة يساوي 60 ثواني 
# 0m and 59s = عندما المستخدم يدخل وقت الجلسة يساوي 59 ثواني 
