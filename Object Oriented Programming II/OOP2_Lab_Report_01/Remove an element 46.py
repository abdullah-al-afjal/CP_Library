def Remove_element(lst, element):
    if element in lst:
        lst.remove(element)
        return lst


lst = [1, 2, 3, 4, 5]
element = 3
print(Remove_element(lst, element))
