class CalculadoraDeducciones:
    """Módulo para deducciones adicionales (ej. préstamos, anticipos)"""

    def calcular_deducciones(self, empleado):
        """
        Retorna la suma de deducciones fijas y porcentuales.
        Estructura esperada en 'empleado':
         - 'deducciones_fijas': número
         - 'deducciones_porcentaje': porcentaje sobre salario (0-1)
        """
        salario = empleado.get('salario_base', 0)
        ded_fijas = empleado.get('deducciones_fijas', 0)
        ded_pct = empleado.get('deducciones_porcentaje', 0)
        return ded_fijas + salario * ded_pct
