"""Run the downloaded site over HTTP so video embeds receive a Referer."""
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
from functools import partial
import webbrowser
handler=partial(SimpleHTTPRequestHandler,directory=str(Path(__file__).resolve().parent/'dist'))
with ThreadingHTTPServer(('127.0.0.1',8000),handler) as server:
 print('Abrir / Open: http://127.0.0.1:8000 — Ctrl+C para cerrar / to stop')
 webbrowser.open('http://127.0.0.1:8000')
 try:server.serve_forever()
 except KeyboardInterrupt:pass
