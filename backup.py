print("Welcome to the Virtual Vending Machine")

print("All products cost $1.25")

total = float(0.00)
while total < 1.25:
    print("Please enter $0.25, or $1.00")
    val = float(input())
       
    if val == .25:
        total = .25
        print("Money inserted so far:", total)
        print("Please enter $0.25, or $1.00")
        val = float(input())
        if val == .25:
            total = .50
            print("Money inserted so far:", total)
            print("Please enter $0.25, or $1.00")
            val = float(input())
            if val == .25:
                total = .75
                print("Money inserted so far:", total)
                print("Please enter $0.25, or $1.00")
                val = float(input())
                if val == .25:
                    total = 1.00
                    print("Money inserted so far:", total)
                    print("Please enter $0.25, or $1.00")
                    val = float(input())
                    if val == .25:
                        total = 1.25
                        print("Money inserted so far:", total)
                        print("Please enter $0.25, or $1.00")
                        val = float(input())
                        if val == .25:
                            total = 1.50
                            print("Money inserted so far:", total)
                        elif val == 1.00:
                            total = 2.25
                            print("Money inserted so far:", total)
                    elif val == 1.00:
                        total = 2.00
                        print("Money inserted so far:", total)          
                elif val == 1.00:
                     total = 1.75
                     print("Money inserted so far:", total)
            elif val == 1.00:
                total = 1.50
                print("Money inserted so far:", total)
        elif val == 1.00:
            total = 1.25
            print("Money inserted so far:", total)
            print("Please enter $0.25, or $1.00")
            val = float(input())
            if val == .25:
                    total = 1.50
                    print("Money inserted so far:", total)
            elif val == 1.00:
                total = 2.25
                print("Money inserted so far:", total)
    elif val == 1.00:
        total = 1.00
        print("Money inserted so far:", total)
        print("Please enter $0.25, or $1.00")
        val = float(input())
        if val == .25:
            total = 1.25
            print("Money inserted so far:", total)
            print("Please enter $0.25, or $1.00")
            val = float(input())
            if val == .25:
                total = 1.50
                print("Money inserted so far:", total)     
            elif val == 1.00:
                total = 2.25
                print("Money inserted so far:", total) 
        elif val == 1.00:
            total = 2.00
            print("Money inserted so far:", total)

else:
    if total == 1.25:
        print("Product Dispensed")
    if total == 1.30:
        print("Product Dispensed")
    if total == 1.35:
        print("Product Dispensed")
    if total == 1.40:
        print("Product Dispensed")
    if total == 1.45:
        print("Product Dispensed")
    if total == 1.50:
        print("Product Dispensed")
    if total == 1.75:
        print("Product Dispensed")
    if total == 2.00:
        print("Product Dispensed")
    if total == 2.25:
        print("Product Dispensed")

