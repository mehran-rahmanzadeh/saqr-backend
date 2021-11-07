"""
Auto Generated test
Automatically generated with ❤️ by django-sage-painless
"""
from django.apps import apps
from django.urls import reverse
from rest_framework.test import APITestCase
from django_seed import Seed


from calls.models.getintouch import GetInTouch

from calls.models.certificaterequest import CertificateRequest


seeder = Seed.seeder()


class GetintouchTest(APITestCase):
    """
    GetInTouch Test
    Auto Generated
    """
    def setUp(self) -> None:
        self.models = apps.get_app_config('calls').get_models()
        self.models_name = [model._meta.object_name for model in self.models]
        
        seeder.add_entity(GetInTouch, 3)
        
        seeder.add_entity(CertificateRequest, 3)
        
        seeder.execute()  # create instances
    
    def test_getintouch_model(self):
        """test GetInTouch creation"""
        seeder.add_entity(GetInTouch, 1)
        seeder.execute()  # create instance
        # assertions
        self.assertTrue(GetInTouch.objects.exists())
        self.assertIn('GetInTouch', self.models_name)
    
    
    
    
    
