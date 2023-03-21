'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import random
import string
import datetime

# Generate a new password function
def generate_password(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letters) for i in range(length))
    return password

# Check if 5 days have passed since the last password change
def is_time_to_change_password(last_change_date):
    today = datetime.datetime.today()
    delta = today - last_change_date
    return delta.days >= 5

# Example usage
last_password_change_date = datetime.datetime(2023, 3, 16) # set the last password change date
if is_time_to_change_password(last_password_change_date):
    new_password = generate_password(10) # generate a new password with 10 characters
    print("Your new password is:", new_password)
    # Update the last password change date
    last_password_change_date = datetime.datetime.today()

