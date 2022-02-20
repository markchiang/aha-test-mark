from django.urls import include, path
from rest_framework import routers
from account import views
from django.contrib import admin
from django.conf.urls import url
from django.views.generic import TemplateView
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('social/',include('social.apps.django_app.urls', namespace='social')),
    path('hello/', TemplateView.as_view(template_name='index.html')),
#    url('', include('social_django.urls', namespace='social')),
]
