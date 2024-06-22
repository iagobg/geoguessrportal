from aiohttp import web
from geoguessr_async  import Geoguessr


async def index(request):
    try:
        return web.FileResponse('./index.html')
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)


async def get_username(request):
    try:
        client = Geoguessr("YOUR-NCFA-COOKIE")
        user_info = await client.get_user_infos("YOUR-USER-ID")
        username = user_info.nick
        return web.json_response({"username": username})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)
    
app = web.Application()
app.router.add_get('/', index)
app.router.add_get('/get-username', get_username)

if __name__ == '__main__':
    web.run_app(app, port=8080)
    