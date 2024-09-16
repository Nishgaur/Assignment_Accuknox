from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, created, **kwargs):
    if not created:
        return
    
    post_save.disconnect(my_model_post_save, sender=MyModel)

    # Attempt to modify the instance
    instance.name = "Modified in signal"
    instance.save()  # This triggers post_save again, but it's disconnected

    # Reconnect the signal
    post_save.connect(my_model_post_save, sender=MyModel)

def create_model_instance():
    with transaction.atomic():
        instance = MyModel(name="Original Name")
        instance.save()  # This triggers the post_save signal

create_model_instance()

modified_instance = MyModel.objects.first()
print(modified_instance.name)  
