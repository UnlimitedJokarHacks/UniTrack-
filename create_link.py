import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random
import string

# Initialize Firebase Admin SDK
cred = credentials.Certificate("storage/emulated/0/Download/jokartracks-firebase-adminsdk-2bcxs-e889ab7897.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Function to generate a random string for the link
def generate_link(length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Function to create a new link in the database
def create_link(location):
    link = generate_link()
    doc_ref = db.collection(u'links').document(link)
    doc_ref.set({
        u'location': location
    })
    return link

# Example usage:
if __name__ == "__main__":
    location = input("Enter the location to track: ")
    link = create_link(location)
    print("Your tracking link is: http://yourdomain.com/track/{}".format(link))
