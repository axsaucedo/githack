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
    return int(min(linesadded+linesremoved, time*7.5)*1.2**(level-1))