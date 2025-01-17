from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from driver_utils import initialize_driver
from helpers import get_soup, get_attributes, get_attribute_list, get_script_attribute
from config import IMDB_URL, HEADERS

def button_click(driver, xpath):
    """Clicks a button specified by its XPath."""
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        driver.execute_script("arguments[0].click()", button)
    except Exception as e:
        print(f"Error clicking button: {e}")

def scrape_movies():
    """Scrapes IMDb movies and saves details to a CSV."""
    driver = initialize_driver()
    driver.get(IMDB_URL)

    soup = get_soup(driver.current_url, HEADERS)
    total_movies = soup.select("div.fwjHEn")[0].get_text(strip=True).split()[-1] #Get the total number of movies
    movie_list = []

    for i in range(1, int(total_movies)+1):  # Scrape movies one by one
        if (i % 50 == 0): #Click the see more button every 50 movies
            see_more_button = "(//span[@class='ipc-see-more__text'])"
            button_click(see_more_button)

        thumbnail = soup.select("li.ipc-metadata-list-summary-item")[i-1] #Get the thumbnail of the movie

        if thumbnail.select_one(".ipc-media--fallback") is not None: #Check if the thumbnail is available
            print("Thumbnail not found!")
            pass
        else:
            movie_poster = f"(//a[@class='ipc-title-link-wrapper'])[{i}]" #Get the movie poster
            button_click(driver, movie_poster)

            sub_page_soup = get_soup(driver.current_url, HEADERS) #Get the movie details soup

            movie_details = {
                "title": get_attributes(sub_page_soup, "span.hero__primary-text"),
                "duration": get_script_attribute(sub_page_soup, "duration"),
                "imdb_rating": get_attributes(sub_page_soup, "span.imUuxf"),
                "directors": get_attribute_list(sub_page_soup, 'a[href*="ref_=tt_cst_dr_"]'),
                "writers": get_attribute_list(sub_page_soup, 'a[href*="ref_=tt_ov_wr_"]'),
                "cast": get_attribute_list(sub_page_soup, 'a.kVdWAO'),
                "genres": get_attribute_list(sub_page_soup, 'a[href*="ref_=tt_ov_in_"]'),
                "release_date": get_attributes(
                    sub_page_soup, 'a.ipc-metadata-list-item__list-content-item[href*="ref_=tt_dt_rdat"]'
                ),
                "languages": get_attribute_list(sub_page_soup, 'a[href*="ref_=tt_dt_ln"]'),
                "production_companies": get_attribute_list(
                    sub_page_soup, 'a[href*="ref_=tt_dt_cmpy_"]'
                ),
            }

            movie_list.append(movie_details)
            driver.back()  # Go back to the main page
            time.sleep(2)

    driver.quit()

    # Save to CSV
    df = pd.DataFrame(movie_list)
    df.to_csv("imdb_movies.csv", index=False)
    print("Scraping completed! Data saved to imdb_movies.csv")

if __name__ == "__main__":
    scrape_movies()
