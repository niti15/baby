# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

app_patterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'
    ),
    path(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm.as_view()),

    path('', views.RootRouter.as_view(), name='root-router'),
    path('welcome/', views.Welcome.as_view(), name='welcome'),

    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/add/', views.UserAdd.as_view(), name='user-add'),
    path(
        'users/<int:pk>/edit/',
        views.UserUpdate.as_view(),
        name='user-update'
    ),
    path(
        'users/<int:pk>/delete/',
        views.UserDelete.as_view(),
        name='user-delete'
    ),

    path(
        'user/password/',
        views.UserPassword.as_view(),
        name='user-password'
    ),
    path(
        'user/reset-api-key/',
        views.UserResetAPIKey.as_view(),
        name='user-reset-api-key'
    ),
    path(
        'user/settings/',
        views.UserSettings.as_view(),
        name='user-settings'
    ),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls', namespace='api')),
    path('', include((app_patterns, 'babybuddy'), namespace='babybuddy')),
    path('', include('core.urls', namespace='core')),
    path('', include('dashboard.urls', namespace='dashboard')),
    path('', include('reports.urls', namespace='reports')),
]

if settings.DEBUG:  # pragma: no cover
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
