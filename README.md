# Retrospective


## Project Overview
Retrospective is a unique social media platform designed to showcase Polaroid-style photos and albums, allowing users to share significant moments from their lives from their own perspectives. This platform aims to create a community centered around gratitude, positivity, and the appreciation of life's highlights. Unlike typical social media where every detail is shared, Retrospective focuses on meaningful memories that users want to cherish and remember.



## Table of Contents

1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
   - [Polaroid Photo Sharing](#polaroid-photo-sharing)
   - [Interactive Community](#interactive-community)
   - [Albums for Special Moments](#albums-for-special-moments)
   - [Follow Friends and Family](#follow-friends-and-family)
   - [Search and Discovery](#search-and-discovery)
   - [User Profiles](#user-profiles)
   - [Community Guidelines](#community-guidelines)
3. [Purpose and Strategy](#purpose-and-strategy)
4. [Retrospective Development Plan](#retrospective-development-plan)
   - [First Sprint](#first-sprint)
   - [Second Sprint](#second-sprint)
   - [Third Sprint](#third-sprint)
   - [Fourth Sprint](#fourth-sprint)
5. [API Endpoints with Tied User Stories](#api-endpoints-with-tied-user-stories)
   - [User Management](#user-management)
   - [Retrospective Posts](#retrospective-posts)
   - [Comments](#comments)
   - [Engagement and Interactivity](#engagement-and-interactivity)
   - [Profiles and Discovery](#profiles-and-discovery)
   - [Search and Discovery](#search-and-discovery-1)
   - [Activity Feed and Notifications](#activity-feed-and-notifications)
   - [Messaging](#messaging)
6. [Reporting](#reporting)
   - [Report Inappropriate Content](#report-inappropriate-content)
7. [Miscellaneous](#miscellaneous)
   - [Image Upload and Google Cloud Storage Integration](#image-upload-and-google-cloud-storage-integration)
   - [Contact Form](#contact-form)
8. [Security Implementation](#security-implementation)
   - [Permissions Class: IsOwnerOrReadOnly](#permissions-class-isownerorreadonly)
   - [Cloudinary Permissions for Service Account](#cloudinary-permissions-for-service-account)
9. [Technologies](#technologies)
10. [Libraries & Tools](#libraries--tools)
11. [Forking a GitHub Repository](#forking-a-github-repository)
    - [After Forking](#after-forking)
12. [Cloudinary](#cloudinary)
    - [Step 1: Sign Up for Cloudinary](#step-1-sign-up-for-cloudinary)
    - [Step 2: Install Required Packages](#step-2-install-required-packages)
    - [Step 3: Configure Django Settings](#step-3-configure-django-settings)
    - [Step 4: Create a Model for Image Uploads](#step-4-create-a-model-for-image-uploads)
13. [Heroku Deployment](#heroku-deployment)


## Key Features

### **Polaroid Photo Sharing**
- **Capture and Share**: Upload Polaroid-style photos that reflect your most cherished memories. Each photo can be accompanied by a heartfelt caption that adds context and emotion to the moment.
- **Editing Tools**: Use built-in filters and editing options to enhance your photos and give them that classic Polaroid feel, ensuring they stand out in your profile.

### **Interactive Community**
- **Engagement**: Interact with other users by liking and commenting on their Polaroid photos, fostering connections through shared experiences.
- **Notifications**: Stay updated with real-time notifications when someone engages with your posts or comments on your highlights.

### **Albums for Special Moments**
- **Create Custom Albums**: Organize your photos into themed albums (e.g., vacations, celebrations, milestones) to tell a cohesive story and preserve your memories in a structured way.
- **Private and Public Options**: Choose whether your albums are public for everyone to see or private, allowing only selected friends and family to view them.

### **Follow Friends and Family**
- **Building Connections**: Follow friends, family, and other users to stay updated on their significant moments, creating a personalized feed filled with meaningful content.
- **Mutual Following**: Receive follow requests and manage your connections easily to cultivate a supportive community.

### **Search and Discovery**
- **Keyword Search**: Discover content that resonates with you by searching for specific keywords, themes, or moments.
- **Category Browsing**: Explore photos and albums categorized by events, seasons, or emotions, making it easy to find inspiration and connect with like-minded individuals.

### **User Profiles**
- **Personalized Profiles**: Create a unique profile that showcases your favorite Polaroid photos and albums, allowing you to express your individuality and perspective on life.
- **Statistics and Highlights**: View engagement metrics on your posts and see which moments resonate most with your audience.

### **Community Guidelines**
- **Positive Environment**: Retrospective is built on the principles of respect and support. Users are encouraged to share meaningful moments and uplift one another, creating a positive online atmosphere.
- **Reporting and Moderation**: A system is in place for reporting inappropriate content, ensuring that the community guidelines are upheld and that the platform remains a safe space for all users.


## Purpose and Strategy
Retrospective aims to provide a dedicated space for users to celebrate life’s special moments, encouraging reflection and connection through the art of photography. This platform focuses on highlighting the experiences that shape our lives rather than sharing every mundane detail, allowing users to create a lasting legacy of their most treasured memories.

Designed to foster gratitude and enhance users' perspectives on life, Retrospective draws inspiration from my own Polaroid album, which is a replica of one my mother used to have when she was young. This project seeks to evoke comfort and a sense of nostalgia. The retro style of the platform pays homage to the past while offering a reliable and unique space for users to celebrate their lives.

By blending purpose with strategy, Retrospective not only serves as a digital gallery for cherished moments but also cultivates a supportive community where users can reflect on and share what truly matters.

#### User Stories

For more details on the user stories go to the [projects KANBAN board](https://github.com/users/naomi-mali/projects/11)

# Retrospective Development Plan

## First Sprint
- **Create an Account & Login**
  - Landing Page
  - Navbar
  - Create Account
  - Log In
  - Log Out
  - Remain Logged In

## Second Sprint
- **Creating Retrospectives**
  - Create Retrospective
  - View Retrospective
  - Update a Retrospective
  - Delete Retrospective

- **Retrospective Feeds**
  - Retrospectives Feed
  - Liked Retrospectives
  - Discover Retrospectives

## Third Sprint
- **Profile Pages**
  - Edit Profile
  - Change Password
  - Who to Follow List
  - User Profiles

- **Interactivity**
  - Like/Un-like a Retrospective
  - Comment on a Retrospective
  - View Comments
  - Edit a Comment
  - Delete a Comment
  - Follow/Unfollow a User

## Fourth Sprint
- **General**
  - Contact Form
  - Responsive Site
  - Simple User Navigation
  - 404 Page

- **User Engagement Features**
  - Update Username and Password
  - Create Posts
  - View Posts of Followed Users
  - Edit Post
  - Delete a Post
  - Create and List Comments
  - View Comments
  - Edit Comment
  - Delete Comments
  - Like a Post
  - View Profile Page
  - Profile List
  - Search Posts by Keyword
  - Messaging
  - View Liked Posts
  - View Activity Feed
  - Report Post for Inappropriate Content
  - Report a Comment
  - Tag Users in Comments
  - Add Post Location
  - Infinite Scroll (for Posts and Comments)
  - Add Google Cloud Storage for Static Images
  - Messaging - Chat
  - Filter Messages
  - Most Followed Profiles
  - Landing Page
  - Log Out Setup
  - Navigation - Conditional Rendering
  - Add Site Favicon
  - User Profile - User Stats
  - Create Contact
  - View a Post
  - Navigation
  - Search Profile
  - Routing
  - Avatar

This plan outlines the sprints needed for the development of Retrospective, with a clear focus on user account management, content creation, interaction features, and overall site functionality. Each sprint builds on the previous one, gradually enhancing the platform's capabilities while ensuring a seamless user experience.

**API Endpoints with Tied User Stories**

---

**User Management**

1. **User Registration & Login**
   - **User Story:** *As a user, I can create an account and log in so that I can access platform features.*
   - **Endpoints:**
     - **POST /api/register** - Create new account.
     - **POST /api/login** - Authenticate and log in user.
     - **POST /api/logout** - End user session.

2. **Edit Profile**
   - **User Story:** *As a user, I can edit my profile so that I can update my personal information.*
   - **Endpoints:**
     - **GET /api/user/profile** - Fetch logged-in user profile.
     - **PUT /api/user/update** - Update username, bio, profile picture.
     - **PUT /api/user/change-password** - Securely change password.

3. **Delete Account**
   - **User Story:** *As a user, I can delete my account so that I can remove my profile and content.*
   - **Endpoint:**
     - **DELETE /api/user/delete** - Delete account and associated data.

---

**Retrospective Posts**

4. **Create and Manage Retrospectives**
   - **User Story:** *As a user, I can create, view, update, and delete retrospectives so that I can share significant moments.*
   - **Endpoints:**
     - **POST /api/retrospectives** - Create a new retrospective.
     - **GET /api/retrospectives** - View list of retrospectives.
     - **GET /api/retrospectives/:id** - View specific retrospective details.
     - **PUT /api/retrospectives/:id** - Edit a retrospective.
     - **DELETE /api/retrospectives/:id** - Delete a retrospective.

5. **Add Post Location**
   - **User Story:** *As a user, I can add a location to my retrospectives so they are contextualized geographically.*
   - **Endpoint:**
     - **GET /api/locations** - Fetch list of locations for tagging.

---

**Comments**

6. **Comment on Retrospectives**
   - **User Story:** *As a user, I can comment on retrospectives so that I can engage with content.*
   - **Endpoints:**
     - **POST /api/retrospectives/:id/comments** - Add comment to a retrospective.
     - **GET /api/retrospectives/:id/comments** - Fetch comments for a specific retrospective.

7. **Edit and Delete Comments**
   - **User Story:** *As a user, I can edit and delete my comments so that I have control over my interactions.*
   - **Endpoints:**
     - **PUT /api/comments/:commentId** - Edit a comment.
     - **DELETE /api/comments/:commentId** - Delete a comment.

---

**Engagement and Interactivity**

8. **Like/Unlike Retrospectives**
   - **User Story:** *As a user, I can like or unlike retrospectives so that I can show appreciation for content.*
   - **Endpoints:**
     - **POST /api/retrospectives/:id/like** - Like a retrospective.
     - **DELETE /api/retrospectives/:id/unlike** - Unlike a retrospective.
     - **GET /api/user/liked-retrospectives** - View retrospectives liked by user.

9. **Follow/Unfollow Users**
   - **User Story:** *As a user, I can follow and unfollow users to personalize my feed and build my community.*
   - **Endpoints:**
     - **POST /api/user/:id/follow** - Follow another user.
     - **DELETE /api/user/:id/unfollow** - Unfollow a user.
     - **GET /api/user/following** - View users the user is following.
     - **GET /api/user/followers** - View user’s followers.

10. **Tag Users in Comments**
    - **User Story:** *As a user, I can tag users in my comments so they are notified and can engage in discussions.*
    - **Endpoint:**
      - **POST /api/retrospectives/:id/comments** (with tagging functionality).

---

**Profiles and Discovery**

11. **Profile Management**
    - **User Story:** *As a user, I can view and edit profiles to share and update personal information.*
    - **Endpoints:**
      - **GET /api/user/:id/profile** - View specific user’s profile by ID.
      - **PUT /api/user/update** - Update user profile information.

12. **View Suggested and Popular Profiles**
    - **User Story:** *As a user, I can discover popular and suggested users so I can follow interesting profiles.*
    - **Endpoints:**
      - **GET /api/user/suggested** - Fetch suggested users list.
      - **GET /api/popular-profiles** - Fetch list of most-followed profiles.

---

**Search and Discovery**

13. **Search Retrospectives and Profiles**
    - **User Story:** *As a user, I can search for retrospectives and profiles to find specific content and users.*
    - **Endpoints:**
      - **GET /api/search/retrospectives** - Search retrospectives by keyword.
      - **GET /api/search/profiles** - Search profiles by username or keyword.

14. **Discover Highlights**
    - **User Story:** *As a user, I can explore a curated feed of highlights to find inspiration and new connections.*
    - **Endpoint:**
      - **GET /api/retrospectives/discover** - Discover a curated feed of retrospectives.

---

**Activity Feed and Notifications**

15. **View Activity Feed**
    - **User Story:** *As a user, I can see an activity feed of users I follow to stay updated on their interactions.*
    - **Endpoint:**
      - **GET /api/user/activity** - Fetch recent activity of followed users.

---

**Messaging**

16. **Messaging and Conversations**
    - **User Story:** *As a user, I can send and receive messages in real-time with other users.*
    - **Endpoints:**
      - **POST /api/messages** - Send messages to users.
      - **GET /api/messages/conversations** - View conversations.
      - **GET /api/messages/:conversationId** - View messages within a specific conversation.
      - **GET /api/messages/unread** - Fetch count of unread messages.

---

**Reporting**

17. **Report Inappropriate Content**
    - **User Story:** *As a user, I can report inappropriate posts and comments to help maintain a positive community.*
    - **Endpoints:**
      - **POST /api/retrospectives/:id/report** - Report a retrospective.
      - **POST /api/comments/:commentId/report** - Report a comment.

---

**Miscellaneous**

18. **Image Upload and Google Cloud Storage Integration**
    - **User Story:** *As a developer, I can integrate Cloudinary Cloud Storage to handle image uploads.*
    - **Endpoint:**
      - **POST /api/upload** - Upload images to Cloudinary Storage.

19. **Contact Form**
    - **User Story:** *As a user, I can submit a contact form to get support or make inquiries.*
    - **Endpoint:**
      - **POST /api/contact** - Submit a contact form request.

### Security Implementation

---

### Permissions Class: *IsOwnerOrReadOnly*

**User Story:**  
*As a developer, I need to ensure that only content creators can modify or delete their posts, preserving content integrity and user privacy.*

**Implementation:**  
A permissions class called `IsOwnerOrReadOnly` was implemented to restrict edit and delete actions on retrospectives and comments to their respective creators. This class checks if the authenticated user is the creator of the content, allowing full access if they are, or limiting them to read-only access otherwise.

---

### Cloudinary Permissions for Service Account

**User Story:**  
*As a developer, I need to configure service account permissions on Cloudinary to ensure security and restrict access to only necessary resources.*

**Implementation:**  
Permissions were configured for Cloudinary service account interactions, ensuring secure image upload and retrieval functionality. The minimal permissions include:
- **Create:** Permission to upload user images to Cloudinary storage.
- **Read:** Permission to retrieve and display stored images on the platform.

**Technologies**

---

- **Django**  
  - Main framework used for developing the Retrospective application, enabling a robust and scalable backend.

- **Django REST Framework (DRF)**  
  - API development framework, used to create and manage the RESTful endpoints that support the application's functionalities.

- **Cloudinary (GCP)**  
  - Cloud provider used specifically for static image hosting via Cloudinary Storage, ensuring efficient and reliable media storage.

- **Heroku**  
  - Platform-as-a-Service (PaaS) used for hosting the Retrospective application, providing a managed environment to deploy and scale.

- **Git**  
  - Version control system, facilitating code management and collaboration through feature branching, commit tracking, and change history.

- **GitHub**  
  - Code repository for securely storing the code base, documentation, and versioned project history.

 ### Languages and Frameworks
 - Python
 - Django Rest Framework
  pip install djangorestframework

  ### Libraries & Tools

- [Cloudinary](https://cloudinary.com/) - Image storage
- [Pillow](https://pypi.org/project/pillow/) - Image processing
- [Django Rest Auth](https://www.django-rest-framework.org/api-guide/authentication/#django-rest-auth-dj-rest-auth) - Authentication
- [Django AllAuth](https://docs.allauth.org/en/latest/index.html) - Authentication
- [Psycopg2](https://pypi.org/project/psycopg2/2.9.3/) - Python PostgreSQL Database Adapter
- [Gunicorn](https://pypi.org/project/gunicorn/20.1.0/) - Python WSGI HTTP Server
- [PostgreSQL](https://www.postgresql.org/) - Database
- [Lucid Chart](https://lucid.app/) - Database schema design
- [Tables Generator](https://www.tablesgenerator.com/markdown_tables) - Mark Down Tables
- [Table of Contents Generator](https://derlin.github.io/bitdowntoc/) - Table of Contents

### Forking a GitHub Repository

1. **Navigate to the GitHub Repository**:
   - Go to the repository you want to fork. You can find it by searching for the project or entering the URL directly.

2. **Click the Fork Button**:
   - On the top right corner of the repository page, you will see a button labeled **Fork**. Click on this button.

3. **Select Your Account**:
   - If you are a member of multiple organizations, GitHub may prompt you to choose where to create the fork (your personal account or one of your organizations). Select your account.

4. **Wait for the Process to Complete**:
   - GitHub will create a duplicate of the repository in your account. This may take a few moments.

5. **Access Your Fork**:
   - Once the forking process is complete, you will be redirected to your copy of the repository. You can start working on it from here.

### After Forking

- **Clone the Forked Repository**:
  - You can clone your forked repository to your local machine using the following command:
    ```bash
    git clone https://github.com/naomi-mali/api-retrospective
    ```
  - Replace `your-username` and `repository-name` with your GitHub username and the name of the repository.

- **Make Changes**:
  - You can now make changes to your local copy of the repository.

- **Push Changes**:
  - After making changes, commit them and push to your fork:
    ```bash
    git add .
    git commit -m "Your commit message"
    git push origin main
    ```
  - Adjust the branch name if you are working on a different branch.

- **Create a Pull Request** (Optional):
  - If you want to propose your changes back to the original repository, you can create a pull request. Go to the original repository, and you will often see an option to create a pull request for the changes in your fork.

-------

## Cloudinary

## Step 1: Sign Up for Cloudinary

1. **Create an Account**: Go to [Cloudinary](https://cloudinary.com/) and sign up for a free account.
2. **Get Your Credentials**: After signing up, navigate to your **Dashboard**. You will find your `API Key`, `API Secret`, and `Cloud Name` in the **Account Details** section.

## Step 2: Install Required Packages

Open your terminal and navigate to your Django project directory. Run the following command to install the necessary packages:

```
pip install django-cloudinary-storage  
pip install Pillow
```

- **cloudinary**: The official Cloudinary library for Python.
- **Pillow**: A Python Imaging Library for image processing.

## Step 3: Configure Django Settings

### Update `settings.py`

1. **Open your Django project’s `settings.py` file**.

2. **Add Cloudinary to Installed Apps**:

   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'cloudinary_storage',
       'django.contrib.staticfiles',
       'cloudinary',
       'rest_framework',
       # Your other apps
   ]
   ```

3. **Add Cloudinary Configuration**:

   At the bottom of your `settings.py`, add the following lines to configure Cloudinary:

   ```python
   import os
   from pathlib import Path

   if os.path.exists('env.py'):
       import env  # This imports your environment variables

   CLOUDINARY_STORAGE = {
       'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
   }

   MEDIA_URL = 'https://res.cloudinary.com/<your_cloud_name>/media/'
   DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
   ```


### Create `env.py`

1. **Create an `env.py` File**: In the root directory of your Django project, create a new file called `env.py`:

   ```
  env.py
   ```

2. **Add Your Cloudinary Configuration**: Open the `env.py` file and add your Cloudinary credentials:

   ```
   import os

   os.environ['CLOUDINARY_URL'] = 'cloudinary://<API_KEY>:<API_SECRET>@2c9njk'  # Update with your Cloudinary credentials
   ```

   Replace `<API_KEY>`, `<API_SECRET>` with your actual credentials from Cloudinary.


## Step 4: Create a Model for Image Uploads

In one of your Django apps (e.g., `profiles` or `posts`), create a model to handle image uploads. For example:

### Create a Model

1. **Open your models file (e.g., `models.py`)**.

2. **Define the model**:

   ```python
   from django.db import models

   class Profile(models.Model):
         image = models.ImageField(
               upload_to='images/', default='../default_profile_mjfgzn'
               )
Here's a refined guide for deploying your application to Heroku, specifically tailored for a Django REST Framework project using Cloudinary for image storage:

---

## Heroku Deployment 

1. **Create a Heroku Account**:
   - Navigate to the [Heroku website](https://www.heroku.com/) and sign up for a free account if you don’t already have one.

2. **Create a New App**:
   - Once logged in, click the **New** button in the top right corner of the dashboard.
   - Select **Create New App**.

3. **Enter App Details**:
   - **App Name**: Enter a unique name for your app.
   - **Region**: Choose the appropriate region for your app.
   - Click **Create App**.

4. **Configure Environment Variables**:
   - Go to the **Settings** tab.
   - Click on **Reveal Config Vars**.
   - Add the following configuration variables:
     - **SECRET_KEY**: (Your secret key)
     - **DATABASE_URL**: (This should already exist)
     - **ALLOWED_HOST**: (e.g., `your-heroku-app-name.herokuapp.com`)
     - **CLIENT_ORIGIN**: (URL for the client front-end React application that will be making requests to these APIs)
     - **CLIENT_ORIGIN_DEV**: (Address of the local server used for previewing and testing UI during development)
     - **CLOUDINARY_URL**: (e.g., `cloudinary://<API_KEY>:<API_SECRET>@<CLOUD_NAME>`)
  
6. **Deploy the Application**:
   - Click on the **Deploy** tab.
   - Scroll down to **Connect to GitHub** and sign in/authorize when prompted.
   - In the search box, find the repository you want to deploy and click **Connect**.
   - Scroll down to **Manual Deploy**, select the **main** branch (or your preferred branch), and click **Deploy Branch**.

7. **Run Migrations**:
   - After deployment, you may need to apply migrations. Run the following command:
     ```
     heroku run python manage.py migrate
     ```

8. **Collect Static Files**:
   - If your application uses static files, run:
     ```
     heroku run python manage.py collectstatic --noinput
     ```

9. **Open Your Application**:
   - Once everything is set up, open your deployed application in the browser:
     ```
     heroku open
     ```

10. **Monitor Logs**:
   - If you encounter any issues, check the logs for debugging:
     ```bash
     heroku logs --tail
     ```

---
