from django.contrib.admin import site, ModelAdmin
from githack.models import GitScore, Commit, Badges
from accounts.models import UserProfile


site.register(GitScore)
site.register(Commit)
site.register(Badges)

site.register(UserProfile)