import requests

from amazon import constants

from bs4 import BeautifulSoup


def get_html(url: str):
    """
    get html of the requested url
    :param url: url to parse html
    :return: return html as a string
    """
    response = requests.get(url=url, headers=constants.AMAZON_HEADERS)

    if response.status_code == 200:
        return response.text
    return None


def parse_website():
    # get html string
    html_string = get_html(url=constants.AMAZON_URL)

    if html_string:
        # parse html using beautiful soup
        soup_obj = BeautifulSoup(markup=html_string, features='html.parser')

        result_dict = {}

        # get all the links in the page
        link = []
        for links in soup_obj.find_all('a'):
            link_str = links.get('href')
            if link_str and (link_str.startswith('https') or link_str.startswith('http')):
                link.append(link_str)

        result_dict['links'] = link

        # get all the texts in the page
        result_dict['texts'] = soup_obj.get_text()

        return result_dict

    return None
