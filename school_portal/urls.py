"""
URL configuration for school_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse


# 🧰 Iyendo Tools Hub homepage view
def hub_home(request):
    from django.http import HttpResponse

def hub_home(request):
    return HttpResponse("""
        <html>
            <head>
                <title>Iyendo Tools Hub 🧰</title>
                <style>
                    body {
                        background-color: #f8fafc;
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        text-align: center;
                        color: #222;
                        margin: 0;
                        padding: 40px;
                    }
                    h1 {
                        color: #0b5394;
                        font-size: 2.5em;
                        margin-bottom: 10px;
                    }
                    p {
                        font-size: 1.2em;
                        color: #555;
                        margin-bottom: 30px;
                    }
                    ul {
                        list-style: none;
                        padding: 0;
                        display: inline-block;
                        text-align: left;
                    }
                    li {
                        background: #fff;
                        margin: 10px 0;
                        padding: 12px 20px;
                        border-radius: 12px;
                        box-shadow: 0 3px 6px rgba(0,0,0,0.1);
                        transition: transform 0.2s ease, box-shadow 0.2s ease;
                    }
                    li:hover {
                        transform: translateY(-3px);
                        box-shadow: 0 5px 10px rgba(0,0,0,0.15);
                    }
                    a {
                        text-decoration: none;
                        color: #0b5394;
                        font-weight: 600;
                    }
                </style>
            </head>
            <body>
                <h1>🧰 Welcome to Iyendo Tools</h1>
                <p>Practical web apps by Daniel Iyendo</p>
                <ul>
                    <li>🏫 <a href='/schoolms/'>School Management System</a></li>
                    <li>🏥 <a href='/queue/'>Queue Management System</a></li>
                    <li>🛍️ <a href='/marketplace/'>Local Marketplace</a></li>
                    <li>💼 <a href='/internconnect/'>InternConnect</a></li>
                </ul>
            </body>
        </html>
    """)


urlpatterns = [
    path('admin/', admin.site.urls),

    # 🧰 Hub homepage
    path('', hub_home, name='hub_home'),

    # 🏫 School Management System under /schoolms/
    path('schoolms/', include("user.urls")),
    path('schoolms/teacher/', include("teacher.urls")),
    path('schoolms/student/', include("student.urls")),
]


# Static/media setup
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
