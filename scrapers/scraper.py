from bs4 import BeautifulSoup
import requests


class Scraper:
    def __init__(self, url):
        self.__url: str = url
        self.__content: str = self.__get_html_content()
        self.__soup = self.__soup_init()

    def get_url(self):
        return self.__url

    def __soup_init(self):
        return BeautifulSoup(self.__content, 'lxml')

    def _get_soup(self):
        return self.__soup

    def __get_html_content(self) -> str:
        return requests.get(self.__url).text

    @staticmethod
    def _create_url(paths: str | list) -> str | list:
        base_url = 'https://kingmed.info'

        if isinstance(paths, str):
            return base_url + paths
        elif isinstance(paths, list):
            return [base_url + path for path in paths]

    def _create_url_from_path(self, paths: list) -> list:
        return self._create_url(paths)
