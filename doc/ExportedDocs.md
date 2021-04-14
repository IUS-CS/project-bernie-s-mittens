#All Documentation for ProVax program                                         Team Bernie’s Mittens

    Begin by downloading Python and then Django(python -m pip install Django), for Django 3.1 you 
need Python version 3.6 or later. You can check your Python version in command line with “py -m 
django –version” or for Mac/Linux “python -m django –version”.
For the rest of this document we will only use the commands for Mac/Linux. Git clone the repository in 
your Python directory. The file will be titled “project-bernie-s-mittens”. You will need to create a virtual 
environment for your Python project. In the “project-bernie-s-mittens” folder you will need the 
command “python -m venv django_env”. Activate the virtual environment with the command
“django_env\Scripts\activate”. Run “pip install -r requirements” to correctly initialize virtual 
environment and Django. Outside of the terminal, hold down Win + Pause to enter system properties 
and navigate to Advanced System Settings then Environment Variables. Click New... and label the 
variable DJANGO_SECRET_KEY and set it to the given key. Return to the terminal and enter python 
manage.py runserver to activate server. Click on the URL http://127.0.0.1:8000/ in a web-browser that 
does not force HTTPS connection to check site status. The server will need to be running in order to run 
the program. You can quit the server by hitting Ctlr+C.
With the program running it will bring up the HOME page:
![Image of Home page](images/ScreenshotHomePage.png?raw=true)

This is framed from the HTML code. It starts with the base.html:

![Imageof base.html](images/Screenshot_base_html.png?raw=true)

Number 1 highlighted is the three URL’s to the pages: home(already pictured), eligibility, and about.
Number 2 highlighted is the Title of the program and the bottom highlight is the link to user_create.html
where the input is taken from the user. This is the HTML code for user_create.html:

![Image of user_create.html](images/ScreenshotUser_create.png?raw=true)

When you click on the “Am I eligible?” button on the home screen it reads the user input with 
“method=’POST’ ” taken from the “form.as_p” which creates objects in “user_detail.html” when the 
options selected either from drop-down menus or typing in your age. Eligibility page:

![Image of Eligibility page](images/ScreenshotEligibility.png?raw=true)
![Image of User_detail.html](images/Screenshot_user_detailHTML.png?raw=true)

This data is input into models.py which lays out your database and stores your data.

![Image of user/models.py](images/Screenshot_users_views_py.png?raw=true)

The inputs from STATES, ESSENTIAL, and GROUPS is changed to 2 or 1 letter abbreviation for the 
corresponding fields. Age is taken in straight from the user_detail.html object and validated with to be
 within 1-120. The data from ths form is validated and stored in users/views.py.

 ![Image of users/views.py](images/Screenshot_users_views_py.png?raw=true)

 The user_detail_view(blue) gets the data from the database and based on the data from 
user_creata_view(red) will be sent to either user_good_view(green) or user_not_view(green).

![Image of Eligibility Good](images/GoodPage.png?raw=true)
![Image of Ineligible page](images/NotGoodPage.png?raw=true)

###Program Use
*  Once installed and in the virtual environment you will run the server.
*  Click on the link or copy and paste the server address http://127.0.0.1:8000/ into a browser window.
*  From the home page you can click the “Am I eligible?” button.
*  Select a home state.
*  Select a work state.
*  Type in your age.
*  Select if you are essential.
*  Select your vaccine group.
*  Click on the “submit” button.
*  The user_good page or user_not page will display your results.