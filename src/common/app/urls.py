from django.urls import include, re_path

from common.app import views

urlpatterns = [
    re_path(r"^version/?", views.version_info),
    re_path(r"^health/liveness/?", views.version_info),
    re_path(r"^health/readiness/?", include("health_check.urls", namespace="health")),
    re_path(r"^health", include("health_check.urls", namespace="health-deprecated")),
    # Aptible health checks must be on /healthcheck and cannot redirect
    # see https://www.aptible.com/docs/core-concepts/apps/connecting-to-apps/app-endpoints/https-endpoints/health-checks
    re_path(r"^healthcheck", include("health_check.urls", namespace="health-aptible")),
]
