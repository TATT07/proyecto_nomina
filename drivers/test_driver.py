class TestDriver:
    """Driver para ejecutar pruebas en módulos base"""

    def __init__(self, modulo):
        self.modulo = modulo
        self.resultados = []

    def ejecutar_prueba_unitaria(self, metodo, parametros, esperado, tol=0.01):
        """Ejecuta una prueba y registra resultado"""
        resultado = getattr(self.modulo, metodo)(*parametros)
        exito = abs(resultado - esperado) <= tol

        self.resultados.append({
            'metodo': metodo,
            'exito': exito,
            'resultado': resultado,
            'esperado': esperado
        })

        assert exito, f"Fallo: {metodo} -> {resultado} != {esperado}"
        return f"✓ {metodo}: OK"
