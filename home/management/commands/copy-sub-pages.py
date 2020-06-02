from django.core.management.base import BaseCommand, CommandError

from home.models import HomePage2, FestivalPage

class Command(BaseCommand):
    help = 'copy the festival sub pages to the new home page root'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        new_root = HomePage2.objects.first()
        old_root = FestivalPage.objects.first()
        if new_root is None or old_root is None:
            print("Aborting. new and old must exist")
            return 2
        for child_page in old_root.get_children():
            print(child_page)
            child_page.copy(recursive=True, to=new_root)
