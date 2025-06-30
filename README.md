# Dampro SAC - Sistema de Gestión de Certificados

Sistema web para la gestión de certificados de capacitaciones desarrollado con Django.

## Características

- ✅ Gestión de usuarios y empresas
- ✅ Registro y emisión de certificados
- ✅ Búsqueda por DNI y RUC
- ✅ Generación de PDFs con códigos QR
- ✅ Verificación online de certificados
- ✅ Panel de administración completo

## Tecnologías Utilizadas

- **Backend**: Django 5.2
- **Base de datos**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript, TailwindCSS
- **PDF Generation**: WeasyPrint
- **QR Codes**: qrcode
- **Deployment**: Vercel

## Instalación Local

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd dampro_project
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   # o
   venv\Scripts\activate     # En Windows
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar base de datos**
   ```bash
   python manage.py migrate
   ```

5. **Crear superusuario**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar servidor**
   ```bash
   python manage.py runserver
   ```

## Despliegue en Vercel

### Preparación

1. **Subir código a GitHub**
   ```bash
   git add .
   git commit -m "Preparar para deploy en Vercel"
   git push origin main
   ```

### En Vercel Dashboard

1. **Conectar repositorio**
   - Ve a [vercel.com](https://vercel.com)
   - Conecta tu cuenta de GitHub
   - Importa el repositorio del proyecto

2. **Configurar variables de entorno**
   En el dashboard de Vercel, ve a Settings > Environment Variables y agrega:
   
   ```
   SECRET_KEY = django-insecure-d2&96j)tfe_dbif-g6@&&6tmu@7)#zqh0tj0nqnb8)#i^6n7i0
   DEBUG = False
   ```

3. **Deploy**
   - Vercel detectará automáticamente que es un proyecto Python
   - El deploy se ejecutará automáticamente
   - Espera a que termine el proceso

### Archivos de Configuración Incluidos

- `vercel.json` - Configuración principal de Vercel
- `build_files.sh` - Script de construcción
- `requirements.txt` - Dependencias de Python
- `.gitignore` - Archivos a ignorar en Git

## Estructura del Proyecto

```
dampro_project/
├── dampro_system/          # Configuración principal de Django
│   ├── settings.py         # Configuraciones
│   ├── urls.py            # URLs principales
│   └── wsgi.py            # Punto de entrada WSGI
├── system/                # Aplicación principal
│   ├── models.py          # Modelos de base de datos
│   ├── views.py           # Vistas y lógica
│   ├── urls.py            # URLs de la aplicación
│   ├── templates/         # Plantillas HTML
│   └── static/            # Archivos estáticos
├── vercel.json            # Configuración de Vercel
├── build_files.sh         # Script de construcción
├── requirements.txt       # Dependencias
└── manage.py              # Comando de gestión de Django
```

## Funcionalidades Principales

### 1. Gestión de Usuarios
- Registro de empleados con DNI
- Búsqueda automática por DNI
- Asignación a empresas

### 2. Gestión de Empresas
- Registro con RUC
- Búsqueda automática por RUC
- Validación de duplicados

### 3. Gestión de Certificados
- Emisión de certificados
- Generación automática de códigos únicos
- Descarga en PDF con QR de verificación
- Verificación online pública

### 4. APIs Implementadas
- `POST /api/buscar-dni/` - Búsqueda de datos por DNI
- `POST /api/buscar-ruc/` - Búsqueda de datos por RUC

## Credenciales de Prueba

### Panel Administrativo
- **Usuario**: admin
- **Contraseña**: [definir durante creación]

### RUCs de Prueba (para búsqueda)
- 20100017491 - Telefónica del Perú
- 20131312955 - Saga Falabella
- 20100070970 - Supermercados Peruanos
- 20100000001 - Empresa de Prueba

## Mantenimiento

### Actualizar en Vercel
1. Hacer cambios en el código local
2. Commitear y pushear a GitHub
3. Vercel desplegará automáticamente

### Backup de Base de Datos
Para proyectos en producción, considera migrar a PostgreSQL:
```bash
pip install psycopg2-binary
```

## Soporte

Para soporte técnico o consultas sobre el sistema, contactar al equipo de desarrollo.

---

**Desarrollado con ❤️ para Dampro SAC**
