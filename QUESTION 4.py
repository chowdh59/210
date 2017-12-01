# Question 4

def Palindrome(array): (1)
  for i in range(0, int(len(array) / 2)): (n) 
     if array[i] != array[len(array) - 1 - i]: (n) 
      return False n2
      
  return True (1)
  
arrayToCheck = [1, 2, 3, 4, 3, 2, 1] (1)
  
print(Palindrome(arrayToCheck))(1)

Run Time = 4 + 2n + n2
BigO = O(n^2)
