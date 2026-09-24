from pathlib import Path
import re
R=Path(__file__).resolve().parents[1]
for p in (R/'dist').rglob('patrimonio.html'):
 s=p.read_text()
 if '<meta name="referrer"' not in s:s=s.replace('</head>','<meta name="referrer" content="strict-origin-when-cross-origin"></head>')
 s=re.sub(r'<iframe src="(https://www.youtube-nocookie.com/embed/9gAK0wLzbLM)"',r'<iframe data-youtube-src="\1" referrerpolicy="strict-origin-when-cross-origin"',s)
 p.write_text(s)
