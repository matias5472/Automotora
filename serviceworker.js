var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/galeria/',
    '/registro/',
    '/Registro-de-Mascota/',
    '/listado-de-mascotas',
    '/static/core/css/Estilo.css',
    '/static/core/css/component.css',
    '/static/core/css/demo.css',
    '/static/core/css/mascotacs.css',
    '/static/core/css/normalize.css',
    '/static/core/css/Registros.css',
    '/static/core/img/Ahorasi.jpg',
    '/static/core/img/crowfunding.jpg',
    '/static/core/img/logo.png',
    '/static/core/img/perro.png',
    '/static/core/img/rescate.jpg',
    '/static/core/img/adoptados/Apolo.jpg',
    '/static/core/img/adoptados/Duque.jpg',
    '/static/core/img/adoptados/Gabi.jpg',
    '/static/core/img/adoptados/Tom.jpg',
    '/static/core/img/rescatados/Bigotes_tn.jpg',
    '/static/core/img/rescatados/Bigotes.jpg',
    '/static/core/img/rescatados/Chocolate_tn.jpg',
    '/static/core/img/rescatados/Chocolate.jpg',
    '/static/core/img/rescatados/Luna_tn.jpg',
    '/static/core/img/rescatados/Luna.jpg',
    '/static/core/img/rescatados/Maya_tn.jpg',
    '/static/core/img/rescatados/Maya.jpg',
    '/static/core/img/rescatados/Oso_tn.jpg',
    '/static/core/img/rescatados/Oso.jpg',
    '/static/core/img/rescatados/Pexel_tn.jpg',
    '/static/core/img/rescatados/Pexel.jpg',
    '/static/core/img/rescatados/Wifi_tn.jpg',
    '/static/core/img/rescatados/wifi.jpg',
    '/static/core/img/social/social-inst.png',
    '/static/core/img/social/social-twitter.png',
    '/static/core/img/social/socialfacebook.png',
    '/static/core/img/social/socialplus.png',
    '/static/core/img/favicon.ico',
    '/static/core/js/inicializacion.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css',
    'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js',
    'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response) {
           

            return fetch(event.request).catch(function() {
                return response
            })
        })
    );
});

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var config = {
    apiKey: "AIzaSyCNfFvEisfkUxGqcC8oqcqd2LAvlkq0K8Y",
    authDomain: "mis-perris-8651e.firebaseapp.com",
    databaseURL: "https://mis-perris-8651e.firebaseio.com",
    projectId: "mis-perris-8651e",
    storageBucket: "mis-perris-8651e.appspot.com",
    messagingSenderId: "763175347300"
  };
firebase.initializeApp(config);


//agregamos un metodo que estara escuchando cuando llegue una notificacion incluso cuando la ventana este cerrada

const messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload){
    console.log(payload);
    var tituloNotoficacion = "titulo"
    var opciones = {
        body:'cuerpo del mensaje',
        icon:'/static/core/img/perro.png'
    }
});