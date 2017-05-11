import os
import cgi
from SimpleHTTPServer import SimpleHTTPRequestHandler
from SocketServer import TCPServer

rootdir = os.getcwd()
global bRunning
bRunning = True

ROUTES = [
	('/', '/index.html'),
	('/help','/web/help.html'),
	('/editor','/web/editor.html'),
	('/launcher','/web/launcher.html'),
	('/smb','/web/smb.html'),
	('/shutdown','/web/exit.html'),
	('/exit','/web/exit.html'),
	('/error','/web/error.html'),
	('/a','/web/la.html'),
	('/b','/web/lb.html'),
	('/c','/web/lc.html'),
	('/startsmb','/web/smbs.html'),
	('/css','/web/style.css'),
	('/icon','/web/icon.ico')
]

def translate_path(path):
	for i, d in ROUTES:
		if path.endswith(i):
			path = d
			break
				
	return path

class http_handler(SimpleHTTPRequestHandler):
		
	def do_GET(self):
	
		try:
			p = translate_path(self.path)
			if p.endswith('.html') or p.endswith('.php'):
				self.send_response(200)
				self.send_header('Content-type','text/html')
			elif p.endswith('.css'):
				self.send_response(200)
				self.send_header('Content-type','text/css')
			elif p.endswith('.ico'):
				self.send_response(200)
				self.send_header('Content-type','image/vnd.microsoft.icon')
			elif p.endswith('.js'):
				self.send_response(200)
				self.send_header('Content-type','application/javascript')
			self.end_headers()
			f = open(rootdir + p,'r')
			self.wfile.write(f.read())
			f.close()
			if p.endswith('/exit.html'):
				global bRunning
				bRunning = False
			elif p.endswith('/la.html'):
				f = open(rootdir + "/LAUNCHER_A","w+")
				f.write("LAUNCH PAYLOAD A")
				f.close()
			elif p.endswith('/lb.html'):
				f = open(rootdir + "/LAUNCHER_B","w+")
				f.write("LAUNCH PAYLOAD B")
				f.close()
			elif p.endswith('/lc.html'):
				f = open(rootdir + "/LAUNCHER_C","w+")
				f.write("LAUNCH PAYLOAD C")
				f.close()
			elif p.endswith('/smbs.html'):
				f = open(rootdir + "/LAUNCHER_SMB","w+")
				f.write("LAUNCH SMB SERVER")
				f.close()
			
			return
			
		except IOError:
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			f = open(rootdir + "/web/error.html",'r')
			self.wfile.write(f.read())
			f.close()
			
	def do_POST(self):
		length = int(self.headers['Content-length'])
		postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
		letter = postvars["Letter"][0]
		data = postvars["Data"][0]
		self.send_response(204)
		if letter == "a":
			f = open(rootdir + "/scripts/la.sh","w")
			f.write(data)
			f.close()
		elif letter == "b":
			f = open(rootdir + "/scripts/lb.sh","w")
			f.write(data)
			f.close()
		elif letter == "c":
			f = open(rootdir + "/scripts/lc.sh","w")
			f.write(data)
			f.close()


def run():
	httpd = TCPServer(('172.16.64.1',80),http_handler)
	while bRunning:
		httpd.handle_request()
	
run()
f = open(rootdir + "/SHUTDOWN","w+")
f.write("Server has shutdown")
f.close()
