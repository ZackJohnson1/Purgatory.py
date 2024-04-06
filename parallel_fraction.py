def calculate_Fp():
    try:
        S = float(input("Please enter a value for S: "))
        if S == 0:
            print("Error: S cannot be zero.")
            return
        Fp = (4.0 / 3.0) * (1.0 - (1.0 / S))
        print(f"The result is: {Fp}")
    except ValueError:
        print("Error: Please enter a valid number.")
calculate_Fp()



