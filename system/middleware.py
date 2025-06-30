from django.http import JsonResponse
import logging
import traceback

logger = logging.getLogger(__name__)

class VercelErrorMiddleware:
    """
    Middleware para manejar errores en Vercel de manera más elegante
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except Exception as e:
            logger.error(f"Error en request: {e}")
            logger.error(traceback.format_exc())
            
            if request.path.startswith('/api/'):
                return JsonResponse({
                    'error': 'Error interno del servidor',
                    'message': str(e) if hasattr(e, 'message') else 'Error desconocido'
                }, status=500)
            
            # Para requests HTML, devolver una respuesta simple
            from django.http import HttpResponse
            return HttpResponse(f"""
            <html>
                <head><title>Error 500</title></head>
                <body>
                    <h1>Error interno del servidor</h1>
                    <p>Lo sentimos, ocurrió un error. Por favor, intente más tarde.</p>
                    <p>Error: {str(e)}</p>
                </body>
            </html>
            """, status=500)

    def process_exception(self, request, exception):
        logger.error(f"Excepción no manejada: {exception}")
        logger.error(traceback.format_exc())
        return None
