from scrapers.scraper import Scraper


class SectionScraper(Scraper):
    def __init__(self, url):
        super().__init__(url)

        self.__sections_names: list = self.__set_names()
        self.__sections_paths: list = self.__set_paths()
        self.__sections_urls: list = self.__set_section_urls()

    def __find_status(self):
        return super()._get_soup().find_all('div', class_='status')

    def __get_section(self) -> tuple:
        paths = []
        names = []

        case_reports = self.__find_status()

        for case_report in case_reports:
            a_tag = case_report.find('a')

            if a_tag:
                href_value = a_tag.get('href')
                text_value = a_tag.text

                if href_value and href_value.startswith('/Istorii-boleznyeĭ/'):
                    names.append(text_value)
                    paths.append(href_value)

        return names, paths

    def __set_names(self) -> list:
        return self.__get_section()[0]

    def __set_paths(self) -> list:
        return self.__get_section()[1]

    def __get_paths(self) -> list:
        return self.__sections_paths

    def __set_section_urls(self) -> list:
        return super()._create_url_from_path(self.__get_paths())

    def _get_urls(self) -> dict:
        return dict(zip(self.__set_names(), self.__set_section_urls()))

    def scrape_sections(self) -> list:
        """
        :return: list of dict with name of sections and case-report urls belong to that sections.
        [
    {
        "section_name_1": {
            "case_name_1": "case_url_1",
            "case_name_2": "case_url_2"
        }
    },
    {
        "section_name_2": {
        }
    }
]
        """
        sections = []

        for name, url in self._get_urls().items():
            section = SectionScraper(url)
            sections.append({name: section._get_urls()})
        return sections
