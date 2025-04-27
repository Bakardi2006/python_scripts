filenames = ['doc.txt', 'report.txt', 'presentation.txt']
content = "Hello"

for filenames in filenames:
    file = open(filenames, 'w')
    file.writelines(content)
    file.close()