from django.apps import AppConfig
from django.conf import settings


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        from django.contrib.auth.models import Group
        from django.db.models.signals import post_save

        def add_to_default_group(sender, **kwargs):
            user = kwargs["instance"]
            if kwargs["created"]:
                group, ok = Group.objects.get_or_create(name="default")
                group.user_set.add(user)
            
        post_save.connect(add_to_default_group,
                              sender=settings.AUTH_USER_MODEL)
        """if the user has created we call to the function bellow and w we send her an sender have a user to add it to the group"""
