# Product Backlog — SteamWeb

## Definition of Ready (DoR)

Una User Story está lista para entrar a un sprint cuando cumple **todos** estos criterios:

- [ ] Tiene título y descripción clara (formato: Como… Quiero… Para…)
- [ ] Tiene criterios de aceptación definidos
- [ ] Fue estimada en Story Points (escala Fibonacci)
- [ ] Tiene prioridad asignada
- [ ] No tiene bloqueos externos conocidos
- [ ] Cumple el principio INVEST (Independiente, Negociable, Valiosa, Estimable, Small, Testeable)

## Definition of Done (DoD)

Una User Story se considera **terminada** cuando cumple **todos** estos criterios:

- [ ] El código funciona correctamente según los criterios de aceptación
- [ ] Pasó pruebas manuales por al menos un integrante diferente al autor
- [ ] No tiene errores críticos ni excepciones no controladas
- [ ] Fue integrada a la rama `main` mediante Pull Request aprobado
- [ ] Las migraciones están generadas y aplicadas (si hubo cambios en modelos)
- [ ] Tiene documentación mínima actualizada (README o docstring si aplica)

---

## Backlog completo

| ID    | Historia de Usuario                          | App         | Prioridad | Story Points | Sprint   | Estado      |
|-------|----------------------------------------------|-------------|-----------|-------------|----------|-------------|
| US01  | Registro con email/teléfono                  | users       | Alta      | 3           | Sprint 1 | ✅ Done     |
| US02  | Validación de email/teléfono                 | users       | Alta      | 5           | Sprint 1 | ✅ Done     |
| US03  | Creación de contraseña                       | users       | Alta      | 2           | Sprint 1 | ✅ Done     |
| US04  | Inicio de sesión                             | users       | Alta      | 3           | Sprint 1 | ✅ Done     |
| US05  | Gestión de sesión (mantener sesión iniciada) | users       | Alta      | 2 ★         | Sprint 2 | 🔄 To Do   |
| US06  | Exploración de listado de juegos             | games       | Alta      | 5           | Sprint 2 | 🔄 To Do   |
| US07  | Búsqueda de juegos por nombre                | games       | Media     | 3           | Sprint 2 | 🔄 To Do   |
| US08  | Visualización de detalles del juego          | games       | Media     | 3           | Sprint 2 | 🔄 To Do   |
| US09  | Filtrado por categoría/género                | games       | Media     | 5           | Sprint 3 | 🔄 To Do   |
| US10  | Agregar juego al carrito                     | cart        | Alta      | 3 ⭐ pivot  | Sprint 3 | 🔄 To Do   |
| US11  | Visualizar carrito                           | cart        | Alta      | 3           | Sprint 3 | 🔄 To Do   |
| US12  | Eliminar juego del carrito                   | cart        | Media     | 2           | Sprint 3 | 🔄 To Do   |
| US13  | Seleccionar método de pago                   | payments    | Alta      | 3 ★         | Sprint 4 | 🔄 To Do   |
| US14  | Confirmar compra                             | payments    | Alta      | 5 ★         | Sprint 4 | 🔄 To Do   |
| US15  | Visualizar biblioteca de juegos              | library     | Media     | 3 ★         | Sprint 4 | 🔄 To Do   |
| US16  | Descargar juego                              | library     | Media     | 3 ★         | Sprint 5 | 🔄 To Do   |
| US17  | Instalar juego                               | library     | Media     | 3 ★         | Sprint 5 | 🔄 To Do   |
| US18  | Actualizar juego                             | library     | Baja      | 2 ★         | Sprint 5 | 🔄 To Do   |

> ★ Estimación propuesta — pendiente de validación en sesión de Planning Poker.
> ⭐ US pivote elegida por el equipo (referencia de 3 SP para estimaciones relativas).

---

## Resumen por sprint

| Sprint   | US incluidas          | Story Points | Estado       |
|----------|-----------------------|-------------|--------------|
| Sprint 1 | US01–US04             | 13 SP       | ✅ Completado |
| Sprint 2 | US05–US08             | 13 SP       | 🔄 Pendiente  |
| Sprint 3 | US09–US12             | 13 SP       | 🔄 Pendiente  |
| Sprint 4 | US13–US15             | 11 SP       | 🔄 Pendiente  |
| Sprint 5 | US16–US18             | 8 SP        | 🔄 Pendiente  |
| **Total**|                       | **58 SP**   |              |
