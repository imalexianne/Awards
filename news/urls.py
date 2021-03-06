from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
     url('^$',views.welcome,name = 'welcome'),
     url(r'^profile/', views.profile, name='profile'),
     url(r'^myProfile/(\d+)', views.myProfile, name='myProfile'),
     # url(r'^comments/', views.comments, name='comments'),
     url(r'^project$',views.project,name ='project'),
     url(r'^projects/(\d+)',views.projects,name ='projects'),
     # url(r'^api/project/$', views.ProjectList.as_view())
     # url(r'^ajax/newsletter/$', views.newsletter, name='newsletter')


    #  url(r'^$',views.all_image,name='all_Images'), 
     url(r'^searchs/', views.search_result, name='search_result'),
     url(r'^search/', views.search_results, name='search_results'),
     url(r'^api/project/$', views.ProjectList.as_view()),
     url(r'api/project/project-id/(?P<pk>[0-9]+)/$',
        views.ProjectDescription.as_view()),
     
     url(r'^api/profile/$', views.ProfileList.as_view()),
     url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',
        views.ProfileDescription.as_view())
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)