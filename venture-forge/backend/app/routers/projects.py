"""项目管理API路由"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.database import get_db
from ..services.project_service import ProjectService
from ..schemas.project import ProjectCreate, ProjectResponse

router = APIRouter(prefix="/api/v1/projects", tags=["projects"])


@router.post("/", response_model=ProjectResponse)
async def create_project(
    data: ProjectCreate,
    db: AsyncSession = Depends(get_db),
):
    service = ProjectService(db)
    project = await service.create(data)
    return project


@router.get("/", response_model=list[ProjectResponse])
async def list_projects(
    user_id: str,
    limit: int = 20,
    db: AsyncSession = Depends(get_db),
):
    service = ProjectService(db)
    projects = await service.list_by_user(user_id=user_id, limit=limit)
    return projects


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: str,
    db: AsyncSession = Depends(get_db),
):
    service = ProjectService(db)
    project = await service.get_by_id(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.post("/{project_id}/deploy")
async def deploy_project(
    project_id: str,
    deploy_url: str,
    db: AsyncSession = Depends(get_db),
):
    service = ProjectService(db)
    project = await service.deploy(project_id, deploy_url)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deployed successfully", "project": project}
