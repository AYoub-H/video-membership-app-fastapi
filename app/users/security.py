from argon2 import PasswordHasher
from argon2.exceptions import VerifyMisMatchError


def generate_hash(pw_raw):
    ph = PasswordHasher()
    return ph.hash(pw_raw)


def verify_hash(pw_hash, pw_raw):
    ph = PasswordHasher()
    verified = False
    message = ""
    try:
        verified = ph.verify(pw_hash, pw_raw)
    except VerifyMisMatchError:
        message = "Invalid password."
    except Exception as e:
        message = f"Unexpected error: \n {e}"
    return verified, message
