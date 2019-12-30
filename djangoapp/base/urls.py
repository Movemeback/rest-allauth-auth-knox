from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include

from rest_framework import routers, serializers, viewsets

from authentication_api.api import login_api, signup_api, is_session_active_api, logout_api
from home.views import home_view
from forum_drf.api import AnswerViewSet, QuestionViewSet
from user_drf.api import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'answer', AnswerViewSet)


urlpatterns = [
    url('^$', home_view, name='home'),
    url('^admin/', admin.site.urls),

    url('^api/v1/rest/', include(router.urls)),
    url('^api/v1/auth/session', is_session_active_api, name='auth_session'),
    url('^api/v1/auth/logout', logout_api, name='auth_logout'),
    url('^api/v1/auth/login', login_api, name='auth_login'),
    url('^api/v1/auth/signup', signup_api, name='auth_signup'),
] + static(settings.MEDIA_DEV_URL, document_root=settings.MEDIA_ROOT)


