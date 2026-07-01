from wagtail.snippets.models import register_snippet
from .viewsets import WarGameModelViewSet

register_snippet(WarGameModelViewSet)