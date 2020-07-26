from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from src import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('userRegistration', views.userRegistration, name='userRegistration'),
    path('login/', views.Login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('costSheet/', views.sheetFirst, name='costSheet'),
    path('viewCostSheet', views.getData, name='viewCostSheet'),
    path('finalCostSheet/<int:cid>', views.finalSheet, name='finalCostSheet'),
    path('pageNotFound', views.PageNotFound.as_view(), name="pageNotFound")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

