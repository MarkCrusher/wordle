

import random

# To Do:
# check if words exist before accepting user input
# Make it case insensitive {done}
# Display capital when correct, lower case when correct but wrong spot, and * when wrong.
# Display list of already tried letters




def getWordFromFile() -> str:
    # Using readlines()
    file1 = open('words.txt', 'r')
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    randomIndex = random.randint(0, len(Lines)-1)
    line = Lines[randomIndex]
    # Limit the word to 5 charaters
    word = line[0:5]
    # Returns in lower case.
    return word.upper()

def main() -> None:
    attempts = 0
    # word = "fante"
    word = getWordFromFile()
    print("!!! word to guess is " + word)

    while attempts < 5:

        badInput = True
        while badInput:
            guess = input("Enter your 5 letter guess: \n")
            guess = guess.upper()
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
