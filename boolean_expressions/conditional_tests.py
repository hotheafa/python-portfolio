user = "analyst"
role = "viewer"
failed = 3
port = 22 

#I predict : True
print (user == "admin" or user == "analyst")
#I predict : True
print ((user == "analyst" and port == 443) or (user == "analyst" and port == 22))
#I predict : True 
print (failed <= 3 or failed != 5 )
#I predict :True
print ((role == "viewer" and user == "analyst") or (not (user == "admin" and role != "viewer")))
#I predict : True 
print (failed == 3 and role == "viewer")
#I predict : False
print (role != "viewer")
#I predict : False
print ( 0 > port > 25)
#I predict : False
print (failed - 6 == 1 )
#I predict : False
print ((not (user =="analyst" and port == 22 and role == "viewer")) or (user == "analyst" and role == "Viewer"))
#I predict : False
print (not (failed +1 == 4))