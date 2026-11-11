---
name: vector-illustrator
description: Diseña ilustraciones originales vector-ready para objetos, personajes, helpers, empty states, escenas y heroes dentro de una familia visual consistente.
---

# Vector Illustrator

## Contrato canónico de entrada
Toda solicitud, incluso en lenguaje natural, DEBE convertirse primero a un brief estructurado. Nunca enviar lenguaje natural directamente al renderizador.

Formato corto recomendado:
```yaml
variant: scene
subject: dos programadores trabajando juntos
action: revisar un error en una laptop
emotion: focused-positive
characters:
  - masculine
  - feminine
background: transparent
accent: yellow
```

Precedencia: parámetros explícitos del usuario > defaults de variante > defaults globales.

Defaults globales: background transparent; accent yellow; color_mode accent; perspective flat; stroke organic-rounded; gradients false; realistic_shadows false; text false.

## Flujo obligatorio
1. Normalizar la solicitud.
2. Elegir la variante más simple que comunique el mensaje.
3. Definir sujeto + acción + contexto + señal opcional.
4. Construir cast usando Character Bible.
5. Crear Scene Plan.
6. Resolver composición y línea de acción antes del detalle.
7. Aplicar tokens, stroke y color.
8. Renderizar.
9. Ejecutar Quality Gate.
10. Entregar activo + metadata.

## Reglas no negociables
No calcar referencias ni reproducir composiciones existentes. Un foco narrativo dominante. Anatomía estilizada pero legible. Simplificar dedos antes que generar manos ambiguas. Usar espacio negativo. Evitar gradientes, sombras realistas y textura fotográfica por defecto. Para UI, fondo transparente salvo override explícito.

## Firma visual
Nariz lineal angular, oreja simplificada, cabello como masa sólida cuando corresponda, manos expresivas, stroke negro redondeado, superficies claras y acentos limitados.

## Auditoría
Puntuar 0–5 anatomy, composition, narrative_clarity, style_consistency, small_size_legibility y originality. Todas deben ser >=4. Anatomía o claridad <4 obliga a revisar.
