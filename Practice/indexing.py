#indexing  = [start:end:step]
cr_no="1234-5678-9101"

print(cr_no[0])
print(cr_no[:5])
print(cr_no[5:])
print(cr_no[5:9])
print(cr_no[-1])
print(cr_no[::2])

last_digits=cr_no[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

reverse=cr_no[::-1]
print(reverse)