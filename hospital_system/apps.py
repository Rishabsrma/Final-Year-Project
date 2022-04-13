from django.apps import AppConfig


class HospitalSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hospital_system'


    def ready(self):
        import hospital_system.signals
