from starlette_admin.contrib.sqla import ModelView
from starlette_admin import FileField
from fastapi.requests import Request
from fastapi import UploadFile
from typing import Dict, Any
import os
import uuid
from app.models import User,Media,Worker,Labaratory,Section,Manaagement,Seminar,News,Slider
from app.utils import password_hash,looks_hashed
UPLOAD_DIR = "static/uploads"
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
    fields = ["id", "file_path", "created_at", "updated_at"]
    exclude_fields_from_create = ["id", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at"]

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
        up = data.get("img_file")
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)

            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)

            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)

            url = f"/{UPLOAD_DIR}/{filename}"

            # SQLAlchemy ob'ektli munosabatni o'zi bog'lab saqlaydi
            obj.image = Media(file_path=url)

        data.pop("img_file", None)

    async def before_edit(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        up = data.get("img_file")
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)

            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)

            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)

            url = f"/{UPLOAD_DIR}/{filename}"

            # Eski rasmni yangisiga almashtirish
            obj.image = Media(file_path=url)

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
        up = data.get("img_file")
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)

            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)

            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)

            url = f"/{UPLOAD_DIR}/{filename}"

            # SQLAlchemy ob'ektli munosabatni o'zi bog'lab saqlaydi
            obj.image = Media(file_path=url)

        data.pop("img_file", None)

    async def before_edit(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        up = data.get("img_file")
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)

            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)

            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)

            url = f"/{UPLOAD_DIR}/{filename}"

            # Eski rasmni yangisiga almashtirish
            obj.image = Media(file_path=url)

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
        up = data.get("img_file")
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)

            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)

            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)

            url = f"/{UPLOAD_DIR}/{filename}"

            # SQLAlchemy ob'ektli munosabatni o'zi bog'lab saqlaydi
            obj.image = Media(file_path=url)

        data.pop("img_file", None)

    async def before_edit(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        up = data.get("img_file")
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)

            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)

            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)

            url = f"/{UPLOAD_DIR}/{filename}"

            # Eski rasmni yangisiga almashtirish
            obj.image = Media(file_path=url)

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
        up = data.get("img_file")
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)

            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)

            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)

            url = f"/{UPLOAD_DIR}/{filename}"

            # SQLAlchemy ob'ektli munosabatni o'zi bog'lab saqlaydi
            obj.image = Media(file_path=url)

        data.pop("img_file", None)

    async def before_edit(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        up = data.get("img_file")
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)

            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)

            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)

            url = f"/{UPLOAD_DIR}/{filename}"

            # Eski rasmni yangisiga almashtirish
            obj.image = Media(file_path=url)

        data.pop("img_file", None)
class SeminarView(ModelView):
    identity="seminars"
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
        up = data.get("img_file")
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)

            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)

            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)

            url = f"/{UPLOAD_DIR}/{filename}"

            # SQLAlchemy ob'ektli munosabatni o'zi bog'lab saqlaydi
            obj.image = Media(file_path=url)

        data.pop("img_file", None)

    async def before_edit(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        up = data.get("img_file")
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)

            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)

            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)

            url = f"/{UPLOAD_DIR}/{filename}"

            # Eski rasmni yangisiga almashtirish
            obj.image = Media(file_path=url)

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
        up = data.get("img_file")
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)

            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)

            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)

            url = f"/{UPLOAD_DIR}/{filename}"

            # SQLAlchemy ob'ektli munosabatni o'zi bog'lab saqlaydi
            obj.image = Media(file_path=url)

        data.pop("img_file", None)

    async def before_edit(
        self, request: Request, data: Dict[str, Any], obj: Any
    ) -> None:
        up = data.get("img_file")
        if up and hasattr(up, "filename") and up.filename:
            os.makedirs(UPLOAD_DIR, exist_ok=True)

            ext = os.path.splitext(up.filename)[1]
            filename = f"{uuid.uuid4().hex}{ext}"
            path = os.path.join(UPLOAD_DIR, filename)

            content = await up.read()
            with open(path, "wb") as f:
                f.write(content)

            url = f"/{UPLOAD_DIR}/{filename}"

            # Eski rasmni yangisiga almashtirish
            obj.image = Media(file_path=url)

        data.pop("img_file", None)
