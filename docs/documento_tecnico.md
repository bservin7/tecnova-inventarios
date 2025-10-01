# Documento Técnico – Proyecto TechNova Inventarios

## 1. Selección de la metodología ágil
Para este proyecto elegí Scrum porque es una metodología ligera y muy usada en el desarrollo de software.  
Scrum se organiza en iteraciones llamadas sprints que son periodos cortos de trabajo. Esto permite dividir el proyecto en partes pequeñas y tener avances visibles.  
Además, facilita integrar nuevas ideas o corregir errores sin que el proyecto se detenga.

---

## 2. Especificación de la arquitectura
La arquitectura es modular y simple, adecuada para un proyecto pequeño:

- **`src/`**: contiene el código principal (funciones para manejar el inventario).
- **`tests/`**: contiene las pruebas automatizadas (usando `pytest`).
- **`docs/`**: documentación técnica (este archivo).
- **`.github/workflows/`**: configuración de GitHub Actions para la integración continua.

Esto asegura que el código esté separado por responsabilidades y sea fácil de mantener.

---

## 3. Selección de patrones de diseño
No utilicé un patrón complejo porque el alcance es pequeño. Sin embargo, apliqué la idea de **modularidad** y **responsabilidad única**:
- Cada función hace solo una cosa (`calcular_stock`, `agregar_producto`, `eliminar_producto`).
- Esto sigue el principio de diseño **SRP (Single Responsibility Principle)**.

---

## 4. Plan de pruebas
El plan se dividió en **3 pruebas automatizadas** y **1 prueba manual**:

### Pruebas automatizadas (con `pytest`):
1. **Calcular stock**: verifica que la función reste correctamente las salidas de inventario.  
2. **Agregar producto**: valida que el stock se incremente con nuevas entradas.  
3. **Eliminar producto**: asegura que el stock no baje de cero al retirar productos.  

### Prueba manual:
Abrí el archivo de código en VS Code y probé con valores simples directamente en un script (`print(calcular_stock(10, 3))`) para comprobar que los resultados fueran los esperados.  
Esto sirve como validación inicial antes de automatizar.

---

## 5. Configuración del repositorio
El repositorio se creó en **GitHub** con la siguiente estructura:

tecnova-inventarios/
│
├── src/
│ └── inventario.py
├── tests/
│ └── test_inventario.py
├── docs/
│ └── documento_tecnico.md
├── .github/
│ └── workflows/
│ └── main.yml
└── README.md


El archivo `main.yml` define el **pipeline de CI/CD** que corre automáticamente las pruebas cada vez que hago un push o un pull request.

---

## 6. Pipeline de integración continua
Configuré un **workflow de GitHub Actions** con estas características:
- Usa la versión de Python 3.10 en la nube.
- Instala dependencias (pytest).
- Ejecuta todas las pruebas dentro de la carpeta `tests/`.
- Si todo pasa, aparece una palomita verde en la sección **Actions** de GitHub.  
- Si alguna prueba falla, GitHub marca una x roja y muestra el error.

Esto asegura que el código se valide automáticamente sin depender de mi computadora.

---

## 7. Conclusiones personales
Fue mi primera experiencia haciendo un pipeline y pruebas automatizadas.  
Al inicio me costó entender cómo organizar carpetas y configurar GitHub Actions, pero logré que todo funcionara.  
Aprendí la importancia de dividir el código en funciones pequeñas y probar cada parte para evitar errores.  
Aunque no fue fácil, el resultado es un proyecto que corre pruebas automáticamente y me da más confianza en el código.
