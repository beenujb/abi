# declare set of '0', '1' . 
    s = {'0', '1'} 
  
    # check set p is same as set s 
    # or set p contains only '0' 
    # or set p contains only '1' 
    # or not, if any one conditon 
    # is true then string is accepted 
    # otherwise not . 
    if s == p or p == {'0'} or p == {'1'}: 
        print("Yes") 
    else : 
        print("No") 
  
  
          
# driver code 
if __name__ == "__main__" : 
  
    string = "1100101"
  
    # function calling 
    check(string) 
