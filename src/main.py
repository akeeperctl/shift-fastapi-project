from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from fastapi_cache import FastAPICache

from src.user_employee.schemas import EmployeeRead, UserEmployeeCreate
from src.role.routers import role_router
from src.auth.auth import auth_backend
from src.auth.user_manager import get_user_manager

from src.job.routers import job_router

app = FastAPI(title="Shift Python Project")
app_users = FastAPIUsers(
    get_user_manager=get_user_manager,
    auth_backends=[auth_backend]
)
app_cache = FastAPICache()


app.include_router(
    app_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    app_users.get_register_router(EmployeeRead, UserEmployeeCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    app_users.get_users_router(EmployeeRead, UserEmployeeCreate),
    prefix="/employees",
    tags=["employees"],
)
app.include_router(
    app_users.get_verify_router(EmployeeRead),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(job_router)
app.include_router(role_router)


# @app.on_event("startup")
# async def on_startup():
#     app_cache.init()