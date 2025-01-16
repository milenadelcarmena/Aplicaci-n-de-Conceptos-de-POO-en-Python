# Aplicaci-n-de-Conceptos-de-POO-en-Python

Explico mi Código


Clases y Herencia

•	Clase Base Empleado Esta clase define los atributos y métodos comunes a todos los empleados. Utiliza encapsulación al definir atributos privados (__nombre y __salario) y proporciona métodos públicos (get_nombre, get_salario) para acceder a ellos. También define un método calcular_bono que debe ser sobrescrito en las subclases.

•	Clases Derivadas EmpleadoTiempoCompleto y EmpleadoTiempoParcial: Ambas clases heredan de Empleado. Cada una tiene atributos específicos adicionales (__horas_extra para empleados a tiempo completo y __salario_por_hora, __horas_trabajadas para empleados a tiempo parcial). Ambas clases sobrescriben el método calcular_bono para proporcionar una lógica específica para el cálculo del bono.


Encapsulación
Los atributos en la clase base están encapsulados (marcados como privados) para proteger su acceso directo. Se utilizan métodos getter para acceder a estos atributos.


Polimorfismo
El polimorfismo se demuestra mediante la función mostrar_detalles_empleado, que acepta un objeto de tipo Empleado. Tanto EmpleadoTiempoCompleto como EmpleadoTiempoParcial implementan su propia versión del método calcular_bono, lo que permite que el mismo código funcione con diferentes tipos de empleados.

