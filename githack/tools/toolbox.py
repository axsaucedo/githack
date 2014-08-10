import os
from uuid import uuid4
from django.utils.text import slugify

import threading

# Send emails asynchronously
class EmailThread(threading.Thread):
    def __init__(self, msg):
        self.msg = msg
        threading.Thread.__init__(self)

    def run (self):
        self.msg.send(fail_silently=True)

def send_async_mail(msg, *args, **kwargs):
    EmailThread(msg).start()


def path_and_rename(path, type):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        rstring = uuid4().get_hex()
        fname = slugify(unicode(rstring) + u'_' + type) + "." + ext

        return os.path.join(path, fname)
    return wrapper

# Experience is based on what is expected for users to achieve in 1 year.
# With these formulas, a programmer would be expected to:
#       >  14,160 minute
#       >  106,200 LOC
#
# With this said, this is based in the following calculation
#    time = 5*level*1.6
#    loc = 30*level*2
#
# The experience required itself will be:
#   experience =

def experience_required(level):
    return int(60*1.2**level)

#def time_loc_required(level):
#    time = 4*level
#    loc = 30*level


def calculate_experience(level, linesadded, linesremoved, time, inputsessions):
#    return int(min(linesadded+linesremoved, time*7.5)*1.2**(level-1))
    return int((linesadded+linesremoved)*1.2**(level-1))


def check_badges(user):

    from githack.models import Badges

    all_badges = []

    def badges_1():
        try:
            closest_badge = Badges.objects.filter(type=1, value__lt=user.gitscore.level).order_by('-value')
            print user.gitscore.level
            print closest_badge
            all_badges.extend(closest_badge)
        except:
            pass

    def badges_2():
        try:
            closest_badge = Badges.objects.filter(type=2, value__lt=user.gitscore.totalloc).order_by('-value')
            all_badges.extend(closest_badge)
        except:
            pass

    def badges_3():
        try:
            closest_badge = Badges.objects.filter(type=3, value__lt=user.gitscore.totaltime).order_by('-value')
            all_badges.extend(closest_badge)
        except:
            pass

    def badges_4():
        try:
            closest_badge = Badges.objects.filter(type=4, value__lt=user.gitscore.totalcommits).order_by('-value')
            all_badges.extend(closest_badge)
        except:
            pass

    badges_1()
    badges_2()
    badges_3()
    badges_4()

    names_to_exclude = [o.name for o in user.gitscore.badges.all() ]
    final_badges = Badges.objects.exclude(name__in=names_to_exclude)

    print "WEREIN"
    print all_badges
    print final_badges

    return final_badges



