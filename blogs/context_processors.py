from .models import Category
from assignments.models import SocialLink

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)

def developer_info(request):
    return {
        'developer_name': 'Ananthakrishnan M Zen',
        'platform_version': '1.0-Prod'
    }