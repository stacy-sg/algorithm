n = int(input())

five = n // 5

while five >= 0:
    rest = n - 5 * five
    if rest % 2 == 0:
        print(five + rest // 2)
        break
    five -= 1
else:
    print(-1)