from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePortal.as_view(), name='main'),
    path('about/', about, name='about'),
    path('category/<int:category_id>/', PortalByCategory.as_view(), name='category'),
    path('portal/<int:pk>/', ViewPost.as_view(), name='view_post'),
    path('portal/add-post/', CreatePost.as_view(), name='add_post'),
]
