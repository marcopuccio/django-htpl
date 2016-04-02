"""
DJANGO HTPL APP URL CONFs
"""

from django.conf.urls import url

from .views import IndexTemplateView, GenericTemplateNameView

app_name = 'htpl'
urlpatterns = [
    url(r'^$', IndexTemplateView.as_view(), name='index'),
    url(r'^(?P<tpl_name>[\w\-\_]+)/$', GenericTemplateNameView.as_view(), name="no_index_template"),
]
