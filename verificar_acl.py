acl = int(input("Ingrese el numero de ACL IPV4: "))

if 1 <=acl <= 99 or 1300 <= acl <=1999:
	print(f"El numero {acl} corresponde a una ACL Estandar.")
elif 100 <= acl <= 199 or 2000 <= acl <= 2699:
	print (f"El numero {acl} corresponde a una ACL Extendida.")
else:
	print(f"El numero {acl} no corresponde a una lista de acceso valida.")
 
