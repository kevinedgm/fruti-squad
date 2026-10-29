# InicioEcosistema

La primera pantalla después de iniciar sesión: el ecosistema completo para que la persona elija a qué app ir.

- Flujo: inicio de sesión único → Inicio del ecosistema → app elegida. Desde cualquier app se vuelve con el botón del ecosistema («Ir al inicio del ecosistema»).
- Saludo en `display` (Urbanist 300) sobre «bruma» con los halos «luz-cian» y «luz-calida», como el directorio Manik, con el nombre y la clínica o grupo activo; «¿A qué app quieres ir?» como subtítulo.
- Una tarjeta por app en el orden fijo: sello a 52 px, nombre «Producto Manik», para quién es y qué hace en una línea. Al pasar el cursor, la tarjeta toma `app-<producto>-soft`.
- Apps sin acceso: visibles pero apagadas (sello en gris), con candado y «Sin acceso · pídelo a tu administrador de grupo»; `aria-disabled`. Así la persona sabe que existen y a quién pedirlas.
- Si la persona solo tiene una app, el inicio se salta y entra directo (propuesta, por confirmar).
- El consumidor provee: nombre y tratamiento, clínica o grupo activo, apps con y sin acceso, último uso.
