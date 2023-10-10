i = 0
int_list = []
while i < 2:
    i += 1
    int_list.append(int(input(f"Please enter {i} number: ")))
sign_input = input("Please enter operation sign '-' '+' '*' '/': ")
if sign_input == "-":
    print(f"Subtraction: {int_list[0]-int_list[1]}")
elif sign_input == "+":
    print(f"Adition: {int_list[0]+int_list[1]}")
elif sign_input == "*":
    print(f"Multiplication: {int_list[0]*int_list[1]}")
elif sign_input == "/":
    print(f"Division: {int_list[0]/int_list[1]}")
