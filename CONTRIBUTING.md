# Guía de contribución — SteamWeb

## Distribución del equipo

| Integrante   | App responsable       | Branch base                  |
|--------------|-----------------------|------------------------------|
| Integrante 1 | `apps/users`          | `feature/users-*`            |
| Integrante 2 | `apps/games`          | `feature/games-*`            |
| Integrante 3 | `apps/cart`           | `feature/cart-*`             |
| Integrante 4 | `apps/payments`       | `feature/payments-*`         |
| Integrante 5 | `apps/library`        | `feature/library-*`          |

---

## Convención de nombres de branches

```
feature/<app>-<descripcion-corta>   → nueva funcionalidad
fix/<app>-<descripcion-corta>       → corrección de bug
docs/<descripcion-corta>            → solo documentación
refactor/<app>-<descripcion-corta>  → refactoring sin cambio de comportamiento
```

**Ejemplos:**
```
feature/users-register
feature/games-catalog
fix/cart-remove-item
docs/update-backlog
refactor/payments-checkout-flow
```

---

## Formato de commits (Conventional Commits)

```
<tipo>(<scope>): <descripción corta en minúsculas>
```

| Tipo       | Cuándo usarlo                                |
|------------|----------------------------------------------|
| `feat`     | Nueva funcionalidad                          |
| `fix`      | Corrección de un bug                         |
| `docs`     | Cambios solo en documentación                |
| `refactor` | Refactoring sin cambio de comportamiento     |
| `style`    | Formato, espacios, sin cambio de lógica      |
| `test`     | Agregar o modificar tests                    |
| `chore`    | Tareas de mantenimiento (deps, config, etc.) |

**Ejemplos:**
```
feat(users): agregar formulario de registro con email
fix(cart): corregir total cuando el carrito está vacío
docs(backlog): actualizar estado sprint 1
refactor(payments): extraer lógica de descuento de saldo
```

---

## Flujo de trabajo

1. Asegurate de estar en `main` actualizado:
   ```bash
   git checkout main
   git pull origin main
   ```
2. Crear tu branch:
   ```bash
   git checkout -b feature/users-register
   ```
3. Desarrollar, commitear frecuentemente.
4. Hacer push y abrir Pull Request a `main`.
5. Mínimo 1 aprobación de otro integrante antes de mergear.
6. El responsable del PR hace el merge una vez aprobado.

---

## Checklist antes de abrir un PR

- [ ] El código corre sin errores (`python manage.py runserver`)
- [ ] Las migraciones están generadas si se modificaron modelos
- [ ] No se commitea el archivo `.env`
- [ ] No se commitea `db.sqlite3`
- [ ] Los templates no tienen código Python embebido complejo (usar vistas)
- [ ] El PR describe qué US implementa y cómo probarlo
