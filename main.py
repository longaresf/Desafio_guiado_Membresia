from membresia import Membresia,Gratis,Basica,Familiar,SinConexion,Pro
import sys

correo_e = input('\nFavor indique su correo electrónico:\n')
numero_tarj = input('\nFavor indique los 16 dígitos de su número de tarjeta:\n')
opcion = int(input('\nBienvenido, para aperturar su suscripción favor indicar tipo de cuenta:\n1: Gratis\n2: Básica\n3: Familiar\n4: Sin Conexión\n5: Pro\n6: Salir\n '))
if opcion == 1:
    Gratis._crear_nueva_membresia(correo_e,numero_tarj)
elif opcion == 2:
    Basica._crear_nueva_membresia(correo_e,numero_tarj)
elif opcion == 3:
    Familiar._crear_nueva_membresia(correo_e,numero_tarj)
elif opcion == 4:
    SinConexion._crear_nueva_membresia(correo_e,numero_tarj)
elif opcion == 5:
    Pro._crear_nueva_membresia(correo_e,numero_tarj)
else:
    print("Vuelva pronto.")
    sys.exit

op_cliente = int(input("\nFavor seleccione su nuevo cambio de membresía\n1: Básica\n2: Familiar\n3: Sin Conexión\n4: Pro\n5: Salir\n"))
if opcion == 1:
    Gratis.cambiar_suscripcion(op_cliente,correo_e,numero_tarj)
elif opcion == 2:
    Basica.cambiar_suscripcion(op_cliente,correo_e,numero_tarj)
elif opcion == 3:
    Familiar.cambiar_suscripcion(op_cliente,correo_e,numero_tarj)
elif opcion == 4:
    SinConexion.cambiar_suscripcion(op_cliente,correo_e,numero_tarj)
elif opcion == 5:
    Pro.cambiar_suscripcion(op_cliente,correo_e,numero_tarj)
else:
    print("Vuelva pronto.")

opc = int(input("\nPara cancelar su suscripción presione 1, otro número para salir\n"))
if opc == 1:
    if opcion == 1:
        print('Usted posee el plan Gratis')
    elif opcion == 2:
        Basica.cancelar_suscripcion(correo_e,numero_tarj)
    elif opcion == 3:
        Familiar.cancelar_suscripcion(correo_e,numero_tarj)
    elif opcion == 4:
        SinConexion.cancelar_suscripcion(correo_e,numero_tarj)
    elif opcion == 5:
        print('Usted no puede cambiar su actual plan Pro')
else:
    print("Vuelva pronto.")
    sys.exit
