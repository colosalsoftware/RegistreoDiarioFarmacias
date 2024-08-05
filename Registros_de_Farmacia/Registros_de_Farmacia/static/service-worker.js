// static/service-worker.js
self.addEventListener('install', event => {
    event.waitUntil(
      caches.open('v1').then(cache => {
        return cache.addAll([
          '/',
          '/static/css/style.css',
          '/static/img/icono-192x192.png',
          '/static/img/icono-512x512.png',
          // Agrega aquí otras rutas que quieras cachear
        ]);
      })
    );
  });
  
  self.addEventListener('fetch', event => {
    event.respondWith(
      caches.match(event.request).then(response => {
        return response || fetch(event.request);
      })
    );
  });
  