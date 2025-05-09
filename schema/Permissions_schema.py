from pydantic import BaseModel, EmailStr
from typing import Optional


# ------------------- Permissions_Roll -------------------
class PermissionsRollBase(BaseModel):
    Name_Roll: str
    Status: int
class PermissionsRollCreate(PermissionsRollBase):
    pass

class PermissionsRollUpdate(BaseModel):
    Name_Roll: Optional[str]
    Status: int
class PermissionsRoll(PermissionsRollBase):
    IDRoll: int

    class Config:
        from_attributes = True


# ------------------- Permissions_Screen -------------------
class PermissionsScreenBase(BaseModel):
    Name: str
    Url: str
    Status: int
class PermissionsScreenCreate(PermissionsScreenBase):
    pass

class PermissionsScreenUpdate(BaseModel):
    Name: Optional[str]
    Url: Optional[str]
    Status: int
class PermissionsScreen(PermissionsScreenBase):
    IDScreen: int

    class Config:
        from_attributes = True


# ------------------- Permissions_Users -------------------
class PermissionsUserBase(BaseModel):
    IDRoll: int
    Name: str
    Email: EmailStr
    Password: str
    Status: int
class PermissionsUserCreate(PermissionsUserBase):
    pass

class PermissionsUserUpdate(BaseModel):
    IDRoll: int
    Name: Optional[str]
    Email: Optional[EmailStr]
    Password: Optional[str]
    Status: int
class PermissionsUser(PermissionsUserBase):
    IDUsers: int

    class Config:
        from_attributes = True


# ------------------- PermissionsAccess -------------------
class PermissionsAccessBase(BaseModel):
    IDUsers: int
    IDRoll: int
    IDScreen: int
    Status: int

class PermissionsAccessCreate(PermissionsAccessBase):
    pass

class PermissionsAccessUpdate(BaseModel):
    IDUsers: Optional[int]
    IDRoll: Optional[int]
    IDScreen: Optional[int]
    Status: Optional[int]

class PermissionsAccess(PermissionsAccessBase):
    IDAccess: int

    class Config:
        from_attributes = True

