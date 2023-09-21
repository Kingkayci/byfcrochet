from django.urls import path
from django.contrib.auth import views as auth_views

from basic_app import views

app_name = "basic_app"   


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path("register/", views.signup_request, name="signup"),
    path("login/", views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('daily/', views.DailyPage.as_view(), name='daily'),
    path('beginners/', views.BeginnersPage.as_view(), name='beginners'),
    path('advanced/', views.AdvancedPage.as_view(), name='advanced'),
    path('professional/', views.ProfessionalPage.as_view(), name='professional'),
    path('glossary/', views.GlossaryPage.as_view(), name='glossary'),
    path('faq/', views.FaqPage.as_view(), name='faq'), 
    path('ebook/', views.EbookPage.as_view(), name='ebook'),
    path('collections/', views.CollectionsPage.as_view(), name='collections'),
    path('terms-conditions/', views.ConditionsPage.as_view(), name="conditions"),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('privacy-policy/', views.PrivacyPolicyPage.as_view(), name='privacy'),

    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name = 'password_reset.html'), 
         name='reset_password'),
    path('accounts/password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_sent.html'), 
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(), 
         name='password_reset_confirm'),
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'), 
         name='password_reset_complete'),
]