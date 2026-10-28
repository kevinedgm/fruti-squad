# User flow · entrar a Nabi

**Entrada:** abrir Nabi o cerrar sesión · **Endpoint observable:** «Listo» en el botón y transición al inicio de Nabi.

```mermaid
flowchart LR
    E["Inicio de sesión"] --> C{"¿Hay conexión?"}
    C -- No --> O["Aviso sin conexión · Entrar deshabilitado con motivo"] -. vuelve la red .-> E
    C -- Sí --> F["Correo + contraseña"] --> V{"¿Formato de correo válido?"}
    V -- No --> X["Error junto al campo"] --> F
    V -- Sí --> S["Verificando…"] --> A{"¿Credenciales correctas?"}
    A -- Sí --> OK["Listo · entrar al inicio"]
    A -- No --> N{"¿Quedan intentos?"}
    N -- Sí --> R["Error arriba: causa + intentos restantes"] --> F
    N -- No --> B["Cuenta bloqueada 15 min (supuesto) · contacto de sistemas"]
    F -. olvidé .-> P["Recuperar contraseña (fuera de la ronda)"]
```

| Paso | Intención | Error posible | Recuperación | ¿Se puede volver? |
|---|---|---|---|---|
| Formulario | Escribir credenciales | Formato de correo | Mensaje junto al campo | Sí |
| Verificando | Esperar | Red lenta | La carga sigue; lo escrito se conserva | Sí |
| Error | Corregir | Contraseña incorrecta | Mensaje con intentos restantes | Sí |
| Bloqueo | Saber qué hacer | — | Tiempo de espera + contacto | Tras el tiempo |
