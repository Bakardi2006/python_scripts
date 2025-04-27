import requests
import os
import secrets
import string

# Configuration
WP_URL = input("Enter site url:")
SITE_TITLE = input("Enter Site Title:")
ADMIN_USER = input("Enter Admin user:")
ADMIN_EMAIL = input("Enter email adress:")

# Generate a secure random password
def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

ADMIN_PASS = generate_password()

# Check if WordPress installation is required
response = requests.get(WP_URL, allow_redirects=False)

if response.status_code == 200:
    print("[+] WordPress install.php is accessible. Proceeding with installation...")
    
    # Prepare installation data
    payload = {
        "weblog_title": SITE_TITLE,
        "user_name": ADMIN_USER,
        "admin_password": ADMIN_PASS,
        "admin_password2": ADMIN_PASS,
        "admin_email": ADMIN_EMAIL,
        "blog_public": 1,
        "Submit": "Install WordPress"
    }

    # Submit installation form
    install_response = requests.post(WP_URL + "?step=2", data=payload)

    if "Success!" in install_response.text or install_response.status_code == 302:
        print("[+] WordPress installation successful!")

        # Print credentials to stdout
        print(f"Username: {ADMIN_USER}")
        print(f"Password: {ADMIN_PASS}")
        print(f"Email: {ADMIN_EMAIL}")

    else:
        print("[-] WordPress installation might have failed. Check manually.")
else:
    print("[-] WordPress is already installed or install.php is not accessible.")

