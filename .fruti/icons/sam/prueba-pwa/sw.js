// Service worker mínimo: hace la app instalable y muestra la notificación de prueba con el icono de la marca.
const CACHE = 'sam-prueba-v1';
const ARCHIVOS = ['./', './index.html', './manifest.webmanifest', './iconos/icon-192.png', './iconos/icon-512.png',
  './iconos/maskable-512.png', './iconos/apple-touch-icon.png', './iconos/favicon.svg', './iconos/simbolo-sobre-oscuro.svg', './iconos/favicon-32.png', './iconos/notificacion-96.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(ARCHIVOS))); self.skipWaiting(); });
self.addEventListener('activate', e => e.waitUntil(self.clients.claim()));
self.addEventListener('fetch', e => e.respondWith(fetch(e.request).catch(() => caches.match(e.request))));
self.addEventListener('message', e => {
  if (e.data === 'notificar') self.registration.showNotification('INC-2041 avanzó a Revisión', {
    body: 'Te toca revisar la evidencia adjunta. (Notificación de prueba de la marca SAM)',
    icon: 'iconos/icon-192.png', badge: 'iconos/notificacion-96.png', tag: 'sam-prueba'
  });
});
self.addEventListener('notificationclick', e => { e.notification.close(); e.waitUntil(self.clients.openWindow('./')); });
