from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from account import views

urlpatterns = [
    path('', views.index, name="index"),

    path('psychomepage/', views.psychomepage, name='psychomepage'),
    path('homepage/', views.homepage, name='homepage'),


    path('loginpediatrician/', views.loginpediatrician, name='loginpediatrician'),
    path('pedhomepage/', views.pedhomepage, name='pedhomepage'),
    path('signup/', views.signup, name='signup'),
    path('Parenthomepage/', views.parenthomepage, name='Parenthomepage'),
    path('loginParent/', views.loginParent, name='loginParent'),
    path('signupys/', views.signupys, name='signupys'),
    path('signuped/', views.signuped, name='signuped'),
    path('parhomepage/', views.parhomepage, name='parhomepage'),
    path('homepageforpys/', views.homepageforpys, name='homepageforpys'),
    path('schedulepys/', views.schedulepys, name='schedulepys'),
    path('Workshopys/', views.Workshopys, name='Workshopys'),
    path('addworkshopform/', views.addworkshopform, name='addworkshopform'),
    path('add_workshop/', views.add_workshop, name='add_workshop'),
    path('successpage/', views.successpage, name='successpage'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('parentprofile/', views.parentprofile, name='parentprofile'),
    path('homepageforparents/', views.homepageforparents, name='homepageforparents'),
    path('logout/', views.logout_view, name='logout'),
    path('contact_pys/', views.contact_pys, name='contact_pys'),
    path('contact_doctor', views.contact_doctor, name='contact_doctor'),
    path('articls/', views.articls, name='articls'),
    path('chatpys/', views.chatpys, name='chatpys'),
    path('meeting/', views.meeting, name='meeting'),
    path('feedback/', views.feedback, name='feedback'),
    path('submit_profile/', views.submit_profile, name='submit_profile'),
    path('profile_detail/', views.profile_detail, name='profile_detail'),
    path('feedback/', views.feedback_submit, name='feedback_submit'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('parent-comments/', views.parent_comment, name='parent_comments'),
    path('submit_comment/', views.submit_comment, name='submit_comment'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('comment_success/', views.comment_success, name='comment_success'),
    path('homepagefordoctors/', views.homepagefordoctors, name='homepagefordoctors'),
    path('add_data/', views.add_data, name='add_data'),
    path('view_data/', views.view_data, name='view_data'),
    path('loginpediatrician/', views.loginpediatrician, name='loginpediatrician'),
    path('loginpsychologist/', views.loginpsychologist, name='loginpsychologist'),









]