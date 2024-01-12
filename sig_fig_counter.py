numbers = ("1","2","3","4","5","6","7","8","9")
significant_figs = 0
i = 0


def checker(test): #checks if the input is only a whole number or a decimal
    test1 = True
    test2 = True
    test3 = True
    for character in test:
        if character.isalpha():
            test1 = False
        elif character.isdigit():
            test2 = True
        elif character == ".":
            test3 = True
    return test1 and test2 and test3


number = input("Enter a number: ")

while number == "":
    number = input("Enter a number: ")
while not checker(number):
    number = input("Enter a number: ")
while number[0] == "0" and "." not in number:
    number = input("Enter a number: ")
if "." in number:
    while number.count(".") != 1:
        number = input("Enter a number: ")

length = len(number)
if "." in number:
    decimal = number.index(".")
    while i < length:
        if number[0] in numbers:
            if number[-1] in numbers or number[-1] == "0" or number[-1] == ".":
                significant_figs += (length-1)
                break
        elif number[i] == ".":
            pass
        elif number[0] == "0":
            if i < decimal:
                pass
            else:
                if number[i] in numbers:
                    significant_figs += len(number[i:])
                    break
        i += 1
else:
    while i < length:
        if number[0] in numbers and number[-1] in numbers:
            significant_figs += length
            break
        elif number[i] in numbers:
            significant_figs += 1
        elif number[i] == "0":
            for j in number[i:]:
                if j not in numbers:
                    pass
                else:
                    significant_figs += 1
        i += 1

print(f"The number of significant figures in {number} is: {significant_figs}")
