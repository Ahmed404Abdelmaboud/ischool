import members
import borrow
import books

while(True):
    print("""
    Welcome, how can I help you?
    ----------------------------
    Members:
    1) Regist a member
    2) Delete a member
    3) Show the members
    ----------------------------
    Borrow:
    4) Borrow a book
    5) Return a book
    6) Show borrow record
    ----------------------------
    Books:
    7) Add a book
    8) Delete a book
    9) Show the books  
          
    10) Exit
    """)
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter his name: ")
        email = input("Enter his email: ")
        tel = input("Enter his telephone number: ")
        id = input("Enter his ID: ")
        members.regist(name, email, tel, id)

    if choice == "2":
        id = input("Enter his ID: ")
        members.delete_member(id)

    if choice == "3":
        members.show_members()

    if choice == "4":
        id = input("Enter his ID: ")
        book_id = input("Enter the book ID: ")
        borrow.borrow(id, book_id)

    if choice == "5":
        book_id = input("Enter the book ID: ")
        borrow.return_book(book_id)

    if choice == "6":
        borrow.show_record()

    if choice == "7":
        name = input("Enter its name: ")
        id = input("Enter its ID: ")
        books.new(name, id)

    if choice == "8":
        id = input("Enter its ID: ")
        books.delete_book(id)

    if choice == "9":
        books.show_books()
    
    if choice == "10":
        break

    del choice