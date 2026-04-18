members = []

def regist(name, email, tel, id):
    if not check_id(id):
        members.append({
            "name": name,
            "email": email,
            "tel": tel,
            "id": id
        })
        print("done👍")
        show_members()

def check_id(id):
    exist = False
    for member in members:
        if member["id"] == id:
            print("this id exists already")
            exist = True
            break
    return exist

def show_members():
    print(members)

def delete_member(id):
    for member in members:
        if member["id"] == id:
            members.remove(member)
            print("done👍")
            show_members()

