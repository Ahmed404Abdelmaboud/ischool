books = []

def new(name, id):
    if not check_id(id):
        books.append({
            "name": name,
            "id": id,
            "avilable": "yes"
        })
        print("done👍")
        show_books()

def check_id(id):
    exist = False
    for book in books:
        if book["id"] == id:
            print("this id exists already")
            exist = True
            break
    return exist

def show_books():
    print(books)

def delete_book(id):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            print("done👍")
            show_books()