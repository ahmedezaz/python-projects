list = []
n = input("Add item: ")

def add():
    list.append(n)

    for item in range(len(list)):
        print(f"{item + 1}.{list[item]}")

def dell():
    list.pop(n-1)
    for item in range(len(list)):
        print(f"{item + 1}.{list[item]}")

add()
n = input("1 for add and 2 for delete: ")

while n != "0":
    if n == "1":
        n = input("Add item: ")
        add()
        n = input("1 for add and 2 for delete: ")

    elif n == "2":
        print("which one want to delete: ")
        n = int(input())
        dell()
        n = input("1 for add and 2 for delete: ")



else:
    print("Goodbye")
