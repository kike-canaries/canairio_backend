# Canairio Backend 
> Recibimos los datos provenientes de los [canair.ios](https://canair.io)

Si tiene interés en analizar información proveniente de la red ciudadana de calidad del aire,
o ayudar en el desarrollo de nuestro backend, está en el lugar correcto.

Si desea conocer más del proyecto, por favor visite https://canair.io .  En este repositorio
encuentra información de como colaborar en el proyecto en la recepción y análisis de datos.

## Ejecutar localmente el proyecto

Este proyecto usa django-rest-framework y almacena los datos en influxdb, para correrlo localmente
se requiere docker y docker-compose

1. clone el repositorio
2. ejecute docker-compose desde el interior del directorio que obtuvo al clonar el repositorio

en el directorio recien clonado en una terminal

docker-compose up

Esto le permitirá hacer peticiones desde su entorno de desarollo a localhost:8000

## Primeros pasos

Para hacer una prueba local rápida puede crear un usuario, autenticarlo, con el token
de autenticación crear un dispositivo y enviar una medición desde tal dispositivo.

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

### Autenticar el usuario

Con el usuario recién creado se puede autenticar

```bash
curl --request POST \
  --url http://localhost:8000/users/auth/login/ \
  --header 'content-type: application/json' \
  --data '{
    "username": "user2",
    "password": "hunter2"
}'
```

Que en caso exitoso ofrecerá un token que puede emplear
para llamadas subsecuentes

```json
{"user":{"id":1,"username":"user2"},"token":"7cf9b723ba1b25fad53ffd4da7855229fbfeb5b6a9790a127a0466d9ae26af88"}
```

Con nuestro usuario autenticado y un token podemos proceder a crear un dispositivo

### Crear un dispositivo

Enviaremos su dirección MAC, latitud, longitud y le asignaremos un nombre

```bash
curl --request POST \
  --url http://localhost:8000/points/sensors/ \
  --header 'content-type: application/json' \
  --header 'Authorization: Token 7cf9b723ba1b25fad53ffd4da7855229fbfeb5b6a9790a127a0466d9ae26af88' \
  --data '{
    "mac": "D714E1CC605C",
    "lat": "4.12345678",
    "lon": "-74.12345678",
    "name": "myhomecanair"
}'
```

Que en caso exitoso responderá con los mismos datos enviados y el id.

```json
{"id":1,"mac":"D714E1CC605C","lat":"4.12345678","lon":"-74.12345678","name":"myhomecanair"}
```

_La descripción de cada uno de los endpoints disponibles en [Wiki][wiki]._

## En desarrollo

Cada vez que haga cambios y los guarde en su entorno de desarrollo local estos
se verán reflejados en la instancia que está ejecutando en docker.

Para que pueda pueda ver las trazas de los posibles erores por favor copie el archivo de configuración, en el mismo podrá hacer cambios de configuraciones si así lo desea.

## Release History

Por ahora el trabajo está en progreso, no hemos hecho un release oficial

## Contributing

El código está en inglés, tanto variables, nombres comentarios, comentarios de
los commits.

1. Haga un fork del proyecto (<https://github.com/yourname/yourproject/fork>)
2. Cree una rama del mismo (`git checkout -b feature/fooBar`)
3. Haga los commits necesarios con mensajes que describan el cometido de los cambios (`git commit -am 'Add some fooBar'`)
4. Envíe los cambios a su rama (`git push origin feature/fooBar`)
5. Abra un pull request
