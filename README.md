# triple_news

## Descripción
Aquí hay una breve lista de las capacidades funcionales del proyecto triple_news:
- La página principal del proyecto muestra las 10 publicaciones de noticias más recientes. La página principal está disponible para todos los usuarios. Las noticias se muestran de forma abreviada (solo las primeras 15 palabras son visibles).
- Cada noticia tiene su propia página con el texto completo; ahí también se muestran los comentarios de los usuarios.
- Cualquier usuario o usuaria puede registrarse por su cuenta en el sitio web.
- Un usuario conectado (autorizado) puede dejar, editar y borrar sus propios comentarios.
- Si hay comentarios sobre la publicación de una noticia, el número de comentarios se muestra en la página principal debajo de la publicación.
- El código del proyecto contiene una lista de palabras prohibidas en los comentarios, como "bribón" y "sinvergüenza".


Para cargar noticias preparadas después de aplicar las migraciones, ejecuta este comando:
```bash
python manage.py loaddata db.json
```


## Cómo trabajar con el repositorio
Para empezar la tarea, necesitas copiar la URL de tu repositorio y clonarlo.
  
### Creación de un entorno virtual

1. Abre Visual Studio Code, ve a "Archivo" / "Abrir carpeta" y abre *Dev/triple_news/*. 
2. Inicia la terminal en VS Code y asegúrate de trabajar desde el directorio *triple_news/*. Si usas Windows, asegúrate de que se ejecute Git Bash en la terminal, y no a través de PowerShell o algún otro. Ejecuta este comando:
- Linux/macOS
    
    ```bash
    python3 -m venv venv
    ```
    
- Windows
    
    ```python
    python -m venv venv
    ```
   
El entorno virtual se desplegará en el directorio *triple_news/*. También la carpeta `venv` aparecerá allí, y almacenará todas las dependencias del proyecto.


### Activación del entorno virtual
En la terminal, navega hasta el directorio raíz del proyecto *Dev/triple_news/* y ejecuta el comando:
- Linux/macOS
    
    ```bash
    source venv/bin/activate
    ```
    
- Windows
    
    ```bash
    source venv/Scripts/activate
    ```
    

Ahora todos los comandos en la terminal irán precedidos por el string `(venv)`.

💡 Todos los comandos posteriores en la terminal deben ejecutarse con el entorno virtual activado.

Actualiza pip:

```bash
python -m pip install --upgrade pip
```

### Instalar las dependencias del archivo *requirements.txt*:
Mientras estás en la carpeta *Dev/triple_news/*, ejecuta el comando:

```bash
pip install -r requirements.txt
```

### Uso de migraciones

    
En el directorio con el archivo "manage.py", ejecuta el siguiente comando:

```bash
python manage.py migrate
```

### Ejecutar el proyecto en modo dev

    
En el directorio con el archivo "manage.py", ejecuta el siguiente comando:

```bash
python manage.py runserver
```

En respuesta, Django indicará que el servidor está funcionando y que el proyecto está disponible en la dirección [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
