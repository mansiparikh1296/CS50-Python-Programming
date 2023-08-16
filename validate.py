import re


email = input("what's your email? ").strip()

if re.search(r"^[\w|\s]+@(\w+\.)?\w+\.(com|edu|in|net|org)$", email, re.IGNORECASE):
    print("valid")
else:
    print("Invalid")

"""if "@" in email and "." in email:
    print("valid")
else:
    print("Invalid")"""

"""username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("valid")
else:
    print("invalid")"""

