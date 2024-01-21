import os
import re
from scrapers.dl import DownloadScraper
from scrapers.section import SectionScraper
from requests.exceptions import RequestException, SSLError


class Downloader:
    BASE_URL = 'https://kingmed.info/Istorii-boleznye%C4%AD/'

    def __init__(self, path):
        self.sections = SectionScraper(self.BASE_URL).scrape_sections()
        self.path = os.path.normpath(path)

    @staticmethod
    def __process_filename(name: str) -> str:
        # Use regex to remove non-alphanumeric characters
        name = re.sub(r'[^a-zA-Z0-9а-яА-Я ]', '', name)
        # Replace spaces with underscores and convert to lowercase
        name = name.replace(' ', '_').lower()
        return name

    @staticmethod
    def create_directory(directory_path):
        os.makedirs(directory_path, exist_ok=True)

    def _download_file(self, case_name, case_url):
        filename = self.__process_filename(case_name)
        if os.path.exists(filename):
            print(f"The file {filename} already exists in the current directory.")
            return

        try:
            dl_scraper = DownloadScraper(case_url)
            dl_scraper.download_file(filename=filename)

        except (RequestException, SSLError) as e:
            print(f"Error downloading {filename}: {e}")

    def download_files(self):
        os.chdir(self.path)

        main_dir = 'case_reports'
        self.create_directory(main_dir)
        main_dir_path = os.path.join(self.path, main_dir)

        for url_dict in self.sections:
            os.chdir(main_dir_path)

            for section_name, cases in url_dict.items():
                section_path = os.path.join(main_dir_path, section_name)
                self.create_directory(section_path)
                os.chdir(section_path)

                for case_name, case_url in cases.items():
                    self._download_file(case_name, case_url)
