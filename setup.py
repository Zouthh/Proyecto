import sys
from cx_Freeze import setup, Executable

# Reemplaza 'nombre_del_script.py' con el nombre de tu archivo .py
script_name = 'e.py'

# Configuración para el ejecutable
build_exe_options = {
    'packages': ['tkinter', 'PIL'],
    'include_files': ['imagen1.jpeg', 'imagen2.jpeg', 'imagen3.jpeg']
}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

# Configuración para el ejecutable y su creación
setup(
    name='BuscadorDeObjetos',
    version='1.0',
    description='Aplicación de Buscador de Objetos',
    options={'build_exe': build_exe_options},
    executables=[Executable(script_name, base=base)]
)
