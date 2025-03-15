import re

def validate_email(email):
    # Improved regex pattern
    pattern = r'^(?=.{1,256})(?=.{1,64}@.{1,255})[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if len(email) > 7:
        if re.match(pattern, email):
            return True
    return False

if __name__ == '__main__':
    emails = input('Enter emails (comma-separated): ').split(',')
    for email in emails:
        email = email.strip()
        if validate_email(email):
            print(f'{email} is valid')
        else:
            print(f'{email} is invalid')