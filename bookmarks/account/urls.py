from django.urls import path,include
from . import views


urlpatterns =[
    # path('login/',auth_views.LoginView.as_view(),name='login'),
    # path('logout/',auth_views.LogoutView.as_view(template_name="registration/logout.html"),name='logout'),
    path('',views.dashboard,name='dashboard'),
    # path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    # path('password_change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password-reset/',
    #       auth_views.PasswordResetView.as_view(),
    #       name='password_reset'),
    # path('password-reset/done/',
    #       auth_views.PasswordResetDoneView.as_view(),
    #       name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/',
    #       auth_views.PasswordResetConfirmView.as_view(),
    #       name='password_reset_confirm'),
    # path('password-reset/complete/',
    #       auth_views.PasswordResetCompleteView.as_view(),
    #       name='password_reset_complete'),
    path('',include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/',views.edit,name="edit")
    ]



