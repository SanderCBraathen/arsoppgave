# Braathen Retail - Simple Online Store

## Overview
Braathen Retail is a simple web application for an online store that allows users to register, log in, browse products, add items to a shopping cart, and view their cart. The application is built using Flask (Python) and uses SQLite for data storage.

## Features
- **User Registration:** Create a new user account with your name, email, and password.
- **User Login/Logout:** Log in with your email and password, or log out securely.
- **Product Browsing:** View a list of available products with descriptions and prices.
- **Shopping Cart:** Add products to your cart, view the cart, and see the total price.
- **Flash Messages:** Get feedback for actions like login, registration, and cart updates.

## Project Structure

### Key Files
- **`app.py`**: Main application file with all routes and logic.
- **`templates/`**: HTML templates for rendering pages.
  - `index.html`: Homepage.
  - `login.html`: Login page.
  - `register.html`: Registration page.
  - `shop.html`: Product listing page.
  - `cart.html`: Shopping cart page.
- **`static/`**: Static assets like CSS and JavaScript.
  - `style.css`: Styles for the application.
  - `script.js`: JavaScript for client-side interactions.

## Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Run the application:
   ```bash
   python app.py
   ```

## Website Pages

### Homepage (`index.html`)
- Welcome message and a button to start shopping.
- Login/logout button and user name if logged in.

### Registration (`register.html`)
- Form to create a new account (first name, last name, email, password).
- Link to login if already registered.

### Login (`login.html`)
- Form to log in with email and password.
- Link to registration if you don't have an account.

### Shop (`shop.html`)
- List of products with name, description, and price.
- Form to add products to the cart (choose quantity).
- Button to view cart.

### Cart (`cart.html`)
- List of items in your cart with quantity and total price.
- Button to proceed to checkout (not implemented).
- Button to continue shopping.

## Universal Website Design Principles Used

- **User-Centered Design:** Simple and intuitive navigation.
- **Responsive Design:** Mobile-friendly layout.
- **Accessibility:** Semantic HTML and clear labels.
- **Clear Navigation:** Consistent header and navigation buttons.
- **Fast Loading:** Minimal assets for quick load times.
- **Trust and Security:** User data stored securely, feedback on actions.
- **Call-to-Action Buttons:** Prominent buttons for main actions.

## Changelog

- **[2025-05-15]**: Changed the "Braathen Retail" header link style so it no longer appears blue or underlined, making it look like normal text while keeping navigation functionality.
- **[2025-05-15]**: Updated the "Braathen Retail" header link so the cursor shows as a pointer (clickable) when hovered.
- **[2025-05-15]**: Added margin and padding to header text and login/logout button for better spacing from screen edges.
- **[2025-05-15]**: Improved the login/logout button style and spacing in the header for all pages for a more consistent and modern look.
- **[2025-05-15]**: Fixed header and login/logout button clipping issue by updating header layout and adding responsive styles.
- **[2025-05-15]**: Changed the login/logout button to display the logged-in user's name instead of "Logg ut" when logged in, on all pages.
- **[2025-05-15]**: Added a dropdown menu to the username button in the header. Clicking the username now shows a "Logg ut" option to prevent accidental logouts.
- **[2025-05-15]**: Fixed and improved the dropdown on the login button (username) so it opens and closes correctly and is styled/positioned properly.

---

By following these principles and providing the above features, Braathen Retail offers a simple and user-friendly online shopping experience.