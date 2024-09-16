from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import threading

class Mymodel(models.Model):
    name = models.CharField(max_length=100)
    description  = models.TextField()

@receiver(pre_save, sender=Mymodel)
def my_model_pre_save(sender,instance, **kwargs):
    current_thread = threading.current_thread()
    print(f"Signal handler running in thread: {current_thread.name}")
    print(f"Sender thread: {threading.current_thread().name}")
    print(f"Receiver thread: {current_thread.name}")