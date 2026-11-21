# ip_check.py
# validate an IPv4 address entered by the user


def is_valid_part(part):
    """Return True if part is digits only and 255 or less."""
    if part.isdecimal() and int(part) <= 255:
        return True
    return False


def ip_problem(address):
    """Return the first problem with the IPv4 address, or empty string."""
    if address.count(".") == 3:
        part_address = address.split(".")
        for part in part_address:
            if part == "":
                return "Invalid: a part is empty."
            if not is_valid_part(part):
                return f"Invalid: {part} is not a number from 0 to 255."
        return ""
    else:
        return "Invalid: it needs exactly 3 dots."


address = input("IPv4 address: ").strip()

problem = ip_problem(address)
if problem == "":
    print(f"{address} is valid.")
else:
    print(problem)
