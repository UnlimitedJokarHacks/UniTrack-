import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("storage/emulated/0/Download/jokartracks-firebase-adminsdk-2bcxs-e889ab7897.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Function to retrieve location from the database
def get_location(link):
    doc_ref = db.collection(u'links').document(link)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict().get('location')
    else:
        return None

# Example usage:
if __name__ == "__main__":
    link = input("Enter the tracking link: ")
    location = get_location(link)
    if location:
        print("Location: ", location)
    else:
        print("Invalid or expired tracking link.")
