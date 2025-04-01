#logoical operators

#OR
temp=35
is_rain=True
if temp<0 or temp>35 or is_rain:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is scheduled")    

#AND
tem=20
is_sun=False
if tem>=20 and is_sun:
    print("Too hot outside")
elif temp<0 and is_sun:
    print("Too cold")    
    