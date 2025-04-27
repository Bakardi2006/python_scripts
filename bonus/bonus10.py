try:
    width = float(input('enter rectangle width:'))
    length = float(input('enter rectangle length:'))
    if width == length:
        exit('That looks like a square.')

    area = width * length
    print(area)
except ValueError:
    print('please enter a number.')