# Sistema de Autenticación

Este proyecto implementa un sistema completo de registro y autenticación con Vue.js en el frontend y FastAPI en el backend.

## si

## Estructura del Proyecto


```
/
├── frontend/          # Aplicación Vue.js
│   ├── src/
│   │   ├── components/
│   │   │   ├── Login.vue
│   │   │   └── Register.vue
│   │   ├── App.vue
│   │   └── main.js
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
└── backend/           # API FastAPI
    ├── main.py
    ├── models.py
    ├── database.py
    └── requirements.txt
```

## Funcionalidades

### Frontend (Vue.js)
- ✅ Formulario de registro con validación
- ✅ Formulario de inicio de sesión
- ✅ Interfaz moderna y responsiva
- ✅ Navegación entre formularios
- ✅ Manejo de errores y mensajes de éxito

### Backend (FastAPI)
- ✅ Modelo User con operaciones CRUD
- ✅ Endpoint de registro (`POST /api/register`)
- ✅ Endpoint de login (`POST /api/login`)
- ✅ Validación de credenciales
- ✅ Encriptación de contraseñas con bcrypt
- ✅ Datos de prueba predefinidos

## Credenciales de Prueba

- **Email:** user@test.com
- **Contraseña:** Test123

## Instalación y Ejecución

### Backend
```bash
cd backend
pip install -r requirements.txt
python main.py
```
El backend estará disponible en: http://localhost:8000

### Frontend
```bash
cd frontend
npm install
npm run dev
```
El frontend estará disponible en: http://localhost:3000

## Endpoints de la API

- `GET /` - Mensaje de bienvenida
- `POST /api/register` - Registrar nuevo usuario
- `POST /api/login` - Iniciar sesión
- `GET /api/users` - Listar todos los usuarios (desarrollo)

## Tecnologías Utilizadas

- **Frontend:** Vue.js 3, Vue Router, Axios, Vite
- **Backend:** FastAPI, Pydantic, bcrypt, uvicorn
- **Estilos:** CSS personalizado con gradientes y animaciones
