####################################################################################################
# ex_2_task_2.py
#
# This file contains the solution to Exercise Two, Task Two.
#
# Prompt:
#   As part of some app, the user has to create a valid email address. Any address will do as long
#   as it's valid according to the validation from the first part. Your validation will only allow a
#   number of retries if a invalid email is given (default 3) once the number of attempts is exhausted
#   (you should show how many retries are left!), set the boolean flag gave_up to True and bail out.
####################################################################################################

from ex_2_task_1 import is_valid_email_address

gave_up = False
num_allowed_attempts = 3

while gave_up is False:
    email = input("Please Enter Your Email Address: ")
    parse_code, parse_message = is_valid_email_address(email)

    if parse_code is None:
        print(email, "Is Valid!")
        break

    num_allowed_attempts -= 1

    if num_allowed_attempts == 0:
        gave_up = True
        print("No Attempts Left... Aborting!")
        break

    print("\n----------------------------------------------------------------------------------------------------")
    print(f"{ email } Is Invalid! Here's The Error Object:")
    print(f"Parse Code: { parse_code }, Parse Message: { parse_message }")

    plurality_string = "" if num_allowed_attempts == 1 else "s"

    print(f"Try Again, { num_allowed_attempts } Attempt{ plurality_string } Left")
    print("----------------------------------------------------------------------------------------------------\n")
