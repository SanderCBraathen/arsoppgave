# Bakkedora - Simple Online Store

## Overview
Bakkedora is a simple web application for an online store that allows users to register, log in, browse products, add items to a shopping cart, and view their cart. The application is built using Flask, a lightweight Python web framework, and uses SQLite for data storage.

## Features
- **User Authentication**: Users can register, log in, and log out.
- **Product Browsing**: Users can view a list of products available in the store.
- **Shopping Cart**: Users can add products to their cart, view the cart, and see the total price.
- **Flash Messages**: Feedback is provided to users for actions like login success, errors, and cart updates.

## Project Structure

### Key Files
- **`app.py`**: The main application file containing all routes and logic.
- **`templates/`**: Contains HTML templates for rendering pages.
  - `index.html`: Homepage.
  - `login.html`: Login page.
  - `register.html`: Registration page.
  - `shop.html`: Product listing page.
  - `cart.html`: Shopping cart page.
- **`static/`**: Contains static assets like CSS and JavaScript.
  - `style.css`: Styles for the application.
  - `script.js`: JavaScript for client-side interactions.

## Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install flask
python app.py

## Universal Website Design Principles for Online Stores

When designing an online store, it is essential to follow universal design principles to ensure usability, accessibility, and a seamless user experience. Below are some key principles:

### 1. **User-Centered Design**
   - Focus on the needs and behaviors of your target audience.
   - Ensure the interface is intuitive and easy to navigate.

### 2. **Responsive Design**
   - Make the website mobile-friendly to accommodate users on different devices.
   - Use flexible layouts and media queries to adapt to various screen sizes.

### 3. **Accessibility**
   - Follow accessibility standards (e.g., WCAG) to ensure the website is usable for people with disabilities.
   - Provide alt text for images, keyboard navigation, and proper color contrast.

### 4. **Clear Navigation**
   - Use a consistent navigation bar with links to key pages (e.g., Home, Shop, Cart, Login).
   - Include a search bar for quick access to products.

### 5. **Fast Loading Times**
   - Optimize images and minimize the use of large scripts to improve page load speed.
   - Use caching and a Content Delivery Network (CDN) for better performance.

### 6. **Trust and Security**
   - Display trust signals like SSL certificates, secure payment options, and customer reviews.
   - Ensure user data is protected with encryption and secure authentication methods.

### 7. **Call-to-Action (CTA) Buttons**
   - Use clear and prominent CTAs like "Add to Cart," "Buy Now," or "Register."
   - Ensure CTAs are visually distinct and easy to click.

---

## Simple Usage of Other Online Stores

### Amazon
- **Search and Browse**: Use the search bar or categories to find products.
- **Add to Cart**: Click "Add to Cart" to save items for later purchase.
- **Checkout**: Proceed to checkout, enter shipping details, and complete payment.

### eBay
- **Bidding and Buying**: Place bids on auction items or use "Buy It Now" for instant purchases.
- **Seller Ratings**: Check seller ratings and reviews before purchasing.
- **Payment**: Use PayPal or other supported payment methods for secure transactions.

### Shopify-Based Stores
- **Product Pages**: View detailed product descriptions, images, and reviews.
- **Cart Management**: Add items to the cart and adjust quantities before checkout.
- **Mobile Experience**: Most Shopify stores are optimized for mobile devices.

### Etsy
- **Handmade and Vintage Items**: Browse unique, handcrafted, or vintage products.
- **Shop Profiles**: Learn about individual sellers and their stories.
- **Customization**: Many items allow for personalization or custom orders.

---

By incorporating these universal design principles and understanding the common features of popular online stores, you can create a user-friendly and competitive e-commerce platform.

## Updates

### Fixed Missing CSS in `index.html`
- Added a `<link>` tag in the `<head>` section of `index.html` to connect the `style.css` file.
- This ensures that the homepage now correctly applies the CSS styles.

### Improved Product Layout in `shop.html`
- Added CSS rules to ensure all product items have the same height.
- Aligned the "Buy" button consistently at the bottom of each product item.
- This improves the visual consistency of the product listing page.

### Made `shop.html` Scrollable with a Fixed Header
- Updated the CSS to set the header as `position: fixed` so it remains visible at the top while scrolling.
- Added padding to the `body` to prevent content from being hidden under the fixed header.
- Ensured the `shop` section has proper spacing for a better user experience.

### Improved Spacing in `shop.html`
- Increased the top padding of the `.shop` section in `style.css` to 60px.
- This change ensures that the text in the shop section has more space from the header, making it look less cramped.