from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', include('todo.urls')),
    path('mood/', include('diary_mood.urls')),
]
