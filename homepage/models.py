from django.db import models


# Create your models here.


class Location(models.Model):
    country = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True)
    allay = models.CharField(max_length=200, null=True)
    long = models.IntegerField(max_length=200, null=True)
    lg = models.IntegerField(max_length=200, null=True)


class User(models.Model):
    user_name = models.CharField(max_length=80, null=False)
    phone = models.IntegerField(max_length=40, null=True)
    email_user = models.EmailField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


class Pro_user(models.Model):
    first_name = models.CharField(max_length=80, null=False)
    last_name = models.CharField(max_length=80, null=False)
    bio = models.CharField(max_length=200, null=True)
    facebook_id = models.IntegerField(max_length=90, null=True)
    insta_id = models.IntegerField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice_gender = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('unspacifide', 'Unspacifide'),
    )
    gender = models.CharField(max_length=100, choices=choice_gender)


class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    body = models.CharField(max_length=200, null=True)
    date_of_start = models.CharField(max_length=100, null=True)
    how_many_days = models.IntegerField(max_length=365, null=True)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Visit(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    loction_id = models.ForeignKey(Location, on_delete=models.CASCADE)


class Conversation_reply(models.Model):
    reply_text = models.CharField(max_length=200, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.CharField(max_length=75, null=True)
    status = models.CharField(max_length=300, null=True)
    c_id = models.CharField(max_length=200, null=True)



class Conversation(models.Model):
    reply_text = models.CharField(max_length=200, null=True)
    user_id = models.CharField(max_length=200, null=True)
    time = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)
    reply = models.ForeignKey(Conversation_reply, on_delete=models.CASCADE)


class Activity(models.Model):
    name = models.CharField(max_length=200, null=True)
    detailsofacivity = models.CharField(max_length=200, null=True)
    typeofactiviy = models.CharField(max_length=200, null=True)


class acti_post(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    activt = models.ForeignKey(Activity, on_delete=models.CASCADE)
