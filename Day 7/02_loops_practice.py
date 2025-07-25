# Print even numbers from 1 to 20
print("Even numbers between 1 and 20: ")
for num in range(1, 21):
    if num % 2 == 0:
        print(num)

# Countdown timer
count = 5
print("Countdown: ")
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")            

# skip number 5 and stop at 10
print("Loop with break and continue: ")
for i in range(1, 15):
    if i == 5:
        continue   # skip 5
    if i == 11:
        break      # stop at 10
print(i)    

# Using continue to skip specific iteration
# using break to stop the loop