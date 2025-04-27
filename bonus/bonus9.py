password = input("Enter a password:")

result = {}

if len(password) >= 8:
    result["Length"] = True
else:
    result["Length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digit"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True

result["upper"] = upper

if all(result.values()):
    print("Strong password!")
else:
    print("Weak password!")