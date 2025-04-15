from app.database import Base, engine
from app import models

# Drop all → for development only!
Base.metadata.drop_all(bind=engine)

# Create tables again
Base.metadata.create_all(bind=engine)