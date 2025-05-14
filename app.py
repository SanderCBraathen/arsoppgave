import sqlite3
import hashlib
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flash messages and sessions

# Database initialization
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  username TEXT UNIQUE NOT NULL, 
                  first_name TEXT NOT NULL, 
                  last_name TEXT NOT NULL, 
                  email TEXT UNIQUE NOT NULL, 
                  password_hash TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Hash password using SHA-256 (simple, no salt for demo)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Initialize database on first run
init_db()

@app.route('/')
def home():
    first_name = None
    if 'email' in session:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT first_name FROM users WHERE email = ?", (session['email'],))
        user = c.fetchone()
        if user:
            first_name = user[0]
        conn.close()
    return render_template('index.html', first_name=first_name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password_hash = hash_password(password)

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = c.fetchone()

        if user:
            stored_password_hash = user[5]
            if stored_password_hash == password_hash:
                session['email'] = email
                flash('Logget inn vellykket!', 'success')
                conn.close()
                return redirect(url_for('home'))
            else:
                flash('Feil passord!', 'error')
        else:
            flash('E-posten finnes ikke!', 'error')

        conn.close()

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        password_hash = hash_password(password)
        username = email.split('@')[0]

        if not all([first_name, last_name, email, password]):
            flash('Alle felter må fylles ut!', 'error')
            return render_template('register.html')

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        if c.fetchone():
            flash('E-posten er allerede i bruk!', 'error')
            conn.close()
            return render_template('register.html')

        try:
            c.execute("INSERT INTO users (username, first_name, last_name, email, password_hash) VALUES (?, ?, ?, ?, ?)", 
                      (username, first_name, last_name, email, password_hash))
            conn.commit()
            flash('Konto opprettet! Logg inn nå.', 'success')
            conn.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Brukernavn eller e-post er allerede i bruk!', 'error')

        conn.close()

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    flash('Logget ut!', 'success')
    return redirect(url_for('home'))

@app.route('/shop', methods=['GET', 'POST'])
def shop():
    products = [
        {"id": 1, "name": "Cola 0,5L", "price": 15, "description": "Forfriskende cola uten sukker."},
        {"id": 2, "name": "Fanta 0,5L", "price": 15, "description": "Fruktig appelsinsmak."},
        {"id": 3, "name": "Sprite 0,5L", "price": 15, "description": "Sitron- og limesmak."},
    ]
    first_name = None
    if 'email' in session:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT first_name FROM users WHERE email = ?", (session['email'],))
        user = c.fetchone()
        if user:
            first_name = user[0]
        conn.close()

    # Initialize cart if not present
    if 'cart' not in session:
        session['cart'] = {}

    # Handle adding to cart
    if request.method == 'POST':
        product_id = request.form['product_id']
        quantity = int(request.form.get('quantity', 1))  # Default to 1 if not specified
        product = next((p for p in products if str(p['id']) == product_id), None)
        if product:
            if product_id in session['cart']:
                session['cart'][product_id]['quantity'] += quantity
            else:
                session['cart'][product_id] = {
                    'name': product['name'],
                    'price': product['price'],
                    'quantity': quantity
                }
            session.modified = True  # Mark session as modified
            flash(f"{product['name']} lagt til i handlekurven!", 'success')
        return redirect(url_for('shop'))

    return render_template('shop.html', products=products, first_name=first_name)

@app.route('/cart')
def cart():
    first_name = None
    if 'email' in session:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT first_name FROM users WHERE email = ?", (session['email'],))
        user = c.fetchone()
        if user:
            first_name = user[0]
        conn.close()

    cart_items = session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart_items.values())
    return render_template('cart.html', cart_items=cart_items, total=total, first_name=first_name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)