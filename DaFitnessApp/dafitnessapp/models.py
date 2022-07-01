from django.db import models


class dafitnessapp(models.Model):
    message = models.CharField(max_length=200)

# model associations
# model for user information
class User(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

# model for user input in questions
class Data(models.Model):
    GENDER = (
        ('m', 'm'),
        ('f', 'f'),
    )
    
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    activity = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)
    age = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


# model for user input in pie chart
class Pie(models.Model):
    breakfast = models.FloatField(null=True)
    lunch = models.FloatField(null=True)
    dinner = models.FloatField(null=True)
    snacks = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

# one to many
class Info(models.Model): 
    user = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    data = models.ForeignKey(Data, null=True, on_delete= models.SET_NULL)
    pie = models.ForeignKey(Pie, null=True, on_delete= models.SET_NULL)