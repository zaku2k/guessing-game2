print("Press enter")

def d1():
    input1 = ["too small", "too big", "you win"]
    while True:
        result = input()
        if result in input1:
            break
        print("Enter 'too small', 'too big', 'you win'")
    return result

def d2():
    print("Imagine number from 0 to 1000")

    min = 0
    max = 1000
    result2 = " "

    while result2 != "you win":
        guess = int((max - min) / 2) + min
        print(f"I guess: {guess}")
        result2 = d1()

        if result2 == "too big":
            max = guess
        elif result2 == "too small":
            min = guess
        elif result2 == "you win":
            print("Im won!")
    print("Guessed!")

d1()
d2()
