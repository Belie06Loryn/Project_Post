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
    url(r'^ProjectVote/(?P<pk>\d+)$',views.ProjectVote,name="ProjectVote"),
    url(r'^Vote/$',views.Vote,name="Vote"),
    url(r'^search/$',views.search_results,name="search_results"), 
    url(r'^api/$',views.api,name="api"),
    url(r'^api/profi/$', views.Profiles.as_view()),
    url(r'^api/foto/$', views.Fotos.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)