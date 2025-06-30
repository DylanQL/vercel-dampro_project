#!/usr/bin/env python

import os
import subprocess
import sys

def run_command(command):
    """Ejecuta un comando y maneja errores"""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {command}")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando: {command}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False

def main():
    """Ejecuta los comandos necesarios para el build de Vercel"""
    print("🚀 Iniciando build de Django para Vercel...")
    
    # Configurar variable de entorno
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dampro_system.settings')
    
    # Ejecutar migraciones
    if not run_command("python manage.py migrate --noinput"):
        sys.exit(1)
    
    # Recopilar archivos estáticos
    if not run_command("python manage.py collectstatic --noinput --clear"):
        sys.exit(1)
    
    print("✅ Build completado exitosamente!")

if __name__ == "__main__":
    main()
