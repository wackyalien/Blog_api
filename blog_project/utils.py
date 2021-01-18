import logging
import re
import pytz
import datetime
import random
import string

# DJANGO
from django.http import Http404
from django.core.mail import EmailMessage
# PROJECT
from blog_project import constants
import json

logger = logging.getLogger('application')

def print_request_body(api_name, request):
    request_unicode = request.body.decode('utf-8')
    request_body = json.loads(request_unicode)
   

def get_value_or_404(dict_, key):
    try:
        return dict_[key]
    except Exception as e:
        logger.error('get_value_or_404: ' + str(e))
        raise Http404('Parameter missing: ' + str(e))


def get_value_or_default(dict_, key, default=None):
    try:
        ret = dict_[key]
    except:
        ret = default
    return ret


def log_error(text):
    logger.error(text)


# def get_error_text(code):
#     if code:
#         return constants.ERROR_CONFIG[code][0]


def raise_error(code=None, text=None):
    if code:
        error_text = constants.ERROR_CONFIG[code][0]
        logger.error(error_text)
        raise ValueError(error_text)
    elif text:
        logger.error(text)
        raise ValueError(text)


def create_response_obj(status, message=None, code=None, data=None):
    if status == 'success':
        val = 1
        success = True
        code = '201'
    elif status == 'error':
        val = 0
        success = False
    resp = {'value': val, 'success': success, 'status': status,
            'message': message, 'code': code, 'data': data}
    return resp


def success_resp(data, message=None):
    return create_response_obj(status='success', message=message, data=data)


def error_resp(message, data=None):
    return create_response_obj(status='error', message=message, data=data)


def create_error_object(message, code=None):
    errors = []
    error = {'status': None, 'code': code, 'message': None, 'extra_data': None}
    error['message'] = message
    errors.append(error)
    return errors


def python_btoa(string):
    import base64
    string_byte = string.encode("utf-8")
    encoded_byte = base64.b64encode(string_byte)
    encoded_string = encoded_byte.decode("utf-8")
    return encoded_string


def validate_email(email):
    if email is None:
        return False
    if re.search(r'[\s]', email):
        return False
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True

def random_with_N_digits(n):
    from random import randint
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def to_bool(val):
    if val is None:
        return None
    elif val is True or val is False:
        return val
    elif val.lower() == 'true':
        return True
    elif val.lower() == 'false':
        return False
    else:
        return None


def get_datetime(date):
    import datetime
    arr = date.split('-')
    return datetime.datetime(year=int(arr[0]), month=int(arr[1]), day=int(arr[2]))


def get_datetime_str(date):
    # return '{}-{}-{}'.format(date.year, f"{date:%m}", f"{date:%d}")
    return '{}-{}-{}'.format(date.year, date.month, date.day)


def create_datetime(year, month, day, timezone=None):
    if timezone:
        tz = pytz.timezone(timezone)
    else:
        tz = pytz.utc

    date_time = tz.localize(datetime.datetime(year, month, day))
    return date_time


def create_datetime_from_iso(datetime_str, timezone=None):
    if datetime_str is None or datetime_str is '':
        return None
    if timezone:
        tz = pytz.timezone(timezone)
    else:
        tz = pytz.utc

    date_time = tz.localize(datetime.datetime.strptime(
        datetime_str, '%Y-%m-%dT%H:%M:%S.%fZ'), is_dst=None)
    return date_time

def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def current_datetime(timezone=None):
    if timezone:
        tz = pytz.timezone(timezone)
    else:
        tz = pytz.utc

    date_time = datetime.datetime.now(tz)
    return date_time

def send_mail(sender_email, receiver_email, subject, message, attachment):
    
    if sender_email == None:
        sender_email = 'crenexa.outbox@gmail.com'
    
   
    mail = EmailMessage(subject, message, sender_email, [receiver_email])
    
    if attachment != None:
        mail.attach(attachment.name, attachment.read(), attachment.content_type)

    mail.send()