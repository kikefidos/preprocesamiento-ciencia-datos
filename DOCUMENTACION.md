## 🔹 Introducción
El objetivo de este proyecto es desarrollar un flujo de preprocesamiento de datos usando Python, aplicando limpieza, normalización y escalado de variables numéricas. Además, se emplea Git y GitHub para controlar versiones y colaborar de forma eficiente.

---

## 🔹 Comandos Git Usados

| Comando | Descripción |
|----------|--------------|
| `git init` | Inicializa el repositorio local |
| `git clone` | Clona un repositorio remoto |
| `git checkout -b feature-preprocesamiento` | Crea una nueva rama |
| `git add .` | Agrega archivos al área de preparación |
| `git commit -m "mensaje"` | Registra cambios en el historial |
| `git push origin <rama>` | Sube los cambios a GitHub |
| `git merge` | Fusiona ramas |
| `git branch -d <rama>` | Elimina una rama local |
| `git push origin --delete <rama>` | Elimina una rama remota |

---

## 🔹 Automatización con GitHub Actions
Se puede crear un workflow básico para ejecutar pruebas automáticas cada vez que se haga un push:

Archivo: `.github/workflows/python-test.yml`
```yaml
name: Python CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"
      - name: Instalar dependencias
        run: |
          pip install pandas scikit-learn
      - name: Ejecutar script
        run: python preprocesamiento.py
