# Flujo F0 · Hacer una pregunta (sin cuenta) · r01

Fuente: descripción del usuario (2026-11-04). Lo marcado [incógnita] no lo definió el usuario.

```mermaid
flowchart TD
    A["Inicio o Preguntas: «Haz tu pregunta»"] --> F["Formulario: pregunta + correo"]
    F -- "Falta algo o correo inválido" --> F
    F -- "Enviar" --> S1["Pantalla: Revisa tu correo"]
    S1 -.-> C1(["Correo 1: Confirma tu pregunta (enlace)"])
    C1 -- "Abre el enlace" --> S2["Pantalla: Pregunta confirmada, en revisión"]
    C1 -. "No llega o correo equivocado" .-> RE["Reenviar o corregir correo [incógnita]"] --> C1
    C1 -. "No la confirma" .-> VE["Se descarta tras un plazo [incógnita]"]
    S2 --> FI{"Filtro de calidad"}
    FI -- "Aprobada" --> PU["Pregunta publicada"]
    PU -.-> C2(["Correo 2: Tu pregunta fue publicada (enlace)"])
    FI -- "No aprobada" --> NO["No se publica"]
    NO -.-> C4(["Correo 4: Tu pregunta necesita cambios + motivo + enlace para reescribir"])
    C4 -- "Abre el enlace" --> RW["Formulario con su pregunta y el motivo arriba"]
    RW -- "Reenviar (sin volver a confirmar el correo)" --> FI
    PU --> MR["Un médico del expediente Manik responde"]
    MR -.-> C3(["Correo 3: «Dra. X respondió a tu pregunta» (enlace)"])
    C3 --> VR["Ve la respuesta → ficha del médico → agendar"]
```

## Estados de la pregunta
| Estado | Lo ve el público | Qué lo dispara | Correo |
|---|---|---|---|
| Pendiente de confirmar | No | Enviar el formulario | Correo 1 |
| En revisión | No | Abrir el enlace de confirmación | — |
| Publicada (sin respuesta) | Sí | Pasa el filtro | Correo 2 |
| Respondida | Sí | Responde un médico | Correo 3 (uno por médico [supuesto]) |
| Necesita cambios | No | No pasa el filtro | Correo 4 (motivo + enlace para reescribir) |
| Vencida | No | No se confirma a tiempo | [incógnita] |
