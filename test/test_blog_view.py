from django.test import TestCase,Client
from django.urls import reverse
from datetime import datetime

from accounts.models import User,Profile
from blog.models import Post,Category


class TestBlogView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email="ali@abc.com",password="Ali@1234")
        self.profile = Profile.objects.create(
            user=self.user,
            first_name = "Ali",
            last_name = "K.",
            description = "Ali K. description",
        )
        self.post = Post.objects.create(
            author = self.user,
            title = "test",
            content = "description",
            status = True,
            category = None,
            published_date = datetime.now()
        )

    
    def test_blog_index_url_successful_response(self):
        url = reverse('blog:cbv-index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTrue(str(response.content).find("index"))
        self.assertTemplateUsed(response,template_name = "index.html")

    def test_blog_post_detail_logged_in_response(self):
        login = self.client.force_login(self.user)
        url = reverse('blog:detail-of-post',kwargs={'pk':self.post.id})
        response = self.client.get(url)
        print(response.url, '************', self.user ,'.........',self.post.id, '........', url)
        self.assertEquals(response.status_code, 200)

    def test_blog_post_detail_anonymouse_response(self):
        url = reverse('blog:detail-of-post',kwargs={'pk':self.post.id})
        print(url,'*********************')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)

    
    