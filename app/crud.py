from sqlalchemy.orm import Session

from . import models, schemas


# Create operations
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(name= item.name, description=item.description)
    db.add(db_item)     # Add the new item to the session
    db.commit()         # Commit (save) the new item to the database
    db.refresh(db_item) # Refresh the instance to reflect the saved data (e.g., new ID)
    return db_item

# Read operation single item by id
def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

# Read operation all Items
def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Item).offset(skip).limit(limit).all()

# Update operation
def update_item(db: Session, item_id: int, updated_item: schemas.ItemUpdate):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    
    if db_item is None:
        return None

    # Updated name only if a new name is provided    
    if updated_item.name is not None and updated_item.name != "string":
        db_item.name = updated_item.name

    # Updated description only if a new description is provided    
    if updated_item.description is not None and updated_item.description != "string":
        db_item.description = updated_item.description

    db.commit()
    db.refresh(db_item)
    return db_item
       
# Delete operation
def delete_item(db: Session, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item: 
        db.delete(db_item)
        db.commit()
    return db_item 



