def common_elements(list1, list2):
    result = []
    for x in list1:
        if x in list2 and x not in result:
            result.append(x)
    return result

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print(common_elements(list1, list2))