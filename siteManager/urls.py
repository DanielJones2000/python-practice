from django.conf.urls import url, include
urlpatterns = [
    url(r'^', include('backstage.urls')),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
