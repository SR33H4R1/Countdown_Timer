import time


def timer(t):
    while t:
        minute, sec = divmod(t, 60)
        hour, minute = divmod(minute, 60)
        print(f"{hour} : {minute} : {sec}", end="\r")
        time.sleep(1)
        t -= 1

    print("Fire in the hole !!!")


if __name__ == '__main__':
    x = int(input("Enter the time in seconds : "))
    timer(x)
