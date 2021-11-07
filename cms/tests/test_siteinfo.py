"""
Auto Generated test
Automatically generated with ❤️ by django-sage-painless
"""
from django.apps import apps
from django.urls import reverse
from rest_framework.test import APITestCase
from django_seed import Seed


from cms.models.aboutcompany import AboutCompany

from cms.models.abouttracker import AboutTracker

from cms.models.aboutdashboard import AboutDashboard

from cms.models.howtogetcertificate import HowToGetCertificate

from cms.models.contactus import ContactUs

from cms.models.faq import Faq

from cms.models.siteinfo import SiteInfo


seeder = Seed.seeder()


class SiteinfoTest(APITestCase):
    """
    SiteInfo Test
    Auto Generated
    """
    def setUp(self) -> None:
        self.models = apps.get_app_config('cms').get_models()
        self.models_name = [model._meta.object_name for model in self.models]
        
        seeder.add_entity(AboutCompany, 3)
        
        seeder.add_entity(AboutTracker, 3)
        
        seeder.add_entity(AboutDashboard, 3)
        
        seeder.add_entity(HowToGetCertificate, 3)
        
        seeder.add_entity(ContactUs, 3)
        
        seeder.add_entity(Faq, 3)
        
        seeder.add_entity(SiteInfo, 3)
        
        seeder.execute()  # create instances
    
    def test_siteinfo_model(self):
        """test SiteInfo creation"""
        seeder.add_entity(SiteInfo, 1)
        seeder.execute()  # create instance
        # assertions
        self.assertTrue(SiteInfo.objects.exists())
        self.assertIn('SiteInfo', self.models_name)
    
    def test_siteinfo_list_success(self):
        """test SiteInfo list"""
        url = reverse('siteinfo-list')
        response = self.client.get(url)
        # assertions
        self.assertEqual(response.status_code, 200)
        if type(response.data) == dict:
            if response.data.get('count'):
                self.assertGreater(response.data['count'], 0)
        else:
            self.assertGreater(len(response.data), 0)

    def test_siteinfo_detail_success(self):
        """test SiteInfo detail"""
        siteinfo = SiteInfo.objects.first()
        url = reverse('siteinfo-detail', args=[siteinfo.pk])
        response = self.client.get(url)
        # assertions
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(response.data.get('tel'), siteinfo.tel)
        
        self.assertEqual(response.data.get('email'), siteinfo.email)
        
        self.assertEqual(response.data.get('address'), siteinfo.address)
        
        self.assertEqual(response.data.get('instagram'), siteinfo.instagram)
        
        self.assertEqual(response.data.get('facebook'), siteinfo.facebook)
        
        self.assertEqual(response.data.get('twitter'), siteinfo.twitter)
        
        self.assertEqual(response.data.get('linkedin'), siteinfo.linkedin)
        
        self.assertEqual(response.data.get('whatsapp'), siteinfo.whatsapp)
        
        self.assertEqual(response.data.get('footer'), siteinfo.footer)
        
        
        
        
        
        
    
    
