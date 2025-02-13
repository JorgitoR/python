# 🛠️ Sistema de Autenticación con Python y SQLite

Este es un sistema básico de autenticación en Python que permite a los usuarios registrarse, iniciar sesión y actualizar su contraseña. Utiliza **arquitectura hexagonal** y sigue **principios SOLID**.

## 👤 Estructura del Proyecto

```
/project-root
│── src/               # Código fuente del proyecto
│   ├── domain/        # Contiene las interfaces (puertos)
│   │   ├── ports/
│   │   │   ├── Idb.py     # Interfaz para la base de datos
│   │   ├── Iauth.py       # Interfaz de autenticación
│   
│   ├── infra/         # Implementaciones de infraestructura
│   │   ├── db/
│   │   │   ├── database.py  # Manejador de conexión SQLite
│   │   │   ├── sql.py       # Implementación SQL de IDatabase
│   
│   ├── ecase/         # Casos de uso
│   │   ├── service.py     # Lógica de autenticación
│   
│   ├── app.py         # Punto de entrada principal
│   
│── data/          # Carpeta para almacenar la base de datos
│   ├── users.db
│   
│── venv/          # Ambiente virtual de Python
│── README.md      # Documentación del proyecto
│── requirements.txt # Dependencias del proyecto
```

## 📦 Requisitos

- **Python 3.x**
- **SQLite3** (incluido en Python por defecto)
- Librerías necesarias en `requirements.txt`

## 🚀 Instalación y Configuración del Ambiente Virtual

1️⃣ **Clonar el repositorio**
```bash
git clone https://github.com/tuusuario/proyecto-autenticacion.git
cd proyecto-autenticacion
```

2️⃣ **Crear y activar un entorno virtual**
```bash
# En Windows
python -m venv venv
venv\Scripts\activate
```
```bash
# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3️⃣ **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4️⃣ **Ejecutar el script de autenticación**
```bash
python src/app.py
```

## 📌 Funcionalidades

✔ **Registrar un usuario (`sign_up`)**  
✔ **Iniciar sesión (`login`)**    

## 📚 Ejemplo de Uso

```bash
==================================================
               Testing User Registration               
==================================================

[Sign Up (test@example.com)] ➞ {'status_code': 201, 'message': 'User has been created successfully'}

==================================================
               Testing User Login                
==================================================

[Login (Correct Password)] ➞ {'status_code': 200, 'message': 'User has been logged in successfully'}
```

---

✏ **Este README se actualizará a medida que el proyecto avance.**

