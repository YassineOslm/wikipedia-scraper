# Wikipedia scraper

BeCode learning project aiming at scraping wikipedia and using API.

## 🔍 Description

This project defines a `WikipediaScraper` class that interacts with the [country-leaders API](https://country-leaders.onrender.com). It retrieves the list of countries and their political leaders, then accesses each leader's Wikipedia page to extract and clean the **first paragraph** of the article. The final data is stored in a structured `.json` file for further use.

## ⚙️ Installation

💻 Make sure you have Python installed. Then, install all required libraries by running:

```
pip install -r requirements.txt
```

## 🚀 Usage

1. Run `main.py` to collect information about all countries and their leaders.  
   You can choose the output format by passing an argument:

   - `python main.py json` → saves the result in `leaders_data.json`
   - `python main.py csv` → saves the result in `leaders_data.csv`

2. You can reuse and extend the scraper using its core methods:
   - `get_countries()` → retrieves the list of available countries from the API
   - `get_leaders(country: str)` → fetches the leaders for a given country and adds the first Wikipedia paragraph for each
   - `get_first_paragraph(wikipedia_url: str)` → extracts and cleans the first paragraph from a Wikipedia page
   - `to_json_file(filepath: str)` → exports the collected data to a JSON file
   - `to_csv_file(filepath: str)` → exports the collected data to a CSV file

## Contributors

- Trainee : Yassine Aârab
- Coach : Vanessa Rivera Quiñones
