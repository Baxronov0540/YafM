from starlette_admin.contrib.sqla import ModelView
from starlette_admin import FileField
from fastapi.requests import Request
from fastapi import UploadFile
from typing import Dict, Any
import os
import uuid
from app.models import User,Media,Worker,Labaratory,Section,Manaagement,Seminar,News,Slider
from app.utils import password_hash,looks_hashed
from app.database import async_session_maker

UPLOAD_DIR = "static/uploads"

async def save_media(file_path: str) -> int:
    """Create and save Media, return its ID"""
    async with async_session_maker() as session:
        media = Media(file_path=file_path)
        session.add(media)
        await session.flush()
        media_id = media.id
        await session.commit()
        return media_id
class UserView(ModelView):
    identity = "users"
    
    fields = ["id", "username", "first_name", "last_name", "is_active", "is_admin", "created_at", "updated_at"]
    exclude_fields_from_create = ["id", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at"]    
    exclude_fields_from_list = ["password"]

    async def before_edit(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        if "password" in data:
            pwd = data.get("password")
            if not pwd:
                data.pop("password", None)
                return
            if not looks_hashed(pwd):
                data["password"] = password_hash(pwd)

    async def before_create(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        pwd = data.get("password")
        if pwd and not looks_hashed(pwd):
            data["password"] = password_hash(pwd)


class MediaView(ModelView):
    identity = "media"
    fields = ["id", FileField("file"), "created_at", "updated_at"]
    exclude_fields_from_create = ["id", "file_path", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "file_path", "created_at", "updated_at"]

    async def before_create(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        file_data = data.get("file")
        up = None
        
        # FileField returns tuple: (UploadFile, is_deleted)
        if file_data:
            if isinstance(file_data, tuple):
                up, is_deleted = file_data
                if is_deleted:
                    up = None
            else:
                up = file_data
        
        if not up or not hasattr(up, "filename") or not up.filename:
            raise ValueError("Fayl yuklanishi zarur")
        
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        ext = os.path.splitext(up.filename)[1]
        filename = f"{uuid.uuid4().hex}{ext}"
        path = os.path.join(UPLOAD_DIR, filename)

        content = await up.read()
        with open(path, "wb") as f:
            f.write(content)

        url = f"/{UPLOAD_DIR}/{filename}"
        obj.file_path = url

        data.pop("file", None)

    async def before_edit(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        file_data = data.get("file")
        up = None
        
        # FileField returns tuple: (UploadFile, is_deleted)
        if file_data:
            if isinstance(file_data, tuple):
                up, is_deleted = file_data
                if is_deleted:
                    up = None
            else:
                up = file_data
        
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)

            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)

            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)

            url = f"/{UPLOAD_DIR}/{filename}"
            obj.file_path = url

        data.pop("file", None)


class WorkerView(ModelView):
    identity="workers"
    fields=[
        "id", "first_name", "last_name", "position", "email", "phone", 
        FileField("img_file"), "image_id", "created_at", "updated_at"
    ]
    exclude_fields_from_create = ["id", "image_id", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "image_id", "created_at", "updated_at"]

    async def before_create(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        file_data = data.get("img_file")
        up = None
        
        if file_data:
            if isinstance(file_data, tuple):
                up, is_deleted = file_data
                if is_deleted:
                    up = None
            else:
                up = file_data
        
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)
            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)
            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)
            url = f"/{UPLOAD_DIR}/{filename}"
            obj.image_id = await save_media(url)

        data.pop("img_file", None)

    async def before_edit(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        file_data = data.get("img_file")
        up = None
        
        if file_data:
            if isinstance(file_data, tuple):
                up, is_deleted = file_data
                if is_deleted:
                    up = None
            else:
                up = file_data
        
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)
            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)
            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)
            url = f"/{UPLOAD_DIR}/{filename}"
            obj.image_id = await save_media(url)

        data.pop("img_file", None)

class LabaratoryView(ModelView):
    identity="labaratories"
    fields=[
        "id", "name_uz", "name_en", "name_ru", "body_uz", "body_en", "body_ru", 
        "worker_id", FileField("img_file"), "image_id", "created_at", "updated_at"
    ]
    exclude_fields_from_create = ["id", "image_id", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "image_id", "created_at", "updated_at"]
    

    async def before_create(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        file_data = data.get("img_file")
        up = None
        
        if file_data:
            if isinstance(file_data, tuple):
                up, is_deleted = file_data
                if is_deleted:
                    up = None
            else:
                up = file_data
        
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)
            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)
            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)
            url = f"/{UPLOAD_DIR}/{filename}"
            obj.image_id = await save_media(url)

        data.pop("img_file", None)

    async def before_edit(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        file_data = data.get("img_file")
        up = None
        
        if file_data:
            if isinstance(file_data, tuple):
                up, is_deleted = file_data
                if is_deleted:
                    up = None
            else:
                up = file_data
        
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)
            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)
            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)
            url = f"/{UPLOAD_DIR}/{filename}"
            obj.image_id = await save_media(url)

        data.pop("img_file", None)

class SectionView(ModelView):
    identity="sections"
    fields=[
        "id", "name_uz", "name_en", "name_ru", "body_uz", "body_en", "body_ru", 
        "worker_id", FileField("img_file"), "image_id", "created_at", "updated_at"
    ]
    exclude_fields_from_create = ["id", "image_id", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "image_id", "created_at", "updated_at"]
    
    async def before_create(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        file_data = data.get("img_file")
        up = None
        
        if file_data:
            if isinstance(file_data, tuple):
                up, is_deleted = file_data
                if is_deleted:
                    up = None
            else:
                up = file_data
        
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)
            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)
            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)
            url = f"/{UPLOAD_DIR}/{filename}"
            obj.image_id = await save_media(url)

        data.pop("img_file", None)

    async def before_edit(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        file_data = data.get("img_file")
        up = None
        
        if file_data:
            if isinstance(file_data, tuple):
                up, is_deleted = file_data
                if is_deleted:
                    up = None
            else:
                up = file_data
        
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)
            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)
            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)
            url = f"/{UPLOAD_DIR}/{filename}"
            obj.image_id = await save_media(url)

        data.pop("img_file", None)

class ManaagementView(ModelView):
    identity="managements"
    fields=[
        "id", "first_name", "last_name", "position", "email", "phone", 
        "degree", "reception_hours", FileField("img_file"), "image_id", "created_at", "updated_at"
    ]
    exclude_fields_from_create = ["id", "image_id", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "image_id", "created_at", "updated_at"]
    
    async def before_create(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        file_data = data.get("img_file")
        up = None
        
        if file_data:
            if isinstance(file_data, tuple):
                up, is_deleted = file_data
                if is_deleted:
                    up = None
            else:
                up = file_data
        
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)
            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)
            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)
            url = f"/{UPLOAD_DIR}/{filename}"
            obj.image_id = await save_media(url)

        data.pop("img_file", None)

    async def before_edit(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        file_data = data.get("img_file")
        up = None
        
        if file_data:
            if isinstance(file_data, tuple):
                up, is_deleted = file_data
                if is_deleted:
                    up = None
            else:
                up = file_data
        
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)
            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)
            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)
            url = f"/{UPLOAD_DIR}/{filename}"
            obj.image_id = await save_media(url)

        data.pop("img_file", None)
class SeminarView(ModelView):
    identity="seminars"
    fields=[
        "id", "full_name", "description", "duration", "start_date", 
    ]
    exclude_fields_from_create = ["id"]
    exclude_fields_from_edit = ["id"]      

class DefenseView(ModelView):
    identity="defense"
    fields=[
        "id", "full_name", "description", "duration", "start_date", 
    ]
    exclude_fields_from_create = ["id"]
    exclude_fields_from_edit = ["id"]      
class NewsView(ModelView):
    identity="news"
    fields=[
        "id", "title_uz", "title_en", "title_ru", "body_uz", "body_en", "body_ru", 
        FileField("img_file"), "image_id", "created_at", "updated_at"
    ]
    exclude_fields_from_create = ["id", "image_id", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "image_id", "created_at", "updated_at"]
    
    async def before_create(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        file_data = data.get("img_file")
        up = None
        
        if file_data:
            if isinstance(file_data, tuple):
                up, is_deleted = file_data
                if is_deleted:
                    up = None
            else:
                up = file_data
        
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)
            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)
            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)
            url = f"/{UPLOAD_DIR}/{filename}"
            obj.image_id = await save_media(url)

        data.pop("img_file", None)

    async def before_edit(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        file_data = data.get("img_file")
        up = None
        
        if file_data:
            if isinstance(file_data, tuple):
                up, is_deleted = file_data
                if is_deleted:
                    up = None
            else:
                up = file_data
        
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)
            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)
            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)
            url = f"/{UPLOAD_DIR}/{filename}"
            obj.image_id = await save_media(url)

        data.pop("img_file", None)

class SliderView(ModelView):
    identity="sliders"
    fields=[
        "id", "title_uz", "title_en", "title_ru", "description_uz", "description_en", "description_ru", 
        FileField("img_file"), "image_id", "created_at", "updated_at"
    ]
    exclude_fields_from_create = ["id", "image_id", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "image_id", "created_at", "updated_at"]
    
    
    async def before_create(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        file_data = data.get("img_file")
        up = None
        
        if file_data:
            if isinstance(file_data, tuple):
                up, is_deleted = file_data
                if is_deleted:
                    up = None
            else:
                up = file_data
        
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)
            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)
            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)
            url = f"/{UPLOAD_DIR}/{filename}"
            obj.image_id = await save_media(url)

        data.pop("img_file", None)

    async def before_edit(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        file_data = data.get("img_file")
        up = None
        
        if file_data:
            if isinstance(file_data, tuple):
                up, is_deleted = file_data
                if is_deleted:
                    up = None
            else:
                up = file_data
        
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)
            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)
            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)
            url = f"/{UPLOAD_DIR}/{filename}"
            obj.image_id = await save_media(url)

        data.pop("img_file", None)
