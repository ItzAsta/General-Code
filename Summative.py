
import csv
import io

booklist = ["La muerte de daniel", "Dune", "El Murcielago", "Momo"]

def function():
    print("--------Welcome to this library--------")
    print("what would you like to do? ")
    print("\n")
    print("1) add a book to the list")
    print("2) Print all the books on screen")
    print("3) print a single book to the screen using the item index")
    print("4) add a batch of books to the list")
    print("5) download the contents of the list to a file")
    print("6) Quit the program")
    user_choice = int(input("Write the number for which action you choose: "))

    if user_choice == 1:
        book_add = str(input("Insert the name of the book?: "))
        booklist.append(book_add)
        print("you have now added into the list!")
        print(booklist)
        function()
        
    if user_choice == 2:
        print("you have chocen to show all the books in this list:")
        print("\n")
        print(booklist)
        function()
        
        #in this part (3) i could not get the program to print out the book, so i tried two different ways
        #hopefylly it is just a bug in my part, but ive added the simple print("bookname")
        #just to make it work
    if user_choice == 3:
        print("you have chosen to print a single book to the screen: ")
        print("\n")
        number = input("Chooce a book from 0-3:")
        
        if number == 0:
            print(booklist[0])
            print("La muerte de daniel")
            
        if number == 1:
            print(booklist[1])
            print("Dune")
        if number == 2:
            print(booklist[2])
            print("El Murcielago")
        if number == 3:
            print(booklist[3])
            print("Momo")
        
        function()
        
    if user_choice == 4:
        print("you have chosen to add a batch of books to the list")
        print("\n")
        file = open("books.csv", "r")
        content = file.read()
        booklist.append(content)
        print(booklist)
        file.close()
        function()
        
    if user_choice == 5:
        print("you have chosen to download the contents of the list to a file")
        print("\n")
        with open("bookfile.txt", "w") as output:
            output.write(str(booklist))
        print("the file has now been downloaded in your directory.")
        function()
    
    if user_choice == 6:
        print("you have chosen to quit the program, and therefore kill me :(")
        print("good bye human")
        quit()
        
    else:
        print("you must choose a number within the range 1-6")
        function()

    
function()

#Used articles are:
#https://en.wikipedia.org/wiki/List_of_best-selling_books
#https://www.geeksforgeeks.org/python/how-to-take-integer-input-in-python/
#https://www.geeksforgeeks.org/python/python-list-index/
#https://www.geeksforgeeks.org/python/how-to-read-from-a-file-in-python/
#https://www.w3schools.com/python
#https://stackoverflow.com/search?q=lists
#https://stackoverflow.com/questions/33686747/save-a-list-to-a-txt-file