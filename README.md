

## Shopify
Shopify app is a ecommerce application where users can purchase the products and admins can sale that products.

## Features

### User Registration:
Users can create accounts by providing their email and password.

### User Login:
Registered users can log in securely to access their accounts

### Password Change
Users have the option to change their passwords when needed.

### Admin Product Management:
Admin users can add new products to the catalog, specifying details such as title, description, price, brand, category, and uploading product images.

### Product Listings:
Users can view a list of available products, including details like title, price, and product image.

### Product Details:
Users can click on a product to view its detailed information, including description and discounted price.

### Adding to Cart: 
Users can add products to their shopping carts.

### Cart Quantity Modification: 
Users can easily increase or decrease the quantity of products in their cart.

### Removing from Cart: 
Users can remove products from their cart, with the cart total updating in real-time based on the quantity and price changes.

### Multiple Address Storage:
Users can store multiple delivery addresses in their profiles for easy selection during checkout.

### Selecting Delivery Address: 
During the order placement process, users can choose from their stored delivery addresses.

###  Order Placement: 
Users can place orders for the products in their shopping carts.

### Order History:
Users can view a history of their past orders, including order details, status, and delivery information.

### Order Status Tracking:
Users can check the status of their orders (e.g., pending, accepted, dispatched, delivered).

### Real-time Price Update: 
The order total updates in real-time as users modify the quantity or products in their cart.

### Order Status Update: 
Admin users can update the status of orders (e.g., from accepted to dispatched).

## Architecture Design
<img src="https://res.cloudinary.com/dpzk9bdae/image/upload/v1695482209/media/shopify_nkse9u.png" alt="Architecture" border="0" />


## Deployment
### Local Deployment
To create a local copy of this project, follow these steps:
1. Clone the project's repository by running the following command in your terminal:
```
git clone https://github.com/shahbakhat/shopify
```
2. Set up a virtual environment and install the project dependencies by running the following commands:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
3. Create a file named `.env` in the project's root directory and add the necessary environment variables, such as database connection details and API keys.

4. Run the development server with the following command:
```
python manage.py runserver
```
5. Access the website locally by visiting `http://localhost:8000` in your web browser.

