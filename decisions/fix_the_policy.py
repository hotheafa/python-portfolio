# fix_the_policy.py 
# Check a new password against an example policy and classify its length. 
MIN_LENGTH = 12 
  
username = input("Username: ") 
password = input("New password: ") 
# (syntax error)الخطأ هنا هو نسيان وضع النقطتين الرأسيتين في اخر الجملة الشرطية
if len(password) < MIN_LENGTH:
    print("- Too short.") 
# (Semantic Error) مما يجعل البرنامج في حال كانت الكلمة قصيرة لا يطبع انها كذلك بل يذهب ليتحقق من قوة الكلمة والحل كان بجعل كل من الامرين يتم تنفيذه بشكل مستقل  elif الخطأ هنا كان استحدام امر
if password == username: 
    print("- Same as the username.") 
#(Semantic Error)الخطأ هنا منطقي لان اي كلمه مرور اكثر من 12 سوف تطبع كلمه مقبول وبتالي من المستحيل ان تاتي  الكلمه طويلة لان البرنامج سيتوقف مباشرة عند  كلمه مقبول ويتم حل هذا الخطأ بقلب الشروط فقط   
if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength =  "acceptable"
else: 
    strength = "short" 
# (Semantic Error)الخطأ هنا هو انه تم وضع امر الطباعه في داخل (else) فقط وهذا يعني انه في حال كانت الكلمه قوية و طويلة لان يطبع البرنامج شيئ بينما يجب ان تطبع دائما في كل نهاية البرنامج 
print(f"Length: {len(password)} ({strength})")
