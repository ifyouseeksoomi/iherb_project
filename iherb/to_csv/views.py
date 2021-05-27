from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re
import csv

from django.views import View
from django.http import JsonResponse

from to_csv.utils import max_page


class CrawlingView(View):
    def post(self, request):
        try:
            csv_filename = 'iherb_bath_and_personal.csv'
            csv_open = open(csv_filename, 'w+', encoding='utf-8')
            csv_writer = csv.writer(csv_open)
            csv_writer.writerow((
                'key_number',
                'category',
                'name',
                'rating',
                'reviews',
                'price',
                'link'
            ))

            url = 'https://kr.iherb.com/c/Bath-Personal-Care?p=1&sort=13'
            response = requests.get(url)
            source = response.text
            soup = BeautifulSoup(source, 'html.parser')

            max_page(soup)

            return JsonResponse({'Crawling done'}, status=200)

        except TypeError as type_e:
            return JsonResponse({'TypeError': str(type_e)}, status=400)

        except KeyError as key_e:
            return JsonResponse({'KeyError': key_e}, status=400)

        except ValueError as value_e:
            return JsonResponse({'ValueError': str(value_e)}, status=400)
