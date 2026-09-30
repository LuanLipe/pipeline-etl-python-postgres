import psycopg2

# Connecting the script to the database
database_connect = psycopg2.connect(
    host="localhost",
    port="5432",
    database="sistema_vendas",
    user="admin_novo",
    password="123456"
)

# Creating a cursor to communicate with the database
cursor = database_connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales(
        id SERIAL PRIMARY KEY,
        customer VARCHAR(100) NOT NULL,
        amount NUMERIC(10,2) NOT NULL,
        email VARCHAR(100) NOT NULL
    );
""")

# Committing to save table creation
database_connect.commit()

# Creating a list with raw data simulating an Excel spreadsheet
excel_data = [
    {"customer": "MARCOS DILVA", "amount": "R$ 150,00", "email": "marcos@email.com"},
    {"customer": "ana souza", "amount": "R$ 89,90", "email": "ana@email.com"},
    {"customer": "Carlos Roberto", "amount": "R$ 300,00", "email": ""}  # no email
]

# Loop to process row by row
print("Starting data processing...")
for row in excel_data:

    # Checking if email exists
    if row["email"] != "":

        # Data cleansing and transformation
        
        # Format name capitalization
        clean_name = row['customer'].title()
        # Clean currency characters
        clean_amount = row['amount'].replace("R$", "").replace(",", ".")
        # Strip whitespace
        clean_amount = clean_amount.strip()
        clean_amount = float(clean_amount)

        cursor.execute("""
            INSERT INTO sales(customer, amount, email)
            VALUES (%s, %s, %s)
        """, (clean_name, clean_amount, row['email']))
        
        print(f"Saved to Postgres: {clean_name} | R$ {clean_amount:.2f}")
    
    else:
        print("Customer does not have a valid email")

database_connect.commit()
cursor.close()
database_connect.close()

print("Process finished successfully!")