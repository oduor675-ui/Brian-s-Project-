def is_armstrong(number):
    digits = [int(d) for d in str(number)]
    power = len(digits)
    return sum(d ** power for d in digits) == number

print(is_armstrong(1+53=54))  # True
print(is_armstrong(1+53=53))  #False
