from datetime import datetime
from sqlalchemy import (
    Integer,
    Boolean,
    String,
    func,
    DateTime,
    ForeignKey,
    Text,
    BigInteger,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class BaseModel(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )


class Media(BaseModel):
    __tablename__ = "media"
    file_path: Mapped[str] = mapped_column(String, nullable=False)

    #relationship
    news: Mapped[list["News"]] = relationship("News",back_populates="image")
    slider: Mapped[list["Slider"]] = relationship("Slider",back_populates="image")
    worker: Mapped[list["Worker"]] = relationship("Worker",back_populates="image")
    labaratory: Mapped[list["Labaratory"]] = relationship("Labaratory",back_populates="image")
    section: Mapped[list["Section"]] = relationship("Section",back_populates="image")
    management: Mapped[list["Manaagement"]] = relationship("Manaagement",back_populates="image")


class User(BaseModel):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)


class Worker(BaseModel):
    __tablename__ = "workers"
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    position: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50), nullable=True)
    phone: Mapped[str] = mapped_column(String(50), nullable=True)
    image_id: Mapped[int] = mapped_column(ForeignKey("media.id"))
    # relationship
    labaratories: Mapped[list["Labaratory"]] = relationship(
        "Labaratory", back_populates="worker"
    )
    image: Mapped["Media"] = relationship("Media")

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class Labaratory(BaseModel):
    __tablename__ = "labaratories"
    name_uz: Mapped[str] = mapped_column(String(50), unique=True)
    name_en: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    name_ru: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    body_uz: Mapped[str] = mapped_column(Text)
    body_en: Mapped[str] = mapped_column(Text, nullable=True)
    body_ru: Mapped[str] = mapped_column(Text, nullable=True)
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id"), nullable=True)
    image_id: Mapped[int] = mapped_column(ForeignKey("media.id"))

    # relationship
    worker: Mapped["Worker"] = relationship("Worker", back_populates="labaratories")
    image: Mapped["Media"] = relationship("Media")

    def __repr__(self):
        return self.name_uz


class Section(BaseModel):
    __tablename__ = "sections"
    name_uz: Mapped[str] = mapped_column(String(50), unique=True)
    name_en: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    name_ru: Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    body_uz: Mapped[str] = mapped_column(Text)
    body_en: Mapped[str] = mapped_column(Text, nullable=True)
    body_ru: Mapped[str] = mapped_column(Text, nullable=True)
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id"), nullable=True)
    image_id: Mapped[int] = mapped_column(ForeignKey("media.id"))

    # relationship
    image: Mapped["Media"] = relationship("Media")
    worker: Mapped["Worker"] = relationship("Worker")


class Manaagement(BaseModel):
    __tablename__ = "managements"
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    reception_hours: Mapped[str] = mapped_column(String(100))
    position: Mapped[str] = mapped_column(String(50), nullable=True)
    email: Mapped[str] = mapped_column(String(50), nullable=True)
    phone: Mapped[str] = mapped_column(String(50), nullable=True)
    degree: Mapped[str] = mapped_column(String(50), nullable=True)
    image_id: Mapped[int] = mapped_column(ForeignKey("media.id"))

    # relationship
    image: Mapped["Media"] = relationship("Media")

    def __repr__(self):
        return self.first_name


class Seminar(Base):
    __tablename__ = "seminar"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    full_name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(Text)
    duration: Mapped[int] = mapped_column(Integer)
    start_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class News(BaseModel):
    __tablename__ = "news"
    title_uz: Mapped[str] = mapped_column(String(255))
    title_en: Mapped[str] = mapped_column(String(255), nullable=True)
    title_ru: Mapped[str] = mapped_column(String(255), nullable=True)
    body_uz: Mapped[str] = mapped_column(Text)
    body_en: Mapped[str] = mapped_column(Text, nullable=True)
    body_ru: Mapped[str] = mapped_column(Text, nullable=True)
    image_id: Mapped[int] = mapped_column(ForeignKey("media.id"), nullable=True)

    # relationships
    image: Mapped["Media"] = relationship("Media",back_populates="news")

    def __repr__(self):
        return self.title_uz


class Slider(BaseModel):
    __tablename__ = "sliders"
    title_uz: Mapped[str] = mapped_column(String(255))
    title_en: Mapped[str] = mapped_column(String(255), nullable=True)
    title_ru: Mapped[str] = mapped_column(String(255), nullable=True)
    description_uz: Mapped[str] = mapped_column(Text, nullable=True)
    description_en: Mapped[str] = mapped_column(Text, nullable=True)
    description_ru: Mapped[str] = mapped_column(Text, nullable=True)
    image_id: Mapped[int] = mapped_column(ForeignKey("media.id"))

    # relationship
    image: Mapped["Media"] = relationship("Media")



class Defense(Base):
    __tablename__ = "defense"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    full_name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(Text)
    duration: Mapped[int] = mapped_column(Integer)
    start_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))


