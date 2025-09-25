# 🧮 Proyecto: Testing Bottom-Up - Sistema de Nómina

## 📌 Descripción
Este proyecto implementa **pruebas Bottom-Up** para un sistema de cálculo de nómina.  
Se comienza validando los módulos más básicos (impuestos, bonos y deducciones) usando **drivers de prueba** y luego se integran en un sistema completo (`NominaSistema`).  

El enfoque **Bottom-Up** permite:
- Validar primero las piezas atómicas del sistema.
- Construir confianza en los módulos antes de la integración.
- Detectar errores temprano en los cálculos.

---

## 🗂️ Estructura del Proyecto
proyecto_nomina/
├── modulos/
│ ├── init.py
│ ├── calculadora_impuestos.py
│ ├── calculadora_bonos.py
│ └── calculadora_deducciones.py
├── drivers/
│ ├── init.py
│ └── test_driver.py
├── nomina_sistema.py
├── test_bottom_up.py
└── README.md

yaml
Copiar código

---

## ⚙️ Requisitos
- Python 3.8+ (se probó en Python 3.13.7)
- pytest (`pip install pytest`)
- pytest-cov (`pip install pytest-cov`)

---

## ▶️ Ejecución de Pruebas

### Nivel 1: Pruebas de módulos base
```bash
python -m pytest test_bottom_up.py::TestNivelBase -v
Nivel 2: Pruebas de integración
bash
Copiar código
python -m pytest test_bottom_up.py::TestIntegracion -v
Cobertura (reporte HTML)
bash
Copiar código
python -m pytest --cov=modulos --cov-report=html
Abrir el archivo generado en htmlcov/index.html.

✅ Resultados esperados
Todos los módulos base deben pasar sus pruebas unitarias (5 passed).

La integración en NominaSistema debe calcular correctamente la nómina neta.

Cobertura esperada: >80% en módulos.

📸 Evidencias
Coloca en esta sección las capturas de pantalla de ejecución:

evidencias/pytest_nivel_base.png → salida de pruebas base.

evidencias/pytest_integracion.png → salida de integración.

evidencias/cobertura.png → captura de reporte coverage.

evidencias/diagrama.png → diagrama Bottom-Up.

Ejemplo de inclusión en el README:


### Ejemplo salida de pruebas (nivel base)
![Pruebas Nivel Base](evidencias/pytest_nivel_base.png)

### Ejemplo salida de cobertura
![Cobertura](evidencias/cobertura.png)
📊 Diagrama de Integración Bottom-Up

📝 Análisis
Se comprobó la validez de cada módulo por separado antes de integrarlos.

Con el enfoque Bottom-Up, la cobertura de pruebas se garantiza desde abajo hacia arriba.

Se facilita la detección de errores de cálculo antes de que impacten en el sistema completo.

📤 Entregables
Código fuente (.py)

Evidencias (/evidencias/ con capturas PNG/JPG)

Reporte HTML de cobertura (/htmlcov/)

Diagrama de integración (diagrama.png)

README.md (este archivo)

