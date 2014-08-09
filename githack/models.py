import tempfile,os
from django.db import models
from django.contrib.auth.models import User
from githack.tools.toolbox import path_and_rename, calculate_experience, experience_required

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
    textimage = models.TextField(null=True)

    def get_photo(self): return self.image.url if self.image else '/media/profiles/badgeplaceholder.jpg'
    def image_tag(self): return u'<img src="%s" />' % self.get_photo()
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def save(self, *args, **kwargs):
        imgf = tempfile.NamedTemporaryFile()
        imgf.write(self.image.read())
        imgf.flush()
        tf = tempfile.NamedTemporaryFile()
        os.popen("convert %s %s" % (imgf.name,tf.name+".jpg"))
        self.textimage = os.popen("jp2a --colors --height=30 %s" % (tf.name+".jpg")).read()
        super(Badges,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

class Commit(models.Model):
    user = models.OneToOneField(User, unique=True, null=True)

    datetime = models.DateTimeField(auto_now_add=True)
    timelength = models.DecimalField(decimal_places=2, max_digits=20)
    linesadded = models.IntegerField()
    linesremoved = models.IntegerField()
    viminputsessions = models.IntegerField(default=1)

    def check_for_badges(self):
        if self.linesadded==1 and self.linesremoved==1:
            return [{"name":"sniper fix"}]
        return []

    def check_for_level(self):
        self.user.gitscore.experience += calculate_experience(self.linesadded, self.linesremoved, self.time, self.viminputsessions)
        return {"level":1, "progress":33, "its_new":random.choice(["no","yes"])}
