import string
import random


def gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    while True:
        passlen = int(input("Enter the password length (or 0 to exit)\n"))

        if passlen == 0:
            print("Exiting...")
            break

        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))

        random.shuffle(s)
        pas = ("".join(s[0:passlen]))
        print(pas)


if __name__ == "__main__":
    gen()
