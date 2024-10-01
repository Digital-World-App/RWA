from django.urls import path
from dashboard import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Dashboard
    path('', views.analytics, name="index"),    
    path('sales/', views.sales, name="sales"),    
    path('smart-home/', views.smart_home, name="smart_home"),
    
    # Applications
    path('applications/test/', views.test, name="test"), 
    
    # Blockchain
    path('blockchain/nft/', views.nft, name="nft"),
    path('blockchain/registration/', views.registration, name="registration"),
    path('blockchain/registration/localizacao_geografica_form', views.localizacao_geografica_form, name="localizacao_geografica_form"),
    path('blockchain/registration/prefeitura_form', views.prefeitura_form, name="prefeitura_form"),
    path('blockchain/registration/oficio_notarial_form', views.oficio_notarial_form, name="oficio_notarial_form"),
    path('blockchain/registration/topografo_form', views.topografo_form, name="topografo_form"),
    path('blockchain/registration/engenheiro_form', views.engenheiro_form, name="engenheiro_form"),
    path('blockchain/registration/advogado_form', views.advogado_form, name="advogado_form"),
    path('blockchain/registration/fotos_do_imovel_form', views.fotos_do_imovel_form, name="fotos_do_imovel_form"),
    path('blockchain/registration/plano_arquitetonico_form', views.plano_arquitetonico_form, name="plano_arquitetonico_form"),
    path('blockchain/registration/topografia_form', views.topografia_form, name="topografia_form"),
    path('blockchain/registration/plano_de_zoneamento_form', views.plano_de_zoneamento_form, name="plano_de_zoneamento_form"),
    path('blockchain/registration/generate_document', views.generate_document, name="generate_document"),
    path('blockchain/defi/', views.defi, name="defi"),
    path('blockchain/token/', views.token, name="token"),
    path('blockchain/storage/', views.storage, name="storage"),
    path('blockchain/marketplace/', views.marketplace, name="marketplace"),
    path('blockchain/emporium/', views.emporium, name="emporium"), 


    # Authentication -> Login
    path('accounts/basic-login/', views.BasicLoginView.as_view(), name="basic_login"),
    
    # Authentication -> Register
    path('accounts/basic-register/', views.basic_register, name="basic_register"),
    
    # Authentication -> Reset
    path('accounts/basic-reset/', views.BasicPasswordResetView.as_view(), name="basic_reset"),
    
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
    
    # Authentication -> Lock
    path('accounts/basic-lock/', views.basic_lock, name="basic_lock"),
    
    # Error
    path('error/404/', views.error_404, name="error_404"),
    path('error/500/', views.error_500, name="error_500"),

    # Logout
    path('accounts/logout/', views.logout_view, name='logout'),
]

