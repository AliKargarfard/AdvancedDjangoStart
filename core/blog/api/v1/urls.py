from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

router = DefaultRouter()
router.register('post',views.PostModelViewSet,basename='post')
router.register('category',views.CategoryModelViewSet,basename='category')
urlpatterns = router.urls



# urlpatterns = [
#     # path('posts/',views.postList,name='post_list'),
#     # path('posts/',views.PostList.as_view(),name='post_list'),
#     path('posts/',views.PostViewSet.as_view({'get':'list','post':'create'}),name='post_list'),
#     # path('posts/<int:id>/',views.postDetails,name='post_details'),
#     # path('posts/<int:id>/',views.PostDetails.as_view(),name='post_details'),
#     path('posts/<int:pk>/',views.PostViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='post_details'),
# ]