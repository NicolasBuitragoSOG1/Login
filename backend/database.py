from models import User
from typing import List, Optional

class UserDatabase:
    def __init__(self):
        self.users: List[User] = []
        self.next_id = 1
        
        # Datos de prueba predefinidos
        test_user = User(
            id=self.next_id,
            name="Usuario de Prueba",
            email="user@test.com",
            hashed_password=User.hash_password("Test123")
        )
        self.users.append(test_user)
        self.next_id += 1
    
    def create_user(self, name: str, email: str, password: str) -> User:
        """Crear un nuevo usuario"""
        # Verificar si el email ya existe
        if self.get_user_by_email(email):
            raise ValueError("El email ya está registrado")
        
        hashed_password = User.hash_password(password)
        user = User(
            id=self.next_id,
            name=name,
            email=email,
            hashed_password=hashed_password
        )
        
        self.users.append(user)
        self.next_id += 1
        return user
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Obtener usuario por email"""
        for user in self.users:
            if user.email == email:
                return user
        return None
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Obtener usuario por ID"""
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """Autenticar usuario con email y contraseña"""
        user = self.get_user_by_email(email)
        if user and User.verify_password(password, user.hashed_password):
            return user
        return None
    
    def get_all_users(self) -> List[User]:
        """Obtener todos los usuarios (para propósitos de desarrollo)"""
        return self.users

# Instancia global de la base de datos
db = UserDatabase()
