from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    template = "core/home_page.html"