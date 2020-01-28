# Racquets a Django powered online tennis racqquet shop app

[Racquets](https://racquet-shop.herokuapp.com/) is a fictional tennis racquet shop that allows tennis lovers to browse the racquets of past champions, with a wide variety of racquets available, from wood to metal, hybrid, graphite composite and modern frames. Many of the items on display are collectors items, and the website would appeal to both tennis enthusiasts and collectors alike.

# Table of Contents

- [UX and Design Planning](#ux-and-design-planning)
	- [Wireframes](#wireframes)
	- [Project Design Summary](#project-design-summary)
	- [User Stories](#user-stories)
	- [App Content](#app-content)
	- [App Style](#app-style)
- [Features](#features)
- [Features to be implemented](#features-to-be-implemented)
- [Technologies Used](#technologies-used)
- [Resources](#resources)
- [Testing](#testing)
- [Further testing](#further-testing)
- [Bugs and known issues](#bugs-and-known-issues)
- [Content credits](#content-credits)
- [Acknowledgements](#acknowledgements)
- [Deployment](#deployment)
	- [Local Deployment](#local-deployment)
	- [Remote Deployment](#remote-deployment)

 ## UX and Design Planning 

Please view the [project strategy document](planning.md) for the app, which details the project strategy, including the project planning of the UX and UI, scope, structure, skeleton and surface. 

### Wireframes

The wireframes for the project, created with [Balsamiq](https://balsamiq.com/), can be found [here](https://github.com/ey7/project-four/tree/master/wireframes)

### Project Design Summary

- The app will be a fully functional django powered online vintage tennis equipment shop. Users will have the chance to register for a seamlesss shopping experience.
- Products will be displayed as attractive cards with interesting descriptive content on the product pages.
- Users can add items to their cart as they browse the site.
- The app will have a shopping cart page, where users can view the items in their cart.
- Further shopping pages of address and shipping details will allows purchasers to enter their personal information.
- A special payment page will handle all payments, which will be implemented in the backend by Stripe.
- Once payment is succcessful, a payment confirmation page will appear with shop contact details.
- The app will have full user registration, authorization and authentication functionality with hashed passwords.
- Search functionality with a searchbox will be implemented on the products page.
- Pagination will be implemented on the products page to limit the number of visible entries.

### User Stories

- As a user, I want to be able to browse vintage tennis racquets and read about their history.
- As a user, I want to be able to navigate easily around the site and find the information I need.
- As a user, I want to be able to register easily to make purchases if I wish, with my contact and shipping details.
- As a user, I want to be able to easily edit my personal information on my account page.
- As a user, I want proper security and peace of mind when making online purchases.
- As a user, I want a good user experience when browsing the website and making purchases, for a hassle free online shopping experience.
- As a user, I want a well designed, logical shopping flow from cart through to checkout and payment.
- As a user, I want well designed shopping pages that clearly detail taxes, surcharges and shipping costs included in the total price.
- As a user, I want to be able to make an easy hassle free purchase with my credit card or paypal.
- As a user, I want to be able to easily add and remove items from my shopping cart.
- As a user, I want to be able to easily add and edit my contact, address and shipping details.
- As a user, I want a confirmation page after I successfully make a purchase.
- As a user, I want to be able to easily find contact information if I wish to make product enquiries.

### App Content

The app consists of over 10 pages relating to app functionality, such as home, about, account, login, register, search, as well as pages relating to the online shop, such as cart, address, shipping, payment and payment confirmation.

### App Style 

- A primary colour of orange with a secondary colour of blue on the buttons and product cards throughout for visual consistency.
- A modern sans serif font of Exo 2.
- An off white background with dark grey text for optimum readability.
- To improve the UX, I used SVG icons from [Zondicons](https://www.zondicons.com/) throughout the site. In my opinion, SVG icons look crisper and are easier to work with than font icons. When placed inline they are easier to style and manipulate for hover colour change effects, and they also load on the page much faster than font icons. 

## Features

### Navbar

The navbar is displayed on all pages. When logged out, it displays links to home, shop, about, login, register, contact, search and cart. Only logged in users can add items to cart.
When logged in, all navbar links are the same, except that login is replaced by an account link, and the register link is replaced by a logout link for the user to log out.

### Home page

The home page uses an attractive sliding carousel with a selection of three product images with links. Below the carousel is a brief description of what the website is about, with two buttons that link to the shop and the about page. Below the buttons, a selection of random product cards (x6) is displayed to the customer. Every time the home page is visited or refreshed, a new selection is available.

### Shop

The shop link in the navbar provides a dropdown of options, from all racquets to the five categories of wood, metal, oversize, graphite and modern racquets. The all racquets page displays all products with product cards, with pagination to limit the number of products displayed to 6. Clicking on a category page will display the products for that category.

### Product list or all racquets pages

The product list pages display all shop products through the use of cards with images, links and price, paginated by 6 per page. On each product is an add to cart buttton, whihc will add the product to the users card, but only if they are logged in. There are numbered buttons and next and previous buttons to allow the user to browse the various product pages.

### Product detail or individual product pages

If a user clicks on the title on any product card, it acts as a link to the individual product detail page which has a more detailed description of the product on offer. An add to cart button on the product card entices the user to add the item to their cart.

### Cart 

When a user is logged in and hits an add to cart button on any item, the item will be added to their cart. If the cart is not empty, a badge will display beside the cart icon in the navbar, displaying the product count and number of items in their cart. Clicking the cart button in the navbar will bring the user to their cart page. If not logged in, they will be redirected to the login page. If logged in, the users cart items will be displayed as product cards. On each cart item card, there will be three buttons to modify the cart. A plus button allows the user to increment the quantity for that particular item. A minus button will decrement the quantity. A third button on each cart item will allow the user to remove all of that particular item from the cart. On each cart item will be badges displaying clearly the quantity. A cart product total and total price will display underneath, along with a checkout button. 

### Checkout

The checkout page will display any cart items for checkout at the top of the page. Underneath there are forms for payment, one form for billing address details and the other for payment details such as credit card. Once both forms are completed, the user can click the buy now button at the bottom. Once both forms validate with no errors, credit card payment will be handled in the backend with Stripe. If sucessfull, the user will be redirected to the payment confirmation page with a success alert message. Errors will be displayed as alert messages and the user will be asked to re-enter their details. 

### Payment confirmation

This page will appear after a sucessful payment transaction, and will tell the user that their payment was sucessful. The user will be thanked for shopping with the website, and a link to the shop and contact page is available.

### Register

A user may register to use the site by entering their username, email and password. They must also confirm their password in a fourth field before validation. Once the form is validated and there is no duplicate username in the database, the new user is created with a success message alert and will be redirected to the login page.

### Login

A user may log into the app by entering their username and password. Once the form is validated with no errors, the user is logged in with a success message alert and redirection to the home page.

### Logout

Once logged in, a user may logout of the app at any time by clicking on the logout button in the navbar. This logs the user out with a success message alert and a redirect to the homepage.

### Account

Once logged in, the user may access a page that welcomes them with their username and gives them the option to update their username and email. Once the form is validated with no errors, the username and email will be updated in the database. Due to time constraints, password reset was not implemented.

### About

The about page contains an image of a tennis player, racquet in hand, along with a brief description of what the website is all about, the sale of vintage tennis racquets. At the bottom of the page is a link to the shop, where users can browse the products available.

### Contact

A contact page gives the user the ability to send a message to the shop owner. There are fields for name, email and message. All are required and once the form is validated with no errors, the app uses EmailJS in the background to redirect the message to the shop owner's email account. An alert modal will display on the screen to tell the user of success, or failure in the case of errors. 

### Search

The user may start a search by clicking on the search icon in the navbar. This brings up the search page with a search box at the top. The search operates by searching on title and category fields in the products database and will return matches in the form of product cards with images and links. The links will bring the user to the individual product detail page where more information is available.

## Features to be implemented

- Password reset: I would like to implement this useful feature for customers. It was not implemented due to time constraints.
- Paypal payment: At present there is only credit card payment through Stripe available on the site. Many people enjoy the convenience of paypal.
- Dispatch email: Similar to password reset, this would be a very useful feature which would notify the customer when their product was dispatched.
- Custom error pages: Django has very basic error pages for 404 and 500 errors for example. It would be nice to implement custom error pages with back links. 

## Technologies Used

- HTML and CSS for website layout and design.
- [Bootstrap](https://getbootstrap.com/) for modern styling with responsive navigation, forms and buttons. 
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/javascript) for site functionality.
- [Jquery](https://jquery.com/) and [Popper Js](https://popper.js.org/) for Bootstrap functionality.
- [Google fonts](https://fonts.google.com/) for fast loading of modern fonts.
- Git for version control and [Github](https://github.com/) for repository hosting.
- [EmailJS](https://www.emailjs.com/) for transfer of emails from contact form to personal email.
- [Cloudinary](https://www.cloudinary.com/) to host uploaded images for products.
- [Heroku](https://heroku.com/) to host the site.
- [Balsamiq](https://balsamiq.com/) for mock ups of the site.
- [Postgres](https://postgresql.org) for database functionality.
- [Stripe](https://stripe.com/) for online payment processing.
- [Zondicons](https://www.zondicons.com/) for modern SVG icons.
  
## Resources

- [Stackoverflow](https://stackoverflow.com/)
- [MDN Mozilla Docs](https://developer.mozilla.org/en-US/)
- [W3 Schools](https://www.w3schools.com/)
- [CSS Tricks](https://css-tricks.com/)
- [Django Documentation](https://docs.djangoproject.com/en/2.2/)
- [Python Docs](https://docs.python.org)
- [YouTube](https://www.youtube.com)
- [Responsinator](https://www.responsinator.com/)
- [Am I Responsive](http://ami.responsivedesign.is/)
- Google
  
## Testing

### Further testing

## Bugs and known issues

## Content credits

## Acknowledgements

## Deployment

### Local Deployment

To deploy locally, firstly you need the following:

- A code editor such as Visual Studio Code, Sublime Text, Atom or another of your choosing.

You must have the the following installed on your machine:

- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://www.python.org/downloads/)
- [GIT](https://git-scm.com/downloads)

### Instructions

1. Save a copy of the github repository located at https://github.com/ey7/project-four by clicking the "download zip" button at the top of the page and extracting the zip file to your download folder. If you have Git installed on your machine, you can clone the repository with the following command:

`git clone https://github.com/ey7/project-four`

- More instructions to follow.....watch this space.......

### Remote Deployment

- The app can be deployed to Heroku. Do the following:

1. In the terminal, create a `requirements.txt` file using the command `pip freeze > requirements.txt`

2. In the terminal, create a Procfile by running the `echo web: python app.py > Procfile` command.

3. Push these files along with the project to your GitHub repository.

4. Create a new app on [Heroku dashboard](https://dashboard.heroku.com/apps), give it a name and set the region to whichever is closest to you.

5. From the Heroku dashboard of your app, click on "Deploy" > "Deployment method" and select GitHub.

6. Confirm the linking of the Heroku app to the correct GitHub repository.

7. In the Heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

Set the following config vars: 

- More instructions to follow.....watch this space.......

## Notice

This project is for educational use only.