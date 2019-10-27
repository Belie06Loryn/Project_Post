from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.page,name = 'page'),
    url(r'^submit/$',views.submit,name = 'submit'),
    url(r'^profile/$',views.profile,name = 'profile'),
    url(r'^profile_display/$', views.profile_display, name='profile_display'),
    url(r'^project/$', views.project, name='project'),
    url(r'^profile_vote/$', views.profile_vote, name='profile_vote'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)