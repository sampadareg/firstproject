from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()
POSITION_CHOICE=[
    ("fr", "First Position"),
    ("sc", "Second Position"),
    ("tr", "Third Position"),
    ("ft", "Fourth Position"),
]
class Profile(models.Model):
    user = models.OneToOneField(to=USER,null=False,blank=False, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=False, blank=False)
    position = models.CharField(null=False, blank=False, choices=POSITION_CHOICE)
    # profile_pic = models.charField(blank=False, null=False)
    # created_at= models.DateTime(USER, blank=False, null=False, on_delete=models.DO_NOTHING)
    # updated_at=models.CharField(max_length=120,null=False, blank=False
    #                             )