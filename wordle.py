

import random

# To Do:
# Display list of already tried letters
# Add a way to quit the game




def getWordFromFile() -> str:
    # Using readlines()
    file1 = open('words.txt', 'r')
    Lines = file1.readlines()
    file1.close()

    count = 0
    # Strips the newline character
    randomIndex = random.randint(0, len(Lines)-1)
    line = Lines[randomIndex]
    # Limit the word to 5 charaters
    word = line[0:5]
    # Returns in lower case.
    return word.upper()

def checkRealWord(wordToCheck: str) -> bool:
    # Using readlines()
    file1 = open('words.txt', 'r')
    Lines = file1.readlines()
    file1.close()

    lineNum: int = 0
    while lineNum < len(Lines):
        line = Lines[lineNum]
        # Limit the word to 5 charaters
        word = line[0:5].upper()
        if wordToCheck == word:
            return True
        lineNum = lineNum + 1
    return False
    


def main() -> None:
    attempts = 0
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
            elif not checkRealWord(guess): 
                 badInput = True
                 print("That word doesnt exist")
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
                output = output + guessChar.lower()
            else:
                output = output + "-"

            

        print("output: " + output)

if __name__ == "__main__":
    main()
