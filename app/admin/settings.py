from starlette_admin.contrib.sqla import Admin
from app.admin.auth import JSONAuthProvider
from app.database import engine
from app.models import User,Media,Worker,Labaratory,Section,Manaagement,Seminar,News,Slider,Defense
from app.admin.views import UserView,MediaView,WorkerView,LabaratoryView,SectionView,ManaagementView,SeminarView,NewsView,SliderView,DefenseView
admin = Admin(
    engine=engine,
    title="YaFm",
    base_url="/admin",
    auth_provider=JSONAuthProvider(login_path="/login", logout_path="/logout"),
)

admin.add_view(UserView(User,icon="fa fa-user"))
admin.add_view(MediaView(Media,icon="fa fa-video"))
admin.add_view(WorkerView(Worker,icon="fa fa-users"))
admin.add_view(LabaratoryView(Labaratory,icon="fa fa-tag"))
admin.add_view(SectionView(Section,icon="fa fa-section"))
admin.add_view(ManaagementView(Manaagement,icon="fa fa-folder"))
admin.add_view(SeminarView(Seminar,icon="fa fa-pen"))
admin.add_view(DefenseView(Defense,icon="fa fa-defense"))
admin.add_view(NewsView(News,icon="fa fa-newspaper"))
admin.add_view(SliderView(Slider,icon="fa fa-image"))