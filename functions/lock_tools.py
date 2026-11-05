#lock_tools.py
# Description: A security module that manages account lockouts, calculates remaining attempts,
# and evaluates the current security status based on failed login tries

def is_locked(failed, max_tries=3):

    """Check if the system or account is locked based on the number of failed attempts."""
    if failed >= max_tries:
        return True

    return False

def tries_left(failed, max_tries=3):

    """Calculate and return the number of remaining tries before getting locked out."""
    if is_locked(failed,max_tries) == True:
        return 0
    
    return max_tries - failed

def status(failed):

    """Return a descriptive string of the current security status (locked or active with remaining tries)."""
    if tries_left(failed, max_tries=3) == 0:
        return "locked"
    
    return f"active ({tries_left(failed,max_tries=3)} tries left)"

print(is_locked(2))
print(is_locked(3))
print(is_locked(3, 5))
print(tries_left(1))
print(tries_left(7))
print(status(1))
print(status(4))
