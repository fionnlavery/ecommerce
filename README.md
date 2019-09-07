[![Build Status](https://travis-ci.org/fionnlavery/ecommerce.svg?branch=master)](https://travis-ci.org/fionnlavery/ecommerce)
## Interactive Recipe Website Website
Stream Four Project: Fullstack Development Milestone Project  - Code Institute

Access the  deployed website here: https://https://ecommerce-fl.herokuapp.com/
This website is a basic ecommerce site utilizing Django connected to postgres database.
It allows users to browse items for sale, add them to their cart and purchase them after registering and logging in.
It incluses an Admin dashboard where new products can be added to the website.

## UX
These are the user stories I came up with for the website:

- As a user I want to be able to browse the products available to see if I wish to purchase anything
 
- As a user I want to be able to see more details on a particular product to see if I wish to purchase it.

- As a user I want to be able I want to be able add the item to my cart

- As a user I want to be able register to save my cart to finish order later

- As a user I want to be able log in to retrieve my cart and complete my purchase

- As a user I want to be able easily see what my cart contains and see the total cost

- As a user I want to be able to remove products from my cart If they change there minds about a product

- As a user I want to be able to use my credit card to purchase the products in my cart
 
- As a user I want to be able to search via keyword for a specific product


The primary goal of this website is sell products.

## Features

A multi page website with
- Responsive layout and nav
- Home page which is automatically populated by Product entrys in the database
- Masthead slider showcasing the best products
- Product detail page is populated with the selected products details
- Register, login, logout, reset password functionality
- Stripe pay integration allows payment via credit card
- Shopping cart and checkout allows users to add products and purchase
- search functionality
- form validation
- messaging system shows if payments was processed and form validation

Django Backend
- Allows easy and user friendly admin functions
- New products can be added and edited by Admin

 
### Features Left to Implement
- search functionality
- filter by categories functionality
- Auction functionality

## Technologies Used

- This project uses HTML and CSS programming languages.
 
- [JQuery](https://jquery.com)
    - The website uses **JQuery** as part of the Materialize  components.

- [AWSCloud9](https://aws.amazon.com/cloud9/)
    - This developer used **AWS Cloud9** for their IDE while building the website.

- [Heroku](https://www.heroku.com)
  -The website uses the platform as a service (PaaS) **heroku** to automatically deploy the website
 

## Testing
- I clicked all links and ensured they went to the right location, I tested the browser on Firefox & Brave(Chromium fork). 
- I tested the responsive layout using Braves inbuilt dev tools
- I tested various inputs into the database to ensure they were entered correctly
- I entered various inputs into the forms to ensure they correctly dealt with the data
- I used Travis integration to check for compatibiliy issues

## Issues yet to be resolved



## Deployment

This website was deployed using heroku and you can check it out [here](https://flask-automatic-deploys-fl.herokuapp.com/)

### Media

- Recipe entrys were taken from BBC Recipes website
- Pixabay for royalty free slider images

### Acknowledgements

- I received inspiration for this project from Giulia and her amazing cooking
