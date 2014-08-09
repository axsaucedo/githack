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
    txt=os.popen('toilet --gay Level UP!!').read()
    #    print f
    #
    #    response = { "text" : f }

    response = {
        "level" : new_levels,
        "newbadges" : new_badges,
        "text" : txt,
    }

    return HttpResponse(json.dumps(response), content_type="application/json")
