"""Manuscript Figure 1 (decision layer) as an editable draw.io file.
Usage: python tools/figure1_drawio.py figures/Figure_1.drawio
Open the file in draw.io and use File > Export as > PDF (crop) to obtain figures/Figure_1.pdf."""
# Canvas ~1060 px wide: at 7.0 in print width, 15 px text = ~7.1 pt.
import html, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "Figure_1.drawio"
cells, nid = [], [10]
F = "fontFamily=Helvetica;"
FS, FH = 15, 15          # body / heading font size (px)

def new_id():
    nid[0] += 1
    return f"c{nid[0]}"

def box(x, y, w, h, label, style):
    i = new_id()
    cells.append(f'<mxCell id="{i}" value="{html.escape(label)}" style="{style}" vertex="1" parent="1">'
                 f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
    return i

def edge(s, t, style, label="", pts=None):
    i = new_id()
    g = '<mxGeometry relative="1" as="geometry">'
    if pts:
        g += '<Array as="points">' + "".join(f'<mxPoint x="{a}" y="{b}"/>' for a, b in pts) + '</Array>'
    g += '</mxGeometry>'
    cells.append(f'<mxCell id="{i}" value="{html.escape(label)}" style="{style}" edge="1" parent="1" source="{s}" target="{t}">{g}</mxCell>')

BLUE = ("#EAF1FB", "#3B6EA8"); PURP = ("#F1ECF7", "#6B4C9A"); ORNG = ("#FDF1E4", "#B8661A")
YELL = ("#FBF6E3", "#9C7F12"); RED = ("#FBEAEA", "#B03A3A"); GRAY = ("#F2F4F6", "#5B6573")
O_R = ("#FFF1C9", "#B98A00"); O_B = ("#F7D9D9", "#B03A3A"); O_A = ("#DDEFE0", "#3C8D4A")

def st(c, extra=""):
    return (f"rounded=1;arcSize=7;whiteSpace=wrap;html=1;fillColor={c[0]};strokeColor={c[1]};strokeWidth=1.5;"
            f"{F}fontSize={FS};fontColor=#1F2933;align=center;verticalAlign=middle;spacing=4;" + extra)

def T(title, c, body):
    return f"<b><font color='{c[1]}'>{title}</font></b><br>{body}"

LANE = ("rounded=1;arcSize=2;whiteSpace=wrap;html=1;fillColor=#FAFBFC;strokeColor=#9AA5B1;dashed=1;dashPattern=6 3;"
        f"{F}fontSize=15;fontStyle=1;fontColor=#3E4C59;align=left;verticalAlign=top;spacingLeft=8;spacingTop=2;")
FLOW = f"endArrow=blockThin;endFill=1;endSize=7;strokeColor=#3E4C59;strokeWidth=2;{F}html=1;"
DASH = (f"endArrow=blockThin;endFill=1;endSize=6;strokeColor=#7B8794;strokeWidth=1.5;dashed=1;dashPattern=5 3;"
        f"{F}fontSize=14;fontColor=#3E4C59;html=1;labelBackgroundColor=#FFFFFF;edgeStyle=orthogonalEdgeStyle;")
ORTH = "edgeStyle=orthogonalEdgeStyle;rounded=1;"

p, a, D = "<i>p</i><sub><i>i</i></sub>", "<i>a</i><sub><i>i</i></sub>", "&Delta;<sub><i>i</i></sub>"
Cr, Cb, X = "<i>C</i><sub>rev</sub>", "<i>C</i><sub>blk</sub>", "<b>x</b><sub><i>i</i></sub>"
W = 1060

# ---------------- A: before the window
box(10, 10, W - 20, 152, "A&nbsp; Before the decision window (validation data only)", LANE)
yA, hA = 44, 104
v1 = box(26, yA, 160, hA, T("Validation window", BLUE, "labelled transactions<br>preceding <i>W</i>"), st(BLUE))
v2 = box(214, yA, 170, hA, T("Fit calibrator <i>g</i>", ORNG, "isotonic (main)<br>or Platt"), st(ORNG))
v3 = box(412, yA, 180, hA, T("Validation gains", RED, "&Delta;<sub><i>j</i></sub> by Eq. (5),<br>keep &Delta;<sub><i>j</i></sub> &gt; 0"), st(RED))
v5 = box(620, yA, 175, 66, T("Operational inputs", GRAY, f"{Cr}, {Cb}, <i>K</i> or <i>k</i>, <i>q</i>"), st(GRAY))
v4 = box(823, yA, 211, hA, T("Review threshold &tau;", RED, "<i>K</i><sub>val</sub>-th largest &Delta;<sub><i>j</i></sub><br>per period: static or<br>adaptive (Eq. 9)"), st(RED))
edge(v1, v2, FLOW); edge(v2, v3, FLOW)
edge(v3, v4, FLOW + ORTH + "exitX=1;exitY=0.85;entryX=0;entryY=0.85;")
edge(v5, v3, DASH + "exitX=0;exitY=0.5;entryX=1;entryY=0.32;")

# ---------------- B: during the window
yB = 186
box(10, yB, W - 20, 236, "B&nbsp; Decision window <i>W</i>, arrival order", LANE)
yb, hb = yB + 58, 150
tx = box(26, yb + 25, 96, 100, T("Input", BLUE, f"{X}<br>{a}"), st(BLUE))
sc = box(146, yb + 15, 132, 120, T("1&nbsp; Scoring", PURP, f"<i>s</i>({X})<br>any classifier"), st(PURP))
ca = box(302, yb + 15, 140, 120, T("2&nbsp; Calibration", ORNG, f"{p} = <i>g</i>(<i>s</i>({X}))"), st(ORNG))
ec = box(466, yb, 196, hb, T("3&nbsp; Expected cost", YELL,
     f"<div style='text-align:left;padding-left:6px'>A:&nbsp; {p}{a}<br>B:&nbsp; (1 &minus; {p}){Cb}<br>R:&nbsp; {Cr} + (1 &minus; <i>q</i>){p}{a}</div>"), st(YELL))
se = box(686, yb - 10, 222, hb + 20, T("4&nbsp; Budgeted selection", RED,
     f"<div style='text-align:left;padding-left:4px'>{D} = <i>m</i><sub><i>i</i></sub> &minus; {Cr} &minus; (1 &minus; <i>q</i>){p}{a}<br>"
     f"<i>m</i><sub><i>i</i></sub> = min{{{p}{a}, (1 &minus; {p}){Cb}}}<br>R if {D} &gt; 0, {D} &ge; &tau;, <i>u</i> &lt; <i>K</i></div>"),
     st(RED, "strokeWidth=2.5;"))
oR = box(932, yb - 10, 102, 50, "<b>REVIEW</b><br><span style='font-size:13px'>to analyst</span>", st(O_R, "strokeWidth=2;"))
oB = box(932, yb + 50, 102, 50, f"<b>BLOCK</b><br><span style='font-size:13px'>B cheaper</span>", st(O_B, "strokeWidth=2;"))
oA = box(932, yb + 110, 102, 50, "<b>APPROVE</b><br><span style='font-size:13px'>otherwise</span>", st(O_A, "strokeWidth=2;"))
for s_, t_ in [(tx, sc), (sc, ca), (ca, ec), (ec, se)]:
    edge(s_, t_, FLOW)
for o in (oR, oB, oA):
    edge(se, o, FLOW + ORTH + "exitX=1;exitY=0.5;entryX=0;entryY=0.5;")
yg = 174   # gap between lanes A and B
edge(v2, ca, DASH + "exitX=0.5;exitY=1;entryX=0.5;entryY=0;", "<i>g</i>", pts=[(299, yg), (372, yg)])
edge(v5, ec, DASH + "exitX=0.5;exitY=1;entryX=0.5;entryY=0;", "", pts=[(707, yg), (564, yg)])
edge(v4, se, DASH + "exitX=0.25;exitY=1;entryX=0.75;entryY=0;", "&tau;", pts=[(876, yg), (852, yg)])
edge(oR, v4, DASH + "exitX=0.5;exitY=0;entryX=0.758;entryY=1;")

# ---------------- C: enforcement modes and guarantee
yC = 446
box(10, yC, W - 20, 112, "C&nbsp; Budget enforcement modes and optimality", LANE)
yc, hc, wc = yC + 36, 66, 238
box(26, yc, wc, hc, "<b>Offline</b><br>top-<i>K</i> gains in hindsight", st(GRAY))
box(26 + (wc + 14), yc, wc, hc, "<b>Online, capped</b><br>&tau; on arrival, cap <i>K</i>", st(GRAY))
box(26 + 2 * (wc + 14), yc, wc, hc, "<b>Per period</b><br>cap <i>k</i> = <i>K</i>/<i>P</i>, static or adaptive &tau;", st(GRAY))
box(26 + 3 * (wc + 14), yc, W - 26 - 26 - 3 * (wc + 14), hc,
    "<b>Proposition 1</b><br><span style='font-size:14px'>top-<i>K</i> by &Delta; minimises expected cost<br>(calibrated <i>p</i>, known <i>q</i>)</span>", st(RED, "fillColor=#FFFFFF;"))

xml = ('<mxfile host="drawio"><diagram id="fig1" name="Figure 1">'
       f'<mxGraphModel dx="{W}" dy="570" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1" pageWidth="{W}" pageHeight="570" math="0" shadow="0">'
       '<root><mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(cells) + '</root></mxGraphModel></diagram></mxfile>')
open(OUT, "w", encoding="utf-8").write(xml)
print("written", OUT, len(cells), "cells")
