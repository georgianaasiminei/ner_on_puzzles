import re
from collections import Counter
from typing import List

import requests
from bs4 import BeautifulSoup

from puzzles_extractor.models import Puzzle

DOMAIN = "https://www.brainzilla.com"
ZEBRA_PUZZLES_PATH = "/logic/zebra/"
SOURCE_ID = 1


class BrainzillaExtractor:
    def extract_pages(self) -> List[str]:
        start_url = f"{DOMAIN}{ZEBRA_PUZZLES_PATH}"
        html_doc = requests.get(start_url)
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        pages_paths = soup.find('div', class_="col-lg-8").findAll('li')
        pages = []
        for page in pages_paths:
            pages.append(page.a['href'])
        return pages

    def extract_puzzle(self, puzzle_url: str) -> Puzzle:
        html_doc = requests.get(puzzle_url)
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        title_selector = soup.find('div', class_="page-header").find('h1').text
        title = re.search("(.*)\sZebra", title_selector).group(1)
        description = soup.find('div', class_="page-header").find('div', class_='description').text
        clues = soup.find('div', class_="clues").text
        return Puzzle(
            title=title.strip(),
            description=description.strip(),
            clues=clues.strip(),
            url=puzzle_url,
            source_id=SOURCE_ID
        )

    def extract_all_puzzles(self) -> List[Puzzle]:
        """Returns a list of all the puzzles found on the Brainzilla source"""
        pages_urls = self.extract_pages()
        print(f"\n{pages_urls}\n")

        # Extract all puzzles
        puzzles = []
        for path in pages_urls:
            full_path = f"{DOMAIN}{path}"
            extracted_puzzle = self.extract_puzzle(full_path)
            puzzles.append(extracted_puzzle)
            # print(extracted_puzzle.title, extracted_puzzle.url, extracted_puzzle.description, extracted_puzzle.clues)
            print(extracted_puzzle.title)
        return puzzles

    # def populate_db(self, puzzles: List[Puzzle]):
    #     # Add Source
    #     brainzilla_source = Source(
    #         name="Brainzilla",
    #         domain="https://www.brainzilla.com",
    #         puzzles_path="/logic/zebra/"
    #     )
    #     brainzilla_source.save()
    #
    #     # Add puzzles
    #     for puzzle in puzzles:
    #         puzzle.save()
