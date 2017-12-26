from django.core.management.base import BaseCommand, CommandError
from shortener.models import KirrURL

class Command(BaseCommand):
  
    help='refesh all kirURl Shortcode '
    


    def handle(self, *args, **options):
        return KirrURL.objects.refresh_shortcodes()
      
