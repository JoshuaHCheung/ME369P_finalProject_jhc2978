from universityScraper import universityScraper
from professorScraper import professorScraper
import os
from pathlib import Path
import pickle

# testScraper1 = universityScraper()
# testScraper1.getProfessors()

# testScraper2 = professorScraper()
# testScraper2.getReviews()

script_dir = os.path.dirname(__file__)
file = os.path.join(script_dir, 'admin_directory', 'professor_urls.pkl')
with open(file, 'rb') as fp:
    reading_lists = pickle.load(fp)
    print(reading_lists)
    print(len(reading_lists))
