# log_analyzer.py
#analyze authentication logs through an interactive menu

ALERT_LIMIT = 3
LOG = """09:01 OK user=sara ip=192.0.2.5
09:02 FAILED user=admin ip=192.0.2.7
09:02 FAILED user=admin ip=192.0.2.7
09:03 FAILED user=root ip=192.0.2.7
09:04 OK user=omar ip=198.51.100.4
09:06 FAILED user=Sara ip=203.0.113.9
09:07 FAILED user=test ip=192.0.2.7
09:09 OK user=admin ip=192.0.2.5
09:12 FAILED user=guest ip=203.0.113.9
09:15 OK user=lina ip=198.51.100.8"""

def get_field(line, name):
    """Return the value after name=, or ""."""

    start_name = line.find(name + "=")
    
    if start_name == -1:
        return ""
    start_name = start_name + len(name) + 1
    end_name = line.find(" ",start_name)
    if end_name == -1:
        return line[start_name:]
    return line[start_name:end_name]


def get_status(line):
    """Return the second word of the line (OK or FAILED)."""

    words = line.split()
    return words[1]


def count_status(status):
    """Return how many lines in LOG have the given status."""

    count_status = LOG.count(status)
    return count_status 


def show_summary():
    """Print total lines, failed count, and OK count."""

    count_line = len(LOG.splitlines())
    count_failed = LOG.count("FAILED")
    count_ok = count_status("OK")
    print(f"Lines: {count_line}")
    print(f"Failed: {count_failed}")
    print(f"OK: {count_ok}")


def search(keyword):
    """Print matching lines with line numbers and total matches."""

    line = LOG.splitlines()
    matches = 0 
    number_line = 1
    for li in line:
        if keyword in li or keyword.lower() in li or keyword.upper() in li or keyword.title() in li :
            print(f"{number_line}: {li}")
            matches += 1
            number_line += 1
        else:
            number_line += 1
    print(f"Matches: {matches}")

def ip_report(ip):
    """Print failed attempts from ip, total count, and alert if needed."""

    line = LOG.splitlines()
    count_failed = 0 
    for li in line:
        if ip in li:
            if "FAILED" in li:
                count_failed += 1
                start_name = li.find("user=")
                end_name = li.find(" ",start_name)
                name = li[start_name + 5:end_name]
                time = li[:5]
                print(time,name)
    print(f"Failed logins from {ip}: {count_failed}")                     
    if count_failed >= 3:
        print(f"ALERT: possible password guessing.")


def mask(word):
    """Return word with middle letters replaced by *, or * if 2 or fewer."""

    first_digit = word[0]
    end_digit = word[-1]
    len_word = len(word)

    if len_word <= 2:
        return "*"
    return first_digit + "*"*(len_word - 2) + end_digit

#09:01 OK user=s**a ip=192.0.2.5
def show_masked():
    """Print the whole LOG with every user name masked."""

    new_log = LOG.splitlines()
    for line in new_log:
        
        name = get_field(line,"user")
        mask_name = mask(name)
        print(line.replace(f"user={name}",f"user={mask_name}"))

def show_menu():
    """Print the program title and menu options."""

    print("AUTH LOG ANALYZER\n1. Summary\n2. Search\n3. IP report\n4. Masked log\nq. Quit")


show_menu()
while True:
    choice = input("Choice: ").strip().lower()
    if choice == "q":
        print("Bye.")
        break
    elif choice == "1":
        show_summary()
    elif choice == "2":
        keyword = input("Keyword: ")
        search(keyword)
    elif choice == "3":
        ip = input("IP: ")
        ip_report(ip)
    elif choice == "4":
        show_masked()
    else:
        print("Unknown choice.")