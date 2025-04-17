# 📈 Stock Price Tracker Web App

A simple and interactive **Flask-based web application** that allows users to fetch and view real-time stock prices using the **Alpha Vantage API**. Users can input a stock symbol (like AAPL, GOOGL, etc.) and instantly get the latest price and timestamp.

---

## 🚀 Features

- 🔎 Search for any valid stock symbol.
- ⏱ Fetches latest stock prices at **5-minute intervals**.
- ❗ Error messages for:
  - Invalid or unsupported symbols.
  - API rate limit exceeded.

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Flask** (Web Framework)
- **Requests** (for API calls)
- **Alpha Vantage API** (for real-time stock data)
- **HTML + Bootstrap** (in `templates/index.html` for the UI)

---

## 📦 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/stock-price-tracker.git
cd stock-price-tracker
Step 2: Install Dependencies
Make sure you have Python installed. Then install Flask and Requests:

bash
Copy
Edit
pip install flask requests
Step 3: Add Your API Key
Replace the placeholder API key in app.py with your own from Alpha Vantage:

python
Copy
Edit
API_KEY = "YOUR_ACTUAL_ALPHA_VANTAGE_API_KEY"
▶️ How to Run the App
Once everything is set up, run the app using:

bash
Copy
Edit
python app.py
By default, it will run at http://127.0.0.1:5000/.

Open that URL in your browser, and you’ll see your stock tracker interface.

📊 How It Works
User enters a stock symbol like AAPL (Apple).

A GET request is sent to:

bash
Copy
Edit
/get_stock_price?symbol=AAPL
Flask sends a request to Alpha Vantage API to fetch the latest 5-minute interval data.

The app parses the JSON response and returns:

✅ Stock Symbol (in uppercase)

💰 Latest Price

🕓 Timestamp

✅ Example Response (JSON)
json
Copy
Edit
{
  "success": true,
  "symbol": "AAPL",
  "price": "170.35",
  "time": "2025-04-17 15:00:00"
}
🧠 Error Handling
The app smartly handles:

No stock symbol provided:

json
Copy
Edit
{"success": false, "message": "No stock symbol provided"}
Invalid or unsupported symbol:

json
Copy
Edit
{"success": false, "message": "Invalid or unsupported stock symbol."}
API Rate Limit exceeded:

json
Copy
Edit
{"success": false, "message": "API rate limit exceeded. Try again later."}
These messages are shown in the UI or console, making it easy for the user to understand what went wrong.

🧪 Testing the API
To manually test the API, open your browser or use a tool like Postman and try:

arduino
Copy
Edit
http://127.0.0.1:5000/get_stock_price?symbol=MSFT
You should receive the JSON response for Microsoft stock.
