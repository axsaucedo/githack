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

