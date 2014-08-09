from django.db import models
from django.contrib.auth.models import User
from githack.tools.toolbox import path_and_rename

class GitScore(models.Model):
    user = models.OneToOneField(User, unique=True)

    level = models.IntegerField(default=1)
    experience = models.BigIntegerField(default=0)

    badges = models.ManyToManyField('Badges')


class Badges(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    type = models.IntegerField()
    value = models.IntegerField()
    image = models.ImageField(upload_to=path_and_rename('badges/', u'profile'), null=True, blank=True)

    def get_photo(self): return self.image.url if self.image else '/media/profiles/badgeplaceholder.jpg'
    def image_tag(self): return u'<img src="%s" />' % self.get_photo()
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name

class Commit(models.Model):
    user = models.OneToOneField(User, unique=True)

    datetime = models.DateTimeField(auto_now_add=True)
    timelength = models.DecimalField(decimal_places=2, max_digits=20)
    linesadded = models.IntegerField()
    linesremoved = models.IntegerField()
    viminputsessions = models.IntegerField(default=1)