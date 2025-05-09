from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.conn import get_db
from schema.Permissions_schema import PermissionsRollCreate, PermissionsRollUpdate, PermissionsRoll
from model.Permissions_model import Permissions_Roll

router = APIRouter(tags=["Permissions_Roll"])

# Obtener todos los Roles
@router.get("/get_roles", response_model=list[PermissionsRoll])
def get_roles(db: Session = Depends(get_db)):
    roles = db.query(Permissions_Roll).all()
    if not roles:
        raise HTTPException(status_code=404, detail="No roles found")
    return roles

# Obtener un Rol por ID
@router.get("/get_role_id", response_model=PermissionsRoll)
def get_role(id: int, db: Session = Depends(get_db)):
    role = db.query(Permissions_Roll).filter(Permissions_Roll.IDRoll == id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

# Crear un nuevo Rol
@router.post("/create_role", response_model=PermissionsRoll)
def create_role(role: PermissionsRollCreate, db: Session = Depends(get_db)):
    # Verificar si el rol ya existe
    db_role = db.query(Permissions_Roll).filter(Permissions_Roll.Name_Roll == role.Name_Roll).first()
    if db_role:
        raise HTTPException(status_code=400, detail="Role already exists")

    db_role = Permissions_Roll(Name_Roll=role.Name_Roll)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

# Actualizar un Rol existente
@router.put("/update_role", response_model=PermissionsRoll)
def update_role(id: int, role: PermissionsRollUpdate, db: Session = Depends(get_db)):
    db_role = db.query(Permissions_Roll).filter(Permissions_Roll.IDRoll == id).first()
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")

    # Solo actualizar si hay cambios
    if role.Name_Roll:
        db_role.Name_Roll = role.Name_Roll
    
    db.commit()
    db.refresh(db_role)
    return db_role

#Eliminar
@router.delete("/delete_role", response_model=PermissionsRoll)
def delete_role(id: int, db: Session = Depends(get_db)):
    db_role = db.query(Permissions_Roll).filter(Permissions_Roll.IDRoll == id).first()
    if not db_role:
        raise HTTPException(status_code=404, detail="Role not found")

    db_role.Status = 0  # Marcamos como eliminado
    db.commit()
    db.refresh(db_role)
    return db_role







