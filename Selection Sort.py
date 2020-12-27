def selectionsortMethod(arr):
     for i in range(len(arr)):
          for j in range(i+1, len(arr)):
               if arr[i]>arr[j]:
                    k = arr[i]
                    arr[i] = arr[j]
                    arr[j] = k
     for i in range(len(arr)):
          print("%d" %arr[i])

arr = [99,12,13,4,-1,-2,3,4,7,100]
selectionsortMethod(arr)
