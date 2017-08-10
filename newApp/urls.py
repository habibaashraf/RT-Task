from django.conf.urls import url
from django.contrib import admin
from . import views

app_name='newApp'

urlpatterns= [
    url('^admin/',admin.site.urls),
    url(r'form/$',views.addData.as_view(),name='add_data'),
    url(r'^$',views.index,name='index'),
    url(r'p/(?P<id>\d+)', views.saved,name='saved'),
]
