import sys

def rotate(x, y, d):
    if d == 1:
        return y, -x
    if d == 2:
        return -x, -y
    if d == 3:
        return -y, x
    return x, y

stroka = sys.stdin.readline().strip()

moves = {
    'F': (0, 1),
    'B': (0, -1),
    'R': (1, 0),
    'L': (-1, 0),
}

x = 0
y = 0
direction = 0
number = 0
stack = []

for command in stroka:
    if command.isdigit():
        number = number * 10 + int(command)

    elif command == '[':
        stack.append((x, y, direction, number))
        x = 0
        y = 0
        direction = 0
        number = 0

    elif command == ']':
        block_x = x
        block_y = y
        turn = direction
        x, y, direction, repeats = stack.pop()

        if turn == 0:
            dx, dy = rotate(block_x, block_y, direction)
            x += dx * repeats
            y += dy * repeats
        else:
            for i in range(repeats % 4):
                dx, dy = rotate(block_x, block_y, direction)
                x += dx
                y += dy
                direction = (direction + turn) % 4
    elif command == ')':
        direction = (direction + 1) % 4

    elif command == '(':
        direction = (direction - 1) % 4

    else:
        dx, dy = moves[command]
        dx, dy = rotate(dx, dy, direction)
        x += dx
        y += dy
print(x, y)