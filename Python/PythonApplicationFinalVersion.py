import csv
import random

def loadWords():
    fields = []
    rows = []
    arrayOfWords = []
    with open('German.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        # creating a csv reader object 
        
        # extracting field names through first row 
        fields = next(csvreader) 
    
        # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
    
    # Parse Each Column Box
    for row in rows:
        newdict = {
            "number": row[0],
            "german": row[1],
            "english": row[2]
        }
        arrayOfWords.append(newdict)
    return arrayOfWords


def printMenu():
    print("Welcome to German Language Helper!")
    print("Select An Option:")
    print("1. German To English")
    print("2. English To German")
    print("3. Quit")


def main():
    while True:
        printMenu()
        option = input('Select Option: ')
        
        if option == '3':
            break
        elif option == '1':
            germanToEnglish(loadWords())        
        elif option == '2':
            print('\nopt2\n')
        else:
            print('\nPlease pick one of the menu options\n')

    print("Have a nice day\n")

 

def germanToEnglish(arrayToUse):
    # print(arrayToUse)
    numberOfQuestions = input("Enter the amount of words to be quizzed on: ")
    quiz = arrayToUse[0:int(numberOfQuestions)]
    numCorrect = 0
    numIncorrect = 0
    
    answer = []
    answerSize = 0
    while answerSize < int(numberOfQuestions):
        r = random.randint(0,int(numberOfQuestions)-1)
        if r not in answer:
            answerSize += 1
            answer.append(r)



    # print(answer)
    # print(quiz)

    questionsAnswered = 0
    while questionsAnswered < int(numberOfQuestions):
        currentGermanWord = quiz[answer[questionsAnswered]]['german']
        currentEnglishWord = quiz[answer[questionsAnswered]]['english']

        print(currentGermanWord)
        guess = input("Translation: ")
        print()

        if guess.upper() == currentEnglishWord.upper():
            print("Correct!")
            numCorrect+=1
            print("Number Correct: " + str(numCorrect))
            print("Number Incorrect: " + str(numIncorrect))
        else:
            print("Incorrect!")
            print("The correct answer was: " + currentEnglishWord)
            numIncorrect+=1
            print("Number Correct: " + str(numCorrect))
            print("Number Incorrect: " + str(numIncorrect))
        

        questionsAnswered+=1


def englishToGerman(arrayToUse):
    # print(arrayToUse)
    numberOfQuestions = input("Enter the amount of words to be quizzed on: ")
    quiz = arrayToUse[0:int(numberOfQuestions)]
    numCorrect = 0
    numIncorrect = 0
    
    answer = []
    answerSize = 0
    while answerSize < int(numberOfQuestions):
        r = random.randint(0,int(numberOfQuestions)-1)
        if r not in answer:
            answerSize += 1
            answer.append(r)


    # print(answer)
    # print(quiz)

    questionsAnswered = 0
    while questionsAnswered < int(numberOfQuestions):
        currentGermanWord = quiz[answer[questionsAnswered]]['german']
        currentEnglishWord = quiz[answer[questionsAnswered]]['english']

        print(currentEnglishWord)
        guess = input("Translation: ")
        print()

        if guess.upper() == currentGermanWord.upper():
            print("Correct!")
            numCorrect+=1
            print("Number Correct: " + str(numCorrect))
            print("Number Incorrect: " + str(numIncorrect))
        else:
            print("Incorrect!")
            print("The correct answer was: " + currentGermanWord)
            numIncorrect+=1
            print("Number Correct: " + str(numCorrect))
            print("Number Incorrect: " + str(numIncorrect))
        
# Run Application
main()
