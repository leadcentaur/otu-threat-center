from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    #for when the user account is created we also create a profile.
    def ready(self):
        import users.signals
