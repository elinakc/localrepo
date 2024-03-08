from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    
    # It is used to store all the users that are active in a room
    participants = models.ManyToManyField(User, related_name='participants', blank=True)

    # This updated is used to update everytime when there is some changes in the table
    # The difference between auto_now and auto_now_add is that auto_now takes a snapshot on  every time we save this item here now and
    # auto_now_add only takes a timestamp when we first create or save this instance .
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        # This -updated and -created will updated the last update file into first
        ordering = ['-updated', '-created']
        

    def __str__(self):
        return self.name


class Message(models.Model):
    # When we put on_delete = models.SET_NULL then we need to set null=True to makesure that the database allow it to be empty
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # This is how we connect the relationship in database,here what we do is give a parent name called Room in foreign key parameter
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE
    )  # What on_delete=models.CASCADE is going to do is that it delete this children node(Message) when parent node(ROOM) is deleted

    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
