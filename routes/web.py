from crya import Router

from app.handlers import welcome

router = Router()

router.get("/", welcome).name("welcome")
