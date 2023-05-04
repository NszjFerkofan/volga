#háromszog
a=int(input("Add meg a haromszog 'a' oldalát "))
b=int(input("Add meg a haromszog 'b' oldalát "))
c=int(input("Add meg a haromszog 'c' oldalát "))
if c<a+b and a<c+b and b<a+c:
	print("A(z)",a,",",b,"és",c,"háromszöget alkot ")
else:
	print("A(z)",a,",",b,"és",c," nem alkot háromszöget")
