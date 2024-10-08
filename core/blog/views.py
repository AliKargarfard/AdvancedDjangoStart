from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from .models import Post
from django.shortcuts import redirect, get_object_or_404
from django.contrib.admin.widgets import AdminDateWidget

from .forms import PostCreateForm

# Create your views here.

"""
def indexView(request):
    name = 'Reza'
    context = {'name': name}
    return render(request,'index.html', context)

def redirectToAsriran(request):
    return redirect('https://asriran.com/')

"""


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):

        # super() is reference to main class functions as an object
        context = super().get_context_data(**kwargs)

        # add favorites fields to object
        context["name"] = "Ali"
        context["posts"] = Post.objects.all()
        return context


class RedirectToAsriran(RedirectView):
    url = "https://asriran.com"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostListView(ListView):
    # model = Post
    queryset = Post.objects.filter(status=True)

    context_object_name = "posts"
    paginate_by = 4
    ordering = "id"

    # def get_queryset(self):
    #     return Post.objects.filter(status=True)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


# create a form view based on the FormView parent class
"""
class PostCreateView(FormView):    
    template_name = "create.html"
    form_class = PostCreateForm
    success_url = "/blog/posts/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""


# Construction of a create View based on CreateView parent class

# class DateInput(forms.DateInput):
#    input_type = 'date'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name_suffix = "_create_form"
    fields = ("title", "content", "status", "published_date")
    # form_class = PostCreateForm
    success_url = "/blog/posts/"
    # widgets = {'published_date': DateInput()}

    # replace author field with current user name
    def form_valid(self, form):
        print(self.request.user)
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Customize date field with AdminDateWidget
    def get_form(self, form_class=None):
        form = super(PostCreateView, self).get_form(form_class)
        form.fields["published_date"].widget = AdminDateWidget(
            attrs={"type": "date"}
        )
        return form


class PostEditView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    """only users that access to right permission are allowed to edit this post
    format of permissions : 'appname.permission_table'
    """

    permission_required = "blog.edit_post"
    model = Post
    form_class = PostCreateForm
    success_url = "/blog/posts/"
    template_name_suffix = "_create_form"


class PostDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = "blog.delete_post"
    model = Post
    success_url = "/blog/posts/"

class PostListApiView(TemplateView):
    template_name = "blog/post_list_api.html"