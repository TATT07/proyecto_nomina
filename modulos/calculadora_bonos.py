class CalculadoraBonos:
    """Módulo base para cálculo de bonos"""

    def calcular_bonos(self, empleado):
        """
        Calcula bonos en base a:
         - bonos por antigüedad (1% por año, hasta 10%)
         - bono por desempeño (si 'desempeno' en empleado)
        """
        salario = empleado.get('salario_base', 0)
        antiguedad = empleado.get('anios_antiguedad', 0)
        desempeno = empleado.get('desempeno', 'medio')  # 'alto','medio','bajo'

        bono_antiguedad = salario * min(antiguedad, 10) * 0.01
        bono_desempeno = 0
        if desempeno == 'alto':
            bono_desempeno = salario * 0.05
        elif desempeno == 'medio':
            bono_desempeno = salario * 0.02
        else:
            bono_desempeno = 0

        return bono_antiguedad + bono_desempeno
