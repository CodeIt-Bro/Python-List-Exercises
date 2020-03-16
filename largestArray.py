def largestFun(arr,n):      #function to find the largest element in an array with two arguements - array and size of array.
    maxNum = arr[0]         #maximum element initialized
    for i in range(1, n):   #Traverse through the array to find the largest element
        if arr[i] > maxNum: 
            maxNum = arr[i] 
    return maxNum
  
arr = [13430, 33424, 45000, 56390, 938408]   #Array intialized
n = len(arr)                                 #Finding the length of array
largestElement = largestFun(arr,n)           #Calling the function to find the largest element in the array. 
print ("Largest element in the given array is",largestElement) #Printing output. 