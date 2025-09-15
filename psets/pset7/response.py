from validator_collection import checkers, validators, errors

email = input("Whats's your email address?")

try:
    email_address = validators.email(email)
    print('Valid')

except errors.EmptyValueError:
    print('Invalid')
except ValueError:
    print('Invalid')
except errors.InvalidEmailError:
    print('Invalid')



