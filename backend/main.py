from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from models import UserCreate, UserLogin, UserResponse
from database import db

app = FastAPI(title="Sistema de Autenticación", version="1.0.0")

# Configurar CORS para permitir requests desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "API de Autenticación funcionando"}

@app.post("/api/register", response_model=UserResponse)
async def register_user(user_data: UserCreate):
    """Endpoint para registrar un nuevo usuario"""
    try:
        user = db.create_user(
            name=user_data.name,
            email=user_data.email,
            password=user_data.password
        )
        return UserResponse(
            id=user.id,
            name=user.name,
            email=user.email
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor"
        )

@app.post("/api/login")
async def login_user(login_data: UserLogin):
    """Endpoint para iniciar sesión"""
    user = db.authenticate_user(login_data.email, login_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )
    
    return {
        "message": "Inicio de sesión exitoso",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }

@app.get("/api/users", response_model=list[UserResponse])
async def get_all_users():
    """Endpoint para obtener todos los usuarios (solo para desarrollo)"""
    users = db.get_all_users()
    return [UserResponse(id=user.id, name=user.name, email=user.email) for user in users]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
