# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 18:51:22 2019

@author: Laxmi
"""
def isPalindrome(s): 
      
    # Using predefined function to  
    # reverse to string print(s) 
    rev = ''.join(reversed(s)) 
  
    # Checking if both string are  
    # equal or not 
    if (s == rev): 
        return True
    return False
  
# main function 
s = "malayalam"
ans = isPalindrome(s) 
  
if (ans): 
    print("Yes") 
else: 
    print("No")