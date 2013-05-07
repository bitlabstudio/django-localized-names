"""
This ``urls.py`` is only used when running the tests via ``runtests.py``.
As you know, every app must be hooked into yout main ``urls.py`` so that
you can actually reach the app's views (provided it has any views, of course).

"""
from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin
from django.http import HttpResponse


admin.autodiscover()


urlpatterns = patterns(
    '',
    # TODO will probably be replaced by a dummy template view to live test
    # some examples
    url(r'^', lambda req: HttpResponse('Dummy home'),
        name='dummy_home'),
    url(r'^admin/', include(admin.site.urls)),
)
