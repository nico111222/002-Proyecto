from fastapi import FastAPI
from routes.Permissions_roll_routes import router as permissions_roll_router
from routes.Permission_screen_routes import router as permissions_screen_router
from routes.Permission_users_routes import router as Permission_users_routes
from routes.Permission_access_routes import router as Permission_access_routes

app = FastAPI()

# Incluir los routers en la aplicación
app.include_router(permissions_roll_router)
app.include_router(permissions_screen_router)
app.include_router(Permission_users_routes)
app.include_router(Permission_access_routes)

