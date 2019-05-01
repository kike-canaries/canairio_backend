# Canairio Backend 
> Recibimos los datos provenientes de los [canair.ios](https://canair.io)

Si tiene interés en analizar información proveniente de la red ciudadana de calidad del aire,
o ayudar en el desarrollo de nuestro backend, está en el lugar correcto.

Si desea conocer más del proyecto, por favor visite [canair.io](https://canair.io) .  En este repositorio
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

Tenemos más endpoints disponibles, pero le invitamos a que vea el conjunto
de pruebas para que pueda ver cómo hacer solicitudes para añadir mediciones
o para obtener la medición más reciente.

## En desarrollo

Cada vez que haga cambios y los guarde en su entorno de desarrollo local estos
se verán reflejados en la instancia que está ejecutando en docker.

Para que pueda pueda ver las trazas de los posibles erores por favor copie el archivo de configuración, en el mismo podrá hacer cambios de configuraciones si así lo desea.

Esto solamente debe hacerlo la primera vez, porque es posible que después quiera
hacer más cambios sobre el mismo para su entorno de desarrollo.

```bash
cp scripts/dev_settings_local.py canairio/settings_local.py
```

### Pruebas

Para ejecutar las pruebas, ubíquese en el directorio clonado y ejecute,
previamente debe haber hecho que el proyecto corra `docker-compose up`.

```bash
docker-compose exec web bash
```

Y una vez en el shell, podrá ejecutar las pruebas

```bash
python manage.py test
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
