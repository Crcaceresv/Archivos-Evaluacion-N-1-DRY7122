ACL = int(input("¿Cual es el numero IPV4 ACL? "))
if ACL >= 1 and ACL <= 99:
    print("Esta es una ACL ESTANDAR.")
elif ACL >=100 and ACL <= 199:
    print("Esta es una ACL IPV4 EXTENDIDA.")
else:
    print("Esta ACl no es ni EXTENDIDA ni ESTANDAR.")
 
