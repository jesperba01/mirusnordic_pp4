from django.contrib import admin
from django.urls import path, include
from .views import handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('summernote/', include('django_summernote.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("home.urls"), name="home-urls"),
    path("treatments/", include("treatments.urls")),
    path("register/", include("register.urls")),
    path("dashboard/", include("dashboard.urls")),
]

handler404 = "main.views.handler404"
handler500 = "main.views.handler500"
