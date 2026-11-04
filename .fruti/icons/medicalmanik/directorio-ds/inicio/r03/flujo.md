# User flow · Encontrar médico desde el inicio

**Entrada:** escribe la dirección, abre la app o vuelve a Manik (sin cuenta: quien tiene cita entra por el enlace de su mensaje) (las entradas por buscador o enlace compartido van directo a resultados o perfil). · **Endpoint observable:** resultados de una especialidad cerca, perfil del médico buscado o detalle de la próxima cita.

```mermaid
flowchart TD
    E1["Escribe manik.mx o abre la app"] --> I["Inicio"]
    E2["Buscador web: «dermatólogo puebla»"] -.-> R["Resultados"]
    E3["Enlace compartido de un médico"] -.-> P["Perfil del médico"]
    E4["Mensaje de confirmación o recordatorio<br/>(SMS / WhatsApp, sin cuenta)"] -.-> DC["Detalle de su cita"]
    I --> Q{"¿Sabe qué necesita?"}
    Q -- "Especialidad" --> B["Buscador: qué + dónde"]
    Q -- "Nombre del médico" --> B
    Q -- "No sabe" --> S["Busca por lo que sientes"]
    S --> R
    B --> D{"¿Dónde?"}
    D -- "Ciudad aproximada" --> R
    D -- "Usar mi ubicación" --> U{"¿Permiso?"}
    U -- Sí --> R
    U -- No --> UW["Escribe tu colonia o ciudad"] --> R
    B -- "Elige un médico sugerido" --> P
    Q -- "Tiene una duda, aún no quiere cita" --> PA["Preguntas y artículos de médicos"]
    PA -- "Lee una respuesta o artículo" --> AU["Ficha del médico autor"] --> P
    PA -- "Ver especialistas del tema" --> R
    PA -- "No encuentra su duda" --> HP["Haz tu pregunta (cualquiera)"] --> AV["Responde un médico del expediente Manik · aviso por mensaje [incógnita]"]
    I --> M["Soy médico"] --> MD["Página para médicos"]
    R -. "pocos médicos cerca (zona sin cobertura densa)" .-> RE["Ampliar distancia o ver especialidad parecida"] --> R
    R --> P
```

| Paso | Intención | Error posible | Recuperación | ¿Se puede volver? |
|---|---|---|---|---|
| Inicio | Entender qué es Manik y empezar | Sin conexión | Aviso; lo estático funciona | — |
| Buscador | Decir qué y dónde | No sabe cómo se llama la especialidad | Sugerencias por síntoma y por nombre; «Busca por lo que sientes» | Sí (conserva lo escrito) |
| Dónde | Ubicar la búsqueda | Permiso denegado | Campo de colonia o ciudad; nunca bloquea | Sí |
| Lo que sientes | Orientarse sin saber de especialidades | No encuentra su síntoma | «Chequeo general» siempre presente | Sí |
| Resultados | Comparar | Nada cerca | Ampliar distancia o especialidad parecida | Sí (conserva filtros) |
| Detalle de su cita (desde el mensaje) | Revisar, cambiar o cancelar sin cuenta | Enlace vencido | Pedir un enlace nuevo con su celular | Sí |
| Preguntas y artículos de médicos | Resolver una duda antes de decidir | No hay respuesta para su duda | «Haz tu pregunta» o ver especialistas del tema | Sí |
| Haz tu pregunta | Preguntar sin cuenta | Nadie responde pronto | Mostrar especialistas del tema mientras espera | Sí |
