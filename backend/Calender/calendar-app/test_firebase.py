import firebase_admin
from firebase_admin import credentials, firestore
import json

def test_firebase():
    try:
        # Initialize Firebase
        cred = credentials.Certificate('firebase-key.json')
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        
        # Test connection by adding a test document
        test_data = {
            'test': 'connection',
            'timestamp': firestore.SERVER_TIMESTAMP
        }
        
        doc_ref = db.collection('test_connection').document()
        doc_ref.set(test_data)
        
        print("✅ Firebase connection SUCCESSFUL!")
        print("✅ Test document written to Firestore")
        
        # Read it back to verify
        doc = doc_ref.get()
        if doc.exists:
            print("✅ Test document read SUCCESSFUL!")
            print(f"✅ Document data: {doc.to_dict()}")
        else:
            print("❌ Failed to read test document")
            
        # Clean up
        doc_ref.delete()
        print("✅ Test cleanup completed")
        
    except Exception as e:
        print(f"❌ Firebase connection FAILED: {e}")
        print("\nTroubleshooting steps:")
        print("1. Check if 'firebase-key.json' exists in the same folder")
        print("2. Verify the JSON file is valid")
        print("3. Check your internet connection")
        print("4. Make sure Firestore is enabled in Firebase console")

if __name__ == '__main__':
    test_firebase()