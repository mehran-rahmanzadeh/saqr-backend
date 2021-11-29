from django.utils.translation import get_language
from django.views.generic import ListView

from blog.models.post import Post
from blog.models.tag import Tag
from cms.models.siteinfo import SiteInfo


class BlogListView(ListView):
    """blog list view"""
    context_object_name = 'posts'
    paginate_by = 6
    model = Post
    ordering = ('-created',)

    def get_template_names(self):
        if self.request.user_agent.is_mobile:
            if get_language() == 'en':
                template = 'responsive/post-list.html'
            else:
                template = 'responsive/post-list-rtl.html'
        else:
            if get_language() == 'en':
                template = 'blogList.html'
            else:
                template = 'blogList-rtl.html'
        return template

    def get_queryset(self):
        query_params = self.request.GET.dict()
        query_params = {k: v for k, v in query_params.items() if v}
        query_params.pop('page', None)
        qs = self.model.objects.filter(**query_params).order_by(*self.ordering)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(BlogListView, self).get_context_data(*args, **kwargs)
        context['site_info'] = SiteInfo.get_all_from_cache()[0] if SiteInfo.get_all_from_cache() else None
        context['tags'] = Tag.get_all_from_cache()
        context['more_visited'] = Post.objects.order_by('?')[:4]
        return context
