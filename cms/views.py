from django.views.generic import TemplateView

from blog.models.post import Post
from calls.forms import GetInTouchForm
from cms.models.aboutcompany import AboutCompany
from cms.models.aboutdashboard import AboutDashboard
from cms.models.abouttest import AboutTest
from cms.models.abouttracker import AboutTracker
from cms.models.contactus import ContactUs
from cms.models.faq import Faq
from cms.models.howtogetcertificate import HowToGetCertificate
from cms.models.siteinfo import SiteInfo


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['site_info'] = SiteInfo.get_all_from_cache()[0] if SiteInfo.get_all_from_cache() else None
        context['about_company'] = AboutCompany.get_all_from_cache()[0] if AboutCompany.get_all_from_cache() else None
        context['about_tracker'] = AboutTracker.get_all_from_cache()[0] if AboutTracker.get_all_from_cache() else None
        context['about_dashboard'] = AboutDashboard.get_all_from_cache()[0] if AboutDashboard.get_all_from_cache() else None
        context['about_test'] = AboutTest.get_all_from_cache()[0] if AboutTest.get_all_from_cache() else None
        context['get_certified'] = HowToGetCertificate.get_all_from_cache()[0] if HowToGetCertificate.get_all_from_cache() else None
        posts = Post.objects.filter(show_in_index=True).order_by('?')[:4]
        context['right_up_blog_post'] = posts[0]
        context['right_down_blog_post'] = posts[1]
        context['left_up_blog_post'] = posts[2]
        context['left_down_blog_post'] = posts[3]
        context['center_blog_post'] = Post.objects.last()
        context['contact_us'] = ContactUs.get_all_from_cache()[0] if ContactUs.get_all_from_cache() else None
        context['faqs'] = Faq.get_all_from_cache()

        return context
