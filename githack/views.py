from django.http import HttpResponse
from django.contrib.auth.models import User
import json

from githack.models import Commit, Badges
from django.contrib.auth import authenticate

import os

def usercommit(request):

#    This is required to use the libraries like toilet, etc
    os.environ['PATH'] += os.pathsep + '/usr/local/bin/'

    data = json.loads(request.body)

    username = data['user']
    password = data['password']

    user = authenticate(username=username, password=password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            obj = Commit()
            obj.timelength =  data['inputtime']
            obj.linesremoved = data['linesremoved']
            obj.linesadded = data['linesadded']
            obj.viminputsessions = data['inputsessions']
            obj.user =user
            obj.save()

            new_levels = obj.check_for_level()
            new_badges = obj.check_for_badges()


            text = ""
            for badge in new_badges:
                text = text + "\n" + badge.textimage + "\n Congratulations!! You've acquired '%s'!!\n" % badge.name

            if new_levels['levelup']:
                text = text + os.popen('toilet --gay LEVEL UP!').read()

            text = text + os.popen('echo " \x1b[42;30mLevel: %i, Exp: %i / %i\033[0m"\n' % (new_levels['level'], new_levels['progress'], new_levels['totalexp'])).read()

            response = {
                "text" : text,
            }
        else:
            response = { "text" : "\x1b[42;30mYour account has been suspended - please contact the team for any questions.\033[0m", }
    else:
        response = { "text" : "\x1b[42;30mThe username and password provided did not match any user in our system. GitHub will still work as expected ;)\033[0m", }

    return HttpResponse(json.dumps(response), content_type="application/json")
