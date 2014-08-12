from django.contrib.admin import site, ModelAdmin
from githack.models import GitScore, Commit, Badges, Subdomain
from accounts.models import UserProfile

class GitScoreAdmin(ModelAdmin):
    list_display = ['user', 'level', 'experience', 'badges_str']


site.register(GitScore, GitScoreAdmin)
site.register(Commit)
site.register(Subdomain)
site.register(Badges)

site.register(UserProfile)