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


## ⚙️ Tecnologías Utilizadas
- **Python 3.13**
- **Pytest** para pruebas unitarias e integración
- **Pytest-cov** para cobertura de código
- **Markdown** para documentación
- **Flowchart Online** para diagrama de integración

---

## 🚀 Ejecución de Pruebas
### Pruebas de Nivel Base

python -m pytest test_bottom_up.py::TestNivelBase -v
📸 Evidencia:
<img width="782" height="367" alt="diagrama" src="https://github.com/user-attachments/assets/35634f91-17f3-4d8e-9ad2-4b22f9dd1fda" />

Pruebas de Integración
bash
Copiar código
python -m pytest test_bottom_up.py -v
##📸 Evidencia:

📊 Cobertura de Código
Se midió la cobertura con:


pytest --cov=src --cov-report=term-missing
📸 Evidencia:
<img width="1461" height="387" alt="nomina2" src="https://github.com/user-attachments/assets/2dc46519-a70a-4bf4-96d6-4e476a6161b3" />


🔗 Diagrama de Integración Bottom-Up
El siguiente diagrama representa el proceso de integración de módulos, comenzando desde los cálculos básicos (ISR, seguridad social, bonos, deducciones) hasta el módulo completo de nómina:

📸 Evidencia:
<img width="782" height="367" alt="diagrama" src="https://github.com/user-attachments/assets/f61ef5ff-89aa-49c2-a9a0-65734d1591ef" />


✅ Conclusiones
El enfoque Bottom-Up permitió validar correctamente los módulos de nómina.

Todos los tests pasaron con éxito en los diferentes niveles.

La estrategia facilitó integrar los componentes de forma ordenada y progresiva.

La cobertura obtenida demuestra un alto nivel de confianza en el sistema implementado.

👨‍💻 Autor: lisandro
📅 Fecha: Septiembre 2025
```
