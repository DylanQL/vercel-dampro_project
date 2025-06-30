# Archivos para Deploy en Vercel - Dampro SAC

## Archivos creados/modificados para el despliegue:

### 1. `vercel.json`
Configuración principal de Vercel que define:
- Cómo construir el proyecto Python
- Ruteo de archivos estáticos
- Configuración del runtime

### 2. `build_files.sh`
Script que se ejecuta durante el deploy:
- Instala dependencias de Python
- Ejecuta collectstatic para archivos estáticos
- Ejecuta migraciones de base de datos

### 3. `requirements.txt`
Lista actualizada de todas las dependencias de Python necesarias.

### 4. `dampro_system/settings.py` (modificado)
Configuraciones actualizadas para producción:
- Variables de entorno para SECRET_KEY y DEBUG
- ALLOWED_HOSTS configurado para Vercel
- Configuración de archivos estáticos para deploy
- Zona horaria configurada para Perú

### 5. `dampro_system/wsgi.py` (modificado)
Punto de entrada WSGI con variable `app` requerida por Vercel.

### 6. `.gitignore` (actualizado)
Archivo actualizado para ignorar archivos innecesarios en el repositorio.

### 7. `.env.example`
Plantilla de variables de entorno para configurar en Vercel.

### 8. `README.md`
Documentación completa del proyecto con instrucciones de instalación y deploy.

## Pasos para el deploy:

1. **Subir a GitHub:**
   ```bash
   git add .
   git commit -m "Corrección configuración Vercel - arreglar errores de build"
   git push origin main
   ```

2. **Configurar en Vercel:**
   - Ir a vercel.com
   - Importar repositorio de GitHub
   - Configurar variables de entorno:
     - SECRET_KEY: django-insecure-d2&96j)tfe_dbif-g6@&&6tmu@7)#zqh0tj0nqnb8)#i^6n7i0
     - DEBUG: False
     - DJANGO_SETTINGS_MODULE: dampro_system.settings

3. **Deploy automático:**
   Vercel detectará la configuración simplificada y desplegará correctamente.

## Correcciones realizadas:

- ✅ Simplificado vercel.json para evitar conflictos con builds
- ✅ Removido build_files.sh que causaba problemas con pip
- ✅ Configuración de archivos estáticos corregida
- ✅ Requirements.txt reorganizado con Django al inicio

## Notas importantes:

- **Base de datos**: SQLite se recrea en cada deploy (datos no persistentes)
- **Para producción real**: Considerar migrar a PostgreSQL
- **Archivos estáticos**: Se sirven desde la carpeta staticfiles_build
- **Variables de entorno**: Configurar en el dashboard de Vercel

¡El proyecto está listo para el deploy en Vercel! 🚀
