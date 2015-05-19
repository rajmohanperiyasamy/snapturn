from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from views import ProfileImageIndexView
from views import ProfileImageView, ProfileDetailView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'snap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'snap.views.home', name='home'),
    url(r'^about/$', 'snap.views.about', name='videos'),
    url(r'^videos/$', 'snap.views.videos', name='awards'),
    url(r'^contacts/$', 'snap.views.contacts', name='contacts'),
    url(r'^$', ProfileImageIndexView.as_view(), name='home'),

    url(r'^upload/', ProfileImageView.as_view(), name='profile_image_upload'),
    url(r'^uploaded/(?P<pk>\d+)/$', ProfileDetailView.as_view(),name='profile_image'),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
