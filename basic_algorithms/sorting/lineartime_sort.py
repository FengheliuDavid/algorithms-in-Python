# -*- coding: utf-8 -*-

def countingsort(array):
    size = len(array)
    output = [0] * size
    # 假设排序数组的范围在0-10
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1
    
    # Store the cummulative count，这之后count里的值就是output的索引
    for i in range(1, 10):
        count[i] += count[i - 1]
    # place the elements in output array
    for i in range(size):
        output[count[array[i]]-1]=array[i]
        count[array[i]]-=1
    return output


#Radix Sort 
def radixsort(array):
    max_element = max(array)
    # 最大的数的位数决定了循环次数
    place = 1  #先从个位开始
    while max_element // place > 0:
        counting_sort_for_place(array, place)
        place *= 10
def counting_sort_for_place(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place  #place=1
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Place the elements in sorted order
    i = size - 1 #指向最后一个元素
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]





data = [121, 4404, 432, 564, 23, 10, 45, 788, 0]
radixsort(data)
print(data)



'''
if __name__=='__main__':
    while True:
        a=input()
        if a=='stop':
            break
        else:
            l=list(map(lambda x: int(x),a.split()))
            print(countingsort(l))
'''       


