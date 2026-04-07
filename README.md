# 🎬 Notflix — Python Flet Course Project

> **A Netflix-inspired multiplatform app built with Python Flet, developed chapter by chapter as part of the course.**
> 📺 [Watch the full course on YouTube](https://youtu.be/sGtCDSKywfg)

---

## 🇬🇧 English

### What is this?

**Notflix** is a student project that mimics the look and feel of a streaming platform — without trying to be Netflix. It's built entirely with [Python Flet](https://flet.dev), a framework that lets you create native multiplatform apps (desktop, mobile, and web) using only Python.

The project is divided into **4 chapters**, each representing a completed phase of the app. Chapter 4 contains the final, fully working version.

### 📁 Project Structure (Chapter 4)

```
chapter_4/
├── assets/                  # Icons and static resources
├── src/
│   ├── components/          # Reusable UI components
│   │   ├── hero_banner.py   # Featured title banner
│   │   ├── logo.py          # App logo component
│   │   └── movie_card.py    # Poster card for each title
│   ├── config/
│   │   └── theme.py         # Global colors, typography and spacing
│   ├── data/
│   │   ├── movie_model.py   # Movie dataclass + CSV loader
│   │   └── netflix_titles.csv
│   ├── views/
│   │   ├── profile_view.py  # Profile selection screen
│   │   ├── home_view.py     # Catalog + search screen
│   │   └── detail_view.py   # Title detail screen
│   ├── main.py              # App entry point
│   └── router.py            # Navigation / routing logic
├── .gitignore
└── requirements.txt
```

### 🚀 Getting Started

**1. Clone the repository**

```bash
git clone <repo-url>
cd chapter_4
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the app**

```bash
cd src
flet run main.py
```

**5. Run on mobile (same Wi-Fi network required)**

```bash
flet run --android main.py
# or
flet run --ios main.py
```

**6. Run as web app**

```bash
flet run --web main.py
```

### 🧩 What You'll Learn in the Course

- Installing Flet and setting up your environment
- Flet controls and how to use them
- Modularization and project structure
- Creating reusable components
- Working with data models and CSV files
- Building views and navigation with a custom router
- Building a streaming-style app from scratch
- Live preview on desktop, mobile, and web
- Virtual environments and basic version control

### 📦 Requirements

```
flet>=0.80.0
```

> Made with 🐍 Python + ❤️ Flet by **Enrique Barros** · [Watch the course on YouTube](https://youtu.be/sGtCDSKywfg)

---

## 🇪🇸 Español

### ¿Qué es esto?

**Notflix** es un proyecto estudiantil que imita la apariencia de una plataforma de streaming — sin pretender ser Netflix. Está desarrollado íntegramente con [Python Flet](https://flet.dev), un framework que permite crear apps nativas multiplataforma (escritorio, móvil y web) usando únicamente Python.

El proyecto está dividido en **4 capítulos**, cada uno representando una fase completada de la app. El capítulo 4 contiene la versión final y completamente funcional.

### 📁 Estructura del Proyecto (Capítulo 4)

```
chapter_4/
├── assets/                  # Iconos y recursos estáticos
├── src/
│   ├── components/          # Componentes de UI reutilizables
│   │   ├── hero_banner.py   # Banner del título destacado
│   │   ├── logo.py          # Componente del logo
│   │   └── movie_card.py    # Tarjeta tipo póster para cada título
│   ├── config/
│   │   └── theme.py         # Colores, tipografía y espaciado global
│   ├── data/
│   │   ├── movie_model.py   # Dataclass Movie + cargador de CSV
│   │   └── netflix_titles.csv
│   ├── views/
│   │   ├── profile_view.py  # Pantalla de selección de perfil
│   │   ├── home_view.py     # Catálogo + buscador
│   │   └── detail_view.py   # Pantalla de detalle de un título
│   ├── main.py              # Punto de entrada de la app
│   └── router.py            # Lógica de navegación y rutas
├── .gitignore
└── requirements.txt
```

### 🚀 Cómo Ejecutar el Proyecto

**1. Clona el repositorio**

```bash
git clone <repo-url>
cd chapter_4
```

**2. Crea y activa un entorno virtual**

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

**3. Instala las dependencias**

```bash
pip install -r requirements.txt
```

**4. Ejecuta la app en escritorio**

```bash
cd src
flet run main.py
```

**5. Ejecuta en móvil (misma red Wi-Fi)**

```bash
flet run --android main.py
# o
flet run --ios main.py
```

**6. Ejecuta como app web**

```bash
flet run --web main.py
```

### 🧩 Qué Aprenderás en el Curso

- Instalar Flet y configurar el entorno de desarrollo
- Controles de Flet y cómo utilizarlos
- Modularización y estructura de proyecto
- Crear componentes reutilizables
- Trabajar con modelos de datos y archivos CSV
- Construir vistas y navegación con un router personalizado
- Desarrollar una app estilo streaming desde cero
- Vista previa en tiempo real en PC, móvil y web
- Entornos virtuales y control de versiones básico

### 📦 Requisitos

```
flet>=0.80.0
```

---

> Hecho con 🐍 Python + ❤️ Flet por **Enrique Barros** · [Ver curso en YouTube](https://youtu.be/sGtCDSKywfg)
