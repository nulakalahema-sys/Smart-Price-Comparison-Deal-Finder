### Project Name

**Smart Price Sentinel** (or **PriceTrack Pro**)

### Overview

**Smart Price Sentinel** is a Python-based tool designed to demonstrate the core functionality of a product price comparison and deal detection engine. It uses the `pandas` library for data manipulation and `matplotlib` for basic price trend visualization.

The current implementation uses **mock data** to simulate the results of a web-scraping operation, comparing different sellers' prices, discounts, and ratings for a given product.

### Features

1.  **Product Search:** Allows a user to search for a product and displays a comparison table of all matching offers from different sellers.
2.  **Best Deal Detection:** Automatically identifies the offer with the lowest price among the search results.
3.  **Discount Analysis:** Flags offers with low or zero discounts (below a set threshold of 5%) as potentially "suspicious" for users to review.
4.  **Alternative Recommendations:** Suggests other products (from the mock dataset) not matching the search query as alternatives.
5.  **Price Trend Visualization (Mock):** Generates a simple line plot using mock historical data to illustrate the price movement over time, aiding in the decision to buy now or wait.
6.  **Price Drop Alert:** Notifies the user if the best price for the searched product meets or falls below a predefined alert price threshold.
7.  **Summary Dashboard:** Provides a quick overview of tracking statistics (Total Products, Savings, Top Deals).

### Dependencies

This script requires the following Python libraries:

  * **`pandas`**: For efficient data handling and manipulation (DataFrames).
  * **`matplotlib`**: For plotting the price trend visualization.

You can install them using pip:

```bash
pip install pandas matplotlib
```

### How to Run the Script

1.  Save the provided code snippet as a Python file (e.g., `price_sentinel.py`).

2.  Run the script from your terminal:

    ```bash
    python price_sentinel.py
    ```

3.  The script will prompt you to **"Enter product name to search:"** (e.g., "iPhone 15" or "S25").

4.  The output will display the comparison table, best deal, analysis, and the price trend plot will open in a new window .

### Code Sections Explained

| Section | Purpose | Logic Used |
| :--- | :--- | :--- |
| **Data Setup** | Creates a `pandas DataFrame` from a list of dictionaries to simulate product offers. | `pd.DataFrame()` |
| **1️⃣ Search Product** | Filters the DataFrame based on user input. | `df['name'].str.contains(search_product, case=False)` |
| **2️⃣ Best Deal Detection** | Finds the row with the minimum value in the 'price' column. | `search_results['price'].idxmin()` |
| **3️⃣ Discount Analysis** | Iterates through results to check if the discount is greater than 5%. | Standard `if/else` loop. |
| **4️⃣ Alternative Recommendations** | Filters the original DataFrame for products *not* in the search results. | Boolean negation (`~`) on the search filter. |
| **5️⃣ Price Trend (Mock)** | Creates and displays a simple line plot for visual historical price tracking. | `matplotlib.pyplot.plot()` |
| **6️⃣ Price Drop Alert** | Checks if the best found price is less than or equal to a set alert value (₹80,000). | Standard `if` condition. |

### Future Enhancements

  * **Real Web Scraping:** Integrate libraries like `BeautifulSoup` or `Scrapy` to fetch real, live data from e-commerce websites.
  * **Advanced Calculation:** Calculate the **effective price** after applying the discount.
  * **User Interface:** Develop a simple web interface (e.g., with Flask or Streamlit) for better user interaction.
  * **Database Integration:** Store historical data in a database (e.g., SQLite, PostgreSQL) for persistent tracking and better trend analysis.
