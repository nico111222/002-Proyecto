from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.conn import get_db
from schema.Permissions_schema import PermissionsAccess, PermissionsAccessCreate,PermissionsAccessUpdate
from model.Permissions_model import Permissions_Access

router = APIRouter(tags=["Permissions_Access"])

# Obtener todos los usuarios
@router.get("/get_access", response_model=list[PermissionsAccess])
def get_access(db: Session = Depends(get_db)):
    access = db.query(Permissions_Access).all()
    if not access:
        raise HTTPException(status_code=404, detail="No users found")
    return access

# Obtener un usuario por ID
@router.get("/get_access_id", response_model=PermissionsAccess)
def get_access(id: int, db: Session = Depends(get_db)):
    access = db.query(Permissions_Access).filter(Permissions_Access.IDAccess == id).first()
    if not access:
        raise HTTPException(status_code=404, detail="User not found")
    return access

# Crear un nuevo usuario
@router.post("/create_access", response_model=PermissionsAccess)
def create_access(access: PermissionsAccessCreate, db: Session = Depends(get_db)):

    
    # Crear el nuevo usuario con los campos necesarios
    db_access = Permissions_Access(
        IDUsers=access.IDUsers,
        IDRoll=access.IDRoll,
        IDScreen=access.IDScreen,
        Status=access.Status
    )
    db.add(db_access)
    db.commit()
    db.refresh(db_access)
    return db_access

#Actualiza
@router.put("/update_access", response_model=PermissionsAccess)
def update_access(id:int,access: PermissionsAccessUpdate, db: Session = Depends(get_db)):
 # Buscar por ID
    db_access = db.query(Permissions_Access).filter(Permissions_Access.IDAccess == id).first()
    
    # Actualizar solo los campos provistos
    if access.IDUsers is not None:
        db_access.IDUsers = access.IDUsers
    if access.IDRoll is not None:
        db_access.IDRoll = access.IDRoll
    if access.IDScreen is not None:
        db_access.IDScreen = access.IDScreen
    if access.Status is not None:
        db_access.Status = access.Status 
    db.commit()
    db.refresh(db_access)
    return db_access

#Elimina
@router.delete("/delete_access/{id}", response_model=PermissionsAccess)
def delete_access(id: int, db: Session = Depends(get_db)):
    db_access = db.query(Permissions_Access).filter(Permissions_Access.IDAccess == id).first()
    
    if not db_access:
        raise HTTPException(status_code=404, detail="Access not found")

    db_access.Status = 0
    db.commit()
    db.refresh(db_access)
    return db_access
