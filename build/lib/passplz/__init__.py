from uuid import uuid4

def generate_password(password_length = 16):
    random_string = str(uuid4())
    random_password = random_string.replace('-', '')[:password_length]
    return random_password
