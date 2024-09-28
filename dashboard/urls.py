from django.urls import path
from dashboard import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Dashboard
    path('', views.analytics, name="index"),    
    path('sales/', views.sales, name="sales"),    
    path('smart-home/', views.smart_home, name="smart_home"),

    
    # Applications
    path('applications/crm/', views.crm, name="crm"),   
    path('applications/kanban/', views.kanban, name="kanban"),   
    path('applications/wizard/', views.wizard, name="wizard"),   
    path('applications/datatables/', views.datatables, name="datatables"),   
    path('applications/calendar/', views.calendar, name="calendar"),   
    path('applications/stats/', views.stats, name="stats"), 

    
    # Authentication -> Login
    path('accounts/basic-login/', views.BasicLoginView.as_view(), name="basic_login"),
    path('accounts/cover-login/', views.CoverLoginView.as_view(), name="cover_login"),
    path('accounts/illustration-login/', views.IllustrationLoginView.as_view(), name="illustration_login"),

    # Authentication -> Register
    path('accounts/basic-register/', views.basic_register, name="basic_register"),
    path('accounts/cover-register/', views.cover_register, name="cover_register"),
    path('accounts/illustration-register/', views.illustration_register, name="illustration_register"),

    # Authentication -> Reset
    path('accounts/basic-reset/', views.BasicPasswordResetView.as_view(), name="basic_reset"),
    path('accounts/cover-reset/', views.CoverPasswordResetView.as_view(), name="cover_reset"),
    path('accounts/illustration-reset/', views.IllustrationPasswordResetView.as_view(), name="illustration_reset"),

    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/done/change-done.html'
    ), name="password_change_done"),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/done/basic.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/complete/basic.html'
    ), name='password_reset_complete'),

    # Authentication -> Verification
    path('accounts/basic-verification/', views.basic_verification, name="basic_verification"),
    path('accounts/cover-verification/', views.cover_verification, name="cover_verification"),
    path('accounts/illustration-verification/', views.illustration_verification, name="illustration_verification"),

    # Authentication -> Lock
    path('accounts/basic-lock/', views.basic_lock, name="basic_lock"),
    path('accounts/cover-lock/', views.cover_lock, name="cover_lock"),
    path('accounts/illustration-lock/', views.illustration_lock, name="illustration_lock"),

    # Error
    path('error/404/', views.error_404, name="error_404"),
    path('error/500/', views.error_500, name="error_500"),

    # Logout
    path('accounts/logout/', views.logout_view, name='logout'),
]

