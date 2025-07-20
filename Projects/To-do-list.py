#Simple to do list using loop and list

def boiler():
    print("Please select the following option")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List task")
    print("0. quit")
    print("Enter your choice: ")
boiler()

#Add function-------------------
def add():
    item = input("Enter item: ")
    item_list.append(item)
    print(item_list)

#Delete function-----------------
def dell():
    dl = int(input())
    item_list.pop(dl - 1)

num = int(input())
item_list = []

while num  != 0:
#Add items
    if num == 1:
        add()
        boiler()
        num = int(input())
#Delete items
    elif num == 2:
        print("which one want to delete: ")
        dell()
        boiler()
        num = int(input())
#Show all items
    elif num == 3:
        for item in range(len(item_list)):
            print(f"{item+1}.{item_list[item]}")
        boiler()
        num = int(input())
print("GOODBYE")


