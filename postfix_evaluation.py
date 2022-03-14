
import re

def post_eval(str):

    if str == "":
        return None

    if str.isalpha():
        return None    
                    
    special_char=re.compile('[@_!#$%^&()<>?\|}{~:]')
    
    if special_char.search(str) == None:
        stack= []
        allowed_nums= "0123456789"

        for i in str:
            if i in allowed_nums:
                stack.append(int(i))

            elif i== "+":
                dig1= stack.pop()
                dig2= stack.pop()
                stack.append(int(dig1)+ int(dig2))

            elif i== "-":
                dig1= stack.pop()
                dig2= stack.pop()
                stack.append(int(dig1)- int(dig2))   

            elif i== "/":
                dig1= stack.pop()
                dig2= stack.pop() 
                stack.append(int(dig1)/ int(dig2))

            elif i== "*":
                dig1= stack.pop()
                dig2= stack.pop()
                stack.append(int(dig1)* int(dig2)) 

        return(stack.pop())

if __name__== "__main__": 
    
    popped_value = post_eval("abcd112+")
    print("Popped Value: ",popped_value)         
          
    

            
