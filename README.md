# Vivino Dashboard

## 📒 Overview

This repository contains a Python project for creating a Tableau dashboard based on data scraped from the Vivino wine ratings website. The project involves scraping data, organizing it into a SQLite database, preprocessing the data, and exporting it to CSV files for use with Tableau (free). Additionally, there are notebooks for exploration and sprint planning templates. The Tableau dashboard provides interactive visualizations for exploring wine ratings, prices, regions, wineries, and more.

## 📦 Repo Structure

```
.
├── data/
│ ├── csv_files/
│ └── vivino.db
├── notebooks/
│ ├── exploration.ipynb
│ └── sprint_planning_template_-_vivino.docx
├── source/
│ ├── data_preprocessing.py
│ └── db_to_csv.py
└── tableau_dashboard/
├── Consumer Insights Dashboard.twb
├── Wine Pairing Dashboard.twb
├── README.md
└── requirements.txt
```

## 🗃️ Database Structure

![Database Diagram](extras\vivino_db_diagram_horizontal.png)

## 🐍 Data Exporter (db_to_csv.py)

The `db_to_csv.py` script exports data from the SQLite database to CSV files. It connects to the database, retrieves table names, fetches rows, and writes them to CSV files. This was necessary to connect to the free version of Tableau

## 📊 Tableau Dashboard

The Tableau dashboard includes:

- Interactive bivariate choropleth maps comparing consumer volume and activity, and wine prices and ratings
- Bar charts detailing wineries, wines, vintages, and grapes by volume, price, and rating
- Drill-down capabilities to explore wine regions and winery locations

## 🎮 Usage

1. **Clone the repository**:
    ```
    git clone https://github.com/nasesmae/vivino.git
    ```

2. **Install dependencies**:
    ```
    pip install -r requirements.txt
    ```

3. **Run the Tableau dashboard**:
    Open `Consumer Insights Dashboard.twb` and `Wine Pairing Dashboard.twb` in Tableau.

## ⏱️ Timeline

The development of this project took 5 days for completion.

## 📌 Personal Situation

This project was completed as part of the AI Boocamp at BeCode.org by team Python Pricers. 

Connect with the Python Pricers on LinkedIn:
1. [Bear Revels](https://www.linkedin.com/in/bear-revels/)
2. [Daryoush Ghanbarpour](https://www.linkedin.com/in/daryoushghanbarpour/)
3. [Nasrin Esmaeilian](https://www.linkedin.com/in/nasrin-esmaeilian-a130022aa/)