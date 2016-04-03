from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'intern.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'intern_1.views.home'),
    url(r'^intern_detail/$', 'intern_1.views.InternDetail'),
    url(r'^single_detail/(?P<intern_id>[\w-]+)/$', 'intern_1.views.SingleDetail',name="single_detail"),
    url(r'^search/$', 'intern_1.views.search'),
    url(r'^login/$', 'intern_1.views.Login'),
     url(r'^register/$', 'intern_1.views.Register'),
    url(r'^intern_form/$', 'intern_1.views.InternForm'), 
    url(r'^logout/$', 'intern_1.views.Logout'),
    url(r'^dashboard/$', 'intern_1.views.dashboard'),
    url(r'^internships/(?P<location>[\w-]+)/$', 'intern_1.views.intern_location',name="intern_location"),
]
