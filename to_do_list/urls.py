from django.conf.urls import url

from to_do_list.views import IndexView, GetDataView, create_new, update, delete

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="main"),
    url(r'^index/$', GetDataView.as_view(), name="index"),
    url(r'^change/(?P<to_do_list_pk>\d+)/$', update, name="update"),
    url(r'^create/$', create_new, name="create"),
    url(r'^delete/(?P<to_do_list_pk>\d+)/$', delete, name="delete"),
]
