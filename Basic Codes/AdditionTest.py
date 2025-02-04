# A Simple Yet Revolutionary assessment for testing your skills in addition! (Not Really xd)
# Answer all 10 additions correctly to get access to my bank account (which is empty XD)

import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        getInt1 = generate_integer(level)
        getInt2 = generate_integer(level)
        problem = getInt1 + getInt2
        error = 0

        while error < 3:
            try:
                solution = int(input(f"{getInt1} + {getInt2} = "))
                if solution == problem:
                    score += 1
                    break
                else:
                    print("EEE")
                    error += 1
            except ValueError:
                print("EEE")
                error += 1

        if error == 3:
            print(f"{getInt1} + {getInt2} = {problem}")

    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
