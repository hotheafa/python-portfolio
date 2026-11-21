# fix_the_parser.py
LINE = "09:02 FAILED user=Admin ip=192.0.2.7"


def get_time(line):
    """Return the time: the first 5 characters."""
    # semantic: slice end is excluded, so 0:5 is needed for 5 characters.

    return line[0:5]


def get_user(line):
    """Return the user name in lowercase."""
    start = line.find("user=") + 5
    end = line.find(" ", start)
    user = line[start:end]
    # semantic: lower() returns a new string; assign it back to keep it.
    user = user.lower()
    return user


def is_failed(line):
    """Return True if the line reports a failed login."""
    # semantic: in is case-sensitive, so convert line to lowercase first.
    return "failed" in line.lower()
    # or : return "FAILED in line"


def hide_first(user):
    """Return user with its first letter replaced by *."""
    # runtime: strings are immutable and do not support item assignment.
    user = "*" + user[1:]
    return user


print(f"Time: {get_time(LINE)}")
print(f"User: {get_user(LINE)}")
print(f"Failed: {is_failed(LINE)}")
print(f"Hidden: {hide_first('admin')}")
# runtime: len() is a built-in function, not a string method.
print(f"Length: {len(LINE)}")
