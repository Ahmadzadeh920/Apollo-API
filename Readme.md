# Django Apollo.io API Integration

This project is a Django application that integrates with Apollo.io to fetch data related to people using specified parameters with selenium library. The application is designed to follow best practices in setting up a Django project, Selenium and utilizes MySQL as the database backend.

## Project Overview

## Clone the repo
Clone this repo anywhere you want and move into the directory:
```bash
git clone https://github.com/Ahmadzadeh920/Advanced-Chat-project.git
```

1. **Set Up a Django Project**: 
  *The first time you run this it's going to take 5-10 minutes depending on your
internet connection speed and computer's hardware specs. That's because it's
going to download a few Docker images and build the Python + requirements dependencies.*

```bash
docker-compose up --build
```


Now that everything is built and running we can treat it like any other Django
app

2. **Develop Models**: 
```bash
docker-compose exec backend sh -c sh -c "python manage.py makemigrations"
docker-compose exec backend sh -c sh -c "python manage.py migrate"
 ```  

3. **Login to External Service**: 
   - with the the library selenium, This application authenticates and logs in to Apollo.io using the provided credentials.
     - **Username**: sophie@skyhighsalescontact.com
     - **Password**: Thankyouforyourassessment24

4. **Listen for Requests and Fetch Data**: 
   - The application listens for incoming requests and navigates to the Apollo People page.
   - It identifies and captures the request for `https://app.apollo.io/api/v1/mixed_people/search`, extracting the cookie, headers, and payload from this request.
   - The extracted data (URL, cookies, headers, and payload) is then stored in the database using the previously created model.

