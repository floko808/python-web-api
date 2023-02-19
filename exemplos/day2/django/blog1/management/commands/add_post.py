from django.core.management.base import BaseCommand, CommandError
from blog1.models import Post
from django.utils.text import slugify


class Command(BaseCommand):
    """Adds new post to the database
    $ django.admin add_post --tile "Post from CLI" --content "Post added from terminal/CLI"
    """
    help = "Creates a new post in the database"

    def add_arguments(self, parser):
        parser.add_argument("--title", type=str)
        parser.add_argument("--content", type=str)
        

    def handle(self, *args, **options):
        try:
            post = Post.objects.create(
                title=options["title"],
                content=options["content"],
                slug=slugify(options["title"]),
            )
        except Exception as e:
            raise CommandError(e)
        else:
            self.stdout.write(self.style.SUCCESS(f"Post {post.title} created."))
