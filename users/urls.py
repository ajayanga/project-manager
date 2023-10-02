from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path("register/", views.registration, name='register'),
    path("login", views.UserLoginView.as_view(), name='login'),
    path("logout", views.user_logout, name='logout'),
    path("update-profile", views.update_profile, name='update_profile'),

    path("password_reset", auth_views.PasswordResetView.as_view(template_name='users/password-reset.html'), name='password_reset'),
    path("password_rest/done", auth_views.PasswordResetDoneView.as_view(template_name='users/password-reset-done.html'), name='password_reset_done'),
    path("reset/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(template_name='users/password-reset-confirm.html'), name='password_reset_confirm'),
    path("password_reset_complete", auth_views.PasswordResetCompleteView.as_view(template_name="users/password-reset-complete.html"), name='password_reset_complete')
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)