# SteamWeb

> Plataforma de distribución digital de videojuegos para PC, desarrollada con Django.
> Proyecto universitario — UNLA, Ingeniería en Sistemas (2026).

---

## Descripción

SteamWeb es un ecosistema digital inspirado en Steam que permite a los usuarios explorar un catálogo de juegos, agregarlos a un carrito, comprarlos con saldo virtual y gestionar su biblioteca personal (descargar, instalar y actualizar).

El proyecto es desarrollado en equipo siguiendo metodologías ágiles (Scrum), con Product Backlog, User Story Mapping y estimaciones en Story Points (Fibonacci).

---

## Funcionalidades principales

| Módulo         | Funcionalidades                                                                 |
|----------------|---------------------------------------------------------------------------------|
| **Usuarios**   | Registro con email/teléfono, validación, inicio de sesión, gestión de sesión    |
| **Juegos**     | Catálogo con búsqueda por nombre, filtrado por categoría, detalle de juego       |
| **Carrito**    | Agregar/eliminar juegos, visualizar carrito con total                            |
| **Pagos**      | Checkout con saldo en cuenta, confirmación/rechazo según balance disponible      |
| **Biblioteca** | Ver juegos adquiridos, descargar, instalar y actualizar (simulado)               |

---

## Tecnologías

| Tecnología        | Versión   | Uso                                      |
|-------------------|-----------|------------------------------------------|
| Python            | 3.12+     | Lenguaje principal                       |
| Django            | 6.0.5     | Framework web                            |
| SQLite            | —         | Base de datos (desarrollo)               |
| Bootstrap         | 5.3       | Framework de estilos (CDN)               |
| python-decouple   | 3.8       | Variables de entorno                     |
| Pillow            | 10.3      | Manejo de imágenes                       |

---

## Estructura del proyecto

```
SteamWeb/                   ← configuración Django (settings, urls, wsgi)
apps/
├── users/                  ← autenticación y perfiles
├── games/                  ← catálogo de juegos
├── cart/                   ← carrito de compras
├── payments/               ← órdenes y pagos simulados
└── library/                ← biblioteca personal del usuario
templates/                  ← HTML por app (base.html + subdirectorios)
static/                     ← CSS, JS e imágenes del proyecto
media/                      ← archivos subidos (imágenes de juegos/avatares)
docs/                       ← documentación del proyecto
manage.py
requirements.txt
.env.example
```

---

## Instalación

### Requisitos previos
- Python 3.12 o superior
- pip

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/UNLA-PS20261C-E10.git
cd UNLA-PS20261C-E10

# 2. Crear y activar entorno virtual
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus valores (SECRET_KEY, DEBUG, etc.)

# 5. Aplicar migraciones
python manage.py migrate

# 6. Crear superusuario (para acceder al admin)
python manage.py createsuperuser
```

---

## Cómo correr el proyecto

```bash
python manage.py runserver
```

Accedé a:
- **Tienda**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

> Para agregar juegos de prueba, usá el panel de administración (`/admin/`).
> Podés asignarle saldo a un usuario desde Admin → Usuarios → editar usuario → campo "saldo".

---

## Cómo probar la Fase 1 (autenticación de usuarios)

> Sprint 1 completado: US01–US04 (registro, validación, contraseña, inicio de sesión).

### Credenciales del superusuario de desarrollo

```
Usuario: admin
Contraseña: admin1234
```

Accedé al panel de administración en: http://127.0.0.1:8000/admin/

---

### URLs de la app `users`

| URL                           | Descripción                                  |
|-------------------------------|----------------------------------------------|
| `http://127.0.0.1:8000/`      | Redirige automáticamente al catálogo         |
| `/users/register/`            | Formulario de registro de nuevo usuario      |
| `/users/login/`               | Formulario de inicio de sesión               |
| `/users/logout/`              | Cierra sesión y redirige al login            |
| `/users/profile/`             | Perfil del usuario autenticado               |

---

### Casos de prueba manuales

#### Registro (`/users/register/`)
- **Registro exitoso**: completar todos los campos con datos válidos → redirige al catálogo y queda logueado automáticamente.
- **Contraseñas no coinciden**: `password1` ≠ `password2` → permanece en el formulario con mensaje de error.
- **Usuario duplicado**: intentar registrar un `username` ya existente → error en el formulario.
- **Nuevo usuario tiene saldo 0**: verificable desde Admin → Usuarios.

#### Login (`/users/login/`)
- **Login exitoso**: credenciales correctas → redirige al catálogo (`/games/`).
- **Contraseña incorrecta**: permanece en la página de login.
- **Usuario inexistente**: permanece en la página de login.
- **Ya autenticado**: acceder a `/users/login/` estando logueado → redirige al catálogo.

#### Perfil (`/users/profile/`)
- **Sin autenticación**: acceder a `/users/profile/` sin estar logueado → redirige a `/users/login/?next=/users/profile/`.
- **Con autenticación**: muestra nombre de usuario y saldo con formato local (`75,50` en lugar de `75.50`).

#### Logout (`/users/logout/`)
- Acceder a `/users/logout/` → cierra sesión y redirige a `/users/login/`.
- Intentar acceder a `/users/profile/` después → redirige al login.

---

### Correr los tests automatizados

```bash
python manage.py test apps.users
```

Debería mostrar **17 tests, 0 errores**:

```
Ran 17 tests in X.XXXs

OK
```

---

## Equipo

| Rol          | App responsable   |
|--------------|-------------------|
| Integrante 1 | `apps/users`      |
| Integrante 2 | `apps/games`      |
| Integrante 3 | `apps/cart`       |
| Integrante 4 | `apps/payments`   |
| Integrante 5 | `apps/library`    |

---

## Documentación

- [Product Backlog](docs/product_backlog.md)
- [User Stories](docs/user_stories.md)
- [User Story Mapping](docs/usm.md)
- [Estimaciones (Planning Poker)](docs/estimaciones.md)
- [Lean Inception](docs/lean_inception.md)
- [Guía de contribución](CONTRIBUTING.md)
