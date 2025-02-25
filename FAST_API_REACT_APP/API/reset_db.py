from database import engine
import models

def reset_database():
    print("Dropping all tables...")
    models.Base.metadata.drop_all(bind=engine)
    
    print("Recreating tables...")
    models.Base.metadata.create_all(bind=engine)
    
    print("Database reset successfully!")

if __name__ == "__main__":
    reset_database()

# In your terminal, execute:
# python reset_db.py
