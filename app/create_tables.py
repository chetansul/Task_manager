from app.database import Base, engine
from app.models import User

# # Drop all → for development only!
# Base.metadata.drop_all(bind=engine)

# # Create tables again
# Base.metadata.create_all(bind=engine)

User.__table__.create(bind=engine, checkfirst=True)