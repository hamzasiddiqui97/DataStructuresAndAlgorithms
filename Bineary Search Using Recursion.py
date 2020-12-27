def BinarySearch(data, l, r, element):
    if l <= r:
        mid = (l+r) // 2
        if data[mid] == element:
            return mid
        elif data[mid] < element:
            return BinarySearch(data, mid+1, r, element)
        else:
            return BinarySearch(data, l, mid-1, element)
    else:
        return -1

data = [1,2,3,4,5,6,7,88,9,9,6,6,65,4]
element = int(input('Enter number: '))
print(BinarySearch(data, 0, len(data)-1, element))