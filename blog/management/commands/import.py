from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone

from ...models import Post

import csv

class Command(BaseCommand):
    help = 'csv import command'

    def handle(self, *args, **options):
        f = csv.reader(open('./blog/data/data.csv', 'r', encoding='ms932', errors='', newline='' ), delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

        for row in f:
            print(row)

            post = Post()
            post.title = row[0]
            post.text = row[1]
            post.published_date = timezone.now()
            post.save()
        
        print('Success!!')