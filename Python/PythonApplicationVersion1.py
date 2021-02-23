import csv

# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()
# print(p1)
# p1.myfunc()

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print((thisdict))
def loadWords():
    fields = []
    rows = []
    arrayOfWords = []

    with open('German.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        # creating a csv reader object 
        # csvreader = csv.reader(csvfile) 
        
        # extracting field names through first row 
        fields = next(csvreader) 
    
        # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
    
        # get total number of rows 
        # print("Total no. of rows: %d"%(csvreader.line_num))

    # print(rows)
    # printing the field names 
    # print('Field names are:' + ', '.join(field for field in fields)) 
    
    #  printing first 5 rows 
    # print('\nFirst 5 rows are:\n') 
    for row in rows:
        newdict = {
            "number": row[0],
            "german": row[1],
            "english": row[2]
        }
        arrayOfWords.append(newdict)
        # parsing each column of a row 
        # for col in row: 
            # print(col)
        # print('\n')
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
            print('opt1')
        elif option == '2':
            print('opt2')
        else:
            print('Please pick one of the menu options')
    print("Have a nice day")
    

main()