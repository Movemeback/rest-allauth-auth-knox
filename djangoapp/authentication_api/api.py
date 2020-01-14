import logging
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotAllowed

logger = logging.getLogger('django')


@csrf_exempt
def is_session_active_api(request):
    """
    API endpoint that tells if user has active session.
    """
    user_id = request.user.id if request.user.is_authenticated else None
    return HttpResponse(json.dumps({'success': request.user.is_authenticated,
                                    'user_id': user_id}),
                        content_type='application/json')


@csrf_exempt
def logout_api(request):
    """
    Ends current session.
    """
    logout(request)
    return HttpResponse(json.dumps({'success': True}),
                        content_type='application/json')


@csrf_exempt
def login_api(request):
    """
    Shows login page and logs user.
    """
    logging.info('here')
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(request,
                            username=data.get('username'),
                            password=data.get('password'))
        if user is not None:
            login(request, user)
            logger.info('Audit: Login successful {}'.format(data))
            return HttpResponse(json.dumps({'success': True}),
                                content_type='application/json')
        else:
            logger.info('Audit: Login unsuccessful {}'.format(data))
            return HttpResponse(json.dumps({'success': False}),
                                content_type='application/json')

    return HttpResponseNotAllowed()


@csrf_exempt
def login_api(request):
    """
    Shows login page and logs user.
    """
    logging.info('here')
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(request,
                            username=data.get('username'),
                            password=data.get('password'))
        if user is not None:
            login(request, user)
            logger.info('Audit: Login successful {}'.format(data))
            return HttpResponse(json.dumps({'success': True}),
                                content_type='application/json')
        else:
            logger.info('Audit: Login unsuccessful {}'.format(data))
            return HttpResponse(json.dumps({'success': False}),
                                content_type='application/json')

    return HttpResponseNotAllowed()


@csrf_exempt
def signup_api(request):
    """
    Shows signup page and signups users.
    """

    if request.method == 'POST':
        data = json.loads(request.body)
        User.objects.create_superuser(
            email='',
            username=data.get('username'),
            password=data.get('password'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'))
        user = authenticate(request,
                            username=data.get('username'),
                            password=data.get('password'))
        login(request, user)
        logging.info('Audit: Signup successful {}'.format(data))
        return HttpResponse(json.dumps({'success': True}),
                            content_type='application/json')

    return HttpResponseNotAllowed()
