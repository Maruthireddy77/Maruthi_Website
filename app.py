from flask import Flask, render_template, request
import sqlite3
import math

app = Flask(__name__)

# Fetch products with filters
def get_products(search="", sort="", page=1, per_page=10):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    query = "SELECT title, price, link, image_link, price_num FROM products WHERE 1=1"
    params = []

    if search:
        query += " AND title LIKE ?"
        params.append(f"%{search}%")

    # Sorting
    if sort == "low":
        query += " ORDER BY price_num ASC"
    elif sort == "high":
        query += " ORDER BY price_num DESC"

    # Pagination
    offset = (page - 1) * per_page
    query += " LIMIT ? OFFSET ?"
    params.append(per_page)
    params.append(offset)

    cursor.execute(query, params)
    products = cursor.fetchall()

    # Total rows with same filters
    count_query = "SELECT COUNT(*) FROM products WHERE 1=1"
    count_params = []

    if search:
        count_query += " AND title LIKE ?"
        count_params.append(f"%{search}%")

    cursor.execute(count_query, count_params)
    total = cursor.fetchone()[0]

    conn.close()
    return products, total


    cursor.execute(query, params)
    products = cursor.fetchall()

    # Total count for pagination
    count_query = "SELECT COUNT(*) FROM products WHERE 1=1"
    count_params = []

    if search:
        count_query += " AND title LIKE ?"
        count_params.append(f"%{search}%")

    cursor.execute(count_query, count_params)

    total = cursor.fetchone()[0]

    conn.close()

    return products, total


@app.route("/")
def home():
    search = request.args.get("search", "")
    sort = request.args.get("sort", "")
    page = int(request.args.get("page", 1))

    products, total = get_products(search, sort, page)

    # total pages
    per_page = 10
    total_pages = math.ceil(total / per_page)

    return render_template("home.html",
                           products=products,
                           search=search,
                           sort=sort,
                           page=page,
                           total_pages=total_pages)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

