from django.apps import AppConfig
import os
import atexit
import threading
from .respaldo import respaldo_periodico  # Asegúrate de que este archivo exista en api/

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        # Solo ejecutar en el proceso principal (no en el watcher del auto-reload)
        if os.environ.get('RUN_MAIN') == 'true':
            # Iniciar respaldo automático en segundo plano
            threading.Thread(target=respaldo_periodico, daemon=True).start()

            # Registrar cierre de sesiones al terminar el servidor (solo una vez)
            if not hasattr(atexit, '_clear_sessions_registered'):
                from django.contrib.sessions.models import Session

                def clear_sessions_on_exit():
                    print("Borrando sesiones activas...")
                    Session.objects.all().delete()

                atexit.register(clear_sessions_on_exit)
                atexit._clear_sessions_registered = True
