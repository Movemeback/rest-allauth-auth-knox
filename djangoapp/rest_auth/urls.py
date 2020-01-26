from django.conf.urls import url

from rest_auth.views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)

urlpatterns = [
    # URLs that do not require a session or valid token
    url(r'^api/password/reset/$', PasswordResetView.as_view(),
        name='rest_password_reset'),
    url(r'^api/password/reset/confirm/$', PasswordResetConfirmView.as_view(),
        name='rest_password_reset_confirm'),
    url(r'^api/login/$', LoginView.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    url(r'^api/logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^api/user/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^api/password/change/$', PasswordChangeView.as_view(),
        name='rest_password_change'),
]
