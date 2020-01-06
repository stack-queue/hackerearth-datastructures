count = int(input())

num_list = []
for i in range(count):
    num_list.append(input())

num_list.reverse()
for num in num_list:
    print(num)
