"""givers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = "Givers"
admin.site.site_title = "Givers"
admin.site.index_title = "Welcome to Givers"

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('', include("customuser.urls")),
    path('', include("events.urls")),
    path('', include("authentication.urls")),
    path('', include("volunteer.urls")),
    path('', include("organization.urls")),
    path('', include("validators.urls")),
    path('', include("category.urls")),
    path('', include("miscellaneous.urls")),
    path('', include("verify.urls")),
    path('', include("invitation.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
