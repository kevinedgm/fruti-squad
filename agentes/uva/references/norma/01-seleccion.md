# Norma de Uva · selección, semántica y lenguaje visual

> Parte de la *Guía y estándar de iconografía accesible* v1.0 (secciones §2–10). Índice y notas: `README.md` de esta carpeta. Se carga en E1 y E2.

## 2. Principios fundamentales

### 2.1 Diseñar significado antes que apariencia

Antes de elegir un icono debe definirse qué representa.

Incorrecto:

```text
Necesito un icono bonito para este botón.
```

Correcto:

```text
Esta acción elimina permanentemente un registro.
semanticName: delete
category: destructive-action
```

Después se selecciona la representación gráfica.

### 2.2 Claridad antes que originalidad

Un icono familiar suele ser preferible a uno visualmente original.

```text
Search    → magnifying glass
Delete    → trash
Edit      → pencil
Settings  → gear
Close     → X
```

La interfaz no debería obligar al usuario a aprender un nuevo idioma pictográfico para realizar operaciones comunes.

### 2.3 El icono no sustituye automáticamente al texto

Los iconos ayudan principalmente a: reconocimiento; escaneo; orientación; jerarquía; reducción de ruido visual.

Pero algunos conceptos son demasiado abstractos para comunicarse únicamente mediante símbolos. Cuando exista ambigüedad, utilizar `[icon] + Label` en lugar de `[icon]`.

### 2.4 Misma función → mismo icono

Una acción debe representarse consistentemente.

```text
delete   → Trash2
edit     → Pencil
search   → Search
settings → Settings
```

No utilizar alternativamente `Trash`, `Trash2`, `CircleX`, `X`, `MinusCircle` para representar la misma operación.

### 2.5 Funciones diferentes → iconos diferentes

No reutilizar el mismo símbolo para acciones conceptualmente diferentes. Por ejemplo, `Delete`, `Archive`, `Remove`, `Close`, `Cancel` no deberían compartir indiscriminadamente el mismo icono.

---

## 3. Taxonomía de iconos

Todo icono utilizado en el Design System debe pertenecer a una categoría semántica.

### 3.1 Decorative
No transmite información nueva. Ejemplo: `[+] Agregar usuario` — el texto ya comunica la acción; el icono es decorativo. Debe permanecer oculto para tecnologías asistivas.

### 3.2 Action
Representa una operación. Ejemplos: Edit, Delete, Copy, Download, Upload, Share, Save.

### 3.3 Navigation
Representa desplazamiento o cambio de contexto. Ejemplos: Home, Back, Forward, Previous, Next, External link.

### 3.4 Informative
Comunica información. Ejemplos: Location, Phone, Calendar, Time, Attachment.

### 3.5 Status
Representa un estado. Ejemplos: Success, Warning, Error, Information, Pending, Offline.

### 3.6 Toggle
Representa un estado binario. Ejemplos: Mute, Favorite, Visibility, Pin, Lock.

### 3.7 Disclosure
Controla contenido expandible. Ejemplos: ChevronDown, ChevronUp, ChevronRight.

### 3.8 Directional
Representa dirección. ArrowLeft, ArrowRight, ArrowUp, ArrowDown.

### 3.9 Object
Representa una entidad. Ejemplos: User, Folder, File, Calendar, Building, Database.

### 3.10 Brand
Representa identidad de marca. Los iconos genéricos de Lucide no deben sustituir logotipos cuando la identidad del tercero sea relevante.

---

## 4. Selección de iconos

Antes de incorporar un icono:

1. definir el significado;
2. identificar la categoría;
3. comprobar si existe un símbolo reconocido;
4. verificar si Lucide contiene una representación apropiada;
5. comprobar que el símbolo no tenga otro significado dentro del producto;
6. evaluar si necesita texto;
7. verificar accesibilidad;
8. registrar la decisión.

---

## 5. Semantic Icon Registry

El Design System debería disponer de un registro semántico. En lugar de que cada componente decida `<Trash2 />`, se recomienda conceptualmente `<SemanticIcon name="delete" />`.

El registro resolvería:

```text
add       → Plus
delete    → Trash2
edit      → Pencil
search    → Search
settings  → Settings
warning   → TriangleAlert
error     → CircleAlert
success   → CircleCheck
info      → Info
close     → X
previous  → ChevronLeft
next      → ChevronRight
```

### 5.1 Estructura del registro

Cada entrada debería poder contener:

```yaml
semanticName: delete
icon:
  library: lucide
  name: Trash2
category:
  destructive-action
accessibility:
  defaultLabel: Eliminar
direction:
  rtl: fixed
motion:
  allowed: feedback
status:
  stable
```

---

## 6. Lenguaje visual Lucide

Cuando se creen iconos propios que deban convivir con Lucide, deben respetarse sus características visuales fundamentales.

- **Canvas:** 24 × 24 px
- **Stroke:** 2 px. El stroke se encuentra centrado sobre el path.
- **Safe zone:** los strokes deben mantenerse aproximadamente ≥ 1 px alejados de los límites del canvas.
- **Line caps:** los paths abiertos utilizan `round`.
- **Line joins:** utilizar `round`.
- **Separación:** entre elementos visuales independientes ≥ 2 px. Los espacios internos deberían aproximarse también a ese mínimo cuando sea posible.

---

## 7. Balance óptico

La geometría matemática no siempre produce equilibrio visual. Un icono puede necesitar desplazarse ligeramente para parecer centrado. Por tanto: `geometric center ≠ optical center`. Debe priorizarse el balance perceptual.

---

## 8. Peso visual

Todos los iconos de una colección deben presentar una densidad visual comparable. No deberían coexistir icono extremadamente ligero, icono extremadamente denso o icono excesivamente detallado dentro del mismo nivel jerárquico.

---

## 9. Complejidad

Eliminar detalles que no sean necesarios para reconocer el concepto.

Principio: un icono debe contener la menor cantidad de información gráfica necesaria para comunicar correctamente su significado.

Evitar: microdetalles; texturas; decoración innecesaria; formas redundantes; exceso de líneas; sombras internas.

---

## 10. Tamaños

Tokens recomendados:

| Token | Tamaño | Uso |
|---|---|---|
| icon.xs | 12–14 px | metadata |
| icon.sm | 16 px | inputs / tablas |
| icon.md | 20 px | controles |
| icon.base | 24 px | estándar |
| icon.lg | 28–32 px | acciones prominentes |
| icon.xl | 40–48 px | estados / empty states |

No aumentar arbitrariamente el stroke al reducir el icono.
