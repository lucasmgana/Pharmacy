from django.apps import AppConfig


class MedicinestockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'medicineStock'



    def ready(self):
        import medicineStock.signals