# from django.apps import AppConfig
# from django.db.models.signals import post_save


# class CustomerConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'customer'


#     def ready(self):
#         from customer.signals import create_profile
#         from django.contrib.auth.models import User
#         post_save.connect(create_profile, sender=User)
#         from customer.signals import save_profile
#         post_save.connect(save_profile, sender=User)
