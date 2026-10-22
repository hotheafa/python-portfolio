#conditional_tests.py
# Ten police tests to examine security conditions

user = "analyst"
role = "viewer"
failed = 3
port = 22 
#Test 1
print("Is user == 'admin' or user == 'analyst'? I predict True.")
print (user == "admin" or user == "analyst")

#Test 2
print("\nIs ((user == 'analyst' and port == 443) or (user == 'analyst' and port == 22))? I predict True.")
print ((user == "analyst" and port == 443) or (user == "analyst" and port == 22))

#Test 3
print("\nIs failed <= 3 or failed != 5? I predict True.")
print (failed <= 3 or failed != 5 )

#Test 4 
print("\nIs ((role == 'viewer' and user == 'analyst') or (not (user == 'admin' and role != 'viewer')))? I predict True.")
print ((role == "viewer" and user == "analyst") or (not (user == "admin" and role != "viewer")))

#Test 5
print("\nIs failed == 3 and role == 'viewer'? I predict True.") 
print (failed == 3 and role == "viewer")

#Test 6 
print("\nIs role != 'viewer'? I predict False.")
print (role != "viewer")

#Test 7
print("\nIs 0 < port and port < 25? I predict False.")
print ( 0 < port and port > 25)

#Test 8 
print("\nIs failed - 6 >== 7? I predict False.")
print (failed - 6 >= 7 )

#Test 9
print("\nIs ((not (user == 'analyst' and port == 22 and role == 'viewer')) or (user == 'analyst' and role == 'Viewer'))? I predict False.")
print ((not (user =="analyst" and port == 22 and role == "viewer")) or (user == "analyst" and role == "Viewer"))

#Test 10 
print("\nIs not (failed + 1 == 4)? I predict False.")
print (not (failed +1 == 4))