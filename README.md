
# API Documentation

## Funcionamiento y Arquitectura
Esta API está diseñada utilizando principios de arquitectura limpia, lo que implica una separación clara entre modelos, servicios, controladores y repositorios. Esto asegura que la API sea fácil de mantener y escalar. La API maneja datos relacionados con usuarios y tiendas.

### Estructura de Directorios
- `/models`: Contiene las definiciones de las entidades.
- `/services`: Lógica de negocio y operaciones de la aplicación.
- `/controllers`: Manejo de las peticiones y respuestas HTTP.
- `/repositories`: Interacción con la base de datos (simulada en este caso).

## Instalación
Para instalar y correr esta API localmente, sigue estos pasos:

1. Clona el repositorio:
   ```
   git clone URL_DEL_REPOSITORIO
   ```
2. Instala las dependencias necesarias:
   ```
   pip install flask
   ```
3. Ejecuta la aplicación:
   ```
   python app.py
   ```
   Esto iniciará el servidor en `localhost` en el puerto `5000`.

## Curls para Uso en Postman
Puedes importar los siguientes comandos CURL en Postman para probar la API:

### Obtener Todos los Usuarios
```
GET /api/v1/users
```

### Eliminar un Usuario
```
DELETE /api/v1/users/{id}
```

### Obtener Todas las Tiendas de un Usuario
```
GET /api/v1/users/{id}/stores
```

Asegúrate de reemplazar `{id}` con el identificador real del usuario cuando pruebes los endpoints.

# clean-architecture-api
