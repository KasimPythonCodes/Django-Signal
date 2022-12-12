from django.apps import AppConfig


class SignaldevappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signaldevapp'
    
    def ready(self):
        import signaldevapp.signals
        
