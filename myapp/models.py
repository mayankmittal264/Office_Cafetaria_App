from django.db import models
import uuid
import datetime

# Create your models here.


class Employee(models.Model):
    regid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    regdate = models.DateTimeField(default=datetime.datetime.now(), editable=False)
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    oname = models.CharField(max_length=20)
    eid = models.CharField(max_length=10, unique=True)
    mono = models.BigIntegerField()
    email = models.CharField(max_length=50)
    img = models.ImageField(upload_to='idcard/')

    def __str__(self):
        return str(self.regid)

    def get_regdate(self):
        return self.regdate

    def get_Name(self):
        Name = self.fname+" "+self.lname
        return Name

    def get_org(self):
        return self.oname

    def get_mobile(self):
        return self.mono

    def get_email(self):
        return self.email

    def get_idcard(self):
        return self.img
