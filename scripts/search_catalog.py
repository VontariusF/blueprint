#!/usr/bin/env python3
"""Search captured UI references without loading the whole catalog into context."""
import argparse
import json
from pathlib import Path

def search(query='', source=None, limit=8):
    data=json.loads((Path(__file__).resolve().parents[1]/'assets/ui-library/components.json').read_text())
    words=query.casefold().split()
    hits=[]
    for entry in data['components']:
        if source and entry['source']!=source:continue
        text=json.dumps(entry,ensure_ascii=False).casefold()
        score=sum(word in text for word in words)
        if not words or score:hits.append((score,entry))
    hits.sort(key=lambda x:(-x[0],x[1]['source'],x[1]['name']))
    return [entry for _,entry in hits[:limit]]

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('query',nargs='?',default='')
    ap.add_argument('--source')
    ap.add_argument('--limit',type=int,default=8)
    a=ap.parse_args()
    if a.limit<1:ap.error('--limit must be positive')
    print(json.dumps(search(a.query,a.source,a.limit),indent=2,ensure_ascii=False))
