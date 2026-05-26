# SteamWeb

> Plataforma de distribución digital de videojuegos para PC, desarrollada con Django.
> Proyecto universitario — UNLA, Ingeniería en Sistemas (2026).

---

## Descripción

SteamWeb es un ecosistema digital inspirado en Steam que permite a los usuarios explorar un catálogo de juegos, agregarlos a un carrito, comprarlos con saldo virtual y gestionar su biblioteca personal (descargar, instalar y actualizar).

El proyecto es desarrollado en equipo siguiendo metodologías ágiles (Scrum), con Product Backlog, User Story Mapping y estimaciones en Story Points (Fibonacci).

---

## Estado del proyecto

| Fase | Módulo | Responsable | Estado |
|------|--------|-------------|--------|
| 1 | Setup + Auth + Landing + Catálogo básico | Integrante 1 | ✅ Completada |
| 2 | Catálogo completo (detalle ✅ — búsqueda y filtros pendientes) | Integrante 2 | 🟡 En progreso |
| 3 | Carrito de compras | Integrante 3 | ✅ Completada |
| 4 | Checkout y pagos simulados | Integrante 4 | ✅ Completada |
| 5 | Biblioteca personal (vista ✅ — descarga/instalación pendientes) | Integrante 5 | 🟡 En progreso |
| 6 | Integración, testing y polish | Integrante 1 | 🔄 Pendiente |

---

## Funcionalidades principales

| Módulo         | Funcionalidades                                                                 | Estado |
|----------------|---------------------------------------------------------------------------------|--------|
| **Usuarios**   | Registro con email/teléfono, inicio de sesión, perfil, gestión de sesión        | ✅ Hecho |
| **Landing**    | Página de inicio con descripción del producto y CTAs de registro/login          | ✅ Hecho |
| **Juegos**     | Grilla de juegos disponibles con imagen, categoría y precio                     | ✅ Hecho |
| **Juegos**     | Página de detalle con descripción, desarrollador y botón de compra              | ✅ Hecho |
| **Juegos**     | Búsqueda por nombre y filtrado por categoría                                    | 🔄 Sprint 3 |
| **Carrito**    | Agregar/eliminar juegos, visualizar carrito con total, validación de duplicados  | ✅ Hecho |
| **Pagos**      | Checkout con saldo en cuenta, confirmación/rechazo según balance disponible     | ✅ Hecho |
| **Biblioteca** | Ver juegos adquiridos tras la compra                                            | ✅ Hecho |
| **Biblioteca** | Descargar, instalar y actualizar juegos (simulado)                              | 🔄 Sprint 3 |

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
git clone https://github.com/AlejoBrites/UNLA-PS20261C-E10.git
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
- **Inicio**: http://127.0.0.1:8000/
- **Tienda**: http://127.0.0.1:8000/games/
- **Admin**: http://127.0.0.1:8000/admin/

> Para agregar juegos de prueba, usá el panel de administración (`/admin/`).
> Podés asignarle saldo a un usuario desde Admin → Usuarios → editar usuario → campo "saldo".

---

## Pruebas manuales — Sprint 1 y Sprint 2

> Sprint 1 completado: US01–US06 (registro, validación, contraseña, login, sesión, landing y catálogo básico).
> Sprint 2 completado: US07, US09, US11–US16 (catálogo completo, detalle, carrito, pagos, biblioteca).

### Credenciales de desarrollo

```
Superusuario: admin / admin1234
Usuario demo: demo  / demo1234  (saldo: $200.00)
```

Panel de administración: http://127.0.0.1:8000/admin/

> Para probar el flujo de compra, asigná saldo a un usuario desde Admin → Usuarios → editar → campo "saldo".
> Agregá juegos de prueba desde Admin → Juegos.

---

### URLs disponibles

| URL | Descripción |
|-----|-------------|
| `/` | Landing page (sin sesión) o redirect a `/games/` (con sesión) |
| `/games/` | Catálogo de juegos disponibles |
| `/games/<slug>/` | Detalle de un juego |
| `/cart/` | Carrito de compras |
| `/cart/add/<id>/` | Agregar juego al carrito |
| `/cart/remove/<id>/` | Eliminar juego del carrito |
| `/payments/checkout/` | Revisión de compra y selección de pago |
| `/payments/confirm/` | Confirmar y procesar el pago |
| `/library/` | Biblioteca personal del usuario |
| `/users/register/` | Formulario de registro |
| `/users/login/` | Formulario de inicio de sesión |
| `/users/logout/` | Cierra sesión y redirige al login |
| `/users/profile/` | Perfil del usuario autenticado |
| `/admin/` | Panel de administración |

---

### Casos de prueba manuales

#### Landing page (`/`)
- **Sin sesión**: muestra la landing con nombre del producto, descripción y botones "Crear cuenta" / "Iniciar sesión".
- **Con sesión activa**: redirige automáticamente a `/games/`.

#### Catálogo (`/games/`)
- **Con juegos cargados**: muestra grilla con imagen (o placeholder), título, categoría y precio.
- **Sin juegos**: muestra mensaje "No hay juegos disponibles por el momento."
- **Sin sesión**: el botón de agregar muestra candado y redirige al login.

#### Detalle de juego (`/games/<slug>/`)
- **Juego existente**: muestra imagen, descripción, desarrollador, categoría, precio y botón "Agregar al carrito".
- **Sin sesión**: el botón muestra "Iniciar sesión para comprar".
- **Juego inexistente**: responde 404.

#### Carrito (`/cart/`)
- **Con ítems**: muestra lista de juegos con precios, total y botón "Continuar al pago".
- **Vacío**: muestra mensaje y enlace a la tienda.
- **Agregar juego ya en carrito**: mensaje informativo, no duplica.
- **Agregar juego ya en biblioteca**: mensaje de advertencia, no agrega.

#### Checkout (`/payments/checkout/`)
- **Saldo suficiente**: muestra total, saldo disponible y botón "Confirmar Compra" activo.
- **Saldo insuficiente**: muestra la diferencia y botón deshabilitado.
- **Carrito vacío**: redirige al catálogo.

#### Confirmación de pago (`/payments/confirm/`)
- **Pago exitoso**: descuenta saldo, crea la orden, agrega juegos a la biblioteca, vacía el carrito y redirige a `/library/`.
- **Saldo insuficiente (validación server-side)**: rechaza la operación sin modificar el saldo.

#### Biblioteca (`/library/`)
- **Con juegos comprados**: muestra grilla con los juegos adquiridos y badge "Comprado".
- **Sin juegos**: muestra mensaje y enlace a la tienda.
- **Sin autenticación**: redirige al login.

#### Registro (`/users/register/`)
- **Registro exitoso**: redirige al catálogo y queda logueado automáticamente.
- **Contraseñas no coinciden**: permanece en el formulario con mensaje de error.
- **Usuario duplicado**: error en el formulario.
- **Nuevo usuario tiene saldo 0**: verificable desde Admin → Usuarios.

#### Login (`/users/login/`)
- **Login exitoso**: credenciales correctas → redirige al catálogo.
- **Contraseña incorrecta**: permanece en la página de login.
- **Ya autenticado**: redirige al catálogo.

#### Perfil (`/users/profile/`)
- **Sin autenticación**: redirige a `/users/login/?next=/users/profile/`.
- **Con autenticación**: muestra nombre de usuario y saldo con formato local (`75,50`).

#### Logout (`/users/logout/`)
- Cerrar sesión → redirige a `/users/login/`.

---

### Tests automatizados

```bash
python manage.py test apps.users
```

Resultado esperado: **17 tests, 0 errores**.

```
Ran 17 tests in X.XXXs

OK
```

---

## Equipo

| Rol          | App responsable   | Branch                      |
|--------------|-------------------|-----------------------------|
| Integrante 1 | `apps/users`      | `feature/users-auth`        |
| Integrante 2 | `apps/games`      | `feature/games-catalog`     |
| Integrante 3 | `apps/cart`       | `feature/cart-management`   |
| Integrante 4 | `apps/payments`   | `feature/payments-checkout` |
| Integrante 5 | `apps/library`    | `feature/library-download`  |

---

## Documentación

- [Product Backlog](docs/product_backlog.md)
- [User Stories](docs/user_stories.md)
- [User Story Mapping](docs/usm.md)
- [Estimaciones (Planning Poker)](docs/estimaciones.md)
- [Lean Inception](docs/lean_inception.md)
- [Guía de contribución](CONTRIBUTING.md)
