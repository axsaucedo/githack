from django.http import HttpResponse
from django.contrib.auth.models import User
import json
from django.contrib.auth.models import User

from githack.models import Commit
import os

def usercommit(request):

    post = request.POST

    data = json.loads(request.body)
   
    user = User.objects.all()[0]

    Commit.objects.all().delete()
    obj = Commit()
    obj.timelength =  data['inputtime']
    obj.linesremoved = data['linesremoved']
    obj.linesadded = data['linesadded']
    obj.viminputsessions = data['inputsessions']
    obj.user =user
    obj.save()
    new_levels = obj.check_for_level()
    new_badges = obj.check_for_badges()

    os.environ['PATH'] += os.pathsep + '/usr/local/bin/'

    if new_levels['its_new']=='yes':
        text = os.popen('toilet --metal NEW LEVEL %i' % new_levels['level']).read()
    else:
        text = "level %i, progress %i" % (new_levels['level'], new_levels['progress'])
    for badge in new_badges:
        text = text + "\n" + os.popen('toilet --gay NEW BADGE: %s' % badge['name']).read()
    response = {
        "text" : text,
    }

    return HttpResponse(json.dumps(response), content_type="application/json")
