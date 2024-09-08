def calculator(operation,num1,num2):
    switcher={
            'add':num1+num2,
            'subract':num1-num2,
            'multiply':num1*num2,
            'divide':num1/num2  if num2!=0 
            else'error:division by zero'
            }
    return switcher.get(operation,'invalid operation')
print(calculator('add',10,5))
print(calculator('subract',10,5))
print(calculator('multiply',10,5))
print(calculator('divide',10,5))
print(calculator('divide',10,0))
print(calculator('mod',10,5))

