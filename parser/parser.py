import requests
from bs4 import BeautifulSoup as BS
from django.views.decorators.csrf import csrf_exempt

URL = 'https://www.kinopoisk.ru/lists/movies/top250/'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
}

@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_="product-card-list")
    _film = []
    for item in items:
        _film.append(
            {
                'title_url': URL + item.find('a').get('href'),
                'title_text': item.find('div', class_="base-movie-main-info_mainInfo__ZL_u3").get_text(),
                'image': URL + item.find('div', class_="styles_image__gRXvn styles_mediumSizeType__fPzdD image styles_root__DZigd").find('img').get('src'),
                'description': item.find('div', class_="desktop-list-main-info_truncatedText__IMQRP").get_text(),
                'role': item.find('div', class_="desktop-list-main-info_additionalInfo__Hqzof").get_text()
            }
        )
        return _film

@csrf_exempt
def parser():
        html = get_html(URL)
        if html.status_code == 200:
            film1 = []
            for page in range(0, 1):
                html = get_html(f'', params=page)
                film1.extend(get_data(html.text))
            # return manas_film
            print(f'\n{film1}\n')
        else:
            raise Exception('Parse Error......')

parser()