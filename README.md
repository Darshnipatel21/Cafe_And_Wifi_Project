****************************************************************Cafe and Wifi Finder********************************************************************

****Overview****
Cafe and Wifi Finder is a Flask web application that helps users find cafes with specific amenities such as wifi, toilets, sockets, and the ability to take calls. 
Users can also add new cafes to the database through a form.

****Skills and Knowledge Gained****

*Web Development with Flask

    > Routing and Views: Implemented various routes to handle different functionalities in the application, such as displaying 
      all cafes, filtering cafes, and adding new cafes.
    > Templating with Jinja2: Used Jinja2 templating engine to dynamically render HTML pages with data from the database.
    > Static Files Management: Managed static files like CSS and JavaScript for styling and interactivity.
    
*Database Management with SQLAlchemy

    > Database Design: Designed and implemented the database schema for the cafes, including fields like name, map URL, image URL,
      location, seats, and amenities.
    > ORM (Object-Relational Mapping): Used SQLAlchemy to interact with the SQLite database, performing CRUD operations seamlessly.
    > Data Validation: Ensured data integrity with proper field validation using SQLAlchemy and WTForms validators.
    
*Form Handling with Flask-WTF

    > Form Creation: Created forms using Flask-WTF for adding new cafes, ensuring that user inputs are validated before submission.
    > Form Rendering: Rendered forms in HTML templates using Flask-WTF's render_form utility, providing a user-friendly interface 
      for data input.

*Frontend Development with Bootstrap

    > Responsive Design: Utilized Bootstrap to create a responsive and visually appealing user interface that works well on both 
      desktop and mobile devices.
    > Filter UI: Designed an intuitive filter interface to allow users to filter cafes based on their amenities.
    > Sticky Header and Filter Section: Implemented sticky headers and filter sections for better user experience and accessibility.

*Deployment and Configuration

    > Application Configuration: Configured the Flask application with necessary settings, including secret keys and database URI.
    > Virtual Environment Management: Managed project dependencies using virtual environments, ensuring a clean and isolated 
      development setup.

*REST API Development

    > API Endpoints: Created RESTful API endpoints for interacting with the cafes database programmatically.
    > JSON Responses: Implemented endpoints to return data in JSON format, making it easy to integrate with other services or 
      applications.
    > CRUD Operations: Enabled create, read, update, and delete operations via the API.

    
****Project Structure****

    cafe-and-wifi-finder/
    ├── templates/
    │   ├── add_cafe.html
    │   ├── header.html
    │   ├── index.html
    │   ├── joincommunity.html
    │   ├── register.html
    ├── forms.py
    ├── main.py
    ├── models.py
    ├── requirements.txt
    └── README.md
    
    templates/: Contains the HTML templates for the project.
    forms.py: Contains the Flask-WTF form classes.
    main.py: The main Flask application file.
    requirements.txt: A list of Python dependencies.


****Key Features****

    > View All Cafes: Displays a list of all cafes with their details.
    > Filter Cafes: Allows users to filter cafes based on amenities.
    > Add New Cafe: A form for users to add new cafes to the database.
    > REST API: Provides API endpoints for interacting with the cafes database.


****Installation and Setup****

*Clone the repository:

   git clone https://github.com/your-username/cafe-and-wifi-finder.git
   cd cafe-and-wifi-finder
   
*Create a virtual environment:

    python -m venv venv

*Activate the virtual environment:

    On Windows:
        venv\Scripts\activate
    On macOS/Linux:
        source venv/bin/activate

*Install the dependencies:

    pip install -r requirements.txt

*Create the database:
   
    from main import db, app
    with app.app_context():
        db.create_all()

*Run the application:
   
    flask run
    Open your browser and go to http://127.0.0.1:5000/.

*REST API (Documentation link):
   
    https://documenter.getpostman.com/view/33062723/2sA3e5eTdz
    
****Future Improvements****
    
    > User Authentication: Implement user authentication to allow users to save their favorite cafes.
    > Enhanced Filtering: Add more filtering options, such as price range and opening hours.
    > Ratings and Reviews: Allow users to rate and review cafes.

****Conclusion****

This project helped me gain practical experience in web development with Flask, database management with SQLAlchemy, form handling 
with Flask-WTF, and frontend development with Bootstrap. It also taught me how to structure a web application, manage dependencies,
develop REST APIs, and ensure a responsive and user-friendly interface.

![image](https://github.com/user-attachments/assets/1f1818da-f0cc-4722-b7ad-ffdf76b7f72a)

