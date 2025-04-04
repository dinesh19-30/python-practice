#format specifiers={value:flags}

price1=3.1419
price2=-968.563
price3=1200.569

print(f"price1 is ${price1:.2f}")
print(f"price2 is ${price2:10}")
print(f"price3 is ${price3:010}")

print(f"price1 is ${price1:<10}")
print(f"price2 is ${price2:>10}")
print(f"price3 is ${price3:^10}")

print(f"price1 is ${price1: }")
print(f"price2 is ${price2: }")
print(f"price3 is ${price3:,}")

print(f"price3 is ${price3:+,.2f}")
