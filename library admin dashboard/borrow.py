import members
import datetime
import books

borrow_record = []

def borrow(id, book_id):
    if check_id(id) and check_book(book_id):
        borrow_record.append({
            "id": id,
            "book_id": book_id,
            "date": datetime.datetime.now().strftime("%d/%m/%Y - %I:%M:%p")
        })
        print("done👍")
        show_record()

def check_id(id):
    exist = False
    for member in members.members:
        if member["id"] == id:
            exist = True
            break
    if not exist:
        print("this member doesn't exists")
        return exist
    else:
        return exist

def check_book(id):
    exist = False
    for book in books.books:
        if book["id"] == id and book["avilable"] == "yes":
            book["avilable"] = "no"
            exist = True
            break
    if not exist:
        print("this book doesn't exists")
        return exist
    else:
        return exist
    
def return_book(book_id):
    for borrow in borrow_record:
        if borrow["book_id"] == book_id:
            borrow_record.remove(borrow)
            for book in books.books:
                if book["id"] == book_id:
                    book["avilable"] = "yes"
                    print("done👍")
                    show_record()


def show_record():
    print(borrow_record)