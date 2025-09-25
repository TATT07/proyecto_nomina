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
```bash
python -m pytest test_bottom_up.py::TestNivelBase -v
📸 Evidencia:
<img width="1468" height="378" alt="nomina1" src="https://github.com/user-attachments/assets/519924e6-f812-4981-a5ec-df0a5369a0f9" />

Pruebas de Integración
bash
Copiar código
python -m pytest test_bottom_up.py -v
📸 Evidencia:
<img width="1461" height="387" alt="nomina2" src="https://github.com/user-attachments/assets/9b9272d2-bf40-4e2d-95a8-b57cd8461b51" />

📊 Cobertura de Código
Se midió la cobertura con:

bash
Copiar código
pytest --cov=src --cov-report=term-missing
📸 Evidencia:

🔗 Diagrama de Integración Bottom-Up
El siguiente diagrama representa el proceso de integración de módulos, comenzando desde los cálculos básicos (ISR, seguridad social, bonos, deducciones) hasta el módulo completo de nómina:

📸 Evidencia:
<img width="782" height="367" alt="diagrama" src="https://github.com/user-attachments/assets/83c6f7d7-bf86-4c45-919c-59bd5df18c14" />

✅ Conclusiones
El enfoque Bottom-Up permitió validar correctamente los módulos de nómina.

Todos los tests pasaron con éxito en los diferentes niveles.

La estrategia facilitó integrar los componentes de forma ordenada y progresiva.

La cobertura obtenida demuestra un alto nivel de confianza en el sistema implementado.

👨‍💻 Autor: lisandro
📅 Fecha: Septiembre 2025

