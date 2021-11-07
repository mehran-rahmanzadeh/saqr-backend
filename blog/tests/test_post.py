"""
Auto Generated test
Automatically generated with ❤️ by django-sage-painless
"""
from django.apps import apps
from django.urls import reverse
from rest_framework.test import APITestCase
from django_seed import Seed


from blog.models.tag import Tag

from blog.models.category import Category

from blog.models.post import Post


seeder = Seed.seeder()


class PostTest(APITestCase):
    """
    Post Test
    Auto Generated
    """
    def setUp(self) -> None:
        self.models = apps.get_app_config('blog').get_models()
        self.models_name = [model._meta.object_name for model in self.models]
        
        seeder.add_entity(Tag, 3)
        
        seeder.add_entity(Category, 3)
        
        seeder.add_entity(Post, 3)
        
        seeder.execute()  # create instances
    
    def test_post_model(self):
        """test Post creation"""
        seeder.add_entity(Post, 1)
        seeder.execute()  # create instance
        # assertions
        self.assertTrue(Post.objects.exists())
        self.assertIn('Post', self.models_name)
    
    def test_post_list_success(self):
        """test Post list"""
        url = reverse('post-list')
        response = self.client.get(url)
        # assertions
        self.assertEqual(response.status_code, 200)
        if type(response.data) == dict:
            if response.data.get('count'):
                self.assertGreater(response.data['count'], 0)
        else:
            self.assertGreater(len(response.data), 0)

    def test_post_detail_success(self):
        """test Post detail"""
        post = Post.objects.first()
        url = reverse('post-detail', args=[post.pk])
        response = self.client.get(url)
        # assertions
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(response.data.get('kind'), post.kind)
        
        self.assertEqual(response.data.get('title'), post.title)
        
        self.assertEqual(response.data.get('body'), post.body)
        
        self.assertEqual(response.data.get('video'), post.video)
        
        self.assertEqual(response.data.get('tags'), post.tags)
        
        
        
        
        
        
    
    
