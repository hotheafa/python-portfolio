# pin_tries.py
# Description: Simulates PIN entry attempts and handles account lockout logic using iterative loops.

MAX_TRIES = 3
CORRECT_PIN = "2580"
tries = 0

while tries < MAX_TRIES:
    PIN = input("PIN: ")
    tries += 1 
    
    if PIN == CORRECT_PIN:
        print("Access granted.")
        break
    else:
        print(f"Wrong PIN. Tries left: {MAX_TRIES - tries}") 
        if tries == 3:
           print("Card blocked.")
           break
       