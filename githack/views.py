from django.http import HttpResponse
from django.contrib.auth.models import User
import json

from githack.models import Commit, Badges
import os

def usercommit(request):

    data = json.loads(request.body)
   
    user = User.objects.all()[0]

    obj = Commit()
    obj.timelength =  data['inputtime']
    obj.linesremoved = data['linesremoved']
    obj.linesadded = data['linesadded']
    obj.viminputsessions = data['inputsessions']
    obj.user =user
    obj.save()

    new_levels = obj.check_for_level()
    new_badges = obj.check_for_badges()
#    new_levels = {"level":2, "progress":100, "totalexp": 300, "levelup":True }
#    new_badges = Badges.objects.all()[1:3]

    os.environ['PATH'] += os.pathsep + '/usr/local/bin/'

    if new_levels['levelup']:
        text = os.popen('toilet --metal NEW LEVEL %i' % new_levels['level']).read()
        text = text + "\n" + os.popen('toilet --metal Exp. %i / %i' % (new_levels['progress'], new_levels['totalexp'])).read()
    else:
        text = "level %i, progress %i / %i" % (new_levels['level'], new_levels['progress'], new_levels['totalexp'])
    for badge in new_badges:
        text = text + "\n" + badge.textimage + "\n you acquired '%s' badge!\n" % badge.name
    response = {
        "text" : text,
    }

    return HttpResponse(json.dumps(response), content_type="application/json")
