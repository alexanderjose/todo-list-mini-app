### Guía de instalación (paso a paso)

>Una mini-guía, para describir un poco los pasos para la creación de una mini-aplicación en python-django.

1. Creamos y accedemos a la carpeta que contendrá nuestro proyecto:<br>
    code $ mkdir todo-list-mini-app/

    ```
    $ cd todo-list-mini-app/
    ```
2. Instalamos e inicializamos el entorno virtual (virtualenv previamente instalado):<br>
    ```
    $ source env/bin/activate
    ```

    ```
    $ virtualenv env
    ```
3. Instalamos django(v1.9)<br>
    ```
    $ env/bin/pip install django==1.9
    ```

4. Inicializamos el proyecto:<br>
    ```
    $ django-admin startproject todo_list
    ```

5. Se inicializa el archivo requirements.txt (Para efectos practicos se incluye dentro del proyecto.)<br>
    ```
    $ env/bin/pip freeze > todo_list/requirements.txt
    ```

6. Usaremos Postgresql para esta aplicación, por lo tanto, regresamos a la raíz del proyecto instalamos el paquete de conexión de django correspondiente (estable) y lo añadimos al requirements.txt<br>
    ```
    $ env/bin/pip install psycopg2==2.6.1
    ```

    ```
    $ env/bin/pip freeze > todo_list/requirements.txt
    ```
7. Ingresamos al proyecto, abrimos el archivo settings.py y modificamos la variable DATABASES, para configurar la conexión con Postgresql (La base de datos debe estar previamente creada) y la base de datos: optic_todolist.<br>
    ```
    $ cd todo_list/
    ```

    ```
    $ nano todo_list/settings.py
    ```
8. Ingresamos al proyecto nuevamente y corremos las migraciones iniciales:<br>
    ```
    $ python manage.py migrate
    ```

9. Comprobamos que el servidor corra correctamente, a través de: [http://127.0.0.1:8000/][f6fc2166]
10. Regresamos a la raíz del proyecto e instalamos la utilidad django-allauth para la gestión de los usuarios.<br>
    ```
    $ env/bin/pip install django-allauth==0.27.0
    ```

11. Una vez instalado django-allauth, procedemos a su configuración siguiendo las indicaciones de la página oficial: [http://django-allauth.readthedocs.io][49a64f26]
12. Ingresamos al proyecto nuevamente y corremos las migraciones correspondientes al módulo allauth:<br>
    ```
    $ python manage.py migrate
    ```

13. Creamos un superusuario para efectos de configuración:<br>
    ```
    $ cd todo_list/
    ```

    ```
    $ python manage.py createsuperuser
    ```

  [f6fc2166]: # "Tú Servidor Local"
  [49a64f26]: http://django-allauth.readthedocs.io "Documentación Django-allauth"
