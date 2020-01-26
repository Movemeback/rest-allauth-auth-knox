from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url, include

from rest_framework import routers, serializers, viewsets

from authentication_api.api import login_api, signup_api, is_session_active_api, logout_api
from home.views import home_view
from forum_drf.api import AnswerViewSet, QuestionViewSet
from user_drf.api import UserViewSet

from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.urls import urlpatterns as classic_urlpatterns

from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.linkedin_oauth2.views import LinkedInOAuth2Adapter
from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter, OAuth2CallbackView, OAuth2LoginView)

from rest_auth.urls import urlpatterns
from rest_auth.registration.views import (
    SocialLoginView, SocialConnectView, SocialAccountListView,
    SocialAccountDisconnectView
)


# special urls for auth test cases
classic_urlpatterns += [
    url(r'^auth/logout/custom_query/$', views.logout, dict(redirect_field_name='follow')),
    url(r'^auth/logout/next_page/$', views.logout, dict(next_page='/somewhere/')),
    url(r'^auth/logout/next_page/named/$', views.logout, dict(next_page='password_reset')),
    url(r'^auth/password_reset_from_email/$', views.password_reset, dict(from_email='staffmember@example.com')),
    url(r'^auth/password_reset/custom_redirect/$', views.password_reset, dict(post_reset_redirect='/custom/')),
    url(r'^auth/password_reset/custom_redirect/named/$', views.password_reset, dict(post_reset_redirect='password_reset')),
    url(r'^auth/password_reset/html_email_template/$', views.password_reset,
        dict(html_email_template_name='registration/html_password_reset_email.html')),
    url(r'^auth/reset/custom/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm,
        dict(post_reset_redirect='/custom/')),
    url(r'^auth/reset/custom/named/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm,
        dict(post_reset_redirect='password_reset')),
    url(r'^auth/password_change/custom/$', views.password_change, dict(post_change_redirect='/custom/')),
    url(r'^auth/password_change/custom/named/$', views.password_change, dict(post_change_redirect='password_reset')),
    url(r'^auth/admin_password_reset/$', views.password_reset, dict(is_admin_site=True)),
    url(r'^auth/login_required/$', login_required(views.password_reset)),
    url(r'^auth/login_required_login_url/$', login_required(views.password_reset, login_url='/somewhere/')),
]

class MovemebackLinkedInOAuth2Adapter(LinkedInOAuth2Adapter):

    def get_callback_url(self, request, app):
        return 'http://localhost:8080/login'


oauth2_login = OAuth2LoginView.adapter_view(MovemebackLinkedInOAuth2Adapter)


class LinkedInLogin(SocialLoginView):
    adapter_class = MovemebackLinkedInOAuth2Adapter
    callback_url = 'http://localhost:8080/login'
    client_class = OAuth2Client


def callback_view(request):
    request.GET.get('code')

    "http://localhost:8080/api/accounts/linkedin_oauth2/login/callback/?code=AQSTFCeROSL3nCF_HfvCmldtz591flJUwPztOlx3dsu3G0wnTr5N9YudmmToXJRry-qLu4VeWxmpWnpWbdnkhdpSY6A_KMDXGcWb-1zbX-xwUaRry8rcX04k3fehycBnktPneq_QnbfIAU0D-Wc5oJ_djRugkPEP-oXDbVt08HT-UsPig8cnpfTwUWZvAQ&state=RMAHF79gVIbx"

urlpatterns += [
    url(r'^api/rest-registration/', include('rest_auth.registration.urls')),
    url(r'^api/test-admin/', include(classic_urlpatterns)),
    url(r'^api/account-email-verification-sent/$', TemplateView.as_view(),
        name='account_email_verification_sent'),
    url(r'^api/account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
        name='account_confirm_email'),
    url(r'^api/social-login/linkedin/get_link/$', csrf_exempt(oauth2_login), name='ln_get_link'),
    url(r'^api/accounts/linkedin_oauth2/login/callback/$', csrf_exempt(callback_view), name='linkedin_oauth2_callback'),

    # url(r'^accounts/', include('allauth.urls')),
    url(r'^api/social-login/linkedin/$', LinkedInLogin.as_view(), name='ln_login'),
    url(r'^api/socialaccounts/$', SocialAccountListView.as_view(), name='social_account_list'),
    url(r'^api/socialaccounts/(?P<pk>\d+)/disconnect/$', SocialAccountDisconnectView.as_view(),

        name='social_account_disconnect'),
    url(r'^api/accounts/', include('allauth.socialaccount.urls')),
# url(r'^api/accounts/', include('allauth.socialaccount.urls'))

]


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'question', QuestionViewSet)
router.register(r'answer', AnswerViewSet)


urlpatterns += [
    url('^$', home_view, name='home'),
    url('^admin/', admin.site.urls),
    url('^api/v1/rest/', include(router.urls)),
    url('^api/v1/auth/session', is_session_active_api, name='auth_session'),
    url('^api/v1/auth/logout', logout_api, name='auth_logout'),
    url('^api/v1/auth/login', login_api, name='auth_login'),
    url('^api/v1/auth/signup', signup_api, name='auth_signup'),
] + static(settings.MEDIA_DEV_URL, document_root=settings.MEDIA_ROOT)


# default_queryset = {'scope': ' '.join(('r_liteprofile', 'r_emailaddress')), 'response_type': 'code'}
# redirect = ''
# authorization_parameters = copy.copy(default_queryset)
# authorization_parameters['redirect_uri'] = redirect
# authorization_parameters['client_id'] = settings.MMB_LINKEDIN_APP_ID
# authorization_parameters['state'] = str(uuid.uuid4()).replace('-', '')[:10]
# authorization_url = '{}?{}'.format('https://api.linkedin.com/oauth/v2/authorization',
#                                    urlencode(authorization_parameters))


{"code": "AQTAfgIqpHpRaTYhTB0eb0bmmXQ4BoTkGRJgQluAJ5AJ50kBiOPFP55ilZL7_gq1vwSTDt--xhhDhWmrkNoeaHRd9sIAvY0n5Tgk8DhcElx9qy3TtztDDqxoWofAG40Wi6EU8DwerP7AeWar_fYWxdbtHjvg_VHZA1Y_KnlSNVOk6MnODL2tuJoI24B-lw", "state": "d2m2iOx3iB71"}
{"code": "AQThMX20Xc7r7LFVXin4p5SYdoFvMtPp-wK48qS4EAY71veD5lMuvhIQdZHzrIc3UioXblubrZ92jyS0ZeOiSpfGh4esiYtnnCBEgf6zc3ZRjmOksZwUMoIHjHCwBWQXV3bONQXctyetBBern1Wrd55NFs-L5yzeeFx-N26sLRxw57Mj4Apl7ZTjavZH5Q', 'state': 'TCDbLZLMMNE5"}