def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_address(street="#123 gandhi street",
                    city="vellore",
                    state="TN",
                    apt="50",
                    zip="632505")    