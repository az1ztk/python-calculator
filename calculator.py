def main():
    
    while True:

        problem = input()

        if problem.strip().lower() == "quit":
            break
        
        pieces = problem.split()

        if len(pieces) == 3:
            x1 = parse(pieces[0])
            sign1 = pieces[1]
            x2 = parse(pieces[2])
            result = equation(x1, x2, sign1)
    
        elif len(pieces) == 2:
            if pieces[0] == "sqr":
                sign1 = "**"
                x1 = parse(pieces[1])
                if x1 < 0:
                    print("Error: Output is a complex number")
                    print()
                    continue 
                x2 = 0.5
                result = equation(x1, x2, sign1)
            else: 
                print("Error: invalid input")
                print()
                continue

        elif len(pieces) == 5:
            x1 = parse(pieces[0])
            sign1 = pieces[1]
            x2 = parse(pieces[2])
            sign2 = pieces[3]
            x3 = parse(pieces[4])
            result = equation(equation(x1, x2, sign1), x3, sign2)

        else: 
            print ("Error: invalid input")
            print()
            continue

        if result is None:
            continue
        
        result = round(result, 10)

        if roundable(result):
            print("=", int(result))
        else:
            print("=", (result))
        print()

def roundable(n):
    return n == int(n)
    
    
def equation(x1, x2, sign1):
    if x1 is None:
        return None
    sign1 = (sign1).lower()
    if sign1 == "-" or sign1 == "minus" or sign1 == "subtract":
        return x1 - x2
    elif sign1 == "+" or sign1 == "add" or sign1 == "plus":
        return x1 + x2
    elif sign1 == "*" or sign1 == "times" or sign1 == "multiply":
        return x1 * x2
    elif sign1 == "/" or sign1 == "divide":
        if x2 == 0:
            print("Error: division by zero")
            print()
            return None
        return x1 / x2
    elif sign1 == "**" or sign1 == "power":
        return x1 ** x2
        
    else: 
        print("Error: invalid sign")
        print()
        return None

def parse(stringx):
    if "." in stringx:
        return float(stringx)
    
    return int(stringx)

main()