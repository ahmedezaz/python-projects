# Using single line input with space

num = input("Enter number")
int_num = list(map(int,num.split()))
add = sum(int_num)
print(add)
