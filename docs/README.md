## **IMDb Movie Scraper**

### **Description**
The IMDb Movie Scraper is a Python project that extracts details of Hindi movies and TV movies set to release in 2024. It utilizes **Selenium** for browser automation, **BeautifulSoup** for HTML parsing, and **Pandas** for saving data in a structured CSV format.

The scraped data includes:
- Movie title
- Duration
- IMDb rating
- Directors, writers, and cast
- Genres, release dates, languages, and production companies

### **Features**
- Automates data scraping from IMDb.
- Extracts detailed information for each movie.
- Stores data in structured CSV and Excel files inside the `data` folder for further analysis.

---

### **Installation**

#### **Step 1: Clone the Repository**
Clone this repository to your local machine using the following command:
```bash
git clone <repository-URL>
```

#### **Step 2: Open the Project in VS Code**
Open the project folder in **Visual Studio Code**.

#### **Step 3: Install Dependencies**
Install the required Python libraries by running:
```bash
pip install -r requirements.txt
```

---

### **Usage**

1. Open **VS Code** and navigate to `web_scraping/scraper.py`.
2. Run the script:
   ```bash
   python web_scraping/scraper.py
   ```
3. The script will:
   - Open IMDb using Selenium.
   - Scrape details of movies releasing in 2024.
   - Save the data to CSV inside `data/`.

---

### **Project Structure**

```
bollywood_movies/
├── web_scraping/
│   ├── scraper.py         # Main script to scrape movie data
│   ├── driver_utils.py    # Selenium WebDriver setup and utility functions
│   ├── helpers.py         # Functions for parsing and extracting data
│   ├── config.py          # Contains constants like URLs and headers
│
├── data/
│   ├── Actors.csv
│   ├── Actresses.csv
│   ├── cleaned_imdb_movies.csv
│   ├── exploded_imdb_movies.csv
│   ├── imdb_movies.csv
│   ├── movies_actors.xlsx
│   ├── movies_actresses.xlsx
│   ├── movies_directors.xlsx
│   ├── movies_genres.xlsx
│   ├── movies_info.xlsx
│   ├── movies_languages.xlsx
│   ├── movies_production_companies.xlsx
│   ├── movies_with_more_than_8_rating.csv
│   ├── movies_with_no_duration.csv
│   ├── movies_with_no_rating.csv
│   ├── movies_writers.xlsx
│
├── notebooks/
│   ├── eda_notebook.ipynb # Jupyter notebook for Exploratory Data Analysis
│   ├── analysis_notebook.ipynb # Jupyter notebook for Data Analysis
│
├── reports/
│   ├── summary_report.pdf  # Final reports and visualizations
│
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

### **Dependencies**
- **Selenium**: For browser automation.
- **BeautifulSoup4**: For HTML parsing.
- **Pandas**: For data manipulation and storage.
- **Requests**: For fetching web page content.

Install dependencies by running:
```bash
pip install -r requirements.txt
```

---

### **Output**
The script generates CSV file inside the `data` folder:
```
data/
├── imdb_movies.csv
```
containing details like:
- Title
- Duration
- IMDb Rating
- Directors, Writers, Cast
- Genres, Release Date
- Languages, Production Companies

---

### **Future Improvements**
- Integrate a database to store movie data.
- Implement better error handling for dynamic website changes.

---

### **License**
This project is licensed under the MIT License. Feel free to use and modify it for your own purposes.

---

