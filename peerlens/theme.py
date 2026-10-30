"""Visual identity: a private-wealth terminal.

Palette
  obsidian   #080B11  the ground; panels lift off it in layers, not shadows
  panel      #0F141D  surfaces, with a 1px top highlight for material depth
  champagne  #C8A96A  the focal company, and nothing else
  steel      #6E8CAF  peers, deliberately cool so the champagne reads as metal
  signals    #4FAE87 positive, #D0A14B watch, #CF6B72 concern
Type
  Instrument Serif carries the brand and the headline numbers (high contrast, the voice of a
  private bank statement); Archivo carries every table, label and control, with tabular figures.
The memorable element is the focal row: warm metal in a cool room.
"""
import datetime as dt
import html

PALETTES = {
    "dark": """
  --ink: #E9EDF4; --page: #080B11; --panel: #0F141D; --slate: #8794A8; --rule: #1E2733;
  --soft: #161D28; --brass: #C8A96A; --brass-tint: #1C1810; --blue: #6E8CAF;
  --pos: #4FAE87; --watch: #D0A14B; --neg: #CF6B72;
  --pos-tint: #11271E; --watch-tint: #2A2112; --neg-tint: #2B1619;
  --masthead: linear-gradient(180deg, #0D1219 0%, #080B11 100%);
  --masthead-ink: #F2F5FA; --masthead-slate: #7E8CA2; --accent: #C8A96A;
  --accent-ink: #0A0D13;
  --input: #141B25; --shadow: 0 1px 0 rgba(255,255,255,.035) inset, 0 8px 24px rgba(0,0,0,.35);
  --lift: inset 0 1px 0 rgba(255,255,255,.045);
""",
    "light": """
  --ink: #12161D; --page: #F2F1EE; --panel: #FFFFFF; --slate: #6B7280; --rule: #E0DED8;
  --soft: #F7F6F3; --brass: #9A7B3F; --brass-tint: #F7F1E4; --blue: #3D6A99;
  --pos: #2E7D5B; --watch: #B7862C; --neg: #A63D40;
  --pos-tint: #E7F2EC; --watch-tint: #F8F0DC; --neg-tint: #F7E5E5;
  --masthead: linear-gradient(180deg, #14181F 0%, #0C1016 100%);
  --masthead-ink: #FFFFFF; --masthead-slate: #9BA5B4; --accent: #12161D;
  --accent-ink: #FFFFFF;
  --input: #FFFFFF; --shadow: 0 1px 2px rgba(18,22,29,.06);
  --lift: none;
""",
}

BASE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=Instrument+Serif:ital@0;1&display=swap');

html, body, .stApp, .stMarkdown, p, li, label, input, textarea, button, td, th, div[data-baseweb] {
  font-family: 'Archivo', 'Segoe UI', Arial, sans-serif;
}
.stApp { background: var(--page); color: var(--ink); }
.block-container { padding-top: 3.2rem !important; max-width: 1360px; }
header[data-testid="stHeader"] { background: var(--page); }
header[data-testid="stHeader"] svg, header[data-testid="stHeader"] button { color: var(--ink); fill: var(--ink); }
.num { font-variant-numeric: tabular-nums; }

/* ---------- masthead ---------- */
.masthead { background: var(--masthead); color: var(--masthead-ink); margin: 0; padding: 1.5rem 1.7rem 1.25rem;
            display: flex; justify-content: space-between; align-items: flex-end; gap: 2rem; flex-wrap: wrap;
            border-bottom: 1px solid var(--brass); position: relative; }
.masthead .brand { font-family: 'Instrument Serif', Georgia, serif; font-size: 2.3rem; font-weight: 400;
                   letter-spacing: -.015em; line-height: 1; }
.masthead .desk { color: var(--masthead-slate); font-size: .92rem; margin-top: .15rem; }
.masthead .meta { text-align: right; color: var(--masthead-slate); font-size: .85rem; line-height: 1.5; }
.masthead .meta b { color: var(--masthead-ink); font-weight: 600; }
.status { display: inline-block; width: 7px; height: 7px; border-radius: 50%; margin-right: .4rem; vertical-align: middle; }
.status.live { background: #5FB88A; } .status.demo { background: var(--brass); }

/* ---------- process line ---------- */
.process { display: flex; flex-wrap: wrap; gap: 0; border: 1px solid var(--rule); border-top: none;
           margin: 0 0 1.6rem; background: var(--panel); padding: 0 1.6rem; }
.process .stage { padding: .8rem 1.4rem .7rem 0; margin-right: 1.4rem; color: var(--slate); opacity: .6;
                  font-size: .9rem; border-bottom: 2px solid transparent; }
.process .stage b { font-weight: 600; margin-right: .45rem; font-variant-numeric: tabular-nums; }
.process .stage.done { color: var(--slate); opacity: 1; }
.process .stage.now { color: var(--ink); opacity: 1; border-bottom-color: var(--ink); font-weight: 600; }

/* ---------- headings ---------- */
h1, h2, h3, .display { font-family: 'Instrument Serif', Georgia, serif !important; color: var(--ink); letter-spacing: -0.01em; }
.h-section { font-family: 'Instrument Serif', Georgia, serif; font-size: 1.95rem; font-weight: 400; color: var(--ink);
             letter-spacing: -.015em; margin: 1.8rem 0 .2rem; }
.h-sub { color: var(--slate); font-size: .95rem; margin-bottom: .9rem; max-width: 80ch; }
.h-minor { font-size: 1rem; font-weight: 600; color: var(--ink); margin: 1.2rem 0 .5rem;
           padding-bottom: .35rem; border-bottom: 1px solid var(--rule); }

/* ---------- report header ---------- */
.report { background: var(--panel); border: 1px solid var(--rule); border-top: 2px solid var(--brass);
          padding: 1.5rem 1.6rem 1.35rem; margin-top: 1.2rem; box-shadow: var(--shadow); border-radius: 3px; }
.report .kicker { color: var(--slate); font-size: .88rem; }
.report .title { font-family: 'Instrument Serif', Georgia, serif; font-size: 2.5rem; font-weight: 400;
                 line-height: 1.08; letter-spacing: -.02em; margin: .25rem 0 .5rem; }
.report .thesis { font-size: 1.02rem; color: var(--ink); max-width: 90ch; line-height: 1.55; }

/* ---------- metric strip ---------- */
.strip { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); background: var(--panel);
         border: 1px solid var(--rule); border-top: none; box-shadow: var(--lift); }
.cell { padding: 1rem 1.2rem 1.05rem; border-right: 1px solid var(--rule); }
.cell:last-child { border-right: none; }
.cell .label { color: var(--slate); font-size: .8rem; }
.cell .value { font-family: 'Instrument Serif', Georgia, serif; font-size: 2.1rem; font-weight: 400;
               font-variant-numeric: tabular-nums; line-height: 1.15; letter-spacing: -.02em; margin-top: .1rem; }
.cell .delta { font-size: .82rem; font-variant-numeric: tabular-nums; }
.delta.pos { color: var(--pos); } .delta.neg { color: var(--neg); } .delta.flat { color: var(--slate); }
.bar { height: 4px; background: var(--soft); margin-top: .45rem; }
.bar span { display: block; height: 4px; background: linear-gradient(90deg, var(--brass) 0%, #E2CB96 100%); }

/* ---------- order blotter (the "hyperfast" log) ---------- */
.blotter { background: var(--panel); border: 1px solid var(--rule); box-shadow: var(--shadow); border-radius: 3px; overflow: hidden; }
.blotter .head { display: flex; justify-content: space-between; align-items: center; gap: .8rem;
                 padding: .6rem .9rem; border-bottom: 1px solid var(--rule); background: var(--soft);
                 flex-wrap: wrap; }
.blotter .head .tag { font-size: .84rem; color: var(--ink); font-weight: 600; letter-spacing: -.005em; }
.blotter .head .pulse { display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: var(--pos);
                        margin-right: .45rem; vertical-align: middle; animation: blotter-pulse 1.1s ease-in-out infinite; }
.blotter .head .cadence { font-size: .76rem; color: var(--slate); font-variant-numeric: tabular-nums; }
.blotter .cols { display: grid; grid-template-columns: 4.6rem 3.2rem 4.4rem 2.8rem 3.6rem 1fr; gap: .5rem;
                 padding: .4rem .9rem; font-size: .74rem; color: var(--slate);
                 border-bottom: 1px solid var(--rule); }
.blotter .rows { max-height: 290px; overflow-y: auto; font-family: 'IBM Plex Mono', 'SFMono-Regular', Consolas, monospace;
                font-size: .8rem; font-variant-numeric: tabular-nums; }
.blotter .row { display: grid; grid-template-columns: 4.6rem 3.2rem 4.4rem 2.8rem 3.6rem 1fr; gap: .5rem;
                padding: .26rem .9rem; border-bottom: 1px solid var(--rule); color: var(--slate); }
.blotter .row:last-child { border-bottom: none; }
.blotter .row:first-child { animation: blotter-flash 900ms ease-out; }
.blotter .row .side.buy { color: var(--pos); font-weight: 600; }
.blotter .row .side.sell { color: var(--neg); font-weight: 600; }
.blotter .row .px, .blotter .row .pos { color: var(--ink); }
.blotter .row .pnl.pos { color: var(--pos); } .blotter .row .pnl.neg { color: var(--neg); }
.blotter .foot { padding: .5rem .9rem; border-top: 1px solid var(--rule); font-size: .78rem; color: var(--slate); }
@keyframes blotter-pulse { 0%, 100% { opacity: 1; } 50% { opacity: .2; } }
@keyframes blotter-flash { 0% { background: var(--brass-tint); } 100% { background: transparent; } }

/* ---------- comps table ---------- */
.comps-wrap { overflow-x: auto; background: var(--panel); border: 1px solid var(--rule); border-radius: 3px; box-shadow: var(--lift); }
table.comps { border-collapse: collapse; width: 100%; font-size: .85rem; font-variant-numeric: tabular-nums; color: var(--ink); }
table.comps th { text-align: right; font-weight: 600; color: var(--slate); font-size: .8rem; padding: .6rem .6rem;
                 border-bottom: 1px solid var(--ink); white-space: nowrap; background: var(--panel); }
table.comps th, table.comps td { border-left: none !important; border-right: none !important; }
table.comps th:first-child, table.comps td:first-child { text-align: left; position: sticky; left: 0; z-index: 1;
                                                       background: var(--panel); }
table.comps td { text-align: right; padding: .5rem .6rem; border-bottom: 1px solid var(--rule); white-space: nowrap; }
table.comps tr.focal td { background: var(--brass-tint); font-weight: 600; }
table.comps tr.focal td:first-child { background: var(--brass-tint); box-shadow: inset 3px 0 0 var(--brass); color: var(--brass); }
table.comps tr.median td { border-top: 1px solid var(--ink); border-bottom: none; color: var(--slate); font-style: italic; }
table.comps td.Green { color: var(--pos); } table.comps td.Red { color: var(--neg); }
table.comps td.Amber { color: var(--watch); }

/* ---------- findings ---------- */
.finding { display: grid; grid-template-columns: 2.2rem 1fr; background: var(--panel); border: 1px solid var(--rule);
           border-left: 3px solid var(--slate); padding: .8rem 1rem; margin-bottom: .5rem; }
.finding.Red { border-left-color: var(--neg); } .finding.Amber { border-left-color: var(--watch); }
.finding.Green { border-left-color: var(--pos); }
.finding .idx { font-family: 'Instrument Serif', Georgia, serif; font-size: 1.25rem; color: var(--slate); }
.finding .what { font-weight: 600; }
.finding .flag { font-size: .78rem; color: var(--slate); margin-left: .5rem; font-weight: 500; }
.finding .body { color: var(--ink); line-height: 1.5; margin-top: .15rem; }
.strengths { background: var(--panel); border: 1px solid var(--rule); padding: .8rem 1rem; line-height: 1.7; }
.strengths .item { color: var(--ink); } .strengths .item::before { content: "▲"; color: var(--pos); font-size: .7rem; margin-right: .5rem; }

/* ---------- Streamlit widgets: explicit in both themes ---------- */
section[data-testid="stSidebar"] { background: var(--panel); border-right: 1px solid var(--rule); }
section[data-testid="stSidebar"] *, div[data-testid="stSidebarContent"] * { color: var(--ink); }
section[data-testid="stSidebar"] h3 { font-family: 'Instrument Serif', Georgia, serif; color: var(--ink); }
section[data-testid="stSidebar"] [data-testid="stCaptionContainer"],
section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] * { color: var(--slate) !important; }
[data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] * { color: var(--ink) !important; }
[data-testid="stCaptionContainer"], [data-testid="stCaptionContainer"] * { color: var(--slate) !important; }
[data-testid="stSliderTickBarMin"], [data-testid="stSliderTickBarMax"],
[data-testid="stTickBarMin"], [data-testid="stTickBarMax"] { color: var(--slate) !important; }
div[data-testid="stRadio"] label p, div[data-testid="stCheckbox"] label p,
div[data-testid="stToggle"] label p { color: var(--ink) !important; }
/* Streamlit's select and text inputs render as unlabelled emotion divs, so style them by container. */
[data-testid="stSelectbox"] > div > div, [data-testid="stMultiSelect"] > div > div,
[data-testid="stTextInput"] > div > div, div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div, div[data-baseweb="base-input"],
div[data-testid="stNumberInputContainer"] { background: var(--input) !important; border-color: var(--rule) !important;
                                            color: var(--ink) !important; }
[data-testid="stSelectbox"] input, [data-testid="stMultiSelect"] input,
[data-testid="stSelectbox"] div[value], div[data-baseweb="select"] * { color: var(--ink); }
div[data-baseweb="select"] svg, div[data-testid="stNumberInputContainer"] svg { fill: var(--slate); }
ul[data-baseweb="menu"], div[data-baseweb="popover"] div { background: var(--panel) !important; color: var(--ink) !important; }
div[data-testid="stTabs"] [role="tablist"] { border-bottom: 1px solid var(--rule); gap: 1.4rem; }
div[data-testid="stTabs"] button { font-weight: 500; padding-left: 0; padding-right: 0;
                                   color: var(--slate) !important; }
div[data-testid="stTabs"] button * { color: inherit !important; }
div[data-testid="stTabs"] button[aria-selected="true"] { color: var(--ink) !important; font-weight: 600; }
div[data-baseweb="tab-highlight"] { background-color: var(--accent) !important; }
div[data-baseweb="tag"] { border-radius: 2px !important; background: var(--accent) !important; }
div[data-baseweb="tag"] span, div[data-baseweb="tag"] svg { color: var(--accent-ink) !important; fill: var(--accent-ink) !important; }
button[data-testid="stBaseButton-primary"] { border-radius: 3px; background: var(--accent); border: 1px solid var(--accent);
                                             color: var(--accent-ink); font-weight: 600; padding: .6rem 1.5rem;
                                             letter-spacing: .005em; transition: filter .15s ease; }
button[data-testid="stBaseButton-primary"]:hover { filter: brightness(1.1); color: var(--accent-ink); }
button[data-testid="stBaseButton-secondary"] { border-radius: 2px; background: var(--panel); color: var(--ink);
                                               border: 1px solid var(--rule); }
div[data-testid="stButtonGroup"] button { border-radius: 2px !important; font-size: .86rem; background: var(--panel);
                                          color: var(--ink); border: 1px solid var(--rule); }
div[data-testid="stButtonGroup"] button p { color: var(--ink); }
div[data-testid="stButtonGroup"] button[kind="pillsActive"], div[data-testid="stButtonGroup"] button[aria-checked="true"],
div[data-testid="stButtonGroup"] button[data-testid="stBaseButton-pillsActive"] {
  background: var(--accent) !important; border-color: var(--accent) !important; }
div[data-testid="stButtonGroup"] button[kind="pillsActive"] p,
div[data-testid="stButtonGroup"] button[aria-checked="true"] p,
div[data-testid="stButtonGroup"] button[data-testid="stBaseButton-pillsActive"] p { color: var(--accent-ink) !important; }
div[data-testid="stDownloadButton"] button { border-radius: 2px; font-weight: 600; }
div[data-testid="stExpander"] details { border-radius: 2px; border-color: var(--rule); background: var(--panel); }
div[data-testid="stExpander"] summary, div[data-testid="stExpander"] summary * { color: var(--ink); }
div[data-testid="stPlotlyChart"] { background: var(--panel); border: 1px solid var(--rule); padding: .4rem; }
div[data-testid="stAlertContainer"] { background: var(--soft); color: var(--ink); border: 1px solid var(--rule); }
div[data-testid="stAlertContainer"] * { color: var(--ink); }
div[data-testid="stMetricValue"], div[data-testid="stMetricLabel"] * { color: var(--ink); }
div[data-testid="stDataFrame"] { border: 1px solid var(--rule); }
.note-src { color: var(--slate); font-size: .8rem; margin-top: .35rem; }
hr, div[data-testid="stSidebar"] hr { border-color: var(--rule); }
:focus-visible { outline: 2px solid var(--accent) !important; outline-offset: 2px; }
@media (max-width: 800px) {
  .masthead, .process { padding-left: 1rem; padding-right: 1rem; }
  .masthead .meta { text-align: left; }
  .process .stage { padding-right: .5rem; margin-right: .6rem; font-size: .8rem; }
  .report .title { font-size: 1.5rem; }
  .cell { border-right: none; border-bottom: 1px solid var(--rule); }
}
</style>
"""


def css(dark=False):
    """The stylesheet with the chosen palette. Variables are declared here, so every rule above
    follows the theme and nothing depends on Streamlit's own light or dark base."""
    return "<style>:root {" + PALETTES["dark" if dark else "light"] + "}</style>" + BASE_CSS


def masthead(mode_is_live, source_label):
    status = "live" if mode_is_live else "demo"
    label = "Live market data" if mode_is_live else "Demo data (synthetic)"
    today = dt.date.today().strftime("%d %b %Y")
    return (f'<div class="masthead"><div><div class="brand">PeerLens</div>'
            f'<div class="desk">Peer comparables for the Nifty 500</div></div>'
            f'<div class="meta"><span class="status {status}"></span><b>{label}</b><br>'
            f'Universe: {html.escape(source_label)}. {today}</div></div>')


def blotter(rows, tag, cadence=None, empty_note="No fills yet this session."):
    """A dense, monospace order-log panel for one strategy's own fills, newest first — the live
    blotter a scalper's own trader would watch, distinct from the whole market's trade tape."""
    cadence_html = f'<span class="cadence">{html.escape(cadence)}</span>' if cadence else ""
    header = (f'<div class="head"><span class="tag"><span class="pulse"></span>'
              f'{html.escape(tag)}</span>{cadence_html}</div>')
    cols = ('<div class="cols"><div>Time</div><div>Side</div><div>Price</div><div>Qty</div>'
            '<div>Position</div><div>Running P&amp;L</div></div>')
    if not rows:
        body = f'<div class="foot">{html.escape(empty_note)}</div>'
    else:
        parts = []
        for r in rows:
            pnl_class = "pos" if r["pnl"] >= 0 else "neg"
            parts.append(
                f'<div class="row"><div class="time">{html.escape(str(r["time"]))}</div>'
                f'<div class="side {r["side"]}">{"BUY" if r["side"] == "buy" else "SELL"}</div>'
                f'<div class="px">{r["price"]:.2f}</div><div class="qty">{r["qty"]:,}</div>'
                f'<div class="pos">{r["position"]:+,}</div>'
                f'<div class="pnl {pnl_class}">₹{r["pnl"]:+,.0f}</div></div>')
        body = '<div class="rows">' + "".join(parts) + '</div>'
    return f'<div class="blotter">{header}{cols}{body}</div>'


def process_line(current):
    stages = ["Universe", "Peer set", "Analysis", "Export"]
    parts = []
    for i, name in enumerate(stages, 1):
        state = "done" if i < current else "now" if i == current else ""
        parts.append(f'<div class="stage {state}"><b>{i}</b>{name}</div>')
    return '<div class="process">' + "".join(parts) + "</div>"


HERO_3D = """
<div id="hero-wrap" style="position:relative;width:100%;height:230px;overflow:hidden;
     background:#080B11;border-bottom:1px solid #C8A96A;">
  <canvas id="hero" style="display:block;width:100%;height:230px;"></canvas>
  <div style="position:absolute;left:1.7rem;bottom:1.15rem;pointer-events:none;">
    <div style="font-family:'Instrument Serif',Georgia,serif;font-size:2.6rem;color:#F2F5FA;
                line-height:1;letter-spacing:-.02em;">PeerLens</div>
    <div style="font-family:Archivo,sans-serif;font-size:.92rem;color:#7E8CA2;margin-top:.3rem;">
      __DESK__</div>
  </div>
  <div style="position:absolute;right:1.7rem;bottom:1.15rem;text-align:right;pointer-events:none;
              font-family:Archivo,sans-serif;font-size:.85rem;color:#7E8CA2;line-height:1.5;">
    <span style="display:inline-block;width:7px;height:7px;border-radius:50%;
                 background:__DOT__;margin-right:.4rem;"></span><b
         style="color:#F2F5FA;font-weight:600;">__LABEL__</b><br>__META__</div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
(function () {
  var canvas = document.getElementById('hero');
  if (!canvas || !window.THREE) return;
  var wrap = document.getElementById('hero-wrap');
  var W = wrap.clientWidth, H = 230;

  var scene = new THREE.Scene();
  scene.fog = new THREE.FogExp2(0x080B11, 0.055);
  var camera = new THREE.PerspectiveCamera(58, W / H, 0.1, 120);
  camera.position.set(0, 3.4, 15);
  camera.lookAt(0, 0.6, 0);

  var renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: false });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.setSize(W, H, false);
  renderer.setClearColor(0x080B11, 1);

  // a terrain of bars: a market depth ladder read as landscape
  var COLS = 56, ROWS = 11, group = new THREE.Group();
  var geo = new THREE.BoxGeometry(0.17, 1, 0.17);
  var gold = new THREE.MeshBasicMaterial({ color: 0xC8A96A });
  var steel = new THREE.MeshBasicMaterial({ color: 0x2A3C52 });
  var bars = [];
  for (var r = 0; r < ROWS; r++) {
    for (var c = 0; c < COLS; c++) {
      var isGold = (r === ((ROWS - 1) / 2)) && (c % 9 === 0);
      var m = new THREE.Mesh(geo, isGold ? gold : steel);
      m.position.set((c - COLS / 2) * 0.42, 0, (r - ROWS / 2) * 0.72);
      m.userData.phase = c * 0.26 + r * 0.42;
      m.userData.gold = isGold;
      group.add(m); bars.push(m);
    }
  }
  scene.add(group);

  var grid = new THREE.GridHelper(44, 44, 0x16202C, 0x111923);
  grid.position.y = -0.02; scene.add(grid);

  var t = 0, raf = null;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function frame() {
    t += reduce ? 0 : 0.012;
    for (var i = 0; i < bars.length; i++) {
      var b = bars[i];
      var h = 0.35 + Math.abs(Math.sin(b.userData.phase + t)) * (b.userData.gold ? 2.6 : 1.5);
      b.scale.y = h; b.position.y = h / 2;
    }
    group.rotation.y = Math.sin(t * 0.18) * 0.11;
    renderer.render(scene, camera);
    raf = requestAnimationFrame(frame);
  }
  frame();

  window.addEventListener('resize', function () {
    W = wrap.clientWidth; camera.aspect = W / H; camera.updateProjectionMatrix();
    renderer.setSize(W, H, false);
  });
  document.addEventListener('visibilitychange', function () {   // stop burning GPU in a hidden tab
    if (document.hidden) { cancelAnimationFrame(raf); raf = null; }
    else if (!raf) frame();
  });
})();
</script>
"""


def hero_3d(mode_is_live, source_label):
    """A WebGL masthead: a depth ladder rendered as terrain, champagne spines marking the focal
    columns. Falls back to nothing if WebGL is unavailable, so the page below always stands alone."""
    today = dt.date.today().strftime("%d %b %Y")
    label = "Live market data" if mode_is_live else "Demo data (synthetic)"
    dot = "#4FAE87" if mode_is_live else "#C8A96A"
    return (HERO_3D
            .replace("__DESK__", "Peer comparables for the Nifty 500")
            .replace("__LABEL__", html.escape(label))
            .replace("__DOT__", dot)
            .replace("__META__", f"Universe: {html.escape(source_label)}. {today}"))
