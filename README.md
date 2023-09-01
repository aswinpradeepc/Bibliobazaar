# Bibliobazaar - Ecommerce Book Selling Website

Bibliobazaar is an e-commerce book-selling website developed using Django, designed to provide a seamless experience for buying and selling books online. This README provides an overview of the project, its features, and how to set it up.

## Features

1. **User Authentication**:
   - Users can register and login

2. **Book Catalog**:
   - Browse and search a wide selection of books.
   - View book details, including title, author, price, and description.
   - Click on a book to get the detailed description of a book.

3. **Shopping Cart**:
   - Add books to the shopping cart.
   - Update cart contents (add or remove items).
   - Calculate the total price of items in the cart.

4. **Checkout**:
   - Secure checkout process for customers.
   - Enter shipping details and payment information.

5. **Payment Integration**:
   - Integration with Razorpay for secure and convenient payments.
   - Supports various payment methods.

6. **Request a Book**:
   - Users can request books that are not available on the website.
   - Admin can review and add requested books to the catalog.

7. **Buy and Sell Used Books**:
   - Users can sell their used books to Bibliobazaar.
   - Customers can purchase used books from other users.

## Getting Started

Follow these steps to set up and run Bibliobazaar on your local environment:

1. Clone the repository

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Payment Integration with Razorpay:
   - To enable payment integration with Razorpay, you must have a Razorpay account.
   - Obtain your Razorpay API credentials and paste them in the `settings.py` file.

5. Run database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser account:
   - You can log in as a superuser to manage the app using the Django admin panel.
   - Use the following command to create a superuser account:

     ```bash
     python manage.py createsuperuser
     ```

   - You can access the Django admin panel by visiting `http://localhost:8000/admin/` after starting the server.

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Visit [http://localhost:8000/](http://localhost:8000/) to explore and use the Bibliobazaar website.
