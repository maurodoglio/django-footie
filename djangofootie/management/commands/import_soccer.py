from django.core.management.base import BaseCommand
from optparse import make_option
from soccerstats.soccer.utils import store_footbal_data
from urllib2 import urlopen
from django.conf import settings
import os
from csv import DictReader

class Command(BaseCommand):
    help = "Import soccer stats from http://www.football-data.co.uk"
    option_list = BaseCommand.option_list + (
        make_option('--dev-mode',
            action='store_true',
            dest='dev_mode',
            default=False,
            help='Run the upload in dev mode'),
        make_option('--year',
            action='store',
            dest='year',
            default=2011,
            help='Specify the year to upload'),
        )
    def handle(self, *args, **options):
        if options['dev_mode']:
            source=open(os.path.join(settings.BASE_DIR,'I1.csv'))
        else:
            url_template = "http://www.football-data.co.uk/mmz4281/%s%s/I1.csv"
            year = int(options['year'])
            begin =  "%s" % year
            end = "%s" % (year+1)
            url = url_template % (begin[-2:],end[-2:])
            source = urlopen(url)
        print "Starting download..."
        store_footbal_data(DictReader(source))
        print "Download completed"
        
        