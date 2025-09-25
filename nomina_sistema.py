from modulos.calculadora_impuestos import CalculadoraImpuestos
from modulos.calculadora_bonos import CalculadoraBonos
from modulos.calculadora_deducciones import CalculadoraDeducciones

class NominaSistema:
    """Sistema integrado usando módulos ya probados"""

    def __init__(self):
        # Integrar módulos base (ya probados)
        self.calc_impuestos = CalculadoraImpuestos()
        self.calc_bonos = CalculadoraBonos()
        self.calc_deducciones = CalculadoraDeducciones()

    def calcular_nomina_neta(self, empleado):
        salario = empleado.get('salario_base', 0)

        # Usar módulos ya validados
        isr = self.calc_impuestos.calcular_isr(salario)
        seguro = self.calc_impuestos.calcular_seguro_social(salario)
        bonos = self.calc_bonos.calcular_bonos(empleado)
        deducciones = self.calc_deducciones.calcular_deducciones(empleado)

        neto = salario + bonos - isr - seguro - deducciones
        return round(neto, 2)
