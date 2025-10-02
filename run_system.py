#!/usr/bin/env python3
"""
Script para ejecutar el sistema completo de autenticación
Ejecuta tanto el backend (FastAPI) como el frontend (servidor HTTP) desde una sola terminal
"""

import subprocess
import threading
import time
import os
import sys
from pathlib import Path

def run_backend():
    """Ejecuta el servidor FastAPI backend"""
    backend_path = Path(__file__).parent / "backend"
    os.chdir(backend_path)
    
    print("🚀 Iniciando backend FastAPI en puerto 8000...")
    try:
        subprocess.run([sys.executable, "main.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando backend: {e}")
    except KeyboardInterrupt:
        print("\n🛑 Backend detenido")

def run_frontend():
    """Ejecuta el servidor HTTP para el frontend"""
    frontend_path = Path(__file__).parent / "frontend"
    os.chdir(frontend_path)
    
    print("🌐 Iniciando frontend en puerto 3000...")
    try:
        subprocess.run([sys.executable, "-m", "http.server", "3000"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando frontend: {e}")
    except KeyboardInterrupt:
        print("\n🛑 Frontend detenido")

def main():
    print("=" * 60)
    print("🎯 SISTEMA DE AUTENTICACIÓN")
    print("=" * 60)
    print("📋 Credenciales de prueba:")
    print("   Email: user@test.com")
    print("   Contraseña: Test123")
    print("=" * 60)
    
    # Crear hilos para ejecutar ambos servidores
    backend_thread = threading.Thread(target=run_backend, daemon=True)
    frontend_thread = threading.Thread(target=run_frontend, daemon=True)
    
    try:
        # Iniciar backend
        backend_thread.start()
        time.sleep(2)  # Esperar a que el backend se inicie
        
        # Iniciar frontend
        frontend_thread.start()
        time.sleep(1)
        
        print("\n✅ Sistema iniciado correctamente!")
        print("🌐 Frontend: http://localhost:3000")
        print("🔧 Backend API: http://localhost:8000")
        print("\n💡 Presiona Ctrl+C para detener ambos servidores")
        
        # Mantener el script ejecutándose
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n\n🛑 Deteniendo sistema...")
        print("👋 ¡Hasta luego!")
        
if __name__ == "__main__":
    main()
