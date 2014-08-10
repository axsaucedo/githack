import tempfile,os
from django.db import models
from django.contrib.auth.models import User
from githack.tools.toolbox import path_and_rename, calculate_experience, experience_required, check_badges

class GitScore(models.Model):
    user = models.OneToOneField(User, unique=True)

    level = models.IntegerField(default=1)
    experience = models.BigIntegerField(default=0)

    totalloc = models.IntegerField(default=0)
    totaltime = models.IntegerField(default=0)
    totalcommits = models.IntegerField(default=0)

    badges = models.ManyToManyField('Badges')

    def __str__(self):
        return self.user.username


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
        self.textimage = os.popen("jp2a --colors --height=15 %s" % (tf.name+".jpg")).read()
        super(Badges,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

class Commit(models.Model):
    user = models.ForeignKey(User)

    datetime = models.DateTimeField(auto_now_add=True)
    timelength = models.DecimalField(decimal_places=2, max_digits=20)
    linesadded = models.IntegerField()
    linesremoved = models.IntegerField()
    viminputsessions = models.IntegerField(default=1)

    def check_for_badges(self):
        badges = check_badges(self.user)
        if badges:
            print "WEREOUT"
            print badges
            for badge in badges:
                self.user.gitscore.badges.add(badge)
            self.user.save()

        return badges

    def check_for_level(self):
        levelup=False

        score = self.user.gitscore

        score.experience = score.experience + calculate_experience(self.user.gitscore.level, self.linesadded, self.linesremoved, self.timelength, self.viminputsessions)
        score.totalloc = score.totalloc + self.linesadded + self.linesremoved
        score.totalcommits = score.totalcommits + 1
        score.totaltime =  self.user.gitscore.totaltime + self.timelength

        if score.experience > experience_required(score.level):
            levelup=True
            score.level = score.level + 1
            score.experience =  score.experience % experience_required(score.level)

        score.save()
        self.user.save()

        print score
        print calculate_experience(self.user.gitscore.level, self.linesadded, self.linesremoved, self.timelength, self.viminputsessions)

        return {"level":score.level, "progress":score.experience, "totalexp": experience_required(score.level), "levelup":levelup }
