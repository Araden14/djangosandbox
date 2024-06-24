from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns  # Corrected import
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include non-i18n patterns here
]

urlpatterns += i18n_patterns(
    path('main/', include('main.urls')),  # Adjust 'myapp.urls' to your app's name
    # Add more i18n URLs here
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)