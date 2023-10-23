from fastapi import APIRouter
from src.endpoints import document,department,departmentAdmin,managementFlow,documentType,templateFlow,attachment,userProfile,signature
from fastapi.middleware import Middleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

router = APIRouter()

router.include_router(document.router)
router.include_router(department.router)
router.include_router(templateFlow.router)
router.include_router(managementFlow.router)
router.include_router(departmentAdmin.router)
router.include_router(documentType.router)
router.include_router(attachment.router)
router.include_router(userProfile.router)
router.include_router(signature.router)
