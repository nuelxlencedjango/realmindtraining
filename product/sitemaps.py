from django.contrib.sitemaps import Sitemap
from .models import Product ,Course



class ProductSitemap(Sitemap):
    def items(self):
        return Product.objects.all()




class CourseSitemap(Sitemap):
    def items(self):
        return Course.objects.all()
