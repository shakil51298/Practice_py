def find_max_num(num1, num2, num3):
    if num1 >= num2 and num1>= num2:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(find_max_num(3, 40, 6))

# Smart Calculator

n1 = float(input("enter 1st number: "))
op = input("enter operator: ")
n2 = float(input("enter 2nd number: "))

if op == "+":
    print(n1 + n2 )
elif op == "-":
    print(n1 - n2 )
elif op == "/":
    print(n1 / n2 )
elif op == "*":
    print(n1 * n2 )
elif op == "%":
    print(n1 % n2)
else:
    print("Your operator is invalid!!")
