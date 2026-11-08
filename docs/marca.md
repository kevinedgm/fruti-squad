# Marca de Fruti Squad

Resumen: todo el sistema se arma con dos piezas, el **marco redondeado** (la pieza de interfaz) y el **punto** (la evidencia). El trazo siempre es neutro y el color vive solo en el punto: cada agente firma su evidencia con su color y el símbolo del squad reúne los cinco. Los archivos están en `assets/marca/`.

## Símbolos

| Agente | Rol | Lema | Símbolo | Color sobre claro | Color sobre oscuro |
|---|---|---|---|---|---|
| Fruti Squad | Workflow Pack | Agentes especialistas que diseñan, gobiernan, implementan, auditan y documentan interfaces. | Espiral: los marcos de la familia girando; cada especialista entra en su turno | degradado de los cinco | degradado de los cinco |
| Kiwi | UX Architect | Define la estructura antes que la apariencia. | Tres tamaños: compact, medium y expanded; la estructura se mantiene | `#0f9e6e` | `#34e0a1` |
| Lima | Design System Governance | Gobierna tu design system: una fuente, muchas piezas coherentes. | Biblioteca: marcos apilados; el de enfrente es el aprobado | `#6f8c00` | `#d4ff3a` |
| Coco | UI Audit | Construye la capa visual y la audita contra el contrato. | Visor: esquinas que encuadran la pieza para revisarla | `#c26a00` | `#ff9f1c` |
| Bruno | Frontend Implementation Engineer | Convierte la pieza aprobada en comportamiento frontend real. | Cierre: la barra de `</>` parte el marco; de plano punteado a pieza sólida | `#3a54d6` | `#4361ee` |
| Mora | Documentation & Knowledge Engineer | Documenta solo lo que existe y fue verificado. | Red de conocimiento: piezas documentadas conectadas | `#d0156e` | `#f72585` |

Bruno tiene marca, pero todavía no es parte del squad: hoy Coco cubre la implementación.

Cada símbolo tiene dos archivos: `<agente>.svg` para fondo claro (trazo `#18181b`, punto oscurecido) y `<agente>-oscuro.svg` para fondo oscuro (trazo blanco, punto vivo). En GitHub se usan juntos con `<picture>` para que cambien solos con el tema.

## Reglas

1. El trazo siempre es neutro: tinta `#18181b` sobre claro y blanco sobre oscuro. El color vive solo en el punto.
2. Cada agente firma su evidencia con su color, y el símbolo del squad reúne los cinco en degradado.
3. Sobre fondo claro se usan los tonos oscurecidos. Los vivos van solo sobre oscuro, porque sobre blanco no tienen contraste suficiente.
4. El color nunca es la única señal: cada agente se reconoce por su silueta.
5. Las plataformas (Codex, Kiro, Claude Code) se nombran en texto, nunca con sus logotipos dentro de la marca.

Usos incorrectos: pintar el trazo de color, usar el color vivo sobre fondo claro, deformar o girar el símbolo, y cambiarle el color del punto a un agente.

## Construcción

- Cuadro de 64 unidades.
- Trazo de 3.5 (3 en la Espiral).
- Radios de 5 a 15.
- Punto de 4 a 6.5.
- Margen de respeto: la mitad del símbolo alrededor.

## Tipografía

**Bricolage Grotesque**: 700 para el nombre, 400 para el producto y el texto. Licencia SIL Open Font (Google Fonts). En los logotipos va convertida a trazos.

## Portada para redes

`assets/marca/fruti-squad-og-1200x630.png` es la portada Open Graph del squad (en inglés). Para usarla como vista previa del repositorio: GitHub → Settings → General → Social preview.
