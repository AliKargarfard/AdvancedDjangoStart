from django.test import SimpleTestCase,TestCase
from datetime import datetime

from blog.forms import PostCreateForm
from blog.models import Category


class TestPostForm(TestCase):

    def test_post_form_with_valid_data(self):
        category_obj = Category.objects.create(name='hello')
        form = PostCreateForm(data={
            "title":"test",
            "content":"description",
            "status":True,
            "category":category_obj,
            "published_date":datetime.now()
        })
        self.assertTrue(form.is_valid())

    def test_post_form_with_no_data(self):        
        form = PostCreateForm(data={})
        self.assertFalse(form.is_valid())