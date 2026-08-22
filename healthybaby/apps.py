from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_default_user(sender, **kwargs):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    USERNAME = 'admin'
    EMAIL = 'admin@admin.com'
    PASSWORD = 'senha_padrao_123'

    if not User.objects.filter(username=USERNAME).exists():
        User.objects.create_superuser(username=USERNAME, email=EMAIL, password=PASSWORD)

class HealthybabyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'healthybaby'

    def ready(self):
        post_migrate.connect(create_default_user, sender=self)