if __name__ == '__main__':
    # n = int(input())
    arr=[1,2,3,4,5,6]
    # if arr[0]>arr[1]:
    #57 57 57 -57
    #6 6 6 6 6 6 6 6 6 5
    largest=arr[0]#57
    second=float('-inf')#57
    # if arr[1]>arr[0]:
    #   largest=arr[1]#
    #   second=arr[0]
    for i in range(1,len(arr)):
      if arr[i]==largest or arr[i]==second:
        continue
      if arr[i]>largest:#57=57
        second=largest#sec=57
        largest=arr[i]#larg=57
      elif arr[i]>second:
        second=arr[i]
      
    
    print(second)
