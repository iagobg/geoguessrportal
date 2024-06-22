from aiohttp import web
from geoguessr_async  import Geoguessr
import json

async def index(request):
    try:
        return web.FileResponse('./index.html')
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)


async def get_userdata(request):
    try:
        client = Geoguessr("BMle7gWIuh5L+9NWsmYqqUioTWxEyvo5PvCxwO2Dapg=PKMPbEteDTmJDIYoPKlahlKhB3dFyaEzY0Whv9WDCzKW2N/BBK8CRMbp0z/aqb1mhPvjlP8r2JxU/kS3A4m3/JOwAX9YaoazVtHJWncAUXM=")
        user_info = await client.get_user_infos("66737bea4b4ad1edf8e37921")
        user_stats = user_info.stats
        del user_info.stats
        return web.json_response(vars(user_info) | vars(user_stats))
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)
    
app = web.Application()
app.router.add_get('/', index)
app.router.add_get('/get-userdata', get_userdata)

if __name__ == '__main__':
    web.run_app(app, port=8080)
    