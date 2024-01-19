import os
import requests
from tqdm import tqdm
from scrapers.scraper import Scraper


class DownloadScraper(Scraper):
    def __init__(self, url):
        super().__init__(url)

    def __find_path(self) -> str:
        return super()._get_soup().find('a', href=True, attrs={'rel': 'nofollow'})['href']

    def __find_download_link(self) -> str:
        return super()._get_soup().find('a', href=True, class_='download_link')['href']

    def _get_dl_page(self) -> str:
        return super()._create_url(paths=self.__find_path())

    def _get_dl_url(self) -> str:
        return super()._create_url(paths=self.__find_download_link())

    def _get_url_for_download(self) -> str:
        """
        str :self.get_url(): take case-report url as an argument.
        str :return: url for file downloading.
        """
        download_url = DownloadScraper(self.get_url())._get_dl_page()
        return DownloadScraper(download_url)._get_dl_url()

    def download_file(self, filename, path=None):
        """
        Download file from the specified URL and save it to the path.

        Parameters:
        - filename (str): The name to be used for the downloaded file.
        - path (str, optional): The local path where the file will be saved.
          If not provided, the file will be saved in the current working directory.

        Returns:
        - str: The full path where the file is saved.
        """
        download_url = self._get_url_for_download()

        if path is None:
            path = ''

        full_path = os.path.join(path, filename)
        response = requests.get(download_url, stream=True)

        if response.status_code == 200:
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024

            with open(full_path, 'wb') as file, tqdm(
                desc=filename,
                total=total_size,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
            ) as bar:
                for data in response.iter_content(block_size):
                    bar.update(len(data))
                    file.write(data)
