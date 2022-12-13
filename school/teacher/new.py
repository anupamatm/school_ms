def divide_dec(func):
    def wrapper(num1,num2):
        if num2>num1:
            num1,num2=num2,num1
        return func(num1,num2)
    return wrapper

    
@divide_dec
def divide(num1,num2):
    result=num1/num2
    return result


c=divide(10,100)
print(c)