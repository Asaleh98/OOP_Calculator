import calculator

for index in range(0, 5):
    number1 = input("Please Enter The First Number:  ")
    number1 = int(number1)5
    number2 = input("Please Input The Second Number: ")
    number2 = int(number2)

    calculatorObject = calculator.CalculatorClass(number1, number2)
    print(f"calculatorObject = {calculatorObject}")
    sum = calculatorObject.add()
    print(sum)
    print(f"Total Operations = {calculator.CalculatorClass.op_count}")

    sub = calculatorObject.subtract()
    print(sub)
    print(f"Total Operations = {calculatorObject.op_count}")

    mul = calculatorObject.multiply()
    print(mul)
    print(f"Total Operations = {calculatorObject.op_count}")

    div = calculatorObject.multiply()
    print(div)
    print(f"Total Operations = {calculatorObject.op_count}")

    print(f"Total Operations = {calculatorObject.op_count}")
    calculatorObject_01 = calculator.CalculatorClass(45, 12)
    print(f"Total Operations For calculatorObject_01= {calculatorObject_01.op_count}")
