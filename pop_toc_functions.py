# Define functions for pop toc here
# Write pseudo code
# Write a function to check if divisible by 3
# Write a function to check if divisible by 5
# Write a function to check if divisible by 3 and 5

# As a user, I can pass a number to the function div_3, so that I know if a number is divisible by 3
def div3(num):
    if num%3 == 0:
        return True
    else:
        return False
# As a user, I can pass a number to the function div_5, so that I know if a number is divisible by 5
def div5(num):
    if num%5 == 0:
        return True
    else:
        return False

# As a user, I can pass a number to the function div_3 and div_5, so that I know if a number is divisible by 3 and 5
def div3div5(num):
    if num%3 and num%5 == 0:
        return True
    else:
        return False


