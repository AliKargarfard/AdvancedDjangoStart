from django.core.management.base import BaseCommand
from faker import Faker
from datetime import datetime
import random

from accounts.models import User, Profile
from blog.models import Post, Category

Category_names = ['SW','HW','AI','IT','HRM','CRM']

class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        # user = User.objects.create_user(email=self.fake.email(),password="ali@1234")
        # profile = Profile.objects.get(user=user)
        # profile.first_name = self.fake.first_name()
        # profile.last_name = self.fake.last_name()
        # profile.description = self.fake.paragraph(nb_sentences=3)
        # profile.save()

        for category_name in Category_names:
            Category.objects.get_or_create(name=category_name)
            print(category_name)

        # for _ in range(10):
        #     Post.objects.create(
        #         author = user,
        #         title = self.fake.paragraph(nb_sentences=1),
        #         content = self.fake.paragraph(nb_sentences=5),
        #         category = Category.objects.create(name=random.choice(Category_names)),
        #         status = random.choice([True, False]),
        #         published_date = datetime.now(),
        #     )

                