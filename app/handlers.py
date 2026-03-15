from crya import Request, view


async def welcome(request: Request):
    return view("welcome.loom", {"name": "crya"})
