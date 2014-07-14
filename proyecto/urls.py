from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

from django.contrib import admin

from app.views import EnlaceListView, EnlaceDetailView
admin.autodiscover()

from rest_framework import routers
from app.views import EnlaceViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'links',EnlaceViewSet)
router.register(r'user',UserViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.hora_actual', name='hora_actual'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^$','app.views.index',name='index'),
    url(r'^plus/(\d+)$','app.views.plus',name='plus'),
    url(r'^minus/(\d+)$','app.views.minus',name='minus'),
    url(r'^categoria/(\d+)$','app.views.categoria',name='categoria'),
    url(r'^add/$','app.views.add',name='add'),
    url(r'^about/$',TemplateView.as_view(template_name='index.html'),name='about'),
    url(r'^enlaces/$',EnlaceListView.as_view(),name='enlaces'),
    url(r'^enlaces/(?P<pk>[\d]+)$',EnlaceDetailView.as_view(),name='enlace'),
    

    url(r'^admin/', include(admin.site.urls)),
)
