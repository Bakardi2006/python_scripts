#!/usr/bin/env python

import requests
import secrets
import string

# Configuration
WP_URL = "https://glavobolja.hr/wp-json/wp/v2/users"  # REST API endpoint for users
ADMIN_USERNAME = "admin"  # A user with admin access to authenticate
ADMIN_PASSWORD = "^/]4JDf&$FdttYZS"  # Password of the above admin user

# List of additional admin users to create
users_to_create = [
    {"username": "pmatic", "email": "petar@ni-na.hr"},
]

# Function to generate a secure random password
def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

# Function to create admin user via REST API
def create_admin_user(username, email):
    password = generate_password()
    headers = {
        'Authorization': f'Basic {requests.auth._basic_auth_str(ADMIN_USERNAME, ADMIN_PASSWORD)}',
        'Content-Type': 'application/json'
    }
    user_data = {
        "username": username,
        "email": email,
        "password": password,
        "roles": ["administrator"]  # Assign admin role
    }

    # Make a POST request to create the user
    response = requests.post(WP_URL, json=user_data, headers=headers)

    if response.status_code == 201:
        print(f"[+] Admin user {username} created successfully!")

        # Print credentials to stdout
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Email: {email}")
    else:
        print(f"[-] Failed to create user {username}: {response.text}")

# Create users
for user in users_to_create:
    create_admin_user(user['username'], user['email'])
