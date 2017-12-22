def FindLetterIndex(randomString, letter):
    index = -1
    while True:
        index = randomString.find(letter, index + 1)
        if index == -1:
            break
        yield index

listOfWords = ["hotdog", "hamburger", "noodle","rice", "sausage", "curry", "chicken", "beef", "pork", "fish"];
from random import randrange
random_index = randrange(0,len(listOfWords))

randomWord = listOfWords[random_index]


print("Example output for <secret word " + randomWord + ">:")
print('WELCOME TO HANGMAN!');
turn = 6
numberOfLetterInAWord = len(randomWord)
default = ""

newStrToList = []
historyList = []
LettersInInvalidList = []
dash = numberOfLetterInAWord
while (dash >0):
    dashChar = "-"
    default += dashChar; 
    dash -= 1

print(default + (" ") + str(turn) + (" error-attempt lefts"))

#Start the game
newStr = default 
while(turn >= 0): 
    letter = input("Guess a word: "); 
    if (letter.isalpha()):
        
                  
        if letter not in historyList:
            historyList.append(letter)
        else:
            print("You already guessed this letter '" + letter + '!')
                    
               
        newStrToList = list(newStr) 

        if letter in randomWord: # if h in hotdog
            
            for i in FindLetterIndex(randomWord, letter):
                newStrToList[i] = letter     #newStrToList = ['h','-','-','-','-','-']
                str1 = ''.join(newStrToList) #convert back to string from list
                
            print(str1 + (" ") + str(turn) + (" error-attempt lefts"))
                
            newStr = str1 #newstr = h-----
            
            if (str1 == randomWord):
                
                print("Good Job! You got it in " +str(turn) +" correct guess!")
                break;
            
        else:
            if letter not in LettersInInvalidList:
                turn -= 1
                LettersInInvalidList.append(letter)
            if (turn > 0):
                print(newStr + (" ") + str(turn) + (" error-attempt lefts"))
            if (turn == 0):
                print("The secret word was " + randomWord + ". Good luck next time." )
                turn -= 1
    else:
        print("You have to guess an alphabetic letter!")

