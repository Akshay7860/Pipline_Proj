from django.conf.urls import url

from test_app.views import TestView

urlpatterns = [
    url(r'^testapp/$', TestView.as_view(),
        name='testappview'),
]
