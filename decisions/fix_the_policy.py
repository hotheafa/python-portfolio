# fix_the_policy.py 
# Check a new password against an example policy and classify its length. 
MIN_LENGTH = 12 
  
username = input("Username: ") 
password = input("New password: ") 
# (Syntax error) The error here is forgetting to place the colon at the end of the conditional clause.
if len(password) < MIN_LENGTH:
    print("- Too short.") 
# (Semantic Error) This causes the program, if the word is short, not to print it as such, but to check the word's strength. The solution was to execute each command independently. The error here was using the `elif` command.
if password == username: 
    print("- Same as the username.") 
#(Semantic Error) The error here is logical because any password longer than 12 will print the word "accepted," and therefore it is impossible for the password to be too long because the program will stop immediately at "accepted." This error is solved by simply reversing the conditions.
if len(password) >= 16:
    strength = "long"
elif len(password) >= MIN_LENGTH:
    strength =  "acceptable"
else: 
    strength = "short" 
# (Semantic Error) The error here is that the print command was placed inside (else) only. This means that if the word is strong and long, the program will not print anything, whereas it should always print at the end of the program.
print(f"Length: {len(password)} ({strength})")
