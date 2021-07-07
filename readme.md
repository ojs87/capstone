Phoenix - TarkovHelper

**Distinctiveness and complexity requirements**

This projects is designed to run alongside the game Escape From Tarkov. It's main function is to track quest progress and provide a quick view of what items you still need to pick up while playing the game.

It utilized a 3rd party web scraper to mine quest data from the Official Wiki - https://escapefromtarkov.fandom.com/wiki/Escape_from_Tarkov_Wiki

This mined data was converted from csv to json on a 3rd party website and then imported into the TarkovFoundInRaid model using the importjson function in views.py.

It uses Django-MPTT to create a tree structure model in TarkovQuestStructure that helps efficiently find parent and children nodes for each quest and allows django template syntax for creating trees in HTML

Each registered user's session is updated and saved automatically into the User model.


**Created Files**

requirements.txt:                Requirements for running the website

webscrapersitemap.txt:           Webscraper scripts for use with Web Scraper application if the quest or item data needs to be updated

static > images:                 Contains image pngs for Quest givers in the game
static > phoenix > script.js:    Contains javascript for the website
static > phoenix > styles.css:   Contains CSS for the website

templates > csvjson(1).json:     File containing json data for quests
templates > csvjson(2).json:     File containing json data for items

templates > phoenix > foundinraid.html:

A page that uses javascript to create a table based on the selection in a Select form. The items are stored in the TarkovFoundInRaid model and the quests are stored in the TarkovQuestTester model. The itemroute view creates a python dictionary in Json format with the data needed for the Table.

templates > phoenix > index.html:

A simple homepage with a description of the website and instructions to use the menu to navigate

templates > phoenix > layout.html:

A page containing the html for the navbar, used as the layout for all the other webpages. The navbar is built with bootstrap and uses jquery to show/hide the Quests menu and submenus.

templates > phoenix > login.html:

Standard login used in other projects

templates > phoenix > quests.html:

A page containing information on each quest, picked from the Quests menu in the navbar. Gives indepth information on the quest. Can use the prequests and leads to links to navigate between quests.

templates > phoenix > register.html:

Standard register used in other projects

templates > phoenix > tracker.html:

A page using the django-mptt template tags to populate a tree structure using lists. Javascript is used to give each button the ability to update the User's model with their quest progress state and then update the html page. The buttons will remove descendants automatically if an ancestor is clicked. Current quests and Items you need are updated automatically as you click a button.


**How to Run the application**

Open the command line terminal
Install apps in the requirements.txt using "pip install"
Navigate to the capstone directory and type "python manage.py runserver"
in your web browser, visit http://127.0.0.1:8000
login to the admin account with username: "ojs", password: "easypass" or create a new account
