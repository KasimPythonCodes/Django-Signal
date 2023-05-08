from django.db.models.signals import post_save , pre_save  ,pre_delete
from django.contrib.auth.models import User
from signaldevapp.models import*
from django.dispatch import receiver

# def save_post(sender ,instance,**kwargs):
#     print("post is save")

# def save_pre(sender ,instance,**kwargs):
#     print("save is not  called pre is before save")

# def delete_pre(sender ,instance,**kwargs):
#     print("hello")

# post_save.connect(save_post  , sender = Student)
# pre_save.connect(save_pre  , sender = Student)
# pre_delete.connect(delete_pre  , sender = Student)


@receiver(post_save , sender=User)
def student(sender , instance ,created ,  **kwargs):
    if created :
        Student.objects.create(user=instance , name="" , password="")