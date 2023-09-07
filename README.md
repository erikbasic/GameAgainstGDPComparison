# Game Sales and GDP Analysis

This project analyzes the relationship between video game sales and GDP (Gross Domestic Product) per resident in different parts of the world. The main objective is to investigate how GDP growth or decline, along with other factors, affects video game sales. The primary regions studied in this analysis are North America and Japan.

## 1. Data Sources

The data for this analysis was collected from the following sources:

- Video Game Sales: [Kaggle Video Game Sales Dataset](https://www.kaggle.com/datasets/gregorut/videogamesales?resource=download)
- GDP by Selected Country: [OECD GDP Data](https://data.oecd.org/gdp/gross-domestic-product-gdp.htm#indicator-chart)

The Kaggle dataset contains information on approximately 16,598 video games, including details such as rank, name, platform, release year, genre, publisher, and sales figures for different regions.

The OECD GDP dataset provides GDP values by year and country, which are essential for understanding the economic context of video game sales.

## 2. Data Cleaning

### Cleaning the First Dataframe

- Removed records with missing 'Year' values.
- Kept records with missing 'Publisher' values.
- Filtered games released between 1980 and 2010.

### Cleaning the Second Dataframe

- Split the comma-separated columns in the second dataframe.
- Removed quotation marks from the 'Time' field.
- Filtered data for countries of interest (USA, Canada, Mexico, Japan).

## 3. Merging Dataframes

Merged the video game sales dataframe with GDP data for each of the selected countries (USA, Canada, Mexico, Japan) based on the 'Year' column.

## 4. Visualizations

### Key Visualizations:

1. **Top 10 Most Sold Games**: Visualized the top-selling video games.
2. **Most Popular Platforms**: Identified the most popular gaming platforms.
3. **Most Popular Genres**: Explored the most popular video game genres.
4. **Top 10 Publishers**: Analyzed the top video game publishers.
5. **Sales Comparison (NA vs. Japan)**: Compared video game sales in North America and Japan over time.
6. **Comparison of GDP**: Examined the GDP trends in the analyzed countries.
7. **Impact of Financial Crisis on Sales (Europe)**: Explored how the 2007 financial crisis impacted video game sales in Europe.
8. **Comparison of Sales (NA, Japan, Europe)**: Compared video game sales in North America, Japan, and Europe.
9. **Comparison of Sales (Rest of the World)**: Analyzed video game sales in the rest of the world compared to the primary regions.

These visualizations provide insights into the video game industry's performance and its correlation with economic factors.

## Notebooks and Data Sources

- The Jupyter Notebook used for this analysis can be found [here](https://colab.research.google.com/drive/1AQp1LNFSLEMws1RmlcKZZ7SPPrwfSD98).
- The video game sales dataset is available on Kaggle [here](https://www.kaggle.com/datasets/gregorut/videogamesales?resource=download).
- The GDP data by selected country can be accessed [here](https://data.oecd.org/gdp/gross-domestic-product-gdp.htm#indicator-chart).

Feel free to explore the full analysis in the provided Jupyter Notebook.
