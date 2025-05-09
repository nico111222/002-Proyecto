from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.conn import get_db
from schema.Permissions_schema import PermissionsUser, PermissionsUserCreate,PermissionsUserUpdate
from model.Permissions_model import Permissions_Users

router = APIRouter(tags=["Permissions_Users"])

# Obtener todos los usuarios
@router.get("/get_users", response_model=list[PermissionsUser])
def get_users(db: Session = Depends(get_db)):
    users = db.query(Permissions_Users).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users

# Obtener un usuario por ID
@router.get("/get_user_id", response_model=PermissionsUser)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(Permissions_Users).filter(Permissions_Users.IDUsers == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Crear un nuevo usuario
@router.post("/create_user", response_model=PermissionsUser)
def create_user(user: PermissionsUserCreate, db: Session = Depends(get_db)):
    # Verificar si el usuario ya existe por email
    db_user = db.query(Permissions_Users).filter(Permissions_Users.Email == user.Email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")
    
    # Crear el nuevo usuario con los campos necesarios
    db_user = Permissions_Users(
        IDRoll=user.IDRoll,
        Name=user.Name,
        Email=user.Email,
        Password=user.Password,
        Status=user.Status
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#Actualiza
@router.put("/update_user", response_model=PermissionsUser)
def update_user(id:int,user: PermissionsUserUpdate, db: Session = Depends(get_db)):
 # Buscar por ID
    db_user = db.query(Permissions_Users).filter(Permissions_Users.IDUsers == id).first()
    
    # Actualizar solo los campos provistos
    if user.Name is not None:
        db_user.Name = user.Name
    if user.Email is not None:
        db_user.Email = user.Email
    if user.Password is not None:
        db_user.Password = user.Password
    db_user.IDRoll = user.IDRoll
    db_user.Status = user.Status

    db.commit()
    db.refresh(db_user)
    return db_user

#Elimina
@router.delete("/delete_user", response_model=PermissionsUser)
def delete_user(id:int,user: PermissionsUserUpdate, db: Session = Depends(get_db)):
 # Buscar por ID
    db_user = db.query(Permissions_Users).filter(Permissions_Users.IDUsers == id).first()
    
    # Actualizar solo los campos provistos
    db_user.Status = 0

    db.commit()
    db.refresh(db_user)
    return db_user
