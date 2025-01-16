# Clase base que representa un empleado
class Empleado:
    def __init__(self, nombre, salario):
        # Atributos encapsulados
        self.__nombre = nombre  # Atributo privado para el nombre del empleado
        self.__salario = salario  # Atributo privado para el salario del empleado

    # Método para obtener el nombre del empleado
    def get_nombre(self):
        return self.__nombre

    # Método para obtener el salario del empleado
    def get_salario(self):
        return self.__salario

    # Método que será sobrescrito en las clases derivadas
    def calcular_bono(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

# Clase derivada que representa un empleado a tiempo completo
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario, horas_extra):
        super().__init__(nombre, salario)  # Llamada al constructor de la clase base
        self.__horas_extra = horas_extra  # Atributo privado específico de empleados a tiempo completo

    # Sobrescritura del método calcular_bono
    def calcular_bono(self):
        # Bono es un porcentaje del salario más un extra por horas extra trabajadas
        return self.get_salario() * 0.12 + (self.__horas_extra * 22)

# Clase derivada que representa un empleado a tiempo parcial
class EmpleadoTiempoParcial(Empleado):
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        super().__init__(nombre, salario_por_hora * horas_trabajadas)  # Llamada al constructor de la clase base
        self.__salario_por_hora = salario_por_hora  # Atributo privado específico de empleados a tiempo parcial
        self.__horas_trabajadas = horas_trabajadas  # Atributo privado para las horas trabajadas

    # Sobrescritura del método calcular_bono
    def calcular_bono(self):
        # Bono es un porcentaje del salario total por horas trabajadas
        return self.get_salario() * 0.05

# Función para mostrar detalles del empleado y su bono
def mostrar_detalles_empleado(empleado: Empleado):
    print(f"Nombre: {empleado.get_nombre()}")
    print(f"Salario: {empleado.get_salario()}")
    print(f"Bono: {empleado.calcular_bono()}")

# Creación de instancias de las clases
empleado1 = EmpleadoTiempoCompleto("Sebastian", 2000, 12)
empleado2 = EmpleadoTiempoParcial("Laura", 17, 90)

# Uso de los métodos y demostración de funcionalidad
print("Detalles del Empleado a Tiempo Completo:")
mostrar_detalles_empleado(empleado1)
print("\nDetalles del Empleado a Tiempo Parcial:")
mostrar_detalles_empleado(empleado2)
