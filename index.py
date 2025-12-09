import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Mock product data
# -----------------------------
products = [
    {"name": "iPhone 15", "seller": "Amazon", "price": 79999, "discount": 10, "rating": 4.5, "link": "https://amazon.in/iphone15"},
    {"name": "iPhone 15", "seller": "Flipkart", "price": 80499, "discount": 5, "rating": 4.3, "link": "https://flipkart.com/iphone15"},
    {"name": "iPhone 15", "seller": "Croma", "price": 81000, "discount": 0, "rating": 4.0, "link": "https://croma.com/iphone15"},
    {"name": "iPhone 15 Pro", "seller": "Amazon", "price": 77999, "discount": 12, "rating": 4.6, "link": "https://amazon.in/iphone15pro"},
    {"name": "Samsung Galaxy S25", "seller": "Flipkart", "price": 76999, "discount": 8, "rating": 4.4, "link": "https://flipkart.com/galaxys25"},
]

df = pd.DataFrame(products)

# -----------------------------
# 1️⃣ Search Product
# -----------------------------
search_product = input("Enter product name to search: ")

search_results = df[df['name'].str.contains(search_product, case=False)]
if search_results.empty:
    print("\n❌ No products found.")
else:
    print("\n🔹 Search Results / Product Comparison Table 🔹")
    print(search_results[['name', 'seller', 'price', 'discount', 'rating', 'link']])

    # -----------------------------
    # 2️⃣ Best Deal Detection
    # -----------------------------
    best_deal = search_results.loc[search_results['price'].idxmin()]
    print(f"\n💰 Best Deal → {best_deal['name']} from {best_deal['seller']} at ₹{best_deal['price']}")

    # -----------------------------
    # 3️⃣ Discount Analysis
    # -----------------------------
    print("\n🔹 Discount Analysis 🔹")
    for _, row in search_results.iterrows():
        if row['discount'] > 5:
            print(f"{row['seller']}: ✔ Genuine Discount ({row['discount']}%)")
        else:
            print(f"{row['seller']}: ⚠ Suspicious/Low Discount ({row['discount']}%)")

    # -----------------------------
    # 4️⃣ Alternative Recommendations
    # -----------------------------
    alt_products = df[~df['name'].str.contains(search_product, case=False)]
    if not alt_products.empty:
        print("\n🔹 Alternative Recommendations 🔹")
        for _, row in alt_products.iterrows():
            print(f"- {row['name']} – ₹{row['price']}")

    # -----------------------------
    # 5️⃣ Price Trend (Mock)
    # -----------------------------
    price_history = [85000, 83000, 81000, best_deal['price']]
    dates = ["Oct", "Nov", "Dec", "Today"]

    plt.plot(dates, price_history, marker='o')
    plt.title(f"Price Trend of {search_product}")
    plt.xlabel("Month")
    plt.ylabel("Price (₹)")
    plt.grid(True)
    plt.show()

    # -----------------------------
    # 6️⃣ Price Drop Alert
    # -----------------------------
    alert_price = 80000
    if best_deal['price'] <= alert_price:
        print(f"\n🔔 Price Alert: {best_deal['name']} dropped to ₹{best_deal['price']} on {best_deal['seller']}!")

# -----------------------------
# 7️⃣ Summary Panel
# -----------------------------
print("\n📊 Summary Panel / Dashboard")
print(f"Tracked Products: 5")
print(f"Total Savings: ₹3200")
print(f"Top Deal Today: Samsung Galaxy S25 – ₹76,999")