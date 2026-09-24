#!/usr/bin/env python3
"""Export public OAN video metadata to a review file; never publishes or overwrites the site.
Requires Python 3 and a YouTube Data API v3 key in YOUTUBE_API_KEY.
Docs: https://developers.google.com/youtube/v3/docs/playlistItems/list
"""
import argparse,csv,json,os,sys,urllib.request,urllib.parse,urllib.error
from pathlib import Path
CHANNEL='UCb1rF7m6wUC4Zhw-zsUWvLA'
def main():
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--output',default='youtube-candidates.json')
 p.add_argument('--max-pages',type=int,default=20,help='Up to 50 videos per page; default 20 pages')
 a=p.parse_args()
 key=os.environ.get('YOUTUBE_API_KEY')
 if not key:p.error('Set YOUTUBE_API_KEY in the environment; never put it in website files.')
 if a.max_pages<1:p.error('--max-pages must be at least 1')
 def get(resource,**params):
  params['key']=key
  try:
   with urllib.request.urlopen('https://www.googleapis.com/youtube/v3/'+resource+'?'+urllib.parse.urlencode(params),timeout=30) as r:return json.load(r)
  except urllib.error.HTTPError as e:raise RuntimeError('YouTube API returned HTTP '+str(e.code)+'. Check key, quota and API activation.') from None
  except Exception:raise RuntimeError('Could not retrieve YouTube data. Check the network and try again.') from None
 ch=get('channels',part='contentDetails',id=CHANNEL).get('items',[])
 if not ch:raise RuntimeError('The Observatory channel was not returned.')
 playlist=ch[0]['contentDetails']['relatedPlaylists']['uploads'];token='';records=[]
 for _ in range(a.max_pages):
  data=get('playlistItems',part='contentDetails',playlistId=playlist,maxResults=50,pageToken=token)
  ids=[x['contentDetails']['videoId'] for x in data.get('items',[])]
  if ids:
   videos=get('videos',part='snippet,contentDetails,liveStreamingDetails',id=','.join(ids)).get('items',[])
   for x in videos:
    s=x['snippet'];thumbs=s.get('thumbnails',{});thumb=next((thumbs[k]['url'] for k in ['high','medium','default'] if k in thumbs),'')
    records.append({'id':x['id'],'title':s['title'],'title_en':'','description':s.get('description',''),'published_at':s['publishedAt'],'broadcast_started_at':x.get('liveStreamingDetails',{}).get('actualStartTime',''),'duration_iso':x.get('contentDetails',{}).get('duration',''),'thumbnail':thumb,'url':'https://www.youtube.com/watch?v='+x['id'],'review_status':'pending'})
  token=data.get('nextPageToken','')
  if not token:break
 out=Path(a.output);out.parent.mkdir(parents=True,exist_ok=True)
 if out.exists():raise RuntimeError('Output already exists. Choose a new --output path to preserve earlier data.')
 out.write_text(json.dumps({'channel_id':CHANNEL,'complete':not bool(token),'next_page_token':token,'videos':records},ensure_ascii=False,indent=2),encoding='utf-8')
 print(str(len(records))+' video records exported for editorial review. '+('Full playlist retrieved.' if not token else 'Page limit reached; this is a partial export.'))
if __name__=='__main__':
 try:main()
 except RuntimeError as e:sys.exit(str(e))
