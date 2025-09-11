cup = 0
running = True

while running:
    cup += 1
    print(cup)
    if cup == 10:
        # running = False(기존의 방식)
        break

print('while문 종료')
