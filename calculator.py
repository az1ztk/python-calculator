def main():
    x = float(input("x equal to ").strip())
    sign = input("Sign? ").strip()
    y = float(input("y equal to ").strip())

    result = equation(x, y, sign)
    if result is None:
        return
    if roundable(result):
        print(int(result))
    else:
        print(result)


def roundable(n):
    return n == int(n)

def equation(x, y, sign):
    if sign == "-":
        return x - y
    elif sign == "+":
        return x + y
    elif sign == "*":
        return  x * y
    elif sign == "/":
        if y == 0:
            print("Error: division by zero")
            return None
        return x / y
    elif sign == "**":
        return x ** y
        
    else: 
        print("Error: invalid sign")
        return None


main()
 