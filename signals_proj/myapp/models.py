from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#Create this instance in django shell by typing in the command : python manage.py shell
# from myapp.models import MyModel
#    ...: my_instance = MyModel.objects.create(name="Test Instance") 
