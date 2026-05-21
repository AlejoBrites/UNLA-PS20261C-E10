# User Story Map — SteamWeb

> Versión basada en la sesión de USM del equipo.
> Organizado por actividades → tareas → historias de usuario (de arriba a abajo por prioridad).

---

## Mapa

| **ACTIVIDAD**  | **Autenticación y acceso** |                      | **Exploración de catálogo** | **Proceso de compra**  |              | **Uso de biblioteca**            |                                          |
|----------------|----------------------------|----------------------|-----------------------------|------------------------|--------------|----------------------------------|------------------------------------------|
| **TAREA**      | Crear cuenta               | Iniciar sesión       | Navegar en la tienda        | Gestión del carrito    | Pagar        | Acceso a la biblioteca           | Gestión de descargas y actualizaciones   |
| **Historia 1** | Registro con email/tel.    | Ingreso credenciales | Exploración del listado     | Agregar al carrito     | Seleccionar método de pago | Visualización de biblioteca  | Descargar juego                          |
| **Historia 2** | Validación email/tel.      | Verificación credenciales | Búsqueda por nombre    | Visualización carrito  | Confirmar compra | Categorización de juegos     | Visualización actualizaciones pendientes |
| **Historia 3** | Generación de contraseña   | Inicio de sesión     | Visualización detalles      | Eliminar del carrito   | Agregar juego a la biblioteca | Acceso a los juegos | Actualizar juego                    |
| **Historia 4** | Confirmación cuenta creada |                      | Filtrado por categorías     |                        |              | Iniciar juego                    |                                          |

---

## Lectura por épica

### Épica 1 — Autenticación y acceso
**App responsable:** `apps/users`

**Flujo completo:**
```
Registro (US01)
  → Validación email/tel. (US02)
  → Creación de contraseña (US03)
  → Confirmación de cuenta
  → Inicio de sesión (US04)
  → Gestión de sesión (US05)
```

### Épica 2 — Exploración de catálogo
**App responsable:** `apps/games`

**Flujo completo:**
```
Exploración del listado (US06)
  → Búsqueda por nombre (US07)
  → Filtrado por categoría (US09)
  → Visualización de detalles (US08)
```

### Épica 3 — Proceso de compra
**Apps responsables:** `apps/cart` + `apps/payments`

**Flujo completo:**
```
Agregar al carrito (US10)
  → Visualizar carrito (US11)
  → Eliminar del carrito (US12)  [opcional]
  → Seleccionar método de pago (US13)
  → Confirmar compra (US14)
  → Juego agregado a biblioteca automáticamente
```

### Épica 4 — Uso de biblioteca
**App responsable:** `apps/library`

**Flujo completo:**
```
Visualizar biblioteca (US15)
  → Descargar juego (US16)
  → Instalar juego (US17)
  → Jugar (botón habilitado)
  → Actualizar juego (US18) [cuando hay actualización]
```

---

## Notas
- La historia "Agregar a lista de deseados" fue mencionada durante la sesión pero **queda pendiente de discusión** para un sprint futuro.
- El acceso a la biblioteca está limitado a usuarios autenticados.
- El flujo de pago es simulado con saldo en cuenta (sin pasarela real).
