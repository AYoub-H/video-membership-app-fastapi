from email_validator import validate_email, EmailNotValidError


def email_validator(email):
    message = ""
    valid = False
    try:
        valid = validate_email(email)
        email = valid.email
        valid = True
    except EmailNotValidError as e:
        message = str(e)
    return valid, message, email
