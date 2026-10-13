#!/usr/bin/env python3
"""Refresh the README's first-star-onward view of the public Star History SVG.

Only the horizontal viewport changes. The original cumulative-count curve,
vertical axis, embedded font and source attribution are preserved. No counts
are reconstructed or rebased. Requires Python 3 and curl; no credentials.
"""

import copy
from datetime import datetime, timedelta, timezone
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET

# First positive record in the public Star History CSV, verified 2026-10-13.
START = datetime(2026, 9, 20, tzinfo=timezone.utc)
ROOT = Path(__file__).resolve().parents[1]
SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)


def tag(name):
    return f"{{{SVG}}}{name}"


def translate(element):
    match = re.fullmatch(r"translate\(([-\d.]+)[ ,]+([-\d.]+)\)", element.get("transform", ""))
    if not match:
        raise ValueError("Star History axis format changed; preserve existing charts.")
    return tuple(map(float, match.groups()))


def focus(source, fetched):
    root = ET.fromstring(source)
    plot = root.find(f".//{tag('g')}[@pointer-events='all']")
    axis = root.find(f".//{tag('g')}[@class='xaxis']")
    if plot is None or axis is None:
        raise ValueError("Missing public chart geometry; preserve existing charts.")
    ticks = axis.findall(f"{tag('text')}[@class='tick']")
    if len(ticks) < 2:
        raise ValueError("Too few dated ticks to crop the chart reliably.")
    dates = []
    previous = None
    year = START.year
    for tick in ticks:
        date = datetime.strptime(f"{year} {tick.text}", "%Y %b %d").replace(tzinfo=timezone.utc)
        if previous and date < previous:
            year += 1
            date = date.replace(year=year)
        dates.append(date)
        previous = date
    x0, baseline = translate(ticks[0])
    x1, _ = translate(ticks[-1])
    px_per_day = (x1 - x0) / (dates[-1] - dates[0]).days
    domain = axis.find(f"{tag('path')}[@class='domain']")
    width_match = re.fullmatch(r"M\.5\.5h([\d.]+)", domain.get("d", "")) if domain is not None else None
    if not width_match or px_per_day <= 0:
        raise ValueError("Unexpected axis scale; preserve existing charts.")
    width = float(width_match[1])
    start_x = x0 + (START - dates[0]).days * px_per_day
    if not 0 < start_x < width - 1:
        raise ValueError("Requested window is not contained in the source chart.")
    scale = width / (width - start_x)
    end = dates[0] + timedelta(days=(width - x0) / px_per_day)
    lines = plot.findall(f"{tag('path')}[@class='xkcd-chart-xyline']")
    if len(lines) != 1:
        raise ValueError("Expected one repository curve; preserve existing charts.")
    defs = root.find(tag("defs"))
    clip = ET.SubElement(defs, tag("clipPath"), {"id": "focused-window", "clipPathUnits": "userSpaceOnUse"})
    ET.SubElement(clip, tag("rect"), {"x": "0", "y": "-5", "width": str(width), "height": str(baseline + 10)})
    line = lines[0]
    index = list(plot).index(line)
    plot.remove(line)
    group = ET.Element(tag("g"), {"clip-path": "url(#focused-window)"})
    zoom = ET.SubElement(group, tag("g"), {"transform": f"matrix({scale:.9f} 0 0 1 {-start_x * scale:.9f} 0)"})
    line.set("vector-effect", "non-scaling-stroke")
    zoom.append(line)
    plot.insert(index, group)
    template = copy.deepcopy(ticks[0])
    for tick in ticks:
        axis.remove(tick)
    days = max(1, (end.date() - START.date()).days)
    step = max(1, (days + 5) // 6)
    for offset in range(0, days + 1, step):
        date = START + timedelta(days=offset)
        x = offset * px_per_day * scale
        tick = copy.deepcopy(template)
        tick.set("transform", f"translate({x:.3f} {baseline:.3f})")
        tick.text = date.strftime("%b %d")
        axis.append(tick)
    for text in root.findall(tag("text")):
        if text.text == "Date":
            text.text = f"Since {START:%b} {START.day}, {START.year}"
    root.insert(0, ET.Element(tag("desc")))
    root[0].text = (f"Cumulative GitHub stars for JethroJames/awesome-robots-icl, "
                    f"shown from {START:%B} {START.day}, {START.year}. Source: api.star-history.com. "
                    f"Snapshot retrieved {fetched}; source may be cached. "
                    "Counts and curve are unchanged from the full-history chart.")
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def main():
    fetched = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    outputs = {}
    for theme in ("light", "dark"):
        url = "https://api.star-history.com/svg?repos=JethroJames/awesome-robots-icl&type=Date"
        if theme == "dark":
            url += "&theme=dark"
        source = subprocess.check_output(["curl", "--fail", "--silent", "--show-error", "--location", "--max-time", "30", url])
        outputs[ROOT / "assets" / f"star-history-{theme}.svg"] = focus(source, fetched)
    # Do not replace either theme if retrieval or validation failed.
    for path, content in outputs.items():
        path.write_bytes(content)
        print(f"Updated {path.relative_to(ROOT)} (source snapshot: {fetched})")


if __name__ == "__main__":
    main()
