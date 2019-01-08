from rest_framework import routers
from LiveEdition.create_path import CareerPathViewSet

create_path_router = routers.SimpleRouter()
create_path_router.register(r'career-path', CareerPathViewSet);
