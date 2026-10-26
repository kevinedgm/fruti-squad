# User flow · registrar una consulta

**Entrada:** «Hoy» → cita del paciente (presencial o teleconsulta) · **Endpoint observable:** consulta con padecimiento, diagnóstico(s) y tratamiento; paso 4 «Receta y cierre» habilitado.

```mermaid
flowchart LR
    E["Hoy · abrir cita"] --> T{"¿Teleconsulta?"}
    T -- Sí --> W["Sala de espera"] --> A["Admitir y empezar"] --> P1
    T -- No --> P1["Paso 1 · Exploración y padecimiento"]
    P1 --> V1{"¿Padecimiento escrito?"}
    V1 -- No --> X1["Error junto al campo · foco"] --> P1
    V1 -- Sí --> P2["Paso 2 · Diagnóstico y tratamiento"]
    P2 --> C{"¿Medicamento contraindicado?"}
    C -- Sí --> J["Elegir otro o justificar"] --> P2
    C -- No --> P2
    P2 --> V2{"¿Al menos un diagnóstico? (supuesto)"}
    V2 -- No --> X2["Error · foco al buscador"] --> P2
    V2 -- Sí --> P3["Paso 3 · Estudios (opcional)"] --> P4["Paso 4 · Receta y cierre"]
    P1 -. herramienta .-> H["Herramienta de apoyo junto a la consulta"] -. Cerrar / Esc .-> P1
    P2 -. sin conexión .-> R["Se guarda local; catálogos bloqueados con aviso"] --> P2
```

| Paso | Intención | Error posible | Recuperación | ¿Se puede volver? |
|---|---|---|---|---|
| Sala de espera | Admitir al paciente | Sin cámara/permiso | Mensaje + cómo dar permiso; seguir sin video | Sí |
| Paso 1 | Registrar signos y padecimiento | Padecimiento vacío; valor fuera de rango | Error con sugerencia; aviso con rango normal | Sí |
| Paso 2 | Diagnosticar y tratar | Sin diagnósticos; contraindicación; pauta incompleta | Error + foco; justificar o elegir otro; error junto al campo | Sí, quitar con deshacer |
| Herramienta | Consultar sin salir | Error al cargar | «Reintentar»; la consulta sigue | Cerrar / Esc |
