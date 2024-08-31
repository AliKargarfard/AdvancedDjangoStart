from django.urls import path, include
from . import views
from django.views.generic import TemplateView

app_name = "blog"
urlpatterns = [
    # path('fbv',views.indexView, name='fbv-blog'),
    # path('goto-asriran',views.redirectToAsriran, name='goto-asriran'),
    # path('cbv',TemplateView.as_view(template_name='index.html',extra_context={"name":"Ali"} )),
    path("cbv", views.IndexView.as_view(), name="cbv-index"),
    path("posts/", views.PostListView.as_view(), name="list-of-posts"),
    path(
        "posts/<int:pk>",
        views.PostDetailView.as_view(),
        name="detail-of-post",
    ),
    path("posts/create/", views.PostCreateView.as_view(), name="create-post"),
    path(
        "posts/<int:pk>/edit", views.PostEditView.as_view(), name="edit-post"
    ),
    path(
        "posts/<int:pk>/delete",
        views.PostDeleteView.as_view(),
        name="delete-post",
    ),
    path(
        "goto-asriran/<int:pk>",
        views.RedirectToAsriran.as_view(),
        name="redirect-to-asriran",
    ),
    path("api/v1/", include("blog.api.v1.urls")),
]
