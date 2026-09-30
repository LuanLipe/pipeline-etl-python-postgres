# ETL Pipeline with Python and PostgreSQL

Data Engineering pipeline developed to extract raw data, perform transformation and data cleansing (string standardization, type conversion, and email validation filtering), and securely load the data into a PostgreSQL relational database.

## 🛠 Technologies Used
- **Python** (`psycopg2`)
- **PostgreSQL**
- **pgAdmin 4**
- **VS Code**

## 🚀 How to Run
1. Clone this repository.
2. Make sure you have PostgreSQL running locally and create a database named `sistema_vendas`.
3. Update your connection credentials in the `app.py` script.
4. Run the script:
   ```bash
   python app.py