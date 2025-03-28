#slicing= create a substring by extracting elements from another string indexing[] or slice()
name="dinesh hariraman"
f_name=name[0:6]
l_name=name[7:]
funky_name=name[::2]
reversed_name=name[::-1]
print(f_name)
print(l_name)
print(funky_name)
print(reversed_name)

web="http://google.com"
web2="http://wikipedia.com"
slice=slice(7,-4)
print(web[slice])
print(web2[slice])