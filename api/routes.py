from fastapi import APIRouter
from gym import routes as gym_endpoints
from users.auth import auth_backend
from users.schemas import UserRead, UserCreate, UserUpdate
from users.utils import fastapi_users


routes = APIRouter()

routes.include_router(
    gym_endpoints.router,
    prefix="/api",
    tags=["api"]
)

routes.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=True),
    prefix="/auth/jwt",
    tags=["auth"],
)

routes.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

routes.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)

routes.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

routes.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate, requires_verification=True),
    prefix="/users",
    tags=["users"],
)
