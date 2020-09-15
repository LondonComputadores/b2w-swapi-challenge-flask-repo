# b2w-swapi-challenge-flask-repo
This is a code challenge for the B2W where I'm going to develop an application based on REST API to consume the SWAPI and then save it into a NoSQL Database and also create some tests.


                        B2W SWAPI CODE CHALLENGE

Initializing the War:

 - Dockerizing the application: $ docker pull mongo
 - Creating a container for MongoDB: $ docker create -it --name MongoTest -p 5000:27017 mongo
 - Running the container always after it's been created: $ docker start MongoTest
 - Stopping the container: $ docker stop MongoTest


Installing the Python REST Frameworks:

 - Installing Flask-RESTframework: $ pip install flask-restful
 - Installing Flask-PyMongo: $ pip install Flask-PyMongo