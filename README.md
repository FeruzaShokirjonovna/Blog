# ***Baby Care Blog - Portfolio Project 4***
---
# **1. Key project information**

- **Description :** This Portfolio Project 4 website called **Baby Care** is a site of imaginary blog, offers news in form of blog from about being Mom and useful tips for mothers. The site is presenting to its visitors with variety of details as blog style functions.
- **Key project goal :** To familiarize visitors of this page with **Baby Care** blog
- **Audience :** There's no age or any other limit to audience of this page. Target audience are Mothers that are using search engines for baby care tips and tricks, advices.
- **Live version :** Live version of **Baby Care** page can be viewed at https://babycare-6f68f42d9b15.herokuapp.com/. 
- **Developer :** [Feruza Orifjonova](https://github.com/FeruzaShokirjonovna/)


---

# **2. Table of content**

[1. Key project information](<#1-key-project-information>)
- [2. Table of content](<#2-table-of-content>)
- [3. User Experience (UX)](<#3-user-experience-ux>)
  - [3.1. The Strategy Plane](<31-the-strategy-plane>)
    - [3.1.1. The Idea](<#311-the-idea>)
    - [3.1.2. The Ideal User](<#312-the-ideal-user>)
    - [3.1.3. Site Goals](<#313-site-goals>)
    - [3.1.4. Epics](<#314-epics>)
    - [3.1.5. User stories](<#315-user-stories>)
  - [3.2. The Scope Plane](<#32-the-scope-plane>)
    - [3.2.1. Features to be implemented](<#321-features-to-be-implemented>)
  - [3.3. The Structure Plane](<#33-the-structure-plane>)
    - [3.3.1. Site Maps](<#331-site-maps>)
    - [3.3.2. Database Schemas](<#332-database-schemas>)
  - [3.4. The Skeleton Plane](<#34-the-skeleton-plane>)
    - [3.4.1. Wire-frames](<#341-wire-frames>)
  - [3.5. The Surface Plane](<#35-the-surface-plane>)
    - [3.5.1. Logo](<#351-logo>)
    - [3.5.2. Color palette](<#352-color-palette>)
    - [3.5.3. Fonts](<#353-fonts>)
- [4. Features](<#4-features>)
  - [4.1. Features used in every HTML template](<#41-features-used-in-every-html-template>)
    - [4.1.1. Header](<#411-header>)
    - [4.1.2. Footer](<#412-footer>)
    - [4.1.3. Favicon](<#413-favicon>)
    - [4.1.4. Error Pages](<#414-error-pages>)
  - [4.2. Main Content](<#42-main-content>)
    - [4.2.1. Landing Page](<#421-landing-page>)
    - [4.2.2. Post Detail Page](<#422-post-detail-page>)
    - [4.2.3. Read Later Page](<#423-read-later-page>)
    - [4.2.4. Forms](<#424-forms>)
- [5. Validation, Testing & Bugs](<#5-validation-testing--bugs>)
  - [5.1. Validation](<#51-validation>)
    - [5.1.1. Table of Content - Validation](<#511-table-of-content---validation>)
    - [5.1.2. PEP8 Validation](<#512-pep8-validation>)
    - [5.1.3. HTML Validation](<#513-html-validation>)
    - [5.1.4. CSS Validation](<#514-css-validation>)
    - [5.1.5. JS Validation](<#515-js-validation>)
  - [5.2. Testing](<#52-testing>)
  - [5.3. Bugs](<#53-bugs>)
- [6. Deployment](<#6-deployment>)
  - [6.1. Transfer of progress from IDE](<#61-transfer-of-progress-from-ide>)
  - [6.2. Offline cloning](<#62-offline-cloning>)
  - [6.3. Deployment Prerequisites](<#63-deployment-prerequisites>)
    - [6.3.1. Gmail](<#631-gmail>)
    - [6.3.2. ElephantSQL](<#632-elephantsql>)
    - [6.3.3. Cloudinary](<#633-cloudinary>)
    - [6.3.4. Settings.py & file-tree](<#634-settingspy--file-tree>)
  - [6.4. Heroku Deployment](<#64-deployment-to-heroku>)
- [7. Technologies & Credits](<#7-technologies--credits>)
  - [7.1. Technologies used to develop and deploy this project](<#71-technologies-used-to-develop-and-deploy-this-project>)
  - [7.2. Requirements.txt](<#73-requirementstxt>)
  - [7.3. Credits](<#73-credits>)

[Back to top](<#1-key-project-information>)
  
---

# **3. User Experience (UX)**

## **3.1. The Strategy Plane**

### **3.1.1 The Idea**

The Baby Care Blog is a dedicated platform aimed at providing comprehensive, reliable, and engaging content for new and expectant parents. Our blog covers a wide range of topics, including infant health, parenting tips, developmental milestones, product reviews, and personal stories from parents. The goal is to create a supportive community where parents can find valuable information and share their experiences.

### **3.1.2 The Ideal User**

The target audience are young parents and couples planning to have a baby

- Ideal user can upvote or downvote on posts
- Ideal user can comment

### **3.1.3 Site Goals**

- Inform and Educate: Provide accurate and up-to-date information on baby care and parenting.
- Engage and Support: Create a community where parents can connect, share experiences, and offer mutual support.

### **3.1.4 Epics**

As a thought process of the strategy plane, 9 epics were created and utilized. Please see below the detail list of epics with links, or a link to the project's [Kanban Board](https://github.com/users/FeruzaShokirjonovna/projects/3/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D). Those Epics were further sliced into USER STORIES.

![Kanban Board](/docs/kanban_board.png)

- [Epic 1: Environment Configuration](https://github.com/users/FeruzaShokirjonovna/projects/3/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D&pane=issue&itemId=66288419)
- [Epic 2: Database Models](https://github.com/users/FeruzaShokirjonovna/projects/3/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D&pane=issue&itemId=66676466)
- [Epic 3: Admin Panel](https://github.com/users/FeruzaShokirjonovna/projects/3/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D&pane=issue&itemId=66676590)
- [Epic 4: Post Views](https://github.com/users/FeruzaShokirjonovna/projects/3/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D&pane=issue&itemId=66676851)
- [Epic 5: User Authentication](https://github.com/users/FeruzaShokirjonovna/projects/3/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D&pane=issue&itemId=66716110)
- [Epic 6: Post Details View](https://github.com/users/FeruzaShokirjonovna/projects/3/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D&pane=issue&itemId=66795769)
- [Epic 7: Comments](https://github.com/users/FeruzaShokirjonovna/projects/3/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D&pane=issue&itemId=66796667)
- [Epic 8: Additional Features](https://github.com/users/FeruzaShokirjonovna/projects/3/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D&pane=issue&itemId=66797020)
- [Epic 9: Testing and Validation](https://github.com/users/FeruzaShokirjonovna/projects/3/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Status%22%2C%22Labels%22%5D&pane=issue&itemId=66797478)

### **3.1.5 User stories**

User stories were created based on the Epics. Each user story uses the MoSCoW prioritization technique. Each user story on the [Kanban Board](https://github.com/users/FeruzaShokirjonovna/projects/3/views/1?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Labels%22%5D) was given labels (MoSCoW).


**MoSCoW prioritization technique stands for**:

**Must-Have**: Critical requirements that must be implemented for the project to be considered successful.

**Should-Have**: Important requirements that are not critical but add significant value.

**Could-Haves**: Desirable features that would be nice to have but are not crucial.

**Won't-Have**: Features that are explicitly excluded from the project scope.


### List of user stories sorted by Epic :

## **3.2. The Scope Plane**

After decided on the strategy, the scope plane was carefully created.

### 3.2.1. Features to be implemented

- **Search** : Search bar for users is provided on landing page so users can find specific News Posts, Styles or Team members.
- **Comment**: Allow users to reply directly to another comment. Replies would then be shown directly underneath that comment as a conversation.

## **3.3. The Structure Plane**

### 3.3.1. Site Maps

### 3.3.2. Database Schemas

Following schema shows intended database structure:

![Database schema](/docs/database_diagram.png)

## **3.4. The Skeleton Plane**

### 3.4.1. Wire-frames

 I created simple ![wireframes](/docs/wireframes.png) for the homepage, and the article detail page. For the registration and login page I was planning to use the default layout, so I omitted wireframes for those pages.


## **3.5. The Surface Plane**

### 3.5.2. Color pallette

- Primary Color (#763ae0): This vibrant shade of purple is eye-catching and energetic, serving as the primary color to draw attention to important elements on the website

- Primary Color Dark (#2002b8): A deeper, darker shade of purple that complements the primary color. This hue can be used for accents or to highlight hover effects, giving the design depth and contrast.

- Secondary Color (#a0d333): This soft green hue complements the primary color palette, bringing a refreshing and natural feel to the design

- Background Color (#fcf9f2): A light, almost off-white cream color that serves as the neutral background for the website. It ensures readability and allows other colors to pop without overwhelming the user. This soft tone helps create a pleasant, warm environment for the site.

- Text Dark (#333333): A dark gray color, perfect for body text or any content where readability is crucial.

- Text Light (#767268): A lighter shade of gray, suitable for secondary text or elements where a softer contrast is desired.

This balanced color palette will create an elegant, readable, and visually appealing design for the website.


### 3.5.3. Fonts
[Google Fonts](https://fonts.google.com/) site was used to pick the best typography style. The most importance was given to balance between style and readability. As a developer I needed to ensure that all text is displayed clear.

### 3.5.4. Icons and pictures

The website integrates various icons and images to enhance the user interface and facilitate easy interaction. The following sections outline how these visual elements are utilized:

- Voting Icons
- Icons Used: The voting buttons feature circular icons that represent user interactions with content. These are designed to be simple and easily   identifiable.
  - Upvote Icon: A thumbs-up icon in a green circle to represent positive feedback.
  - Downvote Icon: A thumbs-down icon in a red circle to indicate negative feedback.
-Design Details: These icons are circular and visually stand out, making it clear where users can vote on content.

- Comment Icons
  - Icons Used: The comment bubble icons appear next to posts, representing the ability to comment on or reply to content.
  - Design Details: The icons are simple and round, placed near the comment sections for easy access.

- Images for Content: Various images are used to complement articles, posts, and user profiles. These images are strategically placed to provide visual interest and context.

[Back](<#2-table-of-content>)

# **4. Features**

## **4.1. Features used in every HTML template**

### **4.1.1 Header**

![Header](static/images/not-logged-header.png)


- It is fully responsive and includes the Baby Care blog name on the left and member links and blog slogan on the right.

- The blog name is wrapped in a link and can be used to navigate to the homepage.

- The logo is wrapped in a link and can be used to navigate to the homepage.

- The navigation bar is identical on each page to allow for easy navigation from page to page across all devices.

![Header Authenticated](static/images/logged-in-header.png)

- After logging in, the links on the right side are replaced by the Read Later and a log-out button.

- The user can always see if they are logged in by their username being displayed. 


### **4.1.2 Footer**

![Footer](static/images/footer.png)

- Every page has a footer at the bottom of the page.
- The footer shows the copyright text and links to four different social media websites. Each link opens in a new tab.

### **4.1.3 Favicon**

![Favicon](static/images/favicon.png)

- Every template in this project is equipped with Favicon. This is to ease navigation for user in case of more tabs opened. 

### **4.1.4 Error Pages**

- This project is designed to have custom error pages. In case of user clicks on broken link, submits action that isn't supported or tries to reach certain view without permission, then user isn't completely "cut off" from browsing, instead an error page with header and footer appears and user is informed of the situation.

The following custom error pages were created :

- 403 - Received when user attempts to access a web resource for which they lack the necessary permissions. 
- 404 - Encountered when the requested web resource by user is not found on the server. 
- 500 - Displayed when the web server encounters an internal error while processing the request.

## **4.2. Main Content**

### **4.2.1. Landing Page**

![Home](static/images/home-page.png)

- **Template File :** `index.html` - extends `base.html`
- Contains list of posts.
- Provides user with all Posts published along with name of creator, date created and a snippet of Post body. Also information of amount of votes is provided to both logged in and not logged in users 

### **4.2.2. Post Detail Page**

![Post Detail page](static/images/post-detail-page.png)

- **Template File :** `post_detail.html` - extends `base.html`
- Every article on the homepage can be opened by clicking on it.
- Provides the user with selected Post along with name of creator, date created and full Post body.
- Logged in user can save the post to read later via Read Later button.
- The User sees votes and amount of comments. 
- Logged in user has ability to comment and vote.

## Comments
![Comment Section](static/images/comment-form.png)
- Every article has a comment section on the detail page.
- At the top of the section, a title shows the number of comments.
- If the user is not authenticated, a hint shows that the user needs to log in or register to join/start a discussion.

### Add Comment
![Add Comment](static/images/comment-form.png)
- If the user is authenticated, a comment form is displayed instead of the hint.
- The user can enter the content of the comment and post it by clicking the button.

### Edit Comment
![Edit Comment](static/images/edit-comment.png)
- The user can edit their comment by clicking the edit button in the top right corner.
- The comment form turns into an edit form, instead of save button displays 'Update' button allowing the user to edit the comment.
- To save the changes, the user can click on the Update button.
- A message notifies the user about the successful edit.

### Delete Comment
![Delete Comment](static/images/delete-confirm-message.png)
- The user can remove their comments permanently from the conversation.
- To delete a comment, the user can click on the delete button.
- Before deleting, the user has to confirm their decision, otherwise, the comment will not be deleted.
- A message notifies the user about the successful deletion.


### **4.2.3. Read Later Page**

![Read Later page](static/images/read-later-page.png)

- **Template File :** `read_later.html` - extends `base.html`
- Enables logged in user to see the list of bookmarked posts. 
- If there is no bookmarked posts, displays that there no posts to read later.

![Read Later page 2](static/images/no-bookmarked-posts-page.png)

### **4.2.4. Forms**

- **App :** `AllAuth` extension
- **Template File :** `*.html` in `./templates/account` - extends `base.html`
- **User :** Forms do interact with the user. They are designed to be clear and to the point, always in center of the screen. 

![Sign-in page](static/images/sign-in-page.png)

- If a user wants to use the features reserved for members of the website, such as commenting and voting, they have to register.
- The user can reach the registration page by the link in the navigation bar.
- To become a member, the user has to enter a username, email, and password.
- If the provided data is valid, the user is automatically logged in and redirected to the page they were on before.


![Register Form Error](static/images/sign-in-error.png)

- If the entered data is invalid when sent off, the form loads again with an error message. 
- The form data, apart from the password, is preserved and the invalid fields are highlighted with an error message below.
- After fixing the invalid fields and reentering the password, the user can send the form again.

![Sign out page](static/images/sign-out-page.png)

- If authenticated user want to log out, the member can reach the logout page by the link in the navigation bar.
- Clicking signout button the member can easily sign out from the website.

![Login page](static/images/login-page.png)

- If an unauthenticated member wants to use the features reserved for members of the website such as commenting and voting, they have to log in.
- The member can reach the login page by the link in the navigation bar.
- To log in, the user has to enter their username and password.
- If the username and/or password are incorrect, the form is loaded again, informing the user about the error.

[Back](<#2-table-of-content>)


# **5. Validation, Testing & Bugs**

## **5.1. Validation**

Validation is documented separately in [validation.md](/docs/validation.md) file.


## **5.2. Testing**

In this project, I used two types of testing: Manual explorative testing and semi-automated tests.

## Manual Testing
- Throughout the development process, I manually tested every page and feature exhaustively.   
[List of manual tests](docs/testing/manual_testing.md)
- When I finished creating my MVP, I shared the website with multiple users to confirm its functionality and to get feedback on their experience.

### Django Tests
- For all my views, models, and forms, I implemented tests with the Django framework.
  - The tests cover the functionality of all pages and the elements within.
  - The tests use a separate test database instead of the production database.
- The Django framework includes a testing library, so no further setup is necessary.
- I started the Django tests with the command `python3 manage.py test`.

### Results

Test results from the Django tests: All 10 tests passed.  

![Django Test Results](static/images/django-tests.png)


## **5.3. Bugs**

Bugs is documented separately in [bugs.md](/docs/bugs/bugs.md) file.

# **6. Deployment**

## **6.1. Transfer of progress from IDE**

- **Task :** To ensure regular commitments are done to avoid any data/progress loss.
- **Method :** 
   - commands `git add [filename]` was used to add specific file to staging area, alternatively command `git add .` was used to add all changed files to staging area
   - command `git commit -m "[commit description]"` was used to add commitments into queue
   - command `git push` was used to push all commitments to remote repository on GitHub

## **6.2. Offline cloning**

- **Task :** To use repository on local machine.
- **Method :** 
  - Navigate to GitHub and follow `Code -> HTTPS -> Copy button` . after those steps open your local coding environment and type `git clone [copied link]`.

## **6.3. Deployment Prerequisites**

### **6.3.1. Gmail**

- **Task :** Obtain GMail username and app key (password) - GMAIL SMTP to be used as mailing client.
- **Method :** 
  - Navigate to `https://accounts.google.com/` and follow all steps for registering new email address
  - Login to google with newly created email address and password.
  - Navigate to `https://accounts.google.com/` once again
  - Select `Security > Signing in to Google > 2-Step Verification > App Passwords`
  - Enter a name of the app password and select `Generate`
  - You will get app password in format `xxxx xxxx xxxx xxxx`
  - Update `settings.py` in the project directory

### **6.3.2. CI DB**

- **Task :** Obtain database URL to be used as project's database.
- **Method :** 
  - Select one of the DB providers, I did use [CI DB](https://dbs.ci-dbs.net/)
  - Navigate to `https://dbs.ci-dbs.net/` and follow all steps for registering new account
  - Login to CI DB with newly created account credentials
  - Navigate to `+ Create New Instance`
  - Select `Name, Plan and Region`
  - Confirm the instance by pressing `Create Instance`
  - Obtain database URL in format 
  - Update `settings.py` in the project directory

### **6.3.3. Cloudinary**

- **Task :** Obtain Cloudinary URL to be used as project's static storage
- **Method :** 
  - Select one of the static storage providers, I did use [Cloudinary](https://console.cloudinary.com/)
  - Navigate to `https://console.cloudinary.com/` and follow all steps for registering new account
  - Login to Cloudinary with newly created account credentials
  - Navigate to `+ Add a new environment`
  - Confirm your selection
  - Obtain Cloudinary URL in format `cloudinary://USER:PASSKEY@ENVIRONMENT`
  - Update `settings.py` in the project directory

### **6.3.4. Settings.py & file-tree**

- **Task :** Prepare `settings.py` adn file-tree for deployment 
- **Method :** 
  - Create file `env.py` to keep all sensitive information in
  - See example of `env.py` file *( Appendix 48 )*
  - Add `env.py` into `.gitignore` file to ensure this fill won't be uploaded to GitHub
  - update `settings.py` with `import os`
  - for every secured variable add code `VARIABLE = os.environ.get("VARIABLE")`
  - ensure this process for Gmail, ElephantSQL, Cloudinary, DEBUG and Django Secret Key
  - update default database settings in `settings.py` with `
if "DATABASE_URL" in os.environ:
    DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }`
  - update default static settings in `settings.py` with `
  STATIC_URL = "/static/"
STATICFILES_STORAGE = "cloudinary_storage.storage.StaticHashedCloudinaryStorage"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL")
MEDIA = "/media/"
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
  `
  - update email settings in `settings.py` with `EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True`
  - Migrate - your database models to Database using `python manage.py migrate` command
  - Create directories `.\static` and `.\templates`
  - commit and push changes to GitHub 

### **6.4. Deployment to Heroku**

- **Task :** To ensure users are able to view live version of **Aneta's Glimmer** project.
- **Method :** 
  - Register & Log In with heroku
  - Navigate to `New > Create New App`
  - Select Name of the app that is unique
  - Navigate to `Settings > Reveal Config Vars`
  - Add all variables from `env.py` to ConfigVars of Heroku App 
  - Add variable pair `PORT:8000`
  - For the testing deployment add variable pair `COLLECT_STATIC:1`
  - Add the Heroku app URL into `ALLOWED HOSTS` in `settings.py`
  - In root create file name `Procfile`
  - Navigate to `Deploy > GitHub > Connect`
  - Navigate to `Deploy > Deploy Branch`
  - Optionally, you can enable automatic deploys
  - See the deployment log - if the deployment was successful, you will be prompted with option to see live page  

[Back](<#2-table-of-content>)


## **7. Technologies & Credits**

### 7.1. Technologies used to develop and deploy this project

- [**Django/Jinja**](https://docs.djangoproject.com/en/5.0/) - main Framework of the project
- [**Python**](https://www.python.org/) - main BackEnd programming language of the project
- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/HTML) - templates programming language of this project (FrontEnd)
- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS) - styling the project via external CSS file `./static/css/style.css`
- [**Java Script**](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - dynamic templates programming language of this project (FrontEnd)
- [**jQuery**](https://api.jquery.com/) - API for JavaScript - dynamic templates programming language of this project (FrontEnd)
- [**Bootstrap v. 5.3**](https://getbootstrap.com/) - styling framework used in this project (FrontEnd)
- [**Heroku**](https://heroku.com) - to deploy this project
- [**Balsamiq**](https://balsamiq.com/support/) - to create wireframes
- [**Git**](https://git-scm.com/doc) - to make commitments of progress and push the results back to GitHub
- [**GitHub**](https://github.com/) - to keep the track of version control
- [**Gitpod**](https://gitpod.com/) - online IDE - CodeAnywhere was initially used to create this project


### 7.3. Requirements.txt

asgiref==3.8.1 - ASGI reference implementation, providing a specification for asynchronous web servers and applications
cloudinary==1.40.0 - SDK for interacting with the Cloudinary media management service, facilitating image and video uploads
dj-database-url==0.5.0 - utility for using database URLs in Django settings, simplifying database configuration
dj3-cloudinary-storage==0.0.6 - Django storage backend for Cloudinary, allowing seamless integration of Cloudinary as a storage solution for media files
Django==5.0.6 - framework that encourages rapid development and clean, pragmatic design
django-allauth==0.63.3 - package providing a set of authentication views, templates, and adapters for handling user registration, authentication, and account management
django-crispy-forms==1.14.0 - application that lets you easily build and customize crispy forms using Bootstrap styles
django-summernote==0.8.20.0 - application for integrating the Summernote WYSIWYG editor into Django admin forms
gunicorn==22.0.0 -  WSGI HTTP server for running Django applications in production
psycopg2==2.9.9 - PostgreSQL adapter for Python, allowing Python applications to interact with PostgreSQL databases
pytz==2024.1 - Python library for working with time zones
sqlparse==0.5.0 - library for parsing SQL statements

### 7.3. Credits
- [**Precious Ijege**](https://www.linkedin.com/in/precious-ijege/?originalSubdomain=uk) - massive shout-out for keeping me in the right direction
- [**Tomáš Kubánčik**](https://ie.linkedin.com/in/tomas-kubancik?utm_source=share&utm_medium=member_mweb&utm_campaign=share_via&utm_content=profile) - thank you for all the support

- [**Google Fonts**](https://fonts.google.com/) - used for picking the best typography
- [**PostgresSQL**](https://www.postgressql.com/) - used as a database storage
- [**Cloudinary**](https://console.cloudinary.com/) - used as a storage of static files
- [**FavIcon.io**](https://favicon.io/favicon-converter/) - used to compress favicon
- [**W3Schools**](https://www.w3schools.com/) - useful information and cheat sheets

[Back](<#2-table-of-content>)
