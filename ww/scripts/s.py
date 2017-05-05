import string, cgi, time
import os
import BaseHTTPServer
import SocketServer

rootdir = os.getcwd()
global bRunning
bRunning = True

class http_handler(BaseHTTPServer.BaseHTTPRequestHandler):
	
	def do_GET(self):
		found_type = ''
		if self.path.endswith('/'):
			self.path = '/index.html'
			found_type = 'text/html'
		try:
			if self.path.endswith('.html') or self.path.endswith('.php') or self.path.endswith('.py'):
				found_type = 'text/html'
			if self.path.endswith('.css'):
				found_type = 'text/css'
			if self.path.endswith('.js'):
				found_type = 'application/javascript'
			if self.path.endswith('.txt') or self.path.endswith('.md') or self.path.endswith('.sh') or self.path.endswith('.ps1'):
				found_type = 'text/plain'
			if self.path.endswith('.ico'):
				found_type = 'image/vnd.microsoft.icon'
			if self.path.endswith('/scripts/a'):
				found_type = 'text/html'
				
			if found_type != '':
				self.send_response(200)
				self.send_header('Content-type',found_type)
				self.end_headers()
				f = open(rootdir + self.path,'r')
				self.wfile.write(f.read())
				f.close()
				if found_type == 'text/html' and self.path.endswith('/exit.html'):
					global bRunning
					bRunning = False
				elif self.path.endswith('/la.html'):
					f = open(rootdir + "/LAUNCHER_A","w+")
					f.write("LAUNCH PAYLOAD A")
					f.close()
				elif self.path.endswith('/lb.html'):
					f = open(rootdir + "/LAUNCHER_B","w+")
					f.write("LAUNCH PAYLOAD B")
					f.close()
				elif self.path.endswith('/lc.html'):
					f = open(rootdir + "/LAUNCHER_C","w+")
					f.write("LAUNCH PAYLOAD C")
					f.close()
				elif self.path.endswith('/smb.html'):
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
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write("<html>")
		self.wfile.write("	<meta http-equiv='refresh' content='1;url=http://172.16.64.1:8080/web/editor.html'/>")
		self.wfile.write("	<body>")
		self.wfile.write("		<p>Redirecting to editor...</p>")
		self.wfile.write("		<h1>Payload Details</h1>")
		self.wfile.write("		<h2>Payload Letter: %s</h2>" % letter)
		self.wfile.write("		<h2>Payload Contents:</h2>")
		self.wfile.write("		<p>%s</p>" % data)
		self.wfile.write("	</body>")
		self.wfile.write("</html>")
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
		else:
			f = open(rootdir + "/scripts/error.sh","w")
			f.write(letter)
			f.write(data)
			f.close()
	
		
	
def run():
	httpd = SocketServer.TCPServer(('172.16.64.1',8080),http_handler)
	while bRunning:
		httpd.handle_request()
	
run()
f = open(rootdir + "/SHUTDOWN","w+")
f.write("Server has shutdown")
f.close()
