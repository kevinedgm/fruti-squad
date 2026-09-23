# Estrategia de descubrimiento

## Orden de reconocimiento

1. Lee manifests mínimos: package/build/framework config.
2. Detecta entry points, incluidas las entradas declaradas en HTML (`<script src>`) y los service workers: arrancan el sistema sin que nadie los importe.
3. Detecta router/route manifests.
4. Recorre imports desde raíces.
5. Identifica state/stores y clientes de API alcanzables.
6. Si existe backend en el mismo repo, detecta sus entry points, controllers/routes, services/repos y schema/migrations.
7. Cruza frontend ↔ API ↔ datos solo con evidencia.

## Exclusiones por defecto

Ignora salvo referencia explícita desde código activo:

- node_modules, vendor de terceros;
- dist, build, coverage, caches;
- binarios y assets sin metadata útil;
- snapshots generados;
- lockfiles para el grafo semántico;
- documentación histórica.

## Señales de uso dinámico

Antes de marcar orphan revisa:

- import() con expresiones;
- import.meta.glob / require.context;
- auto-import plugins;
- registries de componentes/plugins;
- rutas generadas por filesystem;
- service workers/workers;
- scripts de package.json;
- manifests y configuración;
- nombres referenciados desde templates/HTML/CSS cuando aplique;
- barrels (`index.js` que solo reexporta): que nadie los importe es evidencia de huérfano, pero confundirlos con entry points esconde huérfanos reales.

## Confianza

- high: relación explícita y verificable.
- medium: convención/framework o evidencia parcial.
- low: heurística; debe conservarse como unknown o candidato.

Nunca subas confianza para hacer que el reporte se vea más limpio.
