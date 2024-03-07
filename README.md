# [MIRUSNORDIC](https://mirusnordic-f36ddbc9881a.herokuapp.com)

# Welcome to MIRUSNORDIC 
your one-stop solution for booking cars health and wellness treatments. This innovative platform is designed to simplify the process of discovering, booking, and managing your appointments, ensuring a seamless experience for both new and returning users.

# Key Features
- User-Friendly Interface:
- Comprehensive Treatment Options:
- Convenient Booking System:
- Personalized Profiles: 
- Responsive Design:

# Target Audience
Mirus Nordic is tailored for car enthusiasts, busy professionals, and anyone who takes pride in their vehicle's appearance. Whether you drive a luxury sedan, a rugged SUV, or a classic sports car, our services are designed to meet the needs of all types of vehicles. We understand that your car is more than just a mode of transportation – it's a reflection of your personality and style.

## UX

# Intuitive Navigation:
- clean and intuitive interface.
# Mobile Responsiveness:
- platform is fully responsive, ensuring optimal performance and usability across various devices.
# dark theam
- website has a dark theam wit colorfull buttons and navigation for easy navigations and comfortable for the eyes

### Colour Scheme

I've used bootsrap color 

- `#343a40` used for background.
- `#fffff` used for primary text.
- `#6c757d` used for navbar and footer.
- `#f8f9fa` used for primary buttons.

I used [coolors.co](https://coolors.co/e84610-009fe3-4a4a4f-445261-d63649-e6ecf0-000000) to generate my colour palette.

![screenshot](static/documentation/images/colorsp4.png)

### Typography

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## User Stories

### New Site Users

- As a new site user, I would like to Create an acoount.
- As a new site user, I would like to view treatment options.
- As a new site user, I would like to book a treatment option.

### Returning Site Users

- As a returning site user, I would like to Edit my email, if i want to change my email.
- As a returning site user, I would like to edit my password.
- As a returning site user, I would like to Cancel booking if i need to.
- As a returning site user, I would like to Log in, so that I can see my bookings.

### Site Admin

- As a site administrator, I should be able to view relevant info to every user.
- As a site administrator, I should be able to view which dates are booked and the user that booked them.
- As a site administrator, I should be able to remove users that abuse the site.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Figma](https://www.figma.com/) to design my site wireframes.

<details>
<summary> Click here to see the Mobile Wireframes < / summary >

Home
  - ![screenshot](static/documentation/images/wireframe-home.png)

Treatments
  - ![screenshot](static/documentation/images/wireframe-beha.png)

Profile
  - ![screenshot](static/documentation/images/wireframe-profil.png)

</details>


## Features

### Existing Features

- **404  500**

    - Custom 404 and 500 error pages

![screenshot](static/documentation/images/404e.png)![screenshot](static/documentation/images/500e.png)

- **Dashboard #2**

    - Dashboard for easy access to everything about your profile

![screenshot](static/documentation/images/dash.png)

- **Change Password**

    - Form for user to change password

![screenshot](static/documentation/images/andr-los.png)

- **Change Email**

    - Form for user to change email

![screenshot](static/documentation/images/andr-mail.png)

- **Calander**

    - Calander for users to see what dates are available and a easy way for user to pick a date for their booking,

![screenshot](static/documentation/images/cal.png)

- **Dashboard/Login**

    - Button that lets you log in or go to dashboard when logged in

![screenshot](static/documentation/images/prof.png)

### Future Features

- Contact #1
    - Contact form
- Google maps direction #2
    - Google maps directions to help people find the shop

## Tools & Technologies Used

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.
- [fontAwesome](https://fontawesome.com/) used for icons in footer

## Database Design

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models.
Understanding the relationships between different tables can save time later in the project.

![screenshot](static/documentation/images/erd2.png)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/jesperba01/mirusnordic_pp4/projects) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board.

![screenshot](static/documentation/images/pp4.png)

### GitHub Issues

[GitHub Issues](https://github.com/jesperba01/mirusnordic_pp4/issues) served as an another Agile tool.
There, I used my own **User Story Template** to manage user stories.

It also helped with milestone iterations on a weekly basis.

- [Open Issues](https://github.com/jesperba01/mirusnordic_pp4/issues)

    ![screenshot](static/documentation/images/issuesp4.png)

- [Closed Issues](https://github.com/jesperba01/mirusnordic_pp4/issues?q=is%3Aissue+is%3Aclosed)

    ![screenshot](static/documentation/images/issuesclose.png)

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://mirusnordic-f36ddbc9881a.herokuapp.com).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: mirusnordic_pp4).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/jesperba01/mirusnordic_pp4) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/jesperba01/mirusnordic_pp4.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/jesperba01/mirusnordic_pp4)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/jesperba01/mirusnordic_pp4)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Credits

### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | version control | "How to Write a Git Commit Message" |
| [Bootstrap](https://flexboxfroggy.com/) | entire site | modern responsive layouts |
| [StackOverflow](https://stackoverflow.com/a/2450976) | Trubble shoting | Info on how to fix bugs and outher problems |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |
| [Youtube](https://www.youtube.com/watch?v=nGIg40xs9e4) | Django instructions| Helpfull guide ont the basics of django |

### Media

[Nicklas Olsson] All images and logos were provided by my friend Nicklas who owns Mirus Nordic.

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for their support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support.
- I would like to thank Nicklas Olsson For supplying images and insperation on the project.

