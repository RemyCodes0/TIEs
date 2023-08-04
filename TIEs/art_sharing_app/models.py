from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artwork(models.Model):
    titre=models.CharField(max_length=200, blank= True)
    legende = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="artwork/")
    comments = models.ManyToManyField(User, through="ArtworkComment", related_name="artwork_comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="liked_artwork", blank=True)
    
    class Meta:
        verbose_name= "Publication"
        ordering= ['-titre']

    def __str__(self):
        return self.titre

class Message(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    created_at= models.DateField(auto_now_add=True)

class Userprofile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile", default="profile/TIEs 20230802_125509.jpg")
    bio = models.CharField(max_length=200, blank = True, default=None)
    num_like = models.PositiveIntegerField(default=0)
    premium= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"

class Event(models.Model):
    image = models.ImageField(upload_to="events/", default=None)
    theme=models.CharField(max_length=200)
    start_date=models.DateField(auto_now_add=True)

class Like(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    artwork= models.ForeignKey(Artwork, on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} likes {self.artwork}"

class PremiumAccount(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    expiration_date= models.DateTimeField()

class ArtworkComment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    artwork= models.ForeignKey(Artwork, on_delete=models.CASCADE)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.artwork}"

class TiesLogo(models.Model):
    name = models.CharField(max_length=200, default= "TIEs")
    profile = models.ImageField(upload_to='logo')
    
