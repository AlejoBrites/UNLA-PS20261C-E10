# Estimaciones — Planning Poker

## US Pivote

> **"Agregar juego al carrito" (US10) = 3 Story Points**
>
> Fue elegida como US pivote porque es una funcionalidad comprendida por todo el equipo
> y presenta una complejidad media-baja, adecuada para usar como referencia relativa
> en las demás estimaciones.

## Escala Fibonacci utilizada

`1 — 2 — 3 — 5 — 8 — 13 — 21`

---

## Tabla de estimaciones

### Sprint 1 — Autenticación (completado ✅)

| ID   | Historia de Usuario                 | I1 | I2 | I3 | I4 | I5 | Ronda 1 | Ronda 2 | Ronda 3 | **Final** |
|------|-------------------------------------|----|----|----|----|----|---------|---------|---------|-----------:|
| US01 | Registro con email/teléfono         |  1 |  5 |  3 |  2 |  5 |  2      |  3      |         | **3**     |
| US02 | Validación de email/teléfono        |  5 |  5 |  5 |  3 |  3 |  5      |         |         | **5**     |
| US03 | Creación de contraseña              |  2 |  3 |  3 |  2 |  2 |  2      |         |         | **2**     |
| US04 | Inicio de sesión                    |  1 |  2 |  5 |  3 |  3 |  2      |  3      |         | **3**     |

**Total Sprint 1: 13 SP**

---

### Sprint 2 — Catálogo de juegos

| ID   | Historia de Usuario                 | I1 | I2 | I3 | I4 | I5 | Ronda 1 | Ronda 2 | Ronda 3 | **Final** |
|------|-------------------------------------|----|----|----|----|----|---------|---------|---------|-----------:|
| US05 | Gestión de sesión                   |  — |  — |  — |  — |  — |         |         |         | **2** ★   |
| US06 | Exploración de listado de juegos    |  5 |  8 |  5 |  3 |  3 |  5      |  5      |  5      | **5**     |
| US07 | Búsqueda de juegos por nombre       |  5 |  2 |  3 |  3 |  5 |  3      |         |         | **3**     |
| US08 | Visualización de detalles del juego |  5 |  8 |  3 |  3 |  3 |  3      |         |         | **3**     |

**Total Sprint 2: 13 SP**

---

### Sprint 3 — Carrito de compras

| ID   | Historia de Usuario                 | I1 | I2 | I3 | I4 | I5 | Ronda 1 | Ronda 2 | Ronda 3 | **Final** |
|------|-------------------------------------|----|----|----|----|----|---------|---------|---------|-----------:|
| US09 | Filtrado por categoría/género       |  2 |  3 |  3 |  5 |  5 |  3      |  5      |  5      | **5**     |
| US10 | Agregar juego al carrito ⭐          |  3 |  5 |  3 |  3 |  5 |  3      |         |         | **3**     |
| US11 | Visualizar carrito                  |  2 |  3 |  5 |  3 |  2 |  3      |         |         | **3**     |
| US12 | Eliminar juego del carrito          |  2 |  3 |  3 |  2 |  2 |  2      |  2      |         | **2**     |

**Total Sprint 3: 13 SP**

---

### Sprint 4 — Pagos y biblioteca inicial

| ID   | Historia de Usuario                 | Final     | Notas                        |
|------|-------------------------------------|----------:|------------------------------|
| US13 | Seleccionar método de pago          | **3** ★   | Propuesta (pendiente poker)  |
| US14 | Confirmar compra                    | **5** ★   | Propuesta (pendiente poker)  |
| US15 | Visualizar biblioteca de juegos     | **3** ★   | Propuesta (pendiente poker)  |

**Total Sprint 4: 11 SP**

---

### Sprint 5 — Gestión de descargas

| ID   | Historia de Usuario                 | Final     | Notas                        |
|------|-------------------------------------|----------:|------------------------------|
| US16 | Descargar juego                     | **3** ★   | Propuesta (pendiente poker)  |
| US17 | Instalar juego                      | **3** ★   | Propuesta (pendiente poker)  |
| US18 | Actualizar juego                    | **2** ★   | Propuesta (pendiente poker)  |

**Total Sprint 5: 8 SP**

---

## Resumen general

| Sprint   | Story Points | Estado        |
|----------|-------------|---------------|
| Sprint 1 | 13 SP       | ✅ Completado  |
| Sprint 2 | 13 SP       | 🔄 Pendiente   |
| Sprint 3 | 13 SP       | 🔄 Pendiente   |
| Sprint 4 | 11 SP       | 🔄 Pendiente   |
| Sprint 5 | 8 SP        | 🔄 Pendiente   |
| **Total**| **58 SP**   |               |

---

## Notas del proceso

Las diferencias iniciales entre estimaciones en los sprints 1–3 se resolvieron mediante discusión colaborativa, siguiendo el enfoque de Planning Poker y convergiendo a una estimación consensuada. El proceso habitual fue:

1. Cada integrante elige su carta en silencio.
2. Se revelan simultáneamente.
3. El de mayor y menor estimación argumentan su postura.
4. Se repite hasta consenso (máx. 3 rondas).

> ★ Estimaciones marcadas como propuesta deben validarse en la próxima sesión de Planning Poker.
> ⭐ US Pivote = 3 SP (referencia relativa acordada por todo el equipo).
