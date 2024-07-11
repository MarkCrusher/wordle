

import random


def getWordFromFile() -> str:
    # Using readlines()
    file1 = open('words.txt', 'r')
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    randomIndex = random.randint(0, len(Lines)-1)
    line = Lines[randomIndex]
    return line[0:5]

def main() -> None:
    attempts = 0
    # word = "fante"
    word = getWordFromFile()
    print("!!! word to guess is " + word)

    while attempts < 5:

        badInput = True
        while badInput:
            guess = input("Enter your 5 letter guess: \n")
            if len(guess) != 5:
                badInput = True
                print("Please enter a 5 letter word")
            else:
                badInput = False

        attempts = attempts + 1


        if word == guess:
            print("Excellent, you made in " + str(attempts) + " attempts")
            exit()
        
        output = ""

        for x in range(5):
            isMatch = False
            isThere = False

            guessChar = guess[x]
            for y in range(5):
                wordChar = word[y]
                if guessChar == wordChar and x == y:
                    isMatch = True
                elif guessChar == wordChar:
                    isThere = True

            if isMatch:
                output = output + guessChar
            elif isThere:
                output = output + "+"
            else:
                output = output + "-"

            

        print("output: " + output)

if __name__ == "__main__":
    main()
