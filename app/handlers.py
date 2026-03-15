from crya import Request, view


async def welcome(request: Request):
    return view("welcome.loom", {"app_name": "crya"})
