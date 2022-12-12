from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    # user = models.OneToOneField(User , on_delete=models.CASCADE)
    stu_id= models.CharField(max_length = 12 ,blank=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def save(self, *args, **kwargs):
        if self.stu_id == "":
            stu_id = str(uuid.uuid4()).replace("-", "")[:10]
            self.stu_id = stu_id
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)
    
    # def save(self, *args, **kwargs):
    #     if self.stu_id == "":
    #         stu_id = uuid.uuid4()
    #         # .replace("-", "")[:10]
    #         self.stu_id = str(stu_id.hex)[:4]
    #     super().save(*args, **kwargs)
