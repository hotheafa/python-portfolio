# fix_the_stats.py 
# Count failed logins and the average session length. 
events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"] 
minutes = [0, 30, 0, 15, 45] 
failed = 0
for event in events: 
# The mistake here was initializing the variable inside the loop instead of outside. [Semantic Error]
    if event == "FAILED": 
        failed += 1 
print(f"Failed logins: {failed}") 
 
total = 0 
count = 0 
for value in minutes: 
    if value > 0: 
        total += value 
        count += 1 
        pass
# The mistake here was using integer division which discards the remainder, and the correct way is using float division which shows the remainder. [Semantic Error]
# The mistake here was leaving a space before printing and also not putting a break statement inside the conditional statement. [Runtime Error / Syntax Error]
print(f"Average session: {total / count} minutes") 
# The mistake here was putting number 4 instead of 5 so that number 4 appears in the print because it will print the end of the range minus 1. [Semantic Error]
for level in range(1, 5): 
    print(f"Level {level}")