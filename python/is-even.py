def is_even(num):
    if num % 2 == 0:
        return True
    if num % 2 != 0:
        return False

print(is_even(20))

print(is_even(35))


def calc_total(num_list):
    total = 0
    for num in num_list:
        total = total + num
    return total


list = [45,234,65,12,0,102,342]
add = calc_total(list)

print(add)
