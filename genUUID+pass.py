import uuid
import time
import random
import string

def generate_random_password(length=32):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

random_uuid = str(uuid.uuid4())
random_password = generate_random_password()

print(f"UUID: {random_uuid}")
print(f"Pass: {random_password}")
