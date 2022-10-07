# API Djando Example

APi creado con Django Rest Framework

## Set up del proyecto

1. Ejecutar el siguiente comando para crear un ambiente virtual

    ```sh
        python3 -m venv env
    ```

2. Ejecuta el siguiente comando para activar el ambiente virtual\

    ``` sh
        # para linux / mac / git bash
        source env/bin/activate

        # para windows
        .\env\Scripts\python.exe
    ```

3. Ejecutar el siguiente comando para instalar las dependencias necesarios del proyecto

    ```sh
        pip install -r requirements.txt
    ```

4. Ejecuta el siguiente comando para aplicar las migraciones

    ```sh
        python3 manage.py migrate
    ```

5. Ejecuta el siguiente comando para ejecutar el servidor

    ```sh
        python3 manage.py runserver
    ```

6. **Listo!** Tu servidor se estara ejecutando en la siguiente dirección `http://127.0.0.1:8000/`

## Endpoints disponible

- Crear un usuario. **POST** `http://127.0.0.1:8000/api/v1/users`\
    Al hacer la petición necesitaras mandar en el *body* la siguiente estructura:

    ```json
    {
        "email": "email@gmail.com",
        "password": "example123",
        "first_name": "Chanchito",
        "last_name": "Feliz"
    }
    ```

- Validar las credenciales de un usuario (login). **GET** `http://127.0.0.1:8000/api/v1/users/validate`\
    Se debe mandar la siguiente estructura en el *body* de la petición:

    ```json
    {
        "email": "devrrior@gmail.com",
        "password": "123"
    }
    ```
