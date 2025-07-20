#Simple to do list using loop and list
item_list = []
def boiler():
    print("Please select the following option")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List task")
    print("0. quit")
    print("Enter your choice: ")
boiler()
num = int(input())

#Add function-------------------
def add():
    item = input("Enter item: ")
    item_list.append(item)
    print(item_list)
    boiler()

#Delete function-----------------
def delete():
    print("which one want to delete: ")
    dl = int(input())
    item_list.pop(dl - 1)
    boiler()

while num  != 0:
#Add items
    if num == 1:
        add()
        num = int(input())
#Delete items
    elif num == 2:
        delete()
        num = int(input())
#Show all items
    elif num == 3:
        for item in range(len(item_list)):
            print(f"{item+1}.{item_list[item]}")
        boiler()
        num = int(input())
print("GOODBYE")


