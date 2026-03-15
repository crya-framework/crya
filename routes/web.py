from crya import Route

from ..app.handlers import welcome

Route.get("/welcome", welcome).name("welcome")
