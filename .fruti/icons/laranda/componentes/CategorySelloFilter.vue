<!--
  Versión Laranda de CategorySelloFilter (ronda categoria-sellos/r06).
  Misma lógica y plantilla; solo cambia el CSS para consumir los tokens del
  design system de Laranda:
    tinta→text · tinta-2→text-muted · tinta-3→text-subtle · lienzo→surface-sunken (bg en fades y anillo de foco)
    papel→surface · borde→border · borde-fuerte/borde-control→border-control
    violeta→brand · violeta-suave→brand-soft · anillo de foco: 2px focus, offset 2px
    s-N→space-N · r-xs/sm→radius-sm · r-lg (hoja)→radius-xl · fs-xs/sm→12/14px · e-3→shadow-sheet
    cat-N-tinta / cat-N-fondo: tokens de categoría de Laranda (ocho, orden fijo)
    punto de «Más» con filtro oculto activo: accent (naranja)
-->
<script setup lang="ts">
/**
 * CategorySelloFilter — filtro rápido de categorías de servicio.
 * Ronda: categoria-sellos/r05 · Concepto C «Anillo estable»
 * Ronda: categoria-sellos/r06 (#D17) · size/context — ver CategorySelloFilter-contract.ts
 * Patrón APG: Radiogroup (riel) + Dialog modal (panel «Más», solo context='filter') + Listbox (opciones del panel)
 * Contrato: r05/spec/contrato-CategorySelloFilter.md
 */
import { ref, computed, watch, onMounted, onBeforeUnmount, nextTick } from 'vue'
import { useFocusTrap } from '@/composables/useFocusTrap'
import { CS_STRESS, type QuickCategory } from './CategorySelloFilter-contract'

// ── Props (contrato §1) ────────────────────────────────────────────────────
const props = withDefaults(defineProps<{
  categorias: QuickCategory[]
  modelValue?: string
  todosLabel?: string
  error?: string | null
  resultCount?: number
  counts?: Record<string, number>
  loading?: boolean
  ariaLabel?: string
  /** r06 (#D17): densidad del disco — 'md' 44px (sin cambio) · 'lg' 56px. */
  size?: 'md' | 'lg'
  /** r06 (#D17): 'filter' (riel bajo resultados, sin cambio) · 'nav' («Más» = enlace directo, no abre panel). */
  context?: 'nav' | 'filter'
}>(), {
  modelValue: '',
  todosLabel: 'Todos',
  error: null,
  resultCount: undefined,
  counts: undefined,
  loading: false,
  ariaLabel: 'Filtrar por categoría de servicio',
  size: 'md',
  context: 'filter',
})

// ── Emits (contrato §2) ────────────────────────────────────────────────────
const emit = defineEmits<{
  'update:modelValue': [valor: string]
  change: [valor: string]
  retry: []
}>()

// ── DOM refs ───────────────────────────────────────────────────────────────
const wrapRef    = ref<HTMLElement | null>(null)
const railRef    = ref<HTMLElement | null>(null)
const masRef     = ref<HTMLButtonElement | null>(null)
const panelRef   = ref<HTMLElement | null>(null)
const selloButtons = ref<HTMLButtonElement[]>([])
function setSelloRef(el: unknown, i: number) {
  if (el) selloButtons.value[i] = el as HTMLButtonElement
}

// ── maxVisible: ResizeObserver (contrato §7 «Cambio de orientación o redimensión») ──
const maxVisible = ref(6)
function calcMaxVisible() {
  const rail = railRef.value
  if (!rail) return
  // Estimate from container width: each sello is roughly 64px + 8px gap.
  const available = rail.clientWidth
  const n = Math.max(1, Math.floor((available + 8) / 72))
  maxVisible.value = Math.min(n, props.categorias.length)
}
let ro: ResizeObserver | undefined
onMounted(() => {
  calcMaxVisible()
  ro = new ResizeObserver(calcMaxVisible)
  if (wrapRef.value) ro.observe(wrapRef.value)
  updateOverflow()
  railRef.value?.addEventListener('scroll', updateOverflow, { passive: true })
})
onBeforeUnmount(() => {
  ro?.disconnect()
  railRef.value?.removeEventListener('scroll', updateOverflow)
})

// ── Overflow fades ─────────────────────────────────────────────────────────
const hasOverflowStart = ref(false)
const hasOverflowEnd   = ref(false)
function updateOverflow() {
  const el = railRef.value
  if (!el) return
  hasOverflowStart.value = el.scrollLeft > 2
  hasOverflowEnd.value   = el.scrollLeft + el.clientWidth < el.scrollWidth - 2
}
watch(() => props.categorias, () => nextTick(updateOverflow))

// ── Categorías visibles / overflow (contrato §7) ──────────────────────────
const itemsVisibles  = computed(() => props.categorias.slice(0, maxVisible.value))
const itemsOverflow  = computed(() => props.categorias.slice(maxVisible.value))
const activeInOverflow = computed(
  () => props.modelValue !== '' && !itemsVisibles.value.some(c => c.valor === props.modelValue)
)
const masLabel = computed(() => {
  const base = `Más categorías, ${itemsOverflow.value.length} disponibles`
  return activeInOverflow.value
    ? `${base}; hay un filtro activo en las opciones adicionales`
    : base
})

// ── r06 (#D17): «Más» contextual ───────────────────────────────────────────
// context='nav' (Inicio): la tarea siempre termina en navegar — «Más» es un
// enlace directo a «Todos», sin el paso intermedio del panel.
// context='filter' (Resultados, default): sin cambio de r05, abre el panel.
const masEsEnlace = computed(() => props.context === 'nav')
function onMasClick() {
  if (masEsEnlace.value) {
    seleccionar('', masRef.value ?? undefined)
  } else {
    abrirPanel()
  }
}

// ── Panel ──────────────────────────────────────────────────────────────────
const panelAbierto = ref(false)
const panelSearch  = ref('')
const panelItems   = computed(() => {
  const q = panelSearch.value.trim().toLowerCase()
  return q ? props.categorias.filter(c => c.label.toLowerCase().includes(q)) : props.categorias
})
const mostrarBusqueda = computed(
  () => props.categorias.length >= CS_STRESS.PANEL_SEARCH_THRESHOLD
)

useFocusTrap(panelAbierto, panelRef, { onEscape: cerrarPanel })

function abrirPanel() {
  panelSearch.value = ''
  panelAbierto.value = true
}
function cerrarPanel() {
  panelAbierto.value = false
  nextTick(() => masRef.value?.focus())
}

// ── Selección ──────────────────────────────────────────────────────────────
function seleccionar(valor: string, el?: HTMLElement) {
  emit('update:modelValue', valor)
  emit('change', valor)
  if (el && !prefersReduced()) {
    el.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'nearest' })
  }
}
function seleccionarDesdePanel(valor: string) {
  seleccionar(valor)
  cerrarPanel()
}

// ── Aria-live (contrato §9) ────────────────────────────────────────────────
const liveText = ref('')
watch(() => props.modelValue, (val) => {
  const cat = props.categorias.find(c => c.valor === val)
  const label = cat ? cat.label : props.todosLabel
  liveText.value = props.resultCount !== undefined
    ? `${label} seleccionado, ${props.resultCount} resultados`
    : `${label} seleccionado`
})

// ── Teclado riel (APG Radiogroup, contrato §6) ────────────────────────────
// opciones del riel = [todos, ...visibles]; índices alineados con selloButtons
const opcionesRiel = computed(() => [
  { label: props.todosLabel, valor: '' },
  ...itemsVisibles.value,
])
function onKeyRiel(e: KeyboardEvent, index: number) {
  const n = opcionesRiel.value.length
  let next = -1
  if (e.key === 'ArrowRight' || e.key === 'ArrowDown') next = (index + 1) % n
  else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') next = (index - 1 + n) % n
  else if (e.key === 'Home') next = 0
  else if (e.key === 'End')  next = n - 1
  if (next === -1) return
  e.preventDefault()
  const btn = selloButtons.value[next]
  btn?.focus()
  seleccionar(opcionesRiel.value[next].valor, btn)
}

// ── Teclado panel (APG Listbox, contrato §6) ──────────────────────────────
const panelItemRefs = ref<HTMLButtonElement[]>([])
function setPanelItemRef(el: unknown, i: number) {
  if (el) panelItemRefs.value[i] = el as HTMLButtonElement
}
function onKeyPanelItem(e: KeyboardEvent, index: number) {
  const n = panelItems.value.length
  if (e.key === 'ArrowDown') { e.preventDefault(); panelItemRefs.value[(index + 1) % n]?.focus() }
  else if (e.key === 'ArrowUp') { e.preventDefault(); panelItemRefs.value[(index - 1 + n) % n]?.focus() }
}

function prefersReduced() {
  return window.matchMedia?.('(prefers-reduced-motion: reduce)').matches ?? false
}
</script>

<template>
  <!-- Estado error (contrato §4) -->
  <div v-if="error" class="cs-error" role="alert">
    {{ error }}
    <button type="button" class="cs-error-btn" @click="emit('retry')">Reintentar</button>
  </div>

  <template v-else>
    <!-- Rail (contrato §2 anatomía) -->
    <div
      ref="wrapRef"
      class="cs-rail-wrap"
      :class="{ '--fade-start': hasOverflowStart, '--fade-end': hasOverflowEnd, '--lg': size === 'lg' }"
    >
      <div
        ref="railRef"
        class="cs-rail"
        role="radiogroup"
        :aria-label="ariaLabel"
        :aria-busy="loading ? 'true' : undefined"
      >
        <!-- Skeleton de carga (contrato §4 Carga / §7 «Carga inicial») -->
        <template v-if="loading">
          <div v-for="n in 5" :key="n" class="cs-skel">
            <div class="cs-skel-disco" aria-hidden="true"></div>
            <div class="cs-skel-label" aria-hidden="true"></div>
          </div>
        </template>

        <template v-else>
          <!-- Sello «Todos» (contrato §4 «Todos» activo, D2) -->
          <button
            :ref="el => setSelloRef(el, 0)"
            type="button"
            role="radio"
            class="cs-sello cs-sello--todos"
            :aria-checked="modelValue === ''"
            :tabindex="modelValue === '' ? 0 : -1"
            @click="seleccionar('', selloButtons[0])"
            @keydown="(e) => onKeyRiel(e, 0)"
          >
            <span class="cs-disco" aria-hidden="true">{{ todosLabel.slice(0, 4) }}</span>
            <span class="cs-label">{{ todosLabel }}</span>
          </button>

          <!-- Sellos de categoría (contrato §4 Sello activo) -->
          <button
            v-for="(cat, i) in itemsVisibles"
            :key="cat.valor"
            :ref="el => setSelloRef(el, i + 1)"
            type="button"
            role="radio"
            class="cs-sello"
            :class="cat.clase"
            :aria-checked="modelValue === cat.valor"
            :tabindex="modelValue === cat.valor ? 0 : -1"
            @click="seleccionar(cat.valor, selloButtons[i + 1])"
            @keydown="(e) => onKeyRiel(e, i + 1)"
          >
            <span class="cs-disco" aria-hidden="true">
              <component :is="cat.icon" v-if="cat.icon" :size="18" :stroke-width="1.8" aria-hidden="true" />
            </span>
            <span class="cs-label">{{ cat.label }}</span>
          </button>

          <!-- Botón «Más» (contrato §4 «Más» con activo en overflow) — r06: contextual -->
          <button
            v-if="itemsOverflow.length > 0 && !masEsEnlace"
            ref="masRef"
            type="button"
            class="cs-mas"
            :class="{ '--tiene-activo': activeInOverflow }"
            aria-haspopup="dialog"
            :aria-label="masLabel"
            @click="onMasClick"
          >
            <span class="cs-disco" aria-hidden="true">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <path d="M5 12h14"/><path d="M12 5v14"/>
              </svg>
            </span>
            <span class="cs-label">Más · {{ itemsOverflow.length }}</span>
            <span class="cs-mas-dot" aria-hidden="true"></span>
          </button>

          <!-- «Más» como enlace directo (r06, context='nav'): la tarea siempre
               termina en navegar, así que salta el panel y va directo a «Todos». -->
          <button
            v-if="itemsOverflow.length > 0 && masEsEnlace"
            ref="masRef"
            type="button"
            class="cs-mas cs-mas--enlace"
            @click="onMasClick"
          >
            <span class="cs-label">Ver todo →</span>
          </button>
        </template>
      </div>
    </div>

    <!-- Región de anuncio aria-live (contrato §9) -->
    <span role="status" aria-live="polite" class="cs-sr-only">{{ liveText }}</span>
  </template>

  <!-- Panel de «Más» (contrato §5 Panel, APG Dialog) — Teleport a body -->
  <Teleport to="body">
    <div
      class="cs-panel-overlay"
      :class="{ '--open': panelAbierto }"
      aria-hidden="true"
    ></div>

    <div
      ref="panelRef"
      class="cs-panel"
      :class="{ '--open': panelAbierto }"
      role="dialog"
      aria-modal="true"
      aria-label="Todas las categorías"
      tabindex="-1"
    >
      <div class="cs-panel-head">
        <span class="cs-panel-title">Categoría de servicio</span>
        <button
          type="button"
          class="cs-panel-close"
          aria-label="Cerrar"
          @click="cerrarPanel"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M18 6 6 18"/><path d="m6 6 12 12"/>
          </svg>
        </button>
      </div>

      <!-- Búsqueda (contrato §7 «12–20 categorías» / «> 20 categorías») -->
      <input
        v-if="mostrarBusqueda"
        v-model="panelSearch"
        type="search"
        class="cs-panel-search"
        placeholder="Buscar categoría"
        aria-label="Buscar categoría"
        :aria-controls="`cs-panel-list-${$.uid}`"
      />

      <!-- Lista (APG Listbox) -->
      <ul
        :id="`cs-panel-list-${$.uid}`"
        class="cs-panel-list"
        role="listbox"
        aria-label="Categorías"
      >
        <li v-for="(cat, i) in panelItems" :key="cat.valor">
          <button
            :ref="el => setPanelItemRef(el, i)"
            type="button"
            role="option"
            class="cs-panel-item"
            :class="cat.clase"
            :aria-selected="modelValue === cat.valor"
            @click="seleccionarDesdePanel(cat.valor)"
            @keydown="(e) => onKeyPanelItem(e, i)"
          >
            <span class="cs-panel-ico" aria-hidden="true">
              <component :is="cat.icon" v-if="cat.icon" :size="16" :stroke-width="1.8" aria-hidden="true" />
            </span>
            <span>
              {{ cat.label }}
              <span v-if="counts?.[cat.valor] !== undefined" class="cs-panel-count" aria-hidden="true">
                · {{ counts[cat.valor] }}
              </span>
            </span>
          </button>
        </li>
      </ul>
    </div>
  </Teleport>
</template>

<style scoped>
/* ── #pieza-css movido del banco (partes scoped: riel, sellos, error) ─── */

/* 0. Custom property --cs-ring / --cs-fondo
   HALLAZGO DE COCO (R0, rediseño pedido por el usuario — "debe tener la forma
   de sellos"): el disco era un anillo sobre fondo blanco (--papel), sin color
   propio hasta que se activaba — no se leía como un "sello" (timbre con
   esmalte propio), solo como un botón de icono genérico. Se añade --cs-fondo
   (reutiliza --cat-N-fondo, ya usado por las tarjetas de taxonomía de Inicio
   y por EmptyStateResultados — mismo lenguaje visual, ningún token nuevo) para
   que el disco tenga su esmalte de categoría siempre, no solo al activarse. */
.cs-sello, .cs-panel-item { --cs-ring: var(--text); --cs-fondo: var(--surface-sunken); }
.cs-sello.c1, .cs-panel-item.c1 { --cs-ring: var(--cat-1-tinta); --cs-fondo: var(--cat-1-fondo); }
.cs-sello.c2, .cs-panel-item.c2 { --cs-ring: var(--cat-2-tinta); --cs-fondo: var(--cat-2-fondo); }
.cs-sello.c3, .cs-panel-item.c3 { --cs-ring: var(--cat-3-tinta); --cs-fondo: var(--cat-3-fondo); }
.cs-sello.c4, .cs-panel-item.c4 { --cs-ring: var(--cat-4-tinta); --cs-fondo: var(--cat-4-fondo); }
.cs-sello.c5, .cs-panel-item.c5 { --cs-ring: var(--cat-5-tinta); --cs-fondo: var(--cat-5-fondo); }
.cs-sello.c6, .cs-panel-item.c6 { --cs-ring: var(--cat-6-tinta); --cs-fondo: var(--cat-6-fondo); }
.cs-sello.c7, .cs-panel-item.c7 { --cs-ring: var(--cat-7-tinta); --cs-fondo: var(--cat-7-fondo); }
.cs-sello.c8, .cs-panel-item.c8 { --cs-ring: var(--cat-8-tinta); --cs-fondo: var(--cat-8-fondo); }

/* 1. Rail */
.cs-rail-wrap { position: relative; }
.cs-rail {
  display: flex; align-items: flex-start; gap: var(--space-2);
  overflow-x: auto; scrollbar-width: none; -webkit-overflow-scrolling: touch;
  padding-block: var(--space-1); scroll-behavior: smooth;
}
.cs-rail::-webkit-scrollbar { display: none; }

/* r06 (#D17): size='lg' — riel protagonista (Inicio). Solo cambia el tamaño
   del disco; el concepto visual «Anillo estable» no se toca. */
.cs-rail-wrap.--lg .cs-disco,
.cs-rail-wrap.--lg .cs-skel-disco { width: 56px; height: 56px; }

/* Fades de overflow */
.cs-rail-wrap::before, .cs-rail-wrap::after {
  content: ''; position: absolute; inset-block: 0; width: 24px;
  pointer-events: none; z-index: 1; opacity: 0; transition: opacity 0.18s ease;
}
.cs-rail-wrap::before { left: 0;  background: linear-gradient(to right, var(--bg), transparent); }
.cs-rail-wrap::after  { right: 0; background: linear-gradient(to left,  var(--bg), transparent); }
.cs-rail-wrap.--fade-start::before { opacity: 1; }
.cs-rail-wrap.--fade-end::after    { opacity: 1; }

/* 2. Sello */
.cs-sello {
  flex: 0 0 auto; display: flex; flex-direction: column; align-items: center;
  gap: var(--space-1); border: none; background: none; cursor: pointer;
  padding: 0 var(--space-2) var(--space-1); font: inherit; outline: none; /* L1: foco via .cs-disco */
}

/* 3. Disco — esmalte de categoría (--cs-fondo/--cs-ring) siempre visible,
   para que lea como un sello/timbre, no un botón de icono genérico. */
.cs-disco {
  width: 44px; height: 44px; border-radius: 50%; /* forma circular matemática — no token */
  border: 1.5px solid transparent;
  display: grid; place-items: center;
  background: var(--cs-fondo); color: var(--cs-ring);
  transition:
    border-color var(--quick) var(--ease-out),
    border-width var(--quick) var(--ease-out),
    color        var(--quick) ease,
    box-shadow   var(--quick) ease;
}

/* 4. Label */
.cs-label {
  font-family: var(--font-sans); font-size: 12px;
  line-height: 1.2; text-align: center; color: var(--text-muted);
  max-inline-size: 64px; word-break: break-all; overflow-wrap: break-word; transition: color var(--quick) ease;
}

/* 5. Hover — conserva el color propio de la categoría (ya no se apaga a gris;
   el esmalte es permanente, el hover solo marca el borde). */
@media (hover: hover) {
  .cs-sello:not([aria-checked="true"]):not([aria-disabled="true"]):hover .cs-disco {
    border-color: var(--cs-ring);
  }
  .cs-sello:not([aria-checked="true"]):not([aria-disabled="true"]):hover .cs-label { color: var(--text); }
}

/* 6. Activo (Pigmentos: ring en color de categoría) */
.cs-sello[aria-checked="true"] .cs-disco {
  border-width: 3px; border-color: var(--cs-ring); color: var(--cs-ring);
}
.cs-sello[aria-checked="true"] .cs-label { color: var(--text); font-weight: 700; }

/* 7. Focus visible */
.cs-sello:focus-visible .cs-disco {
  box-shadow: 0 0 0 2px var(--bg), 0 0 0 4px var(--focus);
}

/* 8. Disabled */
.cs-sello[aria-disabled="true"] { opacity: 0.45; cursor: not-allowed; pointer-events: none; }

/* 9. «Todos» */
.cs-sello--todos { --cs-ring: var(--border-control); }
.cs-sello--todos .cs-disco {
  font-family: var(--font-sans); font-size: 12px; /* banco usaba 0.68rem — corregido a mínimo del sistema */
  font-weight: 600; letter-spacing: 0.02em; color: var(--text-muted);
}
.cs-sello--todos[aria-checked="true"] .cs-disco { color: var(--text); }

/* 10. «Más» */
.cs-mas {
  flex: 0 0 auto; display: flex; flex-direction: column; align-items: center;
  gap: var(--space-1); border: none; background: none; cursor: pointer;
  padding: 0 var(--space-2) var(--space-1); font: inherit; outline: none; position: relative;
}
.cs-mas .cs-disco { border-style: dashed; color: var(--text-subtle); }
.cs-mas:focus-visible .cs-disco {
  box-shadow: 0 0 0 2px var(--bg), 0 0 0 4px var(--focus);
}
@media (hover: hover) {
  .cs-mas:hover .cs-disco { border-style: solid; border-color: var(--border-control); color: var(--text-muted); }
}
.cs-mas-dot {
  display: none; position: absolute; top: 2px; right: 6px;
  width: 8px; height: 8px; border-radius: 50%;
  background: var(--accent); border: 1.5px solid var(--bg);
}
.cs-mas.--tiene-activo .cs-mas-dot { display: block; }

/* 10b. «Más» como enlace directo (r06, context='nav') */
.cs-mas--enlace {
  flex-direction: row; align-items: center; justify-content: center;
  min-block-size: 44px; padding: 0 var(--space-3);
}
.cs-mas--enlace .cs-label {
  text-decoration: underline; text-underline-offset: 2px; color: var(--text); font-weight: 600;
  max-inline-size: none; white-space: nowrap;
}
.cs-mas--enlace:focus-visible {
  outline: 2px solid var(--focus); outline-offset: 2px;
}

/* 11. Skeleton */
.cs-skel {
  flex: 0 0 auto; display: flex; flex-direction: column; align-items: center; gap: var(--space-1); padding: 0 var(--space-2) var(--space-1);
}
.cs-skel-disco { width: 44px; height: 44px; border-radius: 50%; background: var(--border); animation: cs-skel-pulse 1.4s cubic-bezier(0.4, 0, 0.6, 1) infinite; }
/* Alto = una línea de .cs-label (misma fuente, 1lh): el esqueleto reserva el
   mismo hueco que el sello real y el riel no salta al llegar el catálogo. */
.cs-skel-label { width: 38px; font-size: 12px; line-height: 1.2; height: 1lh; box-sizing: border-box; padding-block: 0.2lh; background-clip: content-box; border-radius: var(--radius-sm); background-color: var(--border); animation: cs-skel-pulse 1.4s cubic-bezier(0.4, 0, 0.6, 1) infinite 0.15s; }
@keyframes cs-skel-pulse { 0%, 100% { opacity: 0.5; } 50% { opacity: 1; } }

/* 12. Error */
.cs-error {
  display: flex; align-items: center; gap: var(--space-2);
  font-size: 12px; color: var(--text-muted);
}
.cs-error-btn {
  border: 1px solid var(--border-control); border-radius: var(--radius-sm);
  background: var(--surface); color: var(--text); padding: var(--space-1) var(--space-4);
  font: inherit; font-size: 12px; cursor: pointer; outline: none;
  min-block-size: 44px; /* B3: área táctil mínima */
  display: inline-flex; align-items: center;
}
.cs-error-btn:focus-visible {
  outline: 2px solid var(--focus); outline-offset: 2px;
}

/* 13. Accesibilidad */
.cs-sr-only {
  position: absolute; inline-size: 1px; block-size: 1px;
  overflow: hidden; clip-path: inset(50%); white-space: nowrap;
}

/* 14. Reduced motion */
@media (prefers-reduced-motion: reduce) {
  .cs-disco, .cs-label { transition: none; }
  .cs-rail-wrap::before, .cs-rail-wrap::after { transition: none; }
  .cs-rail { scroll-behavior: auto; }
  .cs-skel-disco, .cs-skel-label { animation: none; opacity: 0.6; }
}

/* 15. Forced colors */
@media (forced-colors: active) {
  .cs-sello[aria-checked="true"] .cs-disco {
    forced-color-adjust: none; border-color: Highlight; color: Highlight;
  }
  .cs-sello:focus-visible .cs-disco, .cs-mas:focus-visible .cs-disco {
    box-shadow: 0 0 0 2px ButtonFace, 0 0 0 4px Highlight;
  }
}
</style>

<style>
/* No-scoped: Teleport target — overlay y panel se renderizan en <body> */

/* Panel overlay */
.cs-panel-overlay {
  position: fixed; inset: 0; z-index: 49; display: none;
  /* Fallback: opacidad sobre color sólido (browsers sin color-mix) */
  background: var(--text); opacity: 0.35;
}
@supports (background: color-mix(in srgb, red 0%, transparent)) {
  .cs-panel-overlay { background: color-mix(in srgb, var(--text) 35%, transparent); opacity: 1; }
}
.cs-panel-overlay.--open { display: block; }

/* Panel (bottom sheet) */
.cs-panel {
  position: fixed; inset: auto 0 0 0; background: var(--surface);
  border-top: 1px solid var(--border); border-radius: var(--radius-xl) var(--radius-xl) 0 0;
  padding-block: var(--space-4) max(var(--space-5), env(safe-area-inset-bottom));
  padding-inline: var(--space-4);
  max-block-size: 68vh; overflow-y: auto; box-shadow: var(--shadow-sheet); z-index: 50;
  display: none; flex-direction: column; gap: var(--space-5);
}
.cs-panel.--open {
  display: flex;
  animation: cs-panel-enter 220ms var(--ease-out) forwards;
}
@keyframes cs-panel-enter {
  from { opacity: 0.2; transform: translateY(24px); }
  to   { opacity: 1;   transform: translateY(0); }
}

/* Panel internals */
.cs-panel-head { display: flex; align-items: center; justify-content: space-between; }
.cs-panel-title { font-family: var(--font-sans); font-size: 14px; font-weight: 600; color: var(--text); }
.cs-panel-close {
  border: none; background: none; cursor: pointer; padding: var(--space-2); color: var(--text-muted); outline: none;
  border-radius: var(--radius-sm); min-width: 44px; min-height: 44px; /* B1: área táctil mínima */
  display: inline-flex; align-items: center; justify-content: center;
}
.cs-panel-close:focus-visible {
  outline: 2px solid var(--focus); outline-offset: 2px;
}
.cs-panel-search {
  width: 100%; padding: var(--space-3) var(--space-5); border: 1.5px solid var(--border-control);
  border-radius: var(--radius-sm); font-family: var(--font-sans); font-size: 14px;
  color: var(--text); background: var(--surface); outline: none;
  min-block-size: 44px; /* B2: área táctil mínima */
}
.cs-panel-search:focus-visible { border-color: var(--brand); box-shadow: 0 0 0 3px var(--brand-soft); }
.cs-panel-list { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 0; }
.cs-panel-item {
  display: flex; align-items: center; gap: var(--space-5); padding: var(--space-3) var(--space-5);
  border: 1.5px solid transparent; border-radius: var(--radius-sm); cursor: pointer;
  background: none; font: inherit; font-size: 14px; color: var(--text-muted);
  min-block-size: 44px; text-align: start; width: 100%; outline: none;
}
.cs-panel-item[aria-selected="true"] { border-color: var(--cs-ring); color: var(--text); font-weight: 600; }
.cs-panel-item:focus-visible {
  outline: 2px solid var(--focus); outline-offset: 2px;
}
.cs-panel-ico {
  width: 32px; height: 32px; border-radius: 50%;
  display: grid; place-items: center; background: var(--surface-sunken); color: var(--text-muted); flex: 0 0 auto;
}
.cs-panel-item[aria-selected="true"] .cs-panel-ico {
  /* Fallback: lienzo neutro */
  background: var(--surface-sunken); color: var(--cs-ring);
}
@supports (background: color-mix(in srgb, red 0%, transparent)) {
  .cs-panel-item[aria-selected="true"] .cs-panel-ico {
    background: color-mix(in srgb, var(--cs-ring) 12%, transparent);
  }
}
.cs-panel-count { color: var(--text-subtle); font-size: 12px; }

/* Reduced motion para el panel */
@media (prefers-reduced-motion: reduce) {
  .cs-panel.--open { animation: none; }
}

/* Forced colors */
@media (forced-colors: active) {
  .cs-panel { border: 1px solid ButtonText; }
  .cs-panel-item[aria-selected="true"] { forced-color-adjust: none; border-color: Highlight; }
}
</style>