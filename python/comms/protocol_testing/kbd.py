import msvcrt
import time

num = 0
done = False
while not done:
    if msvcrt.kbhit():
        msvcrt.getch()
        print("done")
        done = True