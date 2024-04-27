def print_odd_numbers(lst):
    if not lst:
        return
    if lst[0] % 2 != 0:
        print(lst[0])
    print_odd_numbers(lst[1:])


lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_odd_numbers(lst1)
print('---------------------------------------------------------------------------------')



def count_elements(lst):
    if not lst:
        return 0
    return 1 + count_elements(lst[1:])


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Количество элементов в списке:", count_elements(my_list))
print('---------------------------------------------------------------------------------')



def print_next_element(lst, index=0):
    if index < len(lst):
        print(lst[index])
        print_next_element(lst, index + 1)


my_list = [1, 2, 3, 4, 5]
print("Следующий элемент списка:")
print_next_element(my_list)