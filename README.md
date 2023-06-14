# Retail Task Manager website

![Mockup of Retail Task Manager on desktop, tablet and mobile](static/documentation_images/am_I_responsive.png)

[Visit the live site](https://pooltesting-buddy.onrender.com).

The purpose of this application is to facilitate the completion of day-to-day tasks for managers, supervisors and keyholders in a retail store, thereby enhancing operational efficiency.

This website, meticulously designed and developed, empowers users to seamlessly assign and delegate tasks to various team members, streamlining the store's workflow management process.

The application aims to be intuitive and simple for all users .
* On the Home page of this website, new users will find a brief explanation of its purpose and it features a convenient link that directs users to the login page, where they can register or access their accounts and explore the full range of features and benefits offered.
* All users can see the corresponding tasks assigned to them  once logged in and can updated the status of a task .
* The 'admin' which will be the username cater to a general manager posistion in the shop(username:administrator password:123456) has more options of editing ,deleting , creating new tasks, checking all team members name and task attached to the them .


***

## User Experience

### New User Stories

* As a new user : Understanding the purpose I want to quickly grasp the website's purpose and determine if it provides value to me.
* As a new user : User-friendliness is important and  I want the application to be easy to use and navigate. It should provide intuitive features and functionalities that align with my needs as a user. 
* As a new user: Clear instructions for tasks specifically, I want to be guided on how to updated the status of a task given to me .It is essential for me to have step-by-step instructions that are easy to follow.


### Returning User Stories

* As a returning admin user 'Manager or Supervisor': The website provides me with a platform to assign and track tasks for my team, ensuring that tasks are completed promptly and efficiently.
* As a returning user 'Keyholder': Responsible for overseeing daily operations in the shopfloor and helping the management team it is important for me to comeback and use the website in a convenient way to stay organized and accountable .
* As a returning user 'Keyholder': I can easily track and complete my routine checks, ensuring that critical tasks are not overlooked so the website becomes a reliable tool that helps me maintain a structured approach to my responsibilities.
* As a returning admin user: I want to be able to easily access and delete the data other users have saved in the application.
* As a returning admin user: The website provides valuable insights and analytics that allow me to make data-driven decisions.
* As a returning admin user: I can gain a deeper understanding of the store's operations. These insights enable me to identify trends, make informed decisions, and implement strategies that drive business growth


### Design

The site uses the Materialize framework. I used Materialize's purple darken and accent color palette the choice of using purple as the primary color for the retail store task tracker on the website is purposeful and aligns with the design philosophy.


#### Colours and Shades

* The site uses a #4a148c purple darken-3 for the navbar in mobile and desktop devices.

* The color of the background is white and text is black and white to help and make it easier to read for the user.


![Purple Pallette](static/images/colour-palette-purple.png)

* Colours are used consistently in association with a particular type of editing /deleting task.

* Light blue is used on the change status  buttons
![Buttons colours according to function](static/images/change-status.png)


* Light blue and pink is used for editing and deleting a task from the admin user.
![Buttons colours according to function](static/images/edit-delete-admin.png)


* Lighter purple to add new tasks from the admin user.
![Buttons colours according to function](static/images/add-tasks.png)



#### Typography

* The site logo uses the Poppins font [Poppins font](https://fonts.google.com/specimen/Poppins) from Google Fonts. Poppins is a versatile and elegant font that can work well for a luxury shop website. Clean and Modern: Poppins has a clean and modern appearance, which aligns well with the aesthetics of this websites retail luxury brand. It carries a sense of sophistication and refinement.
* All other text on the site uses the standard Materialize framework font stack, which consists of legible sans-serif fonts.

#### Imagery

* [Font Awesome 6](https://fontawesome.com/) icons are used throughout the site to illustrate buttons.

* [Pexels](https://www.pexels.com/) I used a retail shop image for the home page.![Home page](static/images/background-picture.png)

* [Unsplash](https://unsplash.com/) I used a welcome picture for the Log in page.![Welcome website picture ](static/images/welcome-picture-login.png)

### Wireframes

The site is responsively designed to adapt to the user's viewing device.

## Home Desktop view

 ![Home desktop view](static/images/desktop-image.png)

# Home Tablet view

 ![Home Tablets view](static/images/ipad-image-home.png)


 ## Mobile Home view

 ![Mobile Home view](static/images/phone-image-home.png)
 
 ## log in desktop view

 ![Home desktop view](static/images/desk-login.png)  

  ## log in tablets view

 ![Home desktop view](static/images/tablet-login.png)  

  ## log in phone view

 ![Home desktop view](static/images/phone-login.png)  

  ## Sign Up desktop view

 ![Home desktop view](static/images/desktop-registration.png)  

 ## Sign Up tablet view

 ![Home desktop view](static/images/registration-form-ipad.png)  

 ## Sign Up phone view

 ![Home desktop view](static/images/registration-form-phone.png)  


 
***

## Features

### User Accounts

Task Manager features a user account system that allows ordinary users to create an account using a unique username and password. Once logged in, users can update the status of their assigned tasks. If no tasks have been assigned to them, they can still view all tasks on the website but cannot update their status.
There is only one admin user on the website who has the following privileges: creating tasks and assigning them to each team member, specifying deadlines and departments if urgent. The admin user can also edit existing tasks in the database and delete them as needed. Furthermore, the admin user has access to the overview page, which includes two different charts: "My Daily Charts" and a chart displaying "team members" names and departments.

* Users create accounts by filling in a simple registration form.

* Users sign in to their accounts by filling in a login form and sign out using a link in the navigation bar.

* The application uses the Flask session object to handle user login functionality and passwords are hashed using Werkzeug helper functions.

### Adding task as admin

. Task Manager offers a comprehensive feature set that includes full CRUD functionality for the administrator user.Full CRUD (create, read, update, delete), the administrator has complete control over managing tasks and team members.They can effortlessly create new tasks, assign them to team members, and set deadlines or urgency levels. Lastly, should the need arise, the administrator can delete tasks from the system.

* The process begins by accessing the task creation feature, where you can provide essential details such as the task name, description,date and any specific instructions or requirements.

![Add workout logs by filling a form](static/images/how-to-create-tasks.png)

* All tasks are listed on the home page.

![List of tasks example](static/images/examples-of-alltasks-page.png)


* Once the task is assigned, the team members will be able to see that task in the home page  and can access them through their individual user accounts.

![See task in normal user account only if it has been assigned to that user](static/images/user-changestatus-assigned.png)

* As the administrator, you have access to a dedicated "Manage Team" page, which serves as a central hub for overseeing and managing your team members. This page provides you with a view of all team members registered on the platform. From here, you can edit their names, departments or if needed you can delete the user.

![Admin view Manage Team](static/images/manage-team-admin-page.png)

* Admin Overview page: The page showcases two distinct charts: "My Daily Tasks" and "My Team". The "My Daily Tasks" chart provides a visual representation of your own task assignments.

![Admin Overview Page](static/images/overview-admin-page.png)


### Regular User 

* Firstly, you can effortlessly view all the tasks assigned specifically to you. Upon logging into your user account, you'll be greeted with a personalized dashboard that displays a comprehensive list of tasks tailored to your responsibilities. 

![Admin view of previous test](static/images/just-task-assigned-to-user.png)


* Secondly, Task Manager enables you to easily update the status of the tasks assigned to you. Whether you've completed a task or need to provide an update, you can conveniently modify the task status within the system.

![Edit test logs are prepopulated](static/images/status-user-feature.png)


### FAQ

New users are adviced to visit the F.A.Q page at the home screen. The FAQ page covers a wide range of topics related to the Task Manager platform, including account management, task creation, status updates, and more.

* The FAQ page provides answers to common questions  Users can find detailed instructions for how to complete a test here.

![FAQ page](static/images/faq-page-home.png)


***

## Database Design

Task Manager uses the MongoDB non-relational database. Data is divided into three collections, with the following schema:

![Datbase scheme](static/images/data-scheme.png)

![Logic workchart](static/images/logic-workchart.png)

***

## Future Features

The following features could be added in the future, given more development time:

### 1. Account Management Tools

* Helpful account management tools could be provided, such as the ability to update usernames, email addresses and passwords.
* A password recovery by email function could also be provided. The [flask-security](https://pythonhosted.org/Flask-Security/features.html) extension can provide this functionality, as well as some other more advanced account management tools.

### 2. Collaborative Task Comments

* Introduce a feature that enables users to leave comments and engage in discussions directly within the task interface. This will facilitate seamless communication among team members, allowing for real-time updates, clarifications, and collaboration on specific tasks. It promotes better teamwork and ensures everyone stays on the same page.

## 2. Inventory Management Page

* Incorporate an inventory management module into the Task Manager website, allowing users to track and manage stock levels of products in real-time. Users can create tasks related to inventory management, such as restocking, inventory counts, or product updates, ensuring that the retail shop always has accurate and up-to-date inventory information

### 3. Advanced Reporting and Analytics

* Implement comprehensive reporting and analytics capabilities that provide users with valuable insights into task and project performance. Users will be able to generate detailed reports, track progress, monitor team productivity, and identify areas for improvement. This feature will empower users with data-driven decision-making, enabling them to optimize task management strategies .


### 5. Code optimization and refactoring

* This was my first major project using Python and Flask, so there are a few areas where I feel the code could be made neater and more efficient.
* In particular, more helper functions could be employed to avoid repeating common tasks across the different functions.


***

## Technologies

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.m.wikipedia.org/wiki/JavaScript)
* [Python](https://en.m.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [GitHub](https://github.com/) - Used for version control.
2. [GitPod](https://gitpod.io/) - Used to write all code and test before deploying to GitHub.
3. [Mockplus](https://mockplus.com/) - Used to produce design wireframes.
4. [Materialize](https://materializecss.com/) - Materialize CSS framework used extensively to create layout and styling of site.
5. [jQuery](https://jquery.com/) - Used to initialise Materialize components and validate select elements.
6. [Python 3.8](https://www.python.org/) - Used to code the application.
7. [MongoDB](https://www.mongodb.com/) - Used for the application's database.
7. [Flask](https://palletsprojects.com/p/flask/), [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) and [Werkzeug](https://palletsprojects.com/p/werkzeug/) - Used to build the main application structure, page templates (Jinja) and account security (Werkzeug).
8. [PyMongo](https://github.com/mongodb/mongo-python-driver) - Used to connect Python with MongoDB
9. [Heroku](https://heroku.com/) - Used to deploy the site.
10. [W3C.org](https://www.w3.org/) - W3C [HTML Validator](https://validator.w3.org/nu/) and [CSS Validator](https://jigsaw.w3.org/css-validator/validator) used to check HTML and CSS code for errors.
11. [JSHint](https://jshint.com/) - Used to check JavaScript for errors.
12. [PEP8 Online](http://pep8online.com/) - Used to check Python code for errors.
13. [Kaffeine Heroku](http://kaffeine.herokuapp.com/) -Used to ensure that heroku page doesn't hibernate (Note that page goes to 'sleep' at midnight until 6 am and is not available during those 6 hours)


***

## Testing

## Functionality testing 

 I used Chrome developer tools throughout the project for testing and solving problems with responsiveness and style issues.


## Compatibility testing
 Site was tested across multiple virtual mobile devices and browsers. I checked all supported devices in Chrome developer tools. 
 
 I tested on hardware devices such as: Ipad air with iOS, Iphone 13 mini with iOS 15.4, Macbook air with MacOS and Surface Pro with windows 10


---
## Issues found during site development

* ### Edit reading page not pre-populating the previously selection


![testing-issue-1](static/documentation_images/pre_populating_edit.png)

When clicking on the 'edit' button on a previously recorded pool test, I noticed that the right fields were not being selected and on some ocassions not even appearing on the select fields

> I fixed this by adding the 'value' attribute to the options tag and populating it with the correct Jinja expression to access the relevant data.



* ### Logo overflowing on small and extra small devices

> I fixed this by adding a media query which removes the logo completely by setting the display to 'none' when in small devices.

![resolved4](static/documentation_images/media_query_fix.png)


* ### Login not working.

![testing_issue_2](static/documentation_images/endpoint_non_existent.JPG)

This one was a tough one for me, as I changed the name of some of the templates, the endpoint was not being built properly as it was still pointing to non-existing pages.

> I fixed this by updating the relevant python functions with the new names of the html pages that flask was pointing to.

![resolved](assets/readme-images/counter1.png)


## Performance testing

I run [Lighthouse](https://developers.google.com/web/tools/lighthouse/) tool to check performance of the website.
Screenshots are presented below:


Final results:
![performance_final](static/documentation_images/light_house_testing.png)

I noticed that this tests scores vary from time to time and depends on external libraries as well. 



## Code Validation
 At the end of the project I used three websites to validate my code:
 
 * [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) to validate CSS

 ![CSS validator](static/documentation_images/css_validation.png)

 * [Nu Html Checker](https://validator.w3.org/) to test HTML

 ![HTML validator](static/documentation_images/home_html_validation.png)

 * [JShint](https://jshint.com/) to test JavaScript

 ![JS validator](static/documentation_images/javascript_va;idation.png)
 
 * [Pep8](https://pypi.org/project/pep8/) to test python

 ![JS validator](static/documentation_images/pep8_validation.png)




***

## Deployment

### Forking the GitHub Repository

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/yoesk8/pooltesting_buddy_PP3)
2. At the top right of the page, click the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

You can download the project source code as a zip file by clicking the 'Code' dropdown at the top right of the file navigation window and selecting "Download as ZIP". You can then unzip that file to wherever you want your local copy to be.

If you have Git installed on your computer, you can clone the project by following these steps:

1. Log in to GitHub and locate the [repository](https://github.com/yoesk8/pooltesting_buddy_PP3)
2. Click the 'Code' dropdown at the top right of the file navigation window.
3. Copy the link under 'Clone' and 'HTTPS' to clone the repository using HTTPS.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/yoesk8/pooltesting_buddy_PP3
```
7. Press Enter. Your local clone will be created.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://github.com/yoesk8/pooltesting_buddy_PP3)

### Database Setup

The project uses MongoDB, so for either local or remote deployment you'll need a properly configured database.

1. If you don't have a MongoDB account, sign up for a free account at [MongoDB](https://www.mongodb.com/).
2. If you don't have any clusters, create a new cluster.
3. Add a new database to your cluster with the name: **pooltesting_buddy**
4. The pooltesting_buddy database should have three collections with the following setup:

**users**
```
_id: <ObjectId>
username: <string>
name: <string>
password: <string>
```

**pool_type**
```
_id: <ObjectId>
max_batherload: <string>
type: <string>
```

**readings**
```
_id: <ObjectId>
date: <string>
time: <string>
pool_type: <string>
free_chlorine: <string>
total_chlorine: <string>
combined_chlorine: <string>
ph: <string>
water_temperature: <string>
outside_parameters: <string>
```



In order to connect to the database, you'll need to create a user and generate a MongoDB URI. 

#### Creating a Database User

1. Go to the Overview page of your cluster 
2. Click Database Access under Security in the side menu
3. Next click Add New Database User
4. Select Password as the authentication method and then enter a username and password
5. Under "Built-in role" select "Read and write to any database"
6. Click "Add User"

#### Generating a MongoDB URI

1. Go to the Overview page of your cluster
2. Click the "Connect" button
3. Select "Connect your application"
4. Make sure 'Python' is selected for the driver, then copy the URI provided in the box
5. Replace the "password" and "myFirstDatabase" parts of the URI with your database user's password and the name of your database

### Local Deployment

Follow the steps below to deploy the project locally using VSCode.

(N.B. These instructions are for deployment on a Windows system)

1. Download and install [VSCode](https://code.visualstudio.com/)
6. Open VSCode and click File > Open Folder, then select the folder containing your local cloned repository
7. Download and install [Python](https://www.python.org/downloads/)
8. Download and install the [VSCode Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
9. In VSCode, open the command palette (Ctrl + Shift + P on Windows) and search for the Python: Select Interpreter. Click it, then select the version of Python you have installed.
10. Open a terminal in VSCode and enter the following commands to create and activate a virtual environment:
```
py -3 -m venv .venv
.venv\scripts\activate
```
11. Open the command palette and search for Python: Select Interpreter again. You should see your new virtual environment. Select it.
12. In the terminal, enter the following command to install all required packages:
```
python -m pip install -r requirements.txt
```
13. Create a new file in your project directory called "env.py"
14. Add the following to the env.py file, replacing YOUR_MONGO_URI with your MongoDB URI, YOUR_DATABASE_NAME with your database name, and YOUR_SECRET_KEY with a suitable [secret key](https://flask.palletsprojects.com/en/2.0.x/config/#SECRET_KEY):
```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY")
os.environ.setdefault("MONGO_URI", "YOUR_MONGO_URI")
os.environ.setdefault("MONGO_DBNAME", "YOUR_DATABASE_NAME")
os.environ.setdefault("ENV_DEBUG", "True")
```
15. In the terminal, type `python app.py` to run the app. A link to the locally running instance of the app should be printed in the terminal window.

### Remote Deployment

The app is currently deployed on Heroku [here](https://pooltesting-buddy.herokuapp.com/).

To deploy your own copy of the app, follow the steps below:

1. Sign up for a [Heroku account](https://www.heroku.com/).
2. Check that you have a "requirements.txt" in your app's root directory. This tells Heroku what packages are required by the app. If you've cloned the main branch, this should already be present. If it's missing or if you have added any additional packages, you can generate a requirements.txt file by running the following command from the terminal of your IDE:
```
pip3 freeze --local > requirements.txt
```
3. Check that you have a "Procfile" in your app's root directory. This tells Heroku what kind of application you are trying to run. Again, if you've cloned the main branch, this should already be present. If it's missing, you can create a procfile by running the following command from the terminal of your IDE:
```
echo web: python app.py > Procfile
```
4. Check that there are no trailing blank lines at the bottom of your procfile. Delete any empty lines
5. From your Heroku dashboard, click "New", then "Create a new app"
6. Give the app a unique App name, pick the region closest to you, then click "Create App"
7. From the "Deploy" menu, select GitHub as the Deployment Method, then enter your GitHub repository details and click "Connect"
8. Open the "Settings" menu, scroll down to "Config Vars" and click "Reveal Config Vars"
9. Enter the following Config Vars, replacing YOUR_MONGO_URI with your MongoDB URI, YOUR_DATABASE_NAME with your database name, and YOUR_SECRET_KEY with a suitable [secret key](https://flask.palletsprojects.com/en/2.0.x/config/#SECRET_KEY):
```
IP: 0.0.0.0
PORT: 5000
SECRET_KEY: YOUR_SECRET_KEY
MONGO_URI: YOUR_MONGO_URI
MONGO_DBNAME: YOUR_DATABASE_NAME
ENV_DEBUG:
```
10. Note that ENV_DEBUG should be left blank, unless you wish to deploy the application with debug mode enabled
11. Return to the "Deploy" menu, scroll to "Automatic deploys" and click "Enable Automatic Deploys"
12. Choose your branch and then click "Deploy Branch"
13. Once the application has finished deploying, click "View" to visit the site.

***

## Other Credits and Acknowledgements

* [Code Institute](https://codeinstitute.net/) for their helpful lessons and reference materials.
* [Code Institute Sample README](https://github.com/Code-Institute-Solutions/SampleREADME/blob/master/README.md) for the structure of this project's documentation and parts of the GitHub forking and cloning processes.
