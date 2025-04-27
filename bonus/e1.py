import glob

filepath = glob.glob('../files/*.txt')


for file in filepath:
    with open(file, 'r') as file:
        print(file.read())