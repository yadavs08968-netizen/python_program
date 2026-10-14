def common_element(a,b):
    result=[]
    for x in a:
        if x in b and x not in result:
            result.append(x)
    return result
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = common_element(list1, list2)
print("Common elements:", result)