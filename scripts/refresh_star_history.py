#!/usr/bin/env python3
"""Record public GitHub star totals and render both README themes. Stdlib only."""
import argparse, json, math, os, copy
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
REPO = "JethroJames/awesome-robots-icl"
SEED = [{'date': '2026-09-20', 'stars': 1}, {'date': '2026-09-21', 'stars': 2}, {'date': '2026-09-22', 'stars': 2}, {'date': '2026-09-23', 'stars': 2}, {'date': '2026-09-24', 'stars': 2}, {'date': '2026-09-25', 'stars': 2}, {'date': '2026-09-26', 'stars': 2}, {'date': '2026-09-27', 'stars': 2}, {'date': '2026-09-28', 'stars': 3}, {'date': '2026-09-29', 'stars': 3}, {'date': '2026-09-30', 'stars': 14}, {'date': '2026-10-01', 'stars': 15}, {'date': '2026-10-02', 'stars': 16}, {'date': '2026-10-03', 'stars': 16}, {'date': '2026-10-04', 'stars': 17}, {'date': '2026-10-05', 'stars': 17}, {'date': '2026-10-06', 'stars': 18}, {'date': '2026-10-07', 'stars': 19}, {'date': '2026-10-08', 'stars': 21}, {'date': '2026-10-09', 'stars': 21}, {'date': '2026-10-10', 'stars': 23}, {'date': '2026-10-11', 'stars': 23}, {'date': '2026-10-12', 'stars': 29}]
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)
def tag(s): return "{" + NS + "}" + s

def update(rows, day, count):
    if type(count) is not int or count < 0: raise ValueError("Invalid star count")
    if day < rows[-1]["date"]: raise ValueError("Time moved backwards")
    rows = [dict(r) for r in rows]
    if rows[-1]["date"] == day: rows[-1]["stars"] = count
    else: rows.append({"date": day, "stars": count})
    return rows

def render(rows, theme):
    # Reuse the existing hand-drawn font, not the upstream cached count curve.
    old = ET.parse(ROOT / "assets" / f"star-history-{theme}.svg").getroot()
    root = ET.Element(tag("svg"), {"viewBox":"0 0 800 533", "width":"800", "height":"533", "role":"img"})
    fg, bg, stroke = ("#eeeeee", "#101419", "#ff725e") if theme == "dark" else ("#161616", "#ffffff", "#e7492e")
    for el in old.findall('.//' + tag('style')): root.append(copy.deepcopy(el))
    ET.SubElement(root, tag("title")).text = "Star History — " + REPO
    ET.SubElement(root, tag("desc")).text = f"Daily recorded GitHub star totals from {rows[0]['date']} through {rows[-1]['date']}. Latest: {rows[-1]['stars']}. Historical seed: Star History CSV; updates: GitHub repository API."
    ET.SubElement(root, tag("rect"), {"width":"800", "height":"533", "fill":bg})
    def text(x,y,value,size=18,anchor="middle"):
        el=ET.SubElement(root,tag("text"),{"x":str(x),"y":str(y),"fill":fg,"font-size":str(size),"text-anchor":anchor,"font-family":"xkcd, Comic Sans MS, sans-serif"}); el.text=value
    text(400,37,"Star History",25)
    text(100,77,REPO,18,"start")
    start=date.fromisoformat(rows[0]['date']); end=date.fromisoformat(rows[-1]['date']); days=max(1,(end-start).days)
    maximum=max(r['stars'] for r in rows)
    rough=max(1,maximum/5); power=10**math.floor(math.log10(rough)); step=next(v*power for v in (1,2,5,10) if v*power>=rough)
    top=max(step,math.ceil(maximum/step)*step)
    def x(day): return 82+(date.fromisoformat(day)-start).days/days*672
    def y(n): return 455-n/top*338
    ET.SubElement(root,tag('path'),{'d':'M82 111V455H754','fill':'none','stroke':fg,'stroke-width':'2.5'})
    for n in range(0,int(top)+1,int(step)):
        text(67,y(n)+6,str(n),17,'end')
    for offset in sorted(set(round(i*days/5) for i in range(6))):
        from datetime import timedelta
        d=start+timedelta(days=offset); text(x(d.isoformat()),485,d.strftime('%b %d'),16)
    points=' '.join(f"{x(r['date']):.2f},{y(r['stars']):.2f}" for r in rows)
    ET.SubElement(root,tag('polyline'),{'points':points,'fill':'none','stroke':stroke,'stroke-width':'3.5','stroke-linecap':'round','stroke-linejoin':'round'})
    ET.SubElement(root,tag('circle'),{'cx':str(x(rows[-1]['date'])),'cy':str(y(rows[-1]['stars'])),'r':'4','fill':stroke})
    text(400,521,'Since Sep 20, 2026',16)
    text(754,77,str(rows[-1]['stars'])+' stars',19,'end')
    return ET.tostring(root,encoding='utf-8',xml_declaration=True)

def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path,default=ROOT/'star-history-output'); args=p.parse_args()
    headers={'Accept':'application/vnd.github+json','User-Agent':'robot-icl-star-history'}
    if os.getenv('GITHUB_TOKEN'): headers['Authorization']='Bearer '+os.environ['GITHUB_TOKEN']
    with urlopen(Request('https://api.github.com/repos/'+REPO,headers=headers),timeout=30) as r: count=json.load(r)['stargazers_count']
    path=args.output/'history.json'; rows=json.loads(path.read_text()) if path.exists() else SEED
    rows=update(rows,datetime.now(timezone.utc).date().isoformat(),count)
    outputs={f'star-history-{t}.svg':render(rows,t) for t in ('light','dark')}
    args.output.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(rows,indent=2)+'\n')
    for name,data in outputs.items(): (args.output/name).write_bytes(data)
    print(f'Recorded {count} stars through {rows[-1]["date"]}')
if __name__=='__main__': main()
