from bs4 import BeautifulSoup
import requests
import csv

from django.views import View
from django.http import JsonResponse
from django.core.paginator import (
    Paginator,
    EmptyPage
)

from to_csv.models import (
    BathPersonalProduct
)


class OneCrawlingView(View):
    def post(self, request):
        try:
            csv_filename = 'iherb_bath_and_personal_one_crawling.csv'
            csv_open = open(csv_filename, 'w+', encoding='utf-8')
            csv_writer = csv.writer(csv_open)
            csv_writer.writerow((
                'key_number',  # iherb 내 상품 고유 id
                'img_src',     # 상품 이미지 source url
                'name',        # 상품명 (타이틀)
                'rating',      # 별점
                'reviews',     # 리뷰 수
                'price',       # 가격
                'link'         # 링크 url
            ))

            url = 'https://kr.iherb.com/c/Bath-Personal-Care?p=81'
            response = requests.get(url)
            source = response.text
            soup = BeautifulSoup(source, 'html.parser')

            page_content = soup.find_all(
                'div', {'class': 'product-inner product-inner-wide'})

            for page in page_content:
                a_tag = page.find_all('a')
                img_tag = page.find_all('button')

                product_id = a_tag[0].get(
                    'data-ga-product-id') if a_tag[0].get('data-ga-product-id') != None else ''

                img_src = img_tag[0].get(
                    'data-cart-info').split('"iURLMedium":"')[1].split('","listPrice"')[0]

                name = a_tag[0].get(
                    'aria-label') if a_tag[0].get('aria-label') != None else ''

                if len(a_tag) >= 2:
                    rating = a_tag[2].get('title').split(' - ')[0]
                    reviews = a_tag[2].get('title').split(' - ')[1][:-3]

                else:
                    rating = ''
                    reviews = ''

                price = a_tag[0].get(
                    'data-ga-discount-price') if a_tag[0].get('data-ga-discount-price') != None else ''

                link = a_tag[0].get('href') if a_tag[0].get(
                    'href') != None else ''

                csv_writer.writerow(
                    (product_id, img_src, name, rating, reviews, price, link))

            csv_open.close()

            return JsonResponse({'message': 'Crawling done'}, status=200)

        except TypeError as type_e:
            return JsonResponse({'TypeError': str(type_e)}, status=400)

        except KeyError as key_e:
            return JsonResponse({'KeyError': key_e}, status=400)

        except ValueError as value_e:
            return JsonResponse({'ValueError': str(value_e)}, status=400)


class CrawlingView(View):
    def post(self, request):
        try:
            csv_filename = 'iherb_bath_and_personal.csv'
            csv_open = open(csv_filename, 'w+', encoding='utf-8')
            csv_writer = csv.writer(csv_open)
            csv_writer.writerow((
                'key_number',  # iherb 내 상품 고유 id
                'img_src',     # 상품 이미지 source url
                'name',        # 상품명 (타이틀)
                'rating',      # 별점
                'reviews',     # 리뷰 수
                'price',       # 가격
                'link'         # 링크 url
            ))

            url = 'https://kr.iherb.com/c/Bath-Personal-Care?p=1'
            response = requests.get(url)
            source = response.text
            soup = BeautifulSoup(source, 'html.parser')

            page_list = soup.find_all('div', {'class': 'pagination'})
            max_page = int(page_list[0].find_all('span')[-2].text)

            for page in range(1, max_page+1):
                pagination_url = 'https://kr.iherb.com/c/Bath-Personal-Care?p=' + \
                    str(page)

                pagination_response = requests.get(pagination_url)
                pagination_source = pagination_response.text
                soup = BeautifulSoup(pagination_source, 'html.parser')

                product_list = soup.find_all(
                    'div', {'class': 'product-inner product-inner-wide'}
                )

                for product in product_list:
                    a_tag = product.find_all('a')
                    img_tag = product.find_all('img')

                    product_id = a_tag[0].get(
                        'data-ga-product-id') if a_tag[0].get('data-ga-product-id') != None else ''

                    img_src = img_tag[0].get(
                        'src') if len(img_tag) != 0 else ''

                    # if len(img_tag) != 0:
                    #     img_src = img_tag[0].get(
                    #         'data-cart-info').split('"iURLMedium":"')[1].split('","listPrice"')[0]
                    # else:
                    #     img_src = ''

                    name = a_tag[0].get(
                        'aria-label') if a_tag[0].get('aria-label') != None else ''

                    if len(a_tag) >= 2:
                        rating = a_tag[2].get('title').split(' - ')[0]
                        reviews = a_tag[2].get('title').split(' - ')[1][:-3]

                    else:
                        rating = ''
                        reviews = ''

                    price = a_tag[0].get(
                        'data-ga-discount-price') if a_tag[0].get('data-ga-discount-price') != None else ''

                    link = a_tag[0].get('href') if a_tag[0].get(
                        'href') != None else ''

                    csv_writer.writerow(
                        (product_id, img_src, name, rating, reviews, price, link))

            csv_open.close()

            return JsonResponse({'message': 'Crawling done'}, status=200)

        except TypeError as type_e:
            return JsonResponse({'TypeError': str(type_e)}, status=400)

        except KeyError as key_e:
            return JsonResponse({'KeyError': key_e}, status=400)

        except ValueError as value_e:
            return JsonResponse({'ValueError': str(value_e)}, status=400)


class BathPersonalProductListView(View):
    def get(self, request):
        try:
            page = request.GET.get('page')
            products_list = BathPersonalProduct.objects.all()

            p = Paginator(products_list, 24)
            p_products = p.page(page)

            result = list({
                'key_number': product.key_number,
                'img_src': product.img_src,
                'name': product.name,
                'rating': product.rating,
                'reviews': product.reviews,
                'price': product.price,
                'link': product.link
            } for product in p_products)

            return JsonResponse({
                'pages': p.num_pages,
                'items': p.count,
                'products_list_per_page': result
            }, status=200)

        except TypeError as type_e:
            return JsonResponse({'TypeError': str(type_e)}, status=400)

        except KeyError as key_e:
            return JsonResponse({'KeyError': key_e}, status=400)

        except ValueError as value_e:
            return JsonResponse({'ValueError': str(value_e)}, status=400)

        except EmptyPage as page_e:
            return JsonResponse({'EmptyPage': str(page_e)}, status=400)
