from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login_page,name='login'),
    path('logout',views.logoutuser,name='logout'),
    path('payment',views.payment,name='payment'),
    path('policy',views.policy,name='policy'),
    path('pricing',views.pricing,name='pricing'),
    path('registration1',views.registration1,name='registration1'),
    path('registration2/<int:pk>/',views.registration2,name='registration2'),
    path('submitted/form',views.submitted_form,name='submitted_form'),
    path('signin',views.signin,name='signin'),
    path('stafflogin',views.stafflogin,name='stafflogin'),
    path('staff/page',views.staff_page,name='staff_page'),
    path('tacking/care',views.takeing_care,name='tacking_care'),
    path('elder/care',views.elder_care,name='elder_care'),
    path('pet/care',views.pet_care,name='pet_care'),
    path('everything',views.everythig,name='everything')
    
]