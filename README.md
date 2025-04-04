Versión de jupyter notebook utilizada = 7.3.3

Para ejecutar el programa se deberá instalar  un entorno de trabajo interactivo que permite desarrollar código en Pytho llamado Jupyter notebook.
Este entorno nos permite editar el código desde el navegador, resaltando la sintaxis, indentación y también provee funciones de autocompletado. Permite ejecutar código desde el navegador, mostrando los resultados de esta ejecución Provee facilidades para la documentación y visualización del código. Permite iniciar una sesión de una terminal de bash para ejecutar comandos desde el mismo navegador. Se puede agregar cualquier archivo .py o .ipynb simplemente arrastrandolos hasta la interfaz de la herramienta. Los archivos que genera son de extensión "ipynb" (como el que se proporciona en este caso).

Para la instalación de Jupyter Notebook se deben tener instalado Python 3.10.2 (versión), la Pip3.
Generalmente, pip viene preinstalado con Python. Sin embargo, si no está disponible, podemos instalarlo manualmente descargando el script de instalación desde aquí(http://bootstrap.pypa.io/get-pip.py) y luego ejecutar el siguiente comando:
python get-pip.py

Para instalar Jupyter Notebook utilizando pip, se debe ejecutar el comando: pip3 install jupyter
Una vez instalado, para poder comenzar a utilizarlo es necesario iniciar el servidor de Jupyter Notebook. Este servidor se ejecutará en "localhost", es decir que nuestra computadora creará un servidor local ejecutando la herramienta. Para esto se debe ejecutar el siguiente comando: jupyter notebook
Una vez iniciado el servidor, nuestra computadora abrirá automáticamente el navegador web visualizando la interfaz gráfica de la herramienta. En caso de que esto no suceda automáticamente, abrir un navegador web e ingresar la siguiente url: http://localhost:8888/ Por defecto el servidor se ejecuta utilizando el puerto 8888 de nuestra computadora.
Para terminar la sesión del servidor basta simplemente con ir nuevamente a la terminal donde se ejecuto el comando anterior y presionar las teclas CTRL + C. La herramienta le pedirá una confimación y luego apagará el servidor. Importante: Guardar todos los cambios antes de apagar el servidor. De esta forma, al iniciarlo nuevamente, todos los archivos de la sesión anterior seguirán estando disponibles.

Para comenzar a utilizar Jupyter Notebook, primero debemos crear un archivo de código Python o "notebook". Para esto simplemente debemos hacer click en el botón "New" y seleccionar el intérprete de Python.
Una vez creado nuestro archivo notebook, solo basta con escribir código Python en él y darle click al botón "Play" para ejecutarlo y ver su resultado.