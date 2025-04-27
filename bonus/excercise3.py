filenames = ["/home/rbutara/a.txt", "/home/rbutara/b.txt", "/home/rbutara/c.txt"]

for file in filenames:
    content = open(file, 'r')
    content = content.read()

    print(content)