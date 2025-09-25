import pytest
from modulos.calculadora_impuestos import CalculadoraImpuestos
from modulos.calculadora_bonos import CalculadoraBonos
from modulos.calculadora_deducciones import CalculadoraDeducciones
from drivers.test_driver import TestDriver
from nomina_sistema import NominaSistema

class TestNivelBase:
    """Nivel 1: Prueba módulos atómicos"""

    def setup_method(self):
        self.calc_imp = CalculadoraImpuestos()
        self.driver_imp = TestDriver(self.calc_imp)

    def test_isr_salario_bajo(self):
        salario = 8000
        assert self.calc_imp.calcular_isr(salario) == 400  # 5%

    def test_isr_salario_medio(self):
        assert self.calc_imp.calcular_isr(15000) == 1500  # 10%

    def test_seguro_social(self):
        assert self.calc_imp.calcular_seguro_social(10000) == 625  # 6.25%

    def test_bonos_basico(self):
        calc_b = CalculadoraBonos()
        empleado = {'salario_base': 10000, 'anios_antiguedad': 3, 'desempeno': 'alto'}
        # antiguedad 3% = 300, desempeno alto 5% = 500 => total 800
        assert pytest.approx(calc_b.calcular_bonos(empleado), 0.01) == 800

    def test_deducciones_basico(self):
        calc_d = CalculadoraDeducciones()
        empleado = {'salario_base': 10000, 'deducciones_fijas': 50, 'deducciones_porcentaje': 0.01}
        # 50 + 100 = 150
        assert pytest.approx(calc_d.calcular_deducciones(empleado), 0.01) == 150

class TestIntegracion:
    """Nivel 2: Integración progresiva"""

    def setup_method(self):
        self.nomina = NominaSistema()

    def test_nomina_simple(self):
        empleado = {
            'salario_base': 10000,
            'anios_antiguedad': 2,
            'desempeno': 'medio',
            'deducciones_fijas': 0,
            'deducciones_porcentaje': 0
        }
        # cálculos manuales:
        # bonos: antiguedad 2% => 200, desempeno medio 2% => 200 => bonos 400
        # isr: 5% => 500
        # seguro: 6.25% => 625
        # neto = 10000 + 400 - 500 - 625 = 9275
        assert self.nomina.calcular_nomina_neta(empleado) == 9275.00

    def test_nomina_con_deducciones(self):
        empleado = {
            'salario_base': 25000,
            'anios_antiguedad': 5,
            'desempeno': 'alto',
            'deducciones_fijas': 200,
            'deducciones_porcentaje': 0.02
        }
        # Aquí solo comprobamos que devuelve un número y es razonable (>0)
        neto = self.nomina.calcular_nomina_neta(empleado)
        assert isinstance(neto, float)
        assert neto > 0
