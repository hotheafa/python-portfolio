#pin_space_table.py
# Description: Calculates brute-force combinations and time required to crack PINs of varying lengths.

GUESSES_PER_SECOND = 10

for digits in range(4,9):
    combinations = 10**digits
    second = combinations // GUESSES_PER_SECOND
    minutes = second // 60
    days = (minutes // 60) // 24
    print(f"{digits} digits: {combinations} PINs, {minutes} minutes, {days} days")