from django.core.management.base import BaseCommand
from django.db import transaction
from system.models import Usuario, UserAccount, Course, Empresa

class Command(BaseCommand):
    help = 'Inicializa la base de datos con datos de ejemplo para Vercel'

    def handle(self, *args, **options):
        self.stdout.write('Inicializando datos de ejemplo...')
        
        try:
            with transaction.atomic():
                # Crear usuario administrador si no existe
                if not Usuario.objects.filter(dni='12345678').exists():
                    admin_user = Usuario.objects.create(
                        first_name='Admin',
                        last_name='Sistema',
                        dni='12345678',
                        user_type='Admin'
                    )
                    
                    UserAccount.objects.create(
                        username='admin',
                        password='admin123',  # En producción debería estar encriptado
                        usuario=admin_user,
                        status='active'
                    )
                    self.stdout.write('✅ Usuario administrador creado')
                
                # Crear curso de ejemplo si no existe
                if not Course.objects.filter(name='Seguridad Industrial Básica').exists():
                    Course.objects.create(
                        name='Seguridad Industrial Básica',
                        course_hours=40
                    )
                    self.stdout.write('✅ Curso de ejemplo creado')
                
                # Crear empresa de ejemplo si no existe
                if not Empresa.objects.filter(ruc='20100000001').exists():
                    Empresa.objects.create(
                        ruc='20100000001',
                        nombre='EMPRESA DE PRUEBA S.A.C.'
                    )
                    self.stdout.write('✅ Empresa de ejemplo creada')
                
                self.stdout.write(
                    self.style.SUCCESS('✅ Inicialización completada exitosamente')
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error durante la inicialización: {e}')
            )
