def post_eval(str):
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

    return stack.pop()   

print(post_eval("495+*"))         
              
          
            
