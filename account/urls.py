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
    path('feedback/', views.feedback, name='feedback'),

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
    path('feedbackl/', views.feedbackl, name='feedbackl'),
    path('psyinfoboard/', views.psyinfoboard, name='psyinfoboard'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('get_information/', views.get_information, name='get_information'),
    path('parboardpsy/', views.parboardpsy, name='parboardpsy'),
    path('pedinfoboard/', views.pedinfoboard, name='pedinfoboard'),
    path('delete_ped_item/<int:item_id>/', views.delete_ped_item, name='delete_ped_item'),
    path('get_ped_information/', views.get_ped_information, name='get_ped_information'),
    path('parboardped/', views.parboardped, name='parboardped'),
    path('mwped/', views.mwped, name='mwped'),
    path('vmwped/', views.vmwped, name='vmwped'),
    path('pedvmw/', views.pedvmw, name='pedvmw'),
    path('meetped/', views.meetped, name='meetped'),
    path('pedmeetv/',views.pedmeetv, name='pedmeetv'),
    path('vmeetped/', views.vmeetped, name='vmeetped'),
    path('porall/',views.porall, name='porall'),
    #alaa

    path('extrainfopara', views.view_extra_informationpara, name='extrainfopara'),
    path('extrainfopeda', views.view_extra_informationpeda, name='extrainfopeda'),
    path('extrainfopsya', views.view_extra_informationpsya, name='extrainfopsya'),
    path('add_extra_informationa/', views.add_extra_informationpeda, name='add_extra_informationa'),
    path('add_extra_informationa_psy/', views.add_extra_informationpsya, name='add_extra_informationa_psy'),
    path('parhomepage', views.parhomepage, name='parhomepage'),
    path('par.ped.homepage', views.parpedhomepage, name='par.ped.homepage'),
    path('sorall/', views.sorall, name='sorall'),
    path('delete_', views.delete_, name='delete_'),
    path('delete_confirm', views.delete_confirm, name='delete_confirm'),
    path('delete_ped', views.delete_ped, name='delete_ped'),
    path('delete_confirm_ped', views.delete_confirm_ped, name='delete_confirm_ped'),
    path('delete_psy', views.delete_psy, name='delete_psy'),
    path('delete_confirm_psy', views.delete_confirm_psy, name='delete_confirm_psy'),
    path('tracka', views.track, name='tracka'),
    path('track2/<int:pk>', views.track_next, name='track2'),
    path('track_delete/<int:pk>', views.track_delete, name='track_delete'),
    path('track_add', views.track_add, name='track_add'),
    path('track_edit/<int:pk>', views.track_edit, name='track_edit'),

]
