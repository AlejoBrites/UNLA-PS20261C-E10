# User Stories — SteamWeb

---

## US01 — Registro con email/teléfono
**Prioridad:** Alta | **SP:** 3 | **Sprint:** 1 | **App:** users

**Descripción:**
> Como usuario nuevo,
> quiero registrarme con mi email o teléfono,
> para poder crear una cuenta y usar la app.

**Criterios de aceptación:**
- Dado que soy un usuario nuevo, cuando ingreso un email/teléfono válido, entonces puedo crear una cuenta.
- Dado que ingreso un email/teléfono inválido, cuando intento registrarme, entonces el sistema muestra un error descriptivo.

---

## US02 — Validación de email/teléfono
**Prioridad:** Alta | **SP:** 5 | **Sprint:** 1 | **App:** users

**Descripción:**
> Como nuevo usuario con email/teléfono,
> quiero validar los datos ingresados,
> para confirmar mi registro y confirmar mi identidad.

**Criterios de aceptación:**
- Dado que finalicé el formulario de registro inicial, cuando el sistema procesa mis datos, entonces me envía un código único de verificación (OTP) al medio seleccionado y me muestra la pantalla de ingreso del código.
- Dado que ingreso el código incorrecto, cuando intento confirmar, entonces el sistema muestra un mensaje de error y permite reintentar.

---

## US03 — Creación de contraseña
**Prioridad:** Alta | **SP:** 2 | **Sprint:** 1 | **App:** users

**Descripción:**
> Como usuario nuevo con email/teléfono validado,
> quiero generar una contraseña segura,
> para confirmar mi registro y proteger mi cuenta.

**Criterios de aceptación:**
- Dado que me encuentro en el formulario de registro, cuando ingreso una nueva contraseña, entonces el sistema valida que cumpla los requisitos mínimos de seguridad (longitud, caracteres).
- Dado que las contraseñas no coinciden, cuando intento confirmar, entonces el sistema muestra un error indicando la discrepancia.

---

## US04 — Inicio de sesión
**Prioridad:** Alta | **SP:** 3 | **Sprint:** 1 | **App:** users

**Descripción:**
> Como usuario registrado,
> quiero ingresar mis credenciales,
> para acceder a mi cuenta, biblioteca y tienda.

**Criterios de aceptación:**
- Dado que ingreso credenciales correctas, cuando inicio sesión, entonces accedo a mi cuenta y soy redirigido al catálogo de juegos.
- Dado que ingreso credenciales incorrectas, cuando intento ingresar, entonces el sistema muestra un mensaje de error sin revelar cuál campo es incorrecto.

---

## US05 — Gestión de sesión (mantener sesión iniciada)
**Prioridad:** Alta | **SP:** 2 | **Sprint:** 1 | **App:** users

**Descripción:**
> Como usuario autenticado,
> quiero que mi sesión se mantenga activa,
> para no tener que volver a iniciar sesión cada vez que uso la app.

**Criterios de aceptación:**
- Dado que inicié sesión, cuando navego por la plataforma, entonces mi sesión permanece activa durante la visita.
- Dado que cierro el navegador, cuando vuelvo a abrir la app, entonces puedo configurar si quiero que la sesión persista o no.

---

## US06 — Landing page y catálogo básico
**Prioridad:** Alta | **SP:** 5 | **Sprint:** 1 | **App:** users / games

**Descripción:**
> Como visitante del sitio,
> quiero ver una página de inicio que describa el producto y una grilla de juegos disponibles,
> para entender qué ofrece la plataforma antes de registrarme.

**Criterios de aceptación:**
- Dado que accedo a `/` sin sesión iniciada, cuando cargo la página, entonces veo la landing con el nombre del producto, una descripción y botones de "Crear cuenta" e "Iniciar sesión".
- Dado que accedo a `/` con sesión iniciada, cuando cargo la página, entonces soy redirigido automáticamente a `/games/`.
- Dado que accedo a `/games/`, cuando cargo la página, entonces veo la grilla de juegos disponibles con imagen (o placeholder), título, categoría y precio.
- Dado que no hay juegos cargados, cuando accedo a `/games/`, entonces el sistema muestra un mensaje indicando que no hay juegos disponibles.

---

## US07 — Exploración de listado de juegos
**Prioridad:** Alta | **SP:** 5 | **Sprint:** 2 | **App:** games

**Descripción:**
> Como usuario con sesión iniciada,
> quiero explorar juegos,
> para descubrir nuevas opciones sin perder tiempo.

**Criterios de aceptación:**
- Dado que ingreso a la tienda, cuando navego categorías, entonces puedo ver distintos juegos con su título, imagen y precio.
- Dado que la lista tiene muchos juegos, cuando la cargo, entonces se muestra de forma organizada y rápida.

---

## US08 — Búsqueda de juegos por nombre
**Prioridad:** Media | **SP:** 3 | **Sprint:** 3 | **App:** games

**Descripción:**
> Como usuario,
> quiero buscar un juego,
> para evaluar la opción de adquirirlo.

**Criterios de aceptación:**
- Dado que me encuentro en la tienda de juegos, cuando ingreso el nombre de un juego en la barra de búsqueda, entonces el sistema muestra los juegos relacionados con el texto ingresado.
- Dado que no hay resultados, cuando realizo una búsqueda, entonces el sistema muestra un mensaje indicando que no se encontraron juegos.

---

## US09 — Visualización de detalles del juego
**Prioridad:** Media | **SP:** 3 | **Sprint:** 2 | **App:** games

**Descripción:**
> Como usuario,
> quiero ver detalles de un juego,
> para decidir si comprarlo.

**Criterios de aceptación:**
- Dado que selecciono un juego, cuando ingreso a su página, entonces veo descripción, precio, desarrollador y categoría.
- Dado que ya tengo el juego en mi biblioteca, cuando veo su detalle, entonces el sistema indica que ya está en mi biblioteca.

---

## US10 — Filtrado por categoría/género
**Prioridad:** Media | **SP:** 5 | **Sprint:** 3 | **App:** games

**Descripción:**
> Como usuario con sesión iniciada,
> quiero filtrar juegos,
> para encontrar opciones según mis preferencias.

**Criterios de aceptación:**
- Dado que estoy explorando juegos, cuando aplico un filtro de categoría, entonces se actualiza la lista mostrando solo los juegos de esa categoría.
- Dado que selecciono una categoría sin juegos disponibles, cuando aplico el filtro, entonces el sistema muestra un mensaje indicando que no hay resultados.

---

## US11 — Agregar juego al carrito
**Prioridad:** Alta | **SP:** 2 | **Sprint:** 2 | **App:** cart

> **US Pivote**: referencia base para estimaciones relativas del equipo.

**Descripción:**
> Como usuario registrado,
> quiero agregar un juego seleccionado al carrito de compras,
> para guardarlo antes de proceder al pago.

**Criterios de aceptación:**
- Dado que me encuentro en la página de detalles de un juego disponible, cuando hago clic en "Agregar al carrito", entonces el juego se agrega exitosamente al carrito y se actualiza el indicador de la barra superior.
- Dado que el juego ya está en el carrito, cuando intento agregarlo nuevamente, entonces el sistema muestra un mensaje informativo indicando que el juego ya está en el carrito.
- Dado que el juego ya está en mi biblioteca, cuando intento agregarlo al carrito, entonces el sistema me informa que ya lo poseo.

---

## US12 — Visualizar carrito
**Prioridad:** Alta | **SP:** 3 | **Sprint:** 2 | **App:** cart

**Descripción:**
> Como usuario en proceso de compra,
> quiero acceder a mi carrito,
> para visualizar los productos a comprar.

**Criterios de aceptación:**
- Dado que tengo juegos agregados al carrito, cuando ingreso al carrito, entonces el sistema muestra la lista de juegos seleccionados con sus precios y el total.
- Dado que el carrito está vacío, cuando ingreso, entonces el sistema muestra un mensaje indicando que no hay ítems y ofrece ir a la tienda.

---

## US13 — Eliminar juego del carrito
**Prioridad:** Media | **SP:** 2 | **Sprint:** 2 | **App:** cart

**Descripción:**
> Como usuario con carrito,
> quiero acceder a mi carrito,
> para eliminar un juego seleccionado.

**Criterios de aceptación:**
- Dado que tengo juegos en el carrito, cuando selecciono la opción "eliminar" sobre un juego, entonces el sistema elimina el juego del carrito y actualiza el total.
- Dado que elimino el último juego del carrito, cuando lo remuevo, entonces el carrito queda vacío y se muestra el mensaje correspondiente.

---

## US14 — Seleccionar método de pago
**Prioridad:** Alta | **SP:** 3 | **Sprint:** 2 | **App:** payments

**Descripción:**
> Como usuario con ítems en el carrito,
> quiero seleccionar un método de pago,
> para proceder con la compra.

**Criterios de aceptación:**
- Dado que accedo al checkout, cuando veo la pantalla de pago, entonces puedo ver mi saldo disponible y el total a pagar.
- Dado que el saldo es insuficiente, cuando visualizo el checkout, entonces el sistema indica la diferencia y deshabilita el botón de confirmar.

---

## US15 — Confirmar compra
**Prioridad:** Alta | **SP:** 5 | **Sprint:** 2 | **App:** payments

**Descripción:**
> Como usuario con saldo suficiente,
> quiero confirmar mi compra,
> para adquirir los juegos y que queden en mi biblioteca.

**Criterios de aceptación:**
- Dado que tengo saldo suficiente y confirmo la compra, cuando el sistema procesa el pago, entonces descuenta el monto de mi saldo, genera la orden aprobada y agrega los juegos a mi biblioteca.
- Dado que no tengo saldo suficiente, cuando intento confirmar, entonces el sistema rechaza la compra y muestra el motivo sin realizar cambios en el saldo.

---

## US16 — Visualizar biblioteca de juegos
**Prioridad:** Media | **SP:** 2 | **Sprint:** 2 | **App:** library

**Descripción:**
> Como usuario,
> quiero tener una biblioteca,
> para acceder a mis juegos.

**Criterios de aceptación:**
- Dado que compré un juego, cuando ingreso a mi biblioteca, entonces puedo verlo disponible con su estado actual.
- Dado que la biblioteca está vacía, cuando accedo, entonces el sistema muestra un mensaje indicando que no hay juegos y ofrece ir a la tienda.

---

## US17 — Descargar juego
**Prioridad:** Media | **SP:** 3  | **Sprint:** 4 | **App:** library

**Descripción:**
> Como usuario con sesión iniciada,
> quiero descargar los archivos del juego desde mi biblioteca,
> para poder instalarlo y jugarlo.

**Criterios de aceptación:**
- Dado que tengo un juego en estado "No instalado" en mi biblioteca, cuando inicio la descarga, entonces el estado cambia a "Descargando".
- Dado que el juego está descargando, cuando el proceso finaliza, entonces el estado permite continuar con la instalación.

---

## US18 — Instalar juego
**Prioridad:** Media | **SP:** 3  | **Sprint:** 4 | **App:** library

**Descripción:**
> Como usuario con juego descargado,
> quiero instalar el juego,
> para poder jugarlo.

**Criterios de aceptación:**
- Dado que el juego está en estado "Descargando", cuando ejecuto la instalación, entonces el estado cambia a "Instalado".
- Dado que el juego está instalado, cuando accedo a él en la biblioteca, entonces aparece el botón "Jugar".

---

## US19 — Actualizar juego
**Prioridad:** Baja | **SP:** 2  | **Sprint:** 4 | **App:** library

**Descripción:**
> Como usuario con juegos descargados,
> quiero que mis juegos se encuentren actualizados,
> para jugar la última versión del juego.

**Criterios de aceptación:**
- Dado que hay una actualización disponible para un juego, cuando descargo la misma, entonces el estado vuelve a "Instalado" con la versión actualizada.
- Dado que el juego está en estado "Necesita actualización", cuando lo veo en la biblioteca, entonces aparece un badge indicando la actualización pendiente.

---

