a_list = []
b_list = [a_list, a_list]
c_list = [a_list]

c_list[0].append("Hi")
print(b_list)


