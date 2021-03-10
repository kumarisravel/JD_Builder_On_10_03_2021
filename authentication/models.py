from django.db.models import CharField,IntegerField,DateField,Model,AutoField

# Create your models here.

class Clients(Model):
    ClientId=CharField(max_length=10)
    Email=CharField(max_length=100,primary_key=True)
    ClientName=CharField(max_length=150)
    Password=CharField(max_length=8)

    def __str__(self):
        return self.ClientId


class UserMasterTable(Model):
    UserId=CharField(max_length=10,primary_key=True)
    UserEmail=CharField(max_length=50)
    UserName=CharField(max_length=50)
    UserCompany=CharField(max_length=100)
    UserPassword=CharField(max_length=20)
    UserActiveStatus=IntegerField()
    UserCreatedBy=CharField(max_length=50)
    UserCreatedDate=DateField(max_length=8)
    UserUpdatedBy=CharField(max_length=50)
    UserUpdatedDate=DateField(max_length=8)

    def __str__(self):
        return self.UserId



