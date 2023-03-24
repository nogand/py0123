import os
import time

def main():
    time.sleep(3)
    for i in range(5):
        os.system("python3 hijo.py &")

if __name__ == '__main__':
    main()
