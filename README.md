# Django powered online shop app

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

The app consists of over 10 pages relating to app functionality, such as home, about, account, login, register, search and custom error pages, as well as pages relating to the online shop, such as cart, address, shipping, payment and payment confirmation.

### App Style 

- A primary colour with secondary colours throughout for visual consistency.
- A modern sans serif font of Exo 2.
- An off white background with dark grey text for optimum readability.
- To improve the UX, I plan to use SVG icons throughout the site. In my opinion, SVG icons look crisper and are easier to work with than font icons. When placed inline they are easier to style, and they also load on the page much faster than font icons. 

## Features

## Features to be implemented

## Technologies Used

- HTML and CSS for website layout and design.
- [Bootstrap](https://getbootstrap.com/) for modern styling with responsive navigation, forms and buttons. 
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/javascript) for site functionality.
- [Jquery](https://jquery.com/) and [Popper Js](https://popper.js.org/) for Bootstrap functionality.
- [Google fonts](https://fonts.google.com/) for fast loading of modern fonts.
- Git for version control and [Github](https://github.com/) for repository hosting.
- [Heroku](https://heroku.com/) to host the site.
- [Balsamiq](https://balsamiq.com/) for mock ups of the site.
- [Postgres](https://postgresql.org) for database functionality.
- [Stripe](https://stripe.com/) for online payment processing.
  
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