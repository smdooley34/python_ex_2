####################################################################################################
# ex_2_task_1.py
#
# This file contains the solution to Exercise Two, Task One.
#
# Prompt:
#   Write and test a function, is_valid_email_address(email_address), that validates a string as a
#   proper email address. It should return a tuple of values, one being the error result (None or
#   error code), and the other being the error string ("seems legit" for None and a short error
#   message otherwise).
#
#   Rules (arbitrary rules):
#     - An email address must have three parts that look like this: <A>@<B>.<C>. A represents the
#       local part of the email (the username), with B and C making up the domain part.
#     - A must be 3 - 16 alphanumeric characters
#     - B must be 2 - 8 alphanumeric characters
#     - C must be one of these: `com`, `edu`, `org`, or `gov`
#
#   Example Run:
#     charding@iastate.edu (None, 'Seems legit')
#     chris.edu (1, 'Must have exactly one @!')
#     chris@edu (4, 'post @ part must have exactly one dot!')
#     @bla.edu (2, 'pre @ part must contain 3 - 16 alphanumeric characters')
#     throatwobblermangrove@mpfc.org (2, 'pre @ part must contain 3 - 16 alphanumeric characters')
#     chris@X.com (5, 'part after @ and before . must contain 2 - 8 alphanumeric characters')
#     chris.harding@iastate.edu (3, 'pre @ part must only contain alphanumeric characters')
#     chris@pymart.biz (7, 'past-dot part invalid, must be from: com, edu, org, gov')
#     chris@letsgo!.org (6, 'part after @ and before . must only contain alphanumeric characters')
#     chris@megasavings.org (5, 'part after @ and before . must contain 2 - 8 alphanumeric characters')
#     tc@tank.com (2, 'pre @ part must contain 3 - 16 alphanumeric characters')
#
# NOTES:
#   - Your function must adhere to the tuple return logic but you don't have to use my exact
#     error messages or codes.
#   - You can use Python's isalnum() function to check if a character is alphanumeric.
####################################################################################################

from enum import Enum

class ParsingCode(Enum):
    GoodEmail = None
    AlphaNumericError = 1
    BadAtCharacterError = 2
    BadDotCharacterError = 3
    UserNameLengthError = 4
    DomainNameLengthError = 5
    InvalidDomainError = 6

class ParsingMessage(Enum):
    GoodEmail = "Seems Legit"
    AlphaNumericError = "The Email Address Must Consist Of Alphanumeric Characters Only. Check Your Address."
    BadAtCharacterError = "There Should Be Exactly One `@` In The Email Address."
    BadDotCharacterError = "There Should Be Exactly One `.` In The Email Address."
    UserNameLengthError = "The User Name Is Too Short Or Long! The User Name Must Be 3-16 Characters In Length.."
    DomainNameLengthError = "The Domain Name Is Too Short Or Long! The Domain Name Must Be 2-8 Characters In Length."
    InvalidDomainError = "The Domain Name Must Be `com`, `edu`, `org`, or `gov`"

def is_valid_email_address(email_address):
    # There Must Be Exactly One `@` Character In The Email
    if email_address.count("@") != 1:
        return ParsingCode.BadAtCharacterError.value, ParsingMessage.BadAtCharacterError.value

    # There Must Be Exactly One `.` Character In The Email
    if email_address.count(".") != 1:
        return ParsingCode.BadDotCharacterError.value, ParsingMessage.BadDotCharacterError.value

    # Before We Proceed With Checks, We Split Up The String Into Our Three Parts Of Interest (A, B, And C) For Easier Logic
    user_name_string, b_dot_c_string = email_address.split("@")

    # The UserName Must Consist Of Only Alphanumeric Characters
    if not user_name_string.isalnum():
        return ParsingCode.AlphaNumericError.value, ParsingMessage.AlphaNumericError.value

    # The UserName Must Be Between 2 And 17 Characters
    if not (3 <= len(user_name_string) <= 16):
        return ParsingCode.UserNameLengthError.value, ParsingMessage.UserNameLengthError.value

    b_string, c_string = b_dot_c_string.split(".")

    # The Domain Part Must Also Consist Of Only Alphanumeric Characters (Except The `.`)
    if not b_string.isalnum() or not c_string.isalnum():
        return ParsingCode.AlphaNumericError.value, ParsingMessage.AlphaNumericError.value

    # The B String Must Be Between 1 and 9 Characters
    if not (2 <= len(b_string) <= 8):
        return ParsingCode.DomainNameLengthError.value, ParsingMessage.DomainNameLengthError.value

    # Finally, We Must Check The C String To Be One Of `com`, `edu`, `org`, or `gov`
    if not (c_string == "com" or c_string == "edu" or c_string == "org" or c_string == "gov"):
        return ParsingCode.InvalidDomainError.value, ParsingMessage.InvalidDomainError.value

    # Otherwise, If We Get Here, We Say That The Email Address Is Good
    return ParsingCode.GoodEmail.value, ParsingMessage.GoodEmail.value

if __name__ == "__main__":
    email_list = [
        "charding@iastate.edu",
        "chris.edu",
        "chris@edu",
        "@bla.edu",
        "throatwobblermangrove@mpfc.org",
        "chris@X.com",
        "chris.harding@iastate.edu",
        "chris@pymart.biz",
        "chris@letsgo!.org",
        "chris@megasavings.org",
        "tc@tank.com"
    ]

    for email in email_list:
        parse_code, parse_message = is_valid_email_address(email)

        if parse_code is None:
            print("----------------------------------------------------------------------------------------------------")
            print(f"{ email } { parse_message }")
            print("----------------------------------------------------------------------------------------------------\n")
        else:
            print("----------------------------------------------------------------------------------------------------")
            print(f"{ email } Seems To Have Problems... See The Following Error Object:")
            print(f"Parse Code: { parse_code }, Parse Message: { parse_message }")
            print("----------------------------------------------------------------------------------------------------\n")
