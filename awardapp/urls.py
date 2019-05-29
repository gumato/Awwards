from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^search/', views.search, name='search_project'),
    url(r'signup/', views.Signup, name="signup"),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^review/(?P<pk>\d+)',views.add_review,name='review'),
    url(r'^ajax/project/$',views.ProjectList.as_view()),
    url(r'^api/profile/$', views.ProfileList.as_view()),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)