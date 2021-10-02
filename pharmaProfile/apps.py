from django.apps import AppConfig


class PharmaprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pharmaProfile'


    def ready(self):
        import pharmaProfile.signals