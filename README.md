# Canairio Backend

[![CircleCI](https://circleci.com/gh/kike-canaries/canairio_backend.svg?style=svg)](https://circleci.com/gh/kike-canaries/canairio_backend)

> Recibimos los datos provenientes de los [canair.ios](https://canair.io)

Si tiene interés en analizar información proveniente de la red ciudadana de calidad del aire,
o ayudar en el desarrollo de nuestro backend, está en el lugar correcto.

Si desea conocer más del proyecto, por favor visite [canair.io](https://canair.io) .  En este repositorio
encuentra información de como colaborar en el proyecto en la recepción y análisis de datos.

## Ejecutar localmente el proyecto

Este proyecto está basado en [django-rest-framework](https://www.django-rest-framework.org/) y almacena los datos en influxdb, para correrlo localmente
se requiere [docker](https://www.docker.com/) y [docker-compose](https://docs.docker.com/compose/install/)

1. clone el repositorio
2. ejecute docker-compose desde el interior del directorio que obtuvo al clonar el repositorio

en el directorio recien clonado en una terminal

docker-compose up

Esto le permitirá hacer peticiones desde su entorno de desarollo a localhost:8000

## Primeros pasos

Para hacer una prueba local rápida puede crear un usuario, autenticarlo,
crear un dispositivo y enviar una medición desde tal dispositivo.

Para ello abra una conexión a Docker con

```bash
docker-compose exec web bash
```

Y estando al interior, haga que el servidor web se ejecute

```bash
python manage.py runserver 0.0.0.0:8000
```

### Crear un usuario

```bash
Create a user

curl --request POST \
--url http://localhost:8000/users/auth/register/ \
--header 'content-type: application/json' \
--data '{
  "username": "user2",
  "password": "hunter2"
}'
```

Con este usuario podemos proceder a crear un dispositivo

### Crear un dispositivo

Enviaremos su dirección MAC, latitud, longitud y le asignaremos un nombre

```bash
curl --request POST \
  --user user2:hunter2 \
  --url http://localhost:8000/points/sensors/ \
  --header 'content-type: application/json' \
  --data '{
    "mac": "D714E1KU605C",
    "lat": "4.12345678",
    "lon": "-74.12345678",
    "name": "mysecondcanair"
}'
```

Que en caso exitoso responderá con los mismos datos enviados y el id.

```json
{"id":1,"mac":"D714E1CC605C","lat":"4.12345678","lon":"-74.12345678","name":"myhomecanair"}
```

Tenemos más endpoints disponibles, y le invitamos a que vea el conjunto
de pruebas para que inicie a hacer solicitudes al API para añadir mediciones
o para obtener la medición más reciente.

## Para desarrollar y contribuir

Cada vez que haga cambios y los guarde en su entorno de desarrollo local estos
se verán reflejados en la instancia que está ejecutando en docker.

### Pruebas

Para correr las pruebas, ubíquese en el directorio clonado y ejecute:

```bash
docker-compose exec web bash
```

>asegúrese que en otra terminal está ejecutando `docker-compose up`

Y una vez en el shell, podrá ejercitar las pruebas

```bash
python manage.py test --settings=canairio.settings.testing
```

Tenga en cuenta que la información se almacena en la misma instancia de
influxdb para pruebas y desarrollo, por lo tanto, si tiene un dispositivo
que está enviando información a su instancia de influxdb en Docker, las
pruebas podrían fallar bajo estas condiciones.

## Release History

Por ahora el trabajo está en progreso, no hemos hecho un release oficial

## Contributing

El código está en inglés, tanto variables, nombres comentarios, comentarios de
los commits.

1. Haga un fork del proyecto (<https://github.com/yourname/yourproject/fork>)
1. Cree una rama del mismo (`git checkout -b feature/fooBar`)
1. Haga los commits necesarios con mensajes que describan el cometido de los cambios (`git commit -am 'Add some fooBar'`)
1. Envíe los cambios a su rama (`git push origin feature/fooBar`)
1. Ejecute pruebas y asegure que estas continúan funcionando y que su código nuevo
también es ejercitado
1. Abra un pull request
