#give snake len from user
snake_len = int(input("Enter Snake Length: "))
snake = ''

for i in range(snake_len):
    if i%2==0:
        snake += '*'
    else:
        snake += '#'

print(snake)