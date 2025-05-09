from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.conn import get_db
from schema.Permissions_schema import PermissionsScreen, PermissionsScreenCreate, PermissionsScreenUpdate
from model.Permissions_model import Permissions_Screen

router = APIRouter(tags=["Permissions_Screen"])

# Obtener todos los Screens
@router.get("/get_screens", response_model=list[PermissionsScreen])
def get_screens(db: Session = Depends(get_db)):
    screens = db.query(Permissions_Screen).all()
    if not screens:
        raise HTTPException(status_code=404, detail="No screens found")
    return screens

# Obtener un Screen por ID
@router.get("/get_screen_id", response_model=PermissionsScreen)
def get_screen(id: int, db: Session = Depends(get_db)):
    screen = db.query(Permissions_Screen).filter(Permissions_Screen.IDScreen == id).first()
    if not screen:
        raise HTTPException(status_code=404, detail="Screen not found")
    return screen

# Crear un nuevo Screen
@router.post("/create_screen", response_model=PermissionsScreen)
def create_screen(screen: PermissionsScreenCreate, db: Session = Depends(get_db)):
    # Verificar si el screen ya existe
    db_screen = db.query(Permissions_Screen).filter(Permissions_Screen.Name == screen.Name, Permissions_Screen.Url == screen.Url).first()
    if db_screen:
        raise HTTPException(status_code=400, detail="Screen already exists")
    
    # Crear el nuevo Screen con todos los campos necesarios
    db_screen = Permissions_Screen(
        Name=screen.Name,
        Url=screen.Url,
        Status=screen.Status
    )
    db.add(db_screen)
    db.commit()
    db.refresh(db_screen)
    return db_screen

#Actualiza
@router.put("/update_screen", response_model=PermissionsScreen)
def update_screen(id: int, screen: PermissionsScreenUpdate, db: Session = Depends(get_db)):
    # Buscar el Screen por ID
    db_screen = db.query(Permissions_Screen).filter(Permissions_Screen.IDScreen == id).first()
    
    if not db_screen:
        raise HTTPException(status_code=404, detail="Screen not found")
    
    # Actualizar los campos que han cambiado
    if screen.Name is not None:
        db_screen.Name = screen.Name
    if screen.Url is not None:
        db_screen.Url = screen.Url
    if screen.Status is not None:
        db_screen.Status = screen.Status
    
    # Confirmar los cambios en la base de datos
    db.commit()
    db.refresh(db_screen)
    
    return db_screen

#Actualiza
@router.put("/update_screen", response_model=PermissionsScreen)
def update_screen(id: int, screen: PermissionsScreenUpdate, db: Session = Depends(get_db)):
    # Buscar el Screen por ID
    db_screen = db.query(Permissions_Screen).filter(Permissions_Screen.IDScreen == id).first()
    
    if not db_screen:
        raise HTTPException(status_code=404, detail="Screen not found")
    
    # Actualizar los campos que han cambiado
    if screen.Name is not None:
        db_screen.Name = screen.Name
    if screen.Url is not None:
        db_screen.Url = screen.Url
    if screen.Status is not None:
        db_screen.Status = screen.Status
    
    # Confirmar los cambios en la base de datos
    db.commit()
    db.refresh(db_screen)
    
    return db_screen

#Delete
@router.delete("/delete_screen", response_model=PermissionsScreen)
def delete_screen(id: int, db: Session = Depends(get_db)):
    # Buscar el Screen por ID
    db_screen = db.query(Permissions_Screen).filter(Permissions_Screen.IDScreen == id).first()
    
    if not db_screen:
        raise HTTPException(status_code=404, detail="Screen not found")
    
    # Modificar solo el campo Status a 0
    db_screen.Status = 0
    
    # Confirmar los cambios en la base de datos
    db.commit()
    db.refresh(db_screen)
    
    return db_screen
