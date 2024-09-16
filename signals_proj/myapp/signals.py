from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.apps import apps

# Get the model dynamically instead of importing directly
MyModel = apps.get_model('myapp', 'MyModel')

@receiver(pre_save, sender=MyModel)
def pre_save_handler(sender, instance, **kwargs):
    print(f'Pre-save signal for {instance.name}')

@receiver(post_save, sender=MyModel)
def post_save_handler(sender, instance, **kwargs):
    print(f'Post-save signal for {instance.name}')
