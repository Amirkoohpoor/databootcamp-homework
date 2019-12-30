

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo
from flask import Flask, render_template

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.urls_db
collection = db.urls

# Drops collection if available to remove duplicates
db.urls.drop()


# Creates a collection in the database and inserts two documents
db.urls.insert_many([{"title":titles, "more explanation":explain, "current Featured Mars Image":img_link,
        "Mars Weather":mars_weather, "Mars Facts":df[0],"Mars Hemispheres":hemisphere_image_urls}])

# Set route
@app.route('/')
def index():
    # Store the entire urls collection in a list
    urls = list(db.urls.find())
    print(urls)

    # Return the template with the urls list passed in
    return render_template('index.html', urls=urls)


if __name__ == "__main__":
    app.run(debug=True)

