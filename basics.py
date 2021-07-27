# first solution
def greatest_common_factor(a, b):
    if b == 0:
        print(a)
    else:
        return greatest_common_factor(b, a % b)


# Second solution
def reorder(num_list, num):
    for i in range(0, len(num_list)):
        if num == num_list[i]:
            num_list.remove(num_list[i])
            num_list.append(num)
    print(num_list)


# Third Solution
def special_sum(num_list):
    num = 0
    for i in range(0, len(num_list)):
        if num_list[i] % 2 == 0:
            num += num_list[i]
        else:
            num -= num_list[i]
    print(num)


greatest_common_factor(10, 5)
greatest_common_factor(2669, 2983)
reorder([97, 95, 99, 91, 93, 100, 100, 91, 100, 92, 96, 92, 100, 91], 100)
special_sum([26, 46, 39, 5, 50, 15, 47, 32, 36, 38, 1, 9, 10, 40, 29])

# answers
'''
5
157
[97, 95, 99, 91, 93, 91, 92, 96, 92, 91, 100, 100, 100, 100]
133
'''

