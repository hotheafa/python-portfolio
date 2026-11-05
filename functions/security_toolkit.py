#security_toolkit.py
# Description: A comprehensive security toolkit module that provides port classification,
# password strength evaluation, PIN guessing duration calculation, and formatted box UI outputs

MIN_LENGTH = 8

def border(width):

    """Print a horizontal border line with a specified width surrounded by plus signs."""
    print(f"+{ '-' *(width +2)}+")


def show_box(text):

    """Display a text message enclosed inside a formatted border box."""
    box_width = len(text)
    border(box_width)
    print(f"| {text} |")
    border(box_width)

def show_menu():

    """Display the main title header for the Security Toolkit."""
    print("SECURITY TOOLKIT")
    print("1. Check a port")
    print("2. Check a password")
    print("3. PIN guessing time")
    print("q. Quit")


def port_range(port):

    """Determine the IANA classification range for a given network port number."""

    if port < 0 or port > 65535:
        return"invalid" 
    elif port <= 1023:
        return "system"
    elif 1024 <= port <= 49151:
       return "user"
    else:
        return "dynamic"

 
def check_port():

    """Prompt the user for a port number, check its range, and display the result in a box."""
    port = int(input("Port: "))
    port_type =  port_range(port)
    text = f"Port {port}: {port_type}"
    show_box(text)


def password_problem(password, username):

    """Check password against security rules (minimum length and username match) 
    and return the first error message or an empty string if valid.
    """
    if len(password) < MIN_LENGTH:
        return "too short"
    
    if password == username:
        return "same as the username"
    
    return ""


def check_password():

    """Prompt the user for username and password, evaluate security issues, 
    and display acceptance or rejection status in a box.
    """
    username = input("Username: ")
    password = input("Password: ")
    problem = password_problem(password,username)

    if problem == "too short" or problem == "same as the username":
        show_box(f"Rejected: {problem}")

    else:
        show_box("Password accepted")


def days_to_guess(digits, per_second):

    """Calculate and return the estimated number of days required to guess 
    a PIN based on the number of digits and guessing speed per second.
    """
    number_day = 10 ** digits // per_second // 86400

    return number_day


def check_pin():

    """Prompt the user for PIN digits and guesses per second, calculate 
    the time required to guess, and display the result in a box.
    """
    digits = int(input("PIN digits: ")) 
    per_second = int(input("Guesses per second: "))

    day = days_to_guess(digits,per_second)

    text = f"{digits} digits: {day} days"
    show_box(text)


show_menu()

checks_done = 0

while True:
    choice = input("Choice (1, 2, 3, or q): ")
    if choice == "1":
        check_port()
        checks_done += 1
    elif choice == "2":
        check_password()
        checks_done += 1
    elif choice == "3":
        check_pin()
        checks_done += 1
    elif choice == "q":
        show_box(f"Checks done: {checks_done}")
        break
    else:
        print("Unknown choice.")