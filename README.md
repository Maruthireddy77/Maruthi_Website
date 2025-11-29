# Maruthi’s Smart Buy

**Maruthi’s Smart Buy** is a simple web application built with **Python, Flask, SQLite, and Bootstrap** that automatically scrapes product data from online stores (currently using Books to Scrape for demo) and displays them in a user-friendly, responsive interface. It supports **product images, search, sorting, and pagination**.

---

## Features (Implemented So Far)

* Automatic scraping of products from the web
* Stores scraped data in a SQLite database
* Displays product title, price, link, and image
* Search products by name
* Price sorting (Low → High, High → Low)
* Pagination (10 products per page)
* Responsive Bootstrap design for a clean UI

---

## Project Structure

```
Maruthi_Website/
│
├─ app.py               # Main Flask app
├─ database.db          # SQLite database (auto-created)
├─ scrapper.py          # Scraper script to fetch products
├─ init_db.py           # Creates the initial products table
├─ templates/
│   ├─ home.html        # Main page with products, search, sort, pagination
│   └─ products.html    # Secondary template for products view (currently same as home)
└─ static/              # Optional: store static files (images, CSS, JS)
```

---

## Requirements

* Python 3.x
* Flask
* Requests
* BeautifulSoup4

Install dependencies using:

```bash
pip install flask requests beautifulsoup4
```

---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone <your-repo-url>
cd Maruthi_Website
```

2. **Create the database:**

```bash
python init_db.py
```

3. **Scrape products:**

```bash
python scrapper.py
```

* This will **clear old data** and fetch new products along with images.

4. **Run the Flask application:**

```bash
python app.py
```

* Open your browser at: `http://127.0.0.1:5000`

---

## How It Works

* `scrapper.py` fetches products from online stores and stores them in `database.db`.
* `app.py` reads products from the database and renders them using `home.html` (or `products.html` if used).
* Bootstrap handles the UI, showing **cards with product images, titles, prices, and links**.
* Search and sorting options filter products dynamically.
* Pagination allows navigating large product lists easily.

---

## Next Steps / Future Features

* Add multiple website scrapers (Flipkart, Amazon, Meesho, etc.)
* Add categories and filters
* Add “Refresh Products” button on the UI
* Add user accounts or wishlist
* Deploy online with a custom domain

---

## Notes

* Current setup uses **Books to Scrape** as demo products.
* Images and links are directly scraped and displayed.
* Search and sorting work without needing categories.


Do you want me to do that?
