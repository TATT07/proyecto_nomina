# Proyecto Nómina – Pruebas de Integración Bottom-Up

Este repositorio contiene la implementación de un sistema de **cálculo de nómina** y la estrategia de pruebas de integración aplicando el enfoque **Bottom-Up**.

---

## 📌 Descripción del Proyecto
El objetivo del proyecto es construir el sistema de nómina de forma incremental, integrando y validando primero los **módulos base** (cálculo de ISR, seguro social, bonos, deducciones, etc.), y posteriormente integrando niveles superiores hasta completar la funcionalidad global.

Se aplicó el enfoque **Bottom-Up** porque:
- Permite validar los **módulos fundamentales** antes de subir a capas más complejas.
- Facilita detectar errores en cálculos básicos.
- Reduce el uso de stubs, ya que primero se prueban componentes reales de bajo nivel.

---
<img width="782" height="367" alt="diagrama" src="https://github.com/user-attachments/assets/224169b5-2a7b-4ae6-a2cb-0d805058abf3" />


## ⚙️ Tecnologías Utilizadas
- **Python 3.13**
- **Pytest** para pruebas unitarias e integración
- **Pytest-cov** para cobertura de código
- **Markdown** para documentación
- **Flowchart Online** para diagrama de integración

---

## 🚀 Ejecución de Pruebas
### Pruebas de Nivel Base
```bash
python -m pytest test_bottom_up.py::TestNivelBase -v
📸 Evidencia:

Pruebas de Integración
bash
Copiar código
python -m pytest test_bottom_up.py -v
📸 Evidencia:

📊 Cobertura de Código
Se midió la cobertura con:

bash
Copiar código
pytest --cov=src --cov-report=term-missing
📸 Evidencia:

🔗 Diagrama de Integración Bottom-Up
El siguiente diagrama representa el proceso de integración de módulos, comenzando desde los cálculos básicos (ISR, seguridad social, bonos, deducciones) hasta el módulo completo de nómina:

📸 Evidencia:

✅ Conclusiones
El enfoque Bottom-Up permitió validar correctamente los módulos de nómina.

Todos los tests pasaron con éxito en los diferentes niveles.

La estrategia facilitó integrar los componentes de forma ordenada y progresiva.

La cobertura obtenida demuestra un alto nivel de confianza en el sistema implementado.

👨‍💻 Autor: lisandro
📅 Fecha: Septiembre 2025

