from abc import ABC, abstractmethod
import sys

class Membresia(ABC):
    dias_regalo:int = 0

    def __init__(self, correo_electronico:str, numero_tarjeta:str):
        self.__correo_electronico = correo_electronico
        self.__numero_tarjeta = numero_tarjeta

    @property
    def correo_electronico(self) -> str:
        return self.__correo_electronico

    @property
    def numero_tarjeta(self) -> str:
        return self.__numero_tarjeta
    
    @correo_electronico.setter
    def correo_electronico(self, correo_e:str)->None:
        if not isinstance(correo_e, str):
            raise ValueError("El correo electronico debe ser una cadena de texto")
        else:
            self.__correo_electronico = correo_e

    @numero_tarjeta.setter
    def numero_tarjeta(self, numero_tarj:str)->None:
        if len(numero_tarj) !=  16 or not all(c in "0123456789" for c in numero_tarj):
            raise ValueError("La tarjeta debe contener números de 16 dígitos.")
        else:
            self.__numero_tarjeta = numero_tarj

    @abstractmethod
    def cambiar_suscripcion(op_cliente, correo_electronico, numero_tarjeta):
        pass

    @abstractmethod
    def _crear_nueva_membresia(opcion, correo_electronico, numero_tarjeta):
        pass

class Gratis(Membresia):
    costo:int = 0
    cant_max_disp:int = 1
    op_cambiar_suscripcion:list = [1,2,3,4]
    suscripciones = {1: 'Básica',2: 'Familiar',3: 'Sin Conexión',4: 'Pro'}

    def __init__(self, correo_electronico, numero_tarjeta):
        
        super().__init__(correo_electronico, numero_tarjeta)

    def _crear_nueva_membresia(correo_electronico, numero_tarjeta):
        user = Gratis(correo_electronico, numero_tarjeta)
        print(f'Cuenta Gratis creada con satisfacción.\nSu usuario es: {user.correo_electronico}\nMonto del plan: {Gratis.costo}\nCantidad máxima de equipos: {Gratis.cant_max_disp}')

    def cambiar_suscripcion(op_cliente, correo_electronico, numero_tarjeta):
        if op_cliente in Gratis.op_cambiar_suscripcion:
            if Gratis.suscripciones[op_cliente]  == 'Básica':
                Basica._crear_nueva_membresia(correo_electronico, numero_tarjeta)
            elif Gratis.suscripciones[op_cliente]  == 'Familiar':
                Familiar._crear_nueva_membresia(correo_electronico, numero_tarjeta)
            elif Gratis.suscripciones[op_cliente]  == 'Sin Conexión':
                SinConexion._crear_nueva_membresia(correo_electronico, numero_tarjeta)
            else:
                Pro._crear_nueva_membresia(correo_electronico, numero_tarjeta)
        else:
            print(f"No se puede realizar cambio de membresía a: {Gratis.suscripciones[op_cliente]}" if (op_cliente) < 5 else 'Opción inválida')

class Basica(Membresia):
    costo:int = 3000
    cant_max_disp:int = 2
    op_cambiar_suscripcion:list = [2,3,4]
    suscripciones = {1: 'Básica',2: 'Familiar',3: 'Sin Conexión',4: 'Pro'}

    def __init__(self, correo_electronico, numero_tarjeta):
        Membresia.__init__(self, correo_electronico, numero_tarjeta)

    def _crear_nueva_membresia(correo_electronico, numero_tarjeta):
        user = Basica(correo_electronico, numero_tarjeta)
        print(f'Cuenta Basica creada con satisfacción.\nSu usuario es: {user.correo_electronico}\nMonto del plan: {Basica.costo}\nCantidad máxima de equipos: {Basica.cant_max_disp}')

    def cambiar_suscripcion(op_cliente, correo_electronico, numero_tarjeta):
        if op_cliente in Basica.op_cambiar_suscripcion:
            if Basica.suscripciones[op_cliente]  == 'Familiar':
                Familiar._crear_nueva_membresia(correo_electronico, numero_tarjeta)
            elif Basica.suscripciones[op_cliente]  == 'Sin Conexión':
                SinConexion._crear_nueva_membresia(correo_electronico, numero_tarjeta)
            else:
                Pro._crear_nueva_membresia(correo_electronico, numero_tarjeta)
        else:
            print(f"No se puede realizar cambio de membresía a: {Basica.suscripciones[op_cliente]}" if (op_cliente) < 5 else 'Opción inválida')

    def cancelar_suscripcion(correo_electronico, numero_tarjeta):
        print(f'\nSuscripción cancelada con éxito\nDisfrute de su suscripción Gratis')
        Gratis._crear_nueva_membresia(correo_electronico, numero_tarjeta)

class SinConexion(Membresia):
    costo:int = 3500
    cant_max_disp:int = 2
    dias_regalo:int = 7
    op_cambiar_suscripcion:list = [1,2,4]
    suscripciones = {1: 'Básica',2: 'Familiar',3: 'Sin Conexión',4: 'Pro'}

    def __init__(self, correo_electronico, numero_tarjeta):
        Membresia.__init__(self, correo_electronico, numero_tarjeta)

    def _crear_nueva_membresia(correo_electronico, numero_tarjeta):
        user = SinConexion(correo_electronico, numero_tarjeta)
        print(f'Cuenta Sin Conexion creada con satisfacción.\nSu usuario es: {user.correo_electronico}\nMonto del plan: {SinConexion.costo}\nCuenta con Días de Regalo: {SinConexion.dias_regalo}\nCantidad máxima de equipos: {SinConexion.cant_max_disp}')

    def cambiar_suscripcion(op_cliente, correo_electronico, numero_tarjeta):
        if op_cliente in SinConexion.op_cambiar_suscripcion:
            if SinConexion.suscripciones[op_cliente]  == 'Básica':
                Basica._crear_nueva_membresia(correo_electronico, numero_tarjeta)
            elif SinConexion.suscripciones[op_cliente]  == 'Familiar':
                Familiar._crear_nueva_membresia(correo_electronico, numero_tarjeta)
            else:
                Pro._crear_nueva_membresia(correo_electronico, numero_tarjeta)
        else:
            print(f"No se puede realizar cambio de membresía a: {SinConexion.suscripciones[op_cliente]}" if (op_cliente) < 5 else 'Opción inválida')

    def cancelar_suscripcion(correo_electronico, numero_tarjeta):
        print(f'\nSuscripción cancelada con éxito\nDisfrute de su suscripción Gratis')
        Gratis._crear_nueva_membresia(correo_electronico, numero_tarjeta)

    def cant_max_contenido():
        return f"La cantidad máxima de contenidos que puedes descargar es (^.^)."

class Familiar(Membresia):
    costo:int = 5000
    cant_max_disp:int = 5
    dias_regalo:int = 7
    op_cambiar_suscripcion:list = [1,3,4]
    suscripciones = {1: 'Básica',2: 'Familiar',3: 'Sin Conexión',4: 'Pro'}

    def __init__(self, correo_electronico, numero_tarjeta):
        Membresia.__init__(self, correo_electronico, numero_tarjeta)

    def _crear_nueva_membresia(correo_electronico, numero_tarjeta):
        user = Familiar(correo_electronico, numero_tarjeta)
        print(f'Cuenta Familiar creada con satisfacción.\nSu usuario es: {user.correo_electronico}\nMonto del plan: {Familiar.costo}\nCuenta con Días de Regalo: {Familiar.dias_regalo}\nCantidad máxima de equipos: {Familiar.cant_max_disp}')

    def cambiar_suscripcion(op_cliente, correo_electronico, numero_tarjeta):
        if op_cliente in Familiar.op_cambiar_suscripcion:
            if Familiar.suscripciones[op_cliente]  == 'Básica':
                Basica._crear_nueva_membresia(correo_electronico, numero_tarjeta)
            elif Familiar.suscripciones[op_cliente]  == 'Sin Conexión':
                SinConexion._crear_nueva_membresia(correo_electronico, numero_tarjeta)
            else:
                Pro._crear_nueva_membresia(correo_electronico, numero_tarjeta)
        else:
            print(f"No se puede realizar cambio de membresía a: {Familiar.suscripciones[op_cliente]}" if (op_cliente) < 5 else 'Opción inválida')

    def cancelar_suscripcion(correo_electronico, numero_tarjeta):
        print(f'\nSuscripción cancelada con éxito\nDisfrute de su suscripción Gratis')
        Gratis._crear_nueva_membresia(correo_electronico, numero_tarjeta)

    def control_parental():
        return f"La funcionabilidad de control parental es activa (^.^)."

class Pro(Membresia):
    costo:int = 7000
    cant_max_disp:int = 6
    dias_regalo:int = 15
    op_cambiar_suscripcion:list = [1,3]
    suscripciones = {1: 'Básica',2: 'Familiar',3: 'Sin Conexión',4: 'Pro'}

    def __init__(self, correo_electronico, numero_tarjeta):
        Membresia.__init__(self, correo_electronico, numero_tarjeta)

    def _crear_nueva_membresia(correo_electronico, numero_tarjeta):
        user = Pro(correo_electronico, numero_tarjeta)
        print(f'Cuenta Pro creada con satisfacción.\nSu usuario es: {user.correo_electronico}\nMonto del plan: {Pro.costo}\nCuenta con Días de Regalo: {Pro.dias_regalo}\nCantidad máxima de equipos: {Pro.cant_max_disp}')

    def cambiar_suscripcion(op_cliente, correo_electronico, numero_tarjeta):
        if op_cliente in Pro.op_cambiar_suscripcion:
            if Pro.suscripciones[op_cliente]  == 'Básica':
                Basica._crear_nueva_membresia(correo_electronico, numero_tarjeta)
            else:
                SinConexion._crear_nueva_membresia(correo_electronico, numero_tarjeta)
        else:
            print(f"No se puede realizar cambio de membresía a: {Pro.suscripciones[op_cliente]}" if (op_cliente) < 5 else 'Opción inválida')

    def cant_max_contenido():
        return f"La cantidad máxima de contenidos que puedes descargar es (^.^)."

    def control_parental():
        return f"La funcionabilidad de control parental es activa (^.^)."
