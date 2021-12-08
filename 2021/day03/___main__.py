def main():
    with open('input.txt') as file:
        lines = file.readlines()
    
    dirs = [[s.split()[0], int(s.split()[1])] for s in lines]
    print(dirs)

    x, y = 0, 0

    for d in dirs:
        if d[0] == 'forward':
            x = x + d[1]
        elif d[0] == 'down':
            y = y + d[1]
        elif d[0] == 'up':
            y = y - d[1]

    print(x, y, x*y)

    x, y, a = 0, 0, 0
    for d in dirs:
        if d[0] == 'forward':
            x = x + d[1]
            y = y + a*d[1]
        elif d[0] == 'down':
            a = a + d[1]
        elif d[0] == 'up':
            a = a - d[1]

    print(x, y, x*y)
   

if __name__ == "__main__":
    main()