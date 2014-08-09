from django.http import HttpResponse
from django.contrib.auth.models import User
import json
import os

def usercommit(request):

    post = request.POST

    print json.loads(request.body)
#    print post

    response = {}

    user = User.objects.get(username="axsauze")

    os.environ['PATH'] += os.pathsep + '/usr/local/bin/'
    f=os.popen('toilet --gay Level UP!!').read()
    print f

    response = { "text" : f }

    return HttpResponse(json.dumps(response), content_type="application/json")