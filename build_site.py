import os

base = os.path.dirname(os.path.abspath(__file__))

# ── favicon ──────────────────────────────────────────────────────────────────
FAVICON = '  <link rel="icon" type="image/png" sizes="64x64" href="favicon.png"/>\n  <link rel="shortcut icon" href="favicon.png"/>'

TRACKER = '<script src="https://multum-site-analytics.netlify.app/track.js" data-site="plaiceholder" defer></script>'

# ── SVG icons (solid brand colors, no gradient) ───────────────────────────────
# Usage: ICON["key"] — drop straight into HTML as the icon div's content
ICON = {
  # trending-up (chart line)
  "trending": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>',
  # refresh/cycle
  "refresh": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>',
  # receipt/file
  "receipt": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16l3-2 2 2 2-2 2 2 2-2 3 2V4a2 2 0 0 0-2-2z"/><line x1="8" y1="10" x2="16" y2="10"/><line x1="8" y1="14" x2="16" y2="14"/></svg>',
  # target/crosshair
  "target": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
  # alert triangle
  "alert": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>',
  # search/magnifier
  "search": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>',
  # bar chart
  "chart": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/><line x1="2" y1="20" x2="22" y2="20"/></svg>',
  # key
  "key": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.778 7.778 5.5 5.5 0 0 1 7.777-7.777zm0 0L15.5 7.5m0 0l3 3L22 7l-3-3m-3.5 3.5L19 4"/></svg>',
  # clock/timer
  "clock": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
  # flask/beaker (dry run)
  "flask": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3h6m-6 0v6L4.5 15A2 2 0 0 0 6 18h12a2 2 0 0 0 1.5-3L15 9V3"/><line x1="6" y1="12" x2="18" y2="12"/></svg>',
  # clipboard (pilot first)
  "clipboard": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg>',
  # link/chain (sources)
  "link": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>',
  # coin/dollar (spending caps)
  "coin": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>',
  # ban/shield (never deletes)
  "shield": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
  # file-text (paper trail)
  "filetext": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>',
  # user (people decide)
  "user": '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
}

# ── navigation ────────────────────────────────────────────────────────────────
def nav(active):
    links = [
        ("Home", "index.html", "home"),
        ("Agents", "agents.html", "agents"),
        ("How It Works", "how-it-works.html", "how"),
        ("Pricing", "pricing.html", "pricing"),
        ("ROI Calculator", "roi.html", "roi"),
        ("Case Study", "case-study.html", "case"),
        ("Blog", "blog.html", "blog"),
        ("About", "about.html", "about"),
    ]
    items = ""
    for label, href, key in links:
        cls = ' class="active"' if active == key else ""
        items += f'    <li><a href="{href}"{cls}>{label}</a></li>\n'
    cta_cls = " active" if active == "contact" else ""
    items += f'    <li><a href="contact.html" class="nav-cta{cta_cls}">Book a Call</a></li>\n'
    return f"""<nav>
  <a href="index.html" class="logo">{{PlAIceholder}}</a>
  <ul>
{items}  </ul>
  <button class="hamburger" aria-label="Menu" onclick="this.closest('nav').classList.toggle('open')">&#9776;</button>
</nav>"""

FOOTER = """<footer>
  <div class="footer-inner">
    <div>
      <a href="index.html" class="logo footer-logo">{PlAIceholder}</a>
      <p class="footer-tag">AI agents that do the busywork inside the tools you already use.</p>
    </div>
    <div class="footer-links">
      <a href="agents.html">Agents</a>
      <a href="how-it-works.html">How It Works</a>
      <a href="pricing.html">Pricing</a>
      <a href="case-study.html">Case Study</a>
      <a href="contact.html">Contact</a>
      <a href="https://www.linkedin.com/company/plaiceholder-io" target="_blank" rel="noopener" class="footer-linkedin" aria-label="LinkedIn">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="li-grad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#1A6EF5"/>
              <stop offset="50%" stop-color="#3EC9C9"/>
              <stop offset="100%" stop-color="#2ECC71"/>
            </linearGradient>
          </defs>
          <rect width="24" height="24" rx="5" fill="url(#li-grad)"/>
          <path d="M7 10h2v7H7v-7zm1-3a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm4 3h1.9v1h.1c.3-.5 1-1.1 2-1.1 2.1 0 2.5 1.4 2.5 3.2V17h-2v-3.5c0-.8 0-1.9-1.2-1.9s-1.3.9-1.3 1.8V17H12v-7z" fill="#fff"/>
        </svg>
      </a>
    </div>
  </div>
  <p class="footer-copy">© 2026 {PlAIceholder}. All rights reserved.</p>
</footer>"""

# ── shared CSS ────────────────────────────────────────────────────────────────
CSS = """:root {
  --blue: #1a6ef5;
  --sea:  #3ec9c9;
  --green:#2ecc71;
  --dark: #0d1b2a;
  --ink:  #1a2e20;
  --muted:#5a7a65;
  --light:#f4fdf8;
  --border: rgba(62,201,201,.18);
  --grad: linear-gradient(135deg,#1a6ef5 0%,#3ec9c9 50%,#2ecc71 100%);
  --grad2:linear-gradient(135deg,#0d1b2a 0%,#1a3a5c 100%);
}
*{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:'Segoe UI',system-ui,sans-serif;color:var(--ink);background:var(--light);line-height:1.65;}

/* ── nav ── */
nav{position:sticky;top:0;z-index:200;display:flex;align-items:center;justify-content:space-between;
  padding:.7rem 2.5rem;background:rgba(255,255,255,.97);backdrop-filter:blur(10px);
  border-bottom:1px solid var(--border);}
.logo{font-size:1.2rem;font-weight:800;background:var(--grad);-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;background-clip:text;text-decoration:none;}
nav ul{list-style:none;display:flex;gap:1.5rem;align-items:center;}
nav a{text-decoration:none;color:var(--ink);font-weight:500;font-size:.88rem;transition:color .2s;}
nav a:hover,nav a.active{color:var(--blue);}
.nav-cta{background:var(--grad);color:#fff !important;padding:.38rem 1.1rem;
  border-radius:100px;-webkit-text-fill-color:#fff !important;font-size:.85rem !important;}
.nav-cta:hover,.nav-cta.active{opacity:.85;}
.hamburger{display:none;background:none;border:none;font-size:1.4rem;cursor:pointer;color:var(--ink);}
@media(max-width:760px){
  nav ul{display:none;flex-direction:column;position:absolute;top:100%;left:0;right:0;
    background:#fff;border-bottom:1px solid var(--border);padding:1rem 2rem 1.5rem;gap:.9rem;}
  nav.open ul{display:flex;}
  .hamburger{display:block;}
}

/* ── layout ── */
.section{padding:5rem 2rem;}
.section-white{background:#fff;}
.section-light{background:var(--light);}
.section-dark{background:var(--dark);color:#fff;}
.inner{max-width:1080px;margin:0 auto;}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:start;}
.table-scroll{overflow-x:auto;-webkit-overflow-scrolling:touch;}
.tag{display:block;font-size:.72rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
  background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;margin-bottom:.35rem;}
h2{font-size:clamp(1.6rem,3.5vw,2.4rem);font-weight:800;line-height:1.2;margin-bottom:.8rem;color:var(--dark);}
.section-dark h2{color:#fff;}
.sub{font-size:1rem;color:var(--muted);max-width:580px;margin-bottom:2.5rem;}
.section-dark .sub{color:rgba(255,255,255,.7);}

/* ── hero ── */
.hero-section{min-height:92vh;display:flex;align-items:center;justify-content:center;
  text-align:center;background:var(--grad);padding:6rem 2rem 4rem;position:relative;overflow:hidden;}
.hero-section::before{content:'';position:absolute;inset:0;
  background:url("data:image/svg+xml,%3Csvg width='40' height='40' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='20' cy='20' r='2' fill='%23fff' fill-opacity='.07'/%3E%3C/svg%3E");}
.hero{position:relative;max-width:760px;}
.badge{display:inline-block;background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.4);
  color:#fff;padding:.28rem .9rem;border-radius:100px;font-size:.78rem;font-weight:600;
  margin-bottom:1.25rem;letter-spacing:.06em;}
.hero-section h1{font-size:clamp(2.1rem,5.5vw,3.8rem);font-weight:900;color:#fff;line-height:1.12;margin-bottom:1.1rem;}
.hero-section .lead{font-size:1.1rem;color:rgba(255,255,255,.88);max-width:560px;margin:0 auto 2.2rem;}
.hero-btns{display:flex;gap:.9rem;justify-content:center;flex-wrap:wrap;}

/* ── page banner ── */
.page-banner{background:var(--grad);padding:5rem 2rem 4rem;text-align:center;position:relative;overflow:hidden;}
.page-banner::before{content:'';position:absolute;inset:0;
  background:url("data:image/svg+xml,%3Csvg width='40' height='40' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='20' cy='20' r='2' fill='%23fff' fill-opacity='.07'/%3E%3C/svg%3E");}
.page-banner-inner{position:relative;max-width:680px;margin:0 auto;}
.page-banner h1{font-size:clamp(2rem,4.5vw,3.1rem);font-weight:900;color:#fff;line-height:1.15;margin-bottom:.75rem;}
.page-banner p{font-size:1.05rem;color:rgba(255,255,255,.85);}

/* ── buttons ── */
.btn{display:inline-block;padding:.75rem 1.75rem;border-radius:100px;font-weight:700;
  font-size:.92rem;text-decoration:none;transition:transform .2s,opacity .2s;cursor:pointer;border:none;}
.btn:hover{transform:translateY(-2px);opacity:.9;}
.btn-white{background:#fff;color:var(--blue);}
.btn-outline{background:transparent;border:2px solid #fff;color:#fff;}
.btn-grad{background:var(--grad);color:#fff;}
.btn-dark{background:var(--dark);color:#fff;}

/* ── cards ── */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:1.25rem;}
.card{background:#fff;border-radius:18px;padding:1.75rem;border:1px solid var(--border);
  transition:transform .25s,box-shadow .25s;}
.card:hover{transform:translateY(-5px);box-shadow:0 14px 36px rgba(26,110,245,.1);}
.icon{width:46px;height:46px;border-radius:11px;background:var(--grad);display:flex;
  align-items:center;justify-content:center;font-size:1.3rem;margin-bottom:1rem;flex-shrink:0;color:#fff;}
.card h3{font-size:1rem;font-weight:700;margin-bottom:.45rem;color:var(--dark);}
.card p{color:var(--muted);font-size:.88rem;}

/* ── 5-step diagram ── */
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:0;
  border:1px solid var(--border);border-radius:18px;overflow:hidden;background:#fff;}
.step{padding:1.6rem 1.25rem;border-right:1px solid var(--border);position:relative;}
.step:last-child{border-right:none;}
.step-num{font-size:2rem;font-weight:900;line-height:1;
  background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.step h3{font-size:.95rem;font-weight:700;margin:.35rem 0 .45rem;color:var(--dark);}
.step p{font-size:.82rem;color:var(--muted);}
@media(max-width:700px){
  .steps{grid-template-columns:1fr;}
  .step{border-right:none;border-bottom:1px solid var(--border);}
  .step:last-child{border-bottom:none;}
}

/* ── timeline ── */
.timeline{position:relative;padding-left:2rem;}
.timeline::before{content:'';position:absolute;left:.45rem;top:.5rem;bottom:.5rem;
  width:2px;background:var(--grad);}
.tl-item{position:relative;margin-bottom:2rem;}
.tl-item:last-child{margin-bottom:0;}
.tl-dot{position:absolute;left:-2rem;top:.3rem;width:18px;height:18px;border-radius:50%;
  background:var(--grad);flex-shrink:0;}
.tl-label{font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
  color:var(--sea);margin-bottom:.2rem;}
.tl-item h3{font-size:1rem;font-weight:700;color:var(--dark);margin-bottom:.3rem;}
.tl-item p{font-size:.88rem;color:var(--muted);}

/* ── trust grid ── */
.trust-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:1rem;}
.trust-item{display:flex;gap:.85rem;align-items:flex-start;}
.trust-icon{width:36px;height:36px;border-radius:9px;background:rgba(62,201,201,.15);
  display:flex;align-items:center;justify-content:center;font-size:.95rem;flex-shrink:0;margin-top:.1rem;color:#3EC9C9;}
.trust-item h4{font-size:.92rem;font-weight:700;color:#fff;margin-bottom:.2rem;}
.trust-item p{font-size:.82rem;color:rgba(255,255,255,.65);}

/* ── agent catalog ── */
.filter-bar{display:flex;gap:.6rem;flex-wrap:wrap;margin-bottom:2rem;align-items:center;}
.filter-btn{padding:.4rem 1.1rem;border-radius:100px;font-size:.82rem;font-weight:600;
  border:1.5px solid var(--border);background:#fff;color:var(--ink);cursor:pointer;transition:all .2s;}
.filter-btn.active,.filter-btn:hover{background:var(--grad);border-color:transparent;color:#fff;}
#agent-search{padding:.4rem 1rem;border-radius:100px;border:1.5px solid var(--border);
  font-size:.85rem;outline:none;background:#fff;color:var(--ink);min-width:200px;}
#agent-search:focus{border-color:var(--sea);}
.agent-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.25rem;}
.agent-card{background:#fff;border:1px solid var(--border);border-radius:18px;padding:1.6rem;
  transition:transform .25s,box-shadow .25s;display:flex;flex-direction:column;}
.agent-card:hover{transform:translateY(-4px);box-shadow:0 12px 32px rgba(26,110,245,.1);}
.agent-meta{display:flex;gap:.5rem;margin-bottom:.9rem;flex-wrap:wrap;}
.pill{display:inline-block;padding:.2rem .7rem;border-radius:100px;font-size:.72rem;font-weight:700;}
.pill-area{background:var(--light);color:var(--muted);}
.pill-tier{background:rgba(26,110,245,.08);color:var(--blue);}
.pill-ready{background:rgba(46,204,113,.12);color:#1a7a45;}
.pill-avail{background:rgba(62,201,201,.1);color:#1a6a6a;}
.agent-card h3{font-size:1rem;font-weight:700;color:var(--dark);margin-bottom:.4rem;}
.agent-card .job{font-size:.85rem;color:var(--muted);margin-bottom:.9rem;flex:1;}
.agent-connects{font-size:.78rem;color:var(--muted);}
.agent-connects strong{color:var(--ink);font-weight:600;}
.agent-card .demo-link{display:inline-block;margin-top:1rem;font-size:.82rem;font-weight:700;
  color:var(--blue);text-decoration:none;}
.agent-card .demo-link:hover{text-decoration:underline;}

/* ── pricing ── */
.plans{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.25rem;align-items:start;}
.plan{border:2px solid var(--border);border-radius:22px;padding:2rem;position:relative;
  background:#fff;transition:transform .25s;}
.plan:hover{transform:translateY(-4px);}
.plan.hot{background:var(--grad);border-color:transparent;}
.pbadge{position:absolute;top:-13px;left:50%;transform:translateX(-50%);background:var(--dark);
  color:#fff;font-size:.7rem;font-weight:700;letter-spacing:.08em;
  padding:.25rem 1rem;border-radius:100px;white-space:nowrap;}
.pname{font-size:.75rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
  margin-bottom:.3rem;color:var(--muted);}
.plan.hot .pname{color:rgba(255,255,255,.75);}
.price{font-size:2.3rem;font-weight:900;color:var(--dark);line-height:1;margin-bottom:.15rem;}
.plan.hot .price{color:#fff;}
.price-range{font-size:.95rem;font-weight:600;color:var(--dark);}
.plan.hot .price-range{color:#fff;}
.per{font-size:.82rem;color:var(--muted);margin-bottom:1.25rem;}
.plan.hot .per{color:rgba(255,255,255,.7);}
.feats{list-style:none;margin-bottom:1.75rem;}
.feats li{padding:.42rem 0;border-bottom:1px solid var(--border);font-size:.87rem;
  color:var(--muted);display:flex;align-items:flex-start;gap:.5rem;}
.feats li::before{content:'✓';font-weight:800;color:var(--green);flex-shrink:0;}
.plan.hot .feats li{border-bottom-color:rgba(255,255,255,.15);color:rgba(255,255,255,.9);}
.plan.hot .feats li::before{color:#fff;}
.pbtn{display:block;text-align:center;padding:.78rem;border-radius:100px;
  font-weight:700;font-size:.88rem;text-decoration:none;transition:opacity .2s;}
.pbtn:hover{opacity:.85;}
.pbtn-out{border:2px solid var(--sea);color:var(--blue);}
.plan.hot .pbtn{background:#fff;color:var(--blue);}
.founding-badge{display:inline-block;background:rgba(46,204,113,.12);color:#1a7a45;
  font-size:.72rem;font-weight:700;padding:.2rem .7rem;border-radius:100px;margin-bottom:1rem;}
.plan.hot .founding-badge{background:rgba(255,255,255,.2);color:#fff;}

/* ── comparison table ── */
.compare-table{width:100%;border-collapse:collapse;font-size:.88rem;margin-top:1.5rem;}
.compare-table th,.compare-table td{padding:.75rem 1rem;border-bottom:1px solid var(--border);text-align:left;}
.compare-table th{font-weight:700;color:var(--dark);background:var(--light);}
.compare-table tr:last-child td{border-bottom:none;}
.compare-table .highlight{font-weight:700;color:var(--blue);}
.compare-table a{color:var(--sea);font-size:.78rem;}

/* ── ROI teaser ── */
.roi-teaser{background:var(--dark);border-radius:22px;padding:2.5rem;color:#fff;}
.roi-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:.75rem;margin:1.75rem 0 2rem;}
.roi-stat{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.1);
  border-radius:12px;padding:1.25rem 1rem;}
.roi-stat .rval{font-size:1.8rem;font-weight:900;background:var(--grad);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1.1;}
.roi-stat .rlabel{font-size:.75rem;color:rgba(255,255,255,.6);margin-top:.3rem;}
.roi-teaser-note{font-size:.75rem;color:rgba(255,255,255,.4);margin-top:-.5rem;margin-bottom:1.5rem;}
/* ── ROI calculator (standalone page) ── */
.calc-results{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:.75rem;margin-bottom:1.5rem;}
.calc-result{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.1);
  border-radius:12px;padding:1rem;}
.calc-result .rval{font-size:1.6rem;font-weight:900;background:var(--grad);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.calc-result .rlabel{font-size:.75rem;color:rgba(255,255,255,.6);margin-top:.1rem;}
.calc-note{font-size:.75rem;color:rgba(255,255,255,.45);margin-bottom:1rem;}
.slider-row{display:flex;align-items:center;gap:.75rem;}
.slider-row input[type=range]{flex:1;accent-color:var(--blue);}
.slider-val{font-size:1rem;font-weight:700;color:var(--sea);min-width:3rem;text-align:right;}

/* ── quiz ── */
.quiz-wrap{background:#fff;border:1px solid var(--border);border-radius:22px;padding:2rem;}
.quiz-q{font-size:.95rem;font-weight:700;color:var(--dark);margin-bottom:.8rem;}
.quiz-opts{display:flex;flex-direction:column;gap:.45rem;margin-bottom:1.25rem;}
.quiz-opt{display:flex;align-items:center;gap:.6rem;font-size:.88rem;color:var(--muted);cursor:pointer;}
.quiz-opt input{accent-color:var(--blue);}
.quiz-result{background:var(--light);border:1px solid var(--border);border-radius:12px;
  padding:1.25rem;font-size:.9rem;color:var(--dark);display:none;}
.quiz-result.show{display:block;}
.quiz-result strong{color:var(--blue);}

/* ── FAQ ── */
.faq{max-width:720px;}
details{border-bottom:1px solid var(--border);padding:.9rem 0;}
summary{font-weight:700;font-size:.95rem;color:var(--dark);cursor:pointer;list-style:none;
  display:flex;justify-content:space-between;align-items:center;gap:1rem;}
summary::after{content:'+';font-size:1.2rem;color:var(--sea);flex-shrink:0;}
details[open] summary::after{content:'−';}
details p{padding:.7rem 0 0;font-size:.88rem;color:var(--muted);max-width:640px;}

/* ── care plan table ── */
.care-table{width:100%;border-collapse:collapse;font-size:.87rem;}
.care-table th,.care-table td{padding:.75rem 1rem;border-bottom:1px solid var(--border);text-align:left;}
.care-table th{font-weight:700;color:var(--dark);background:var(--light);}
.care-table td:not(:first-child){text-align:center;}
.care-table .yes{color:var(--green);font-weight:700;}
.care-table .no{color:var(--muted);}

/* ── contact ── */
.contact-wrap{display:grid;grid-template-columns:1fr 1.5fr;gap:3.5rem;align-items:start;}
.ci p{color:var(--muted);margin-bottom:1.5rem;font-size:.92rem;}
.ci-chip{display:flex;align-items:center;gap:.65rem;margin-bottom:.9rem;color:var(--muted);font-size:.88rem;}
.ci-chip .ic{width:34px;height:34px;border-radius:8px;background:var(--grad);
  display:flex;align-items:center;justify-content:center;font-size:.88rem;flex-shrink:0;}
form.contact-form{display:flex;flex-direction:column;gap:1rem;}
.frow{display:grid;grid-template-columns:1fr 1fr;gap:.8rem;}
input,textarea,select{width:100%;padding:.7rem .9rem;border:1.5px solid var(--border);
  border-radius:10px;font-size:.88rem;font-family:inherit;background:#fff;
  color:var(--ink);outline:none;transition:border-color .2s;}
input:focus,textarea:focus,select:focus{border-color:var(--sea);}
textarea{resize:vertical;min-height:90px;}
fieldset{border:1.5px solid var(--border);border-radius:12px;padding:.85rem 1rem;}
legend{font-size:.75rem;font-weight:700;color:var(--muted);padding:0 .4rem;letter-spacing:.05em;text-transform:uppercase;}
.chip-group{display:flex;flex-wrap:wrap;gap:.45rem;margin-top:.5rem;}
.chip-check{cursor:pointer;position:relative;}
.chip-check input{position:absolute;opacity:0;width:0;height:0;}
.chip-check span{display:inline-block;padding:.35rem .85rem;border:1.5px solid var(--border);
  border-radius:100px;font-size:.8rem;color:var(--muted);transition:all .15s;white-space:nowrap;}
.chip-check input:checked+span{background:var(--blue);border-color:var(--blue);color:#fff;}
.chip-check:hover span{border-color:var(--sea);color:var(--sea);}
.sbtn{background:var(--grad);color:#fff;padding:.78rem 1.75rem;border-radius:100px;
  font-size:.92rem;font-weight:700;border:none;cursor:pointer;
  transition:opacity .2s,transform .2s;align-self:flex-start;}
.sbtn:hover{opacity:.88;transform:translateY(-2px);}
.form-success{display:none;background:rgba(46,204,113,.1);border:1.5px solid var(--green);
  border-radius:12px;padding:1rem 1.25rem;color:#1a7a45;font-size:.9rem;font-weight:600;}
/* ── chat widget ── */
#nl-badge-frame,[class*="netlify"],[id*="netlify"]{display:none!important;}
.chat-widget{position:fixed;bottom:1.25rem;right:1.25rem;z-index:9999;display:flex;flex-direction:column;align-items:flex-end;gap:.6rem;}
.chat-btn{background:rgba(13,27,42,.8);color:var(--blue);font-size:.9rem;font-weight:800;
  padding:.35rem .75rem;border-radius:100px;border:1px solid rgba(255,255,255,.18);
  backdrop-filter:blur(8px);cursor:pointer;transition:opacity .2s;letter-spacing:.02em;font-family:inherit;}
.chat-btn:hover{opacity:.8;}
.chat-panel{display:none;flex-direction:column;width:414px;height:580px;
  background:#fff;border-radius:18px;box-shadow:0 20px 60px rgba(0,0,0,.22);
  overflow:hidden;border:1.5px solid var(--border);}
.chat-panel.open{display:flex;}
.chat-header{background:var(--dark);padding:1rem 1.25rem;display:flex;align-items:center;justify-content:space-between;}
.chat-logo{font-size:1.05rem;font-weight:800;background:var(--grad);-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;background-clip:text;line-height:1.2;}
.chat-sub{font-size:.74rem;color:rgba(255,255,255,.45);margin-top:.1rem;}
.chat-close{background:none;border:none;color:rgba(255,255,255,.45);font-size:1.2rem;
  cursor:pointer;padding:.2rem;line-height:1;transition:color .15s;font-family:inherit;}
.chat-close:hover{color:#fff;}
.chat-messages{flex:1;overflow-y:auto;padding:1rem;display:flex;flex-direction:column;gap:.65rem;}
.msg{max-width:85%;padding:.6rem .9rem;border-radius:14px;font-size:.86rem;line-height:1.5;word-break:break-word;}
.msg-ai{background:var(--light);color:var(--ink);border-bottom-left-radius:4px;align-self:flex-start;}
.msg-user{background:var(--blue);color:#fff;border-bottom-right-radius:4px;align-self:flex-end;}
.msg-typing{align-self:flex-start;padding:.6rem .9rem;background:var(--light);border-radius:14px;border-bottom-left-radius:4px;}
.typing-dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--muted);
  animation:tdot 1.2s infinite ease-in-out;margin:0 2px;}
.typing-dot:nth-child(2){animation-delay:.2s;}
.typing-dot:nth-child(3){animation-delay:.4s;}
@keyframes tdot{0%,60%,100%{transform:translateY(0);}30%{transform:translateY(-6px);}}
.chat-input-row{display:flex;gap:.5rem;padding:.75rem;border-top:1.5px solid var(--border);background:#fff;}
.chat-input-row input{flex:1;padding:.6rem .85rem;border:1.5px solid var(--border);border-radius:9px;
  font-size:.85rem;font-family:inherit;outline:none;transition:border-color .2s;}
.chat-input-row input:focus{border-color:var(--sea);}
.chat-send{background:var(--grad);color:#fff;border:none;border-radius:9px;
  padding:.6rem .95rem;font-size:.95rem;cursor:pointer;transition:opacity .2s;}
.chat-send:hover{opacity:.85;}
.chat-send:disabled,.chat-input-row input:disabled{opacity:.5;cursor:default;}
@media(max-width:460px){.chat-panel{width:calc(100vw - 1.5rem);height:72vh;}}

/* ── case study ── */
.cs-grid{display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:start;}
.cs-stat{text-align:center;padding:1.5rem;background:var(--light);border-radius:16px;border:1px solid var(--border);}
.cs-stat .n{font-size:2rem;font-weight:900;background:var(--grad);-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;background-clip:text;display:block;}
.cs-stat .l{font-size:.82rem;color:var(--muted);}
.cs-stats{display:grid;grid-template-columns:1fr 1fr;gap:.75rem;margin-bottom:1.5rem;}
.pending-block{background:rgba(26,110,245,.05);border:1.5px dashed rgba(26,110,245,.25);
  border-radius:12px;padding:1rem 1.25rem;font-size:.85rem;color:var(--muted);margin-top:.75rem;}
.pending-block strong{color:var(--blue);}
@media(max-width:700px){.cs-grid{grid-template-columns:1fr;}}

/* ── about strip ── */
.about-grid{display:grid;grid-template-columns:1fr 1fr;gap:3.5rem;align-items:center;}
.about-vis{background:var(--grad);border-radius:20px;padding:2.5rem;
  display:flex;flex-direction:column;gap:.9rem;}
.astat{background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.3);
  border-radius:12px;padding:1rem 1.25rem;color:#fff;}
.astat .n{font-size:1.9rem;font-weight:900;display:block;}
.astat .l{font-size:.82rem;opacity:.85;}
.checklist{list-style:none;margin-top:1rem;}
.checklist li{display:flex;gap:.55rem;margin-bottom:.55rem;color:var(--muted);align-items:flex-start;font-size:.9rem;}
.checklist li::before{content:'✓';background:var(--grad);-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;background-clip:text;font-weight:900;flex-shrink:0;}

/* ── footer ── */
footer{background:var(--dark);padding:2.5rem 2rem 1.5rem;}
.footer-inner{max-width:1080px;margin:0 auto;display:flex;justify-content:space-between;
  align-items:flex-start;flex-wrap:wrap;gap:2rem;margin-bottom:2rem;}
.footer-logo{font-size:1.2rem !important;-webkit-text-fill-color:#fff !important;display:inline-block;margin-bottom:.4rem;}
.footer-tag{font-size:.82rem;color:rgba(255,255,255,.45);max-width:260px;margin-top:.3rem;}
.footer-links{display:flex;gap:1.5rem;flex-wrap:wrap;}
.footer-links a{text-decoration:none;color:rgba(255,255,255,.5);font-size:.85rem;transition:color .2s;}
.footer-links a:hover{color:var(--sea);}
.footer-linkedin{display:flex;align-items:center;line-height:1;}
.footer-linkedin:hover{opacity:.8;}
.contact-linkedin{display:inline-flex;align-items:center;gap:.5rem;margin-top:1.25rem;font-size:.88rem;font-weight:600;color:var(--blue);text-decoration:none;}
.contact-linkedin:hover{opacity:.8;}
.footer-copy{text-align:center;font-size:.78rem;color:rgba(255,255,255,.3);max-width:1080px;margin:0 auto;}

@media(max-width:700px){
  /* layout */
  .section{padding:3rem 1rem;}
  .two-col,.about-grid,.contact-wrap,.frow,.cs-grid,.cs-stats{grid-template-columns:1fr;}
  .two-col{gap:2rem;}
  .footer-inner{flex-direction:column;}

  /* nav */
  nav{padding:.6rem 1rem;}

  /* hero */
  .hero-section{min-height:auto;padding:4rem 1rem 3rem;}
  .hero-section h1{font-size:clamp(1.9rem,8vw,2.8rem);}
  .hero-section .lead{font-size:1rem;margin-bottom:1.6rem;}
  .page-banner{padding:3rem 1rem 2.5rem;}
  .page-banner h1{font-size:clamp(1.7rem,7vw,2.4rem);}

  /* agents */
  .agent-grid{grid-template-columns:1fr;}
  #agent-search{width:100%;min-width:0;box-sizing:border-box;}
  .filter-bar{gap:.4rem;}
  .filter-btn{font-size:.78rem;padding:.35rem .85rem;}

  /* pricing */
  .plans{grid-template-columns:1fr;}

  /* ROI calc */
  .calc-grid{grid-template-columns:1fr;}
  .calc-wrap{padding:1.5rem 1rem;}

  /* contact form */
  .contact-wrap{grid-template-columns:1fr;}
  .frow{grid-template-columns:1fr;}
  .sbtn{width:100%;text-align:center;}

  /* buttons */
  .hero-btns{flex-direction:column;align-items:center;}
  .hero-btns .btn{width:100%;max-width:280px;text-align:center;}

  /* blog */
  .post-grid{grid-template-columns:1fr;}
}

/* ── blog ─────────────────────────────────────────────────────────────────── */
.post-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.5rem;}
.post-card{display:flex;flex-direction:column;gap:.6rem;padding:1.5rem;border-radius:14px;
  border:1.5px solid var(--border);background:#fff;text-decoration:none;color:inherit;
  transition:box-shadow .18s,transform .18s;}
.post-card:hover{box-shadow:0 8px 28px rgba(0,0,0,.09);transform:translateY(-2px);}
.post-tag{font-size:.74rem;font-weight:700;color:var(--sea);text-transform:uppercase;letter-spacing:.06em;}
.post-card h3{font-size:1.05rem;font-weight:700;color:var(--ink);line-height:1.35;margin:0;}
.post-preview{font-size:.88rem;color:var(--muted);line-height:1.55;margin:0;flex:1;}
.post-date{font-size:.78rem;color:var(--muted);margin-top:.25rem;}
.post-body{font-size:.95rem;line-height:1.75;color:var(--ink);}
.post-body h2{font-size:1.3rem;font-weight:700;margin:2rem 0 .75rem;}
.post-body p{margin:0 0 1.1rem;}
"""

# ── chat widget ───────────────────────────────────────────────────────────────
CHAT_WIDGET = """<div class="chat-widget">
  <button class="chat-btn" id="chat-btn" onclick="toggleChat()" aria-label="Chat with us">;)</button>
  <div class="chat-panel" id="chat-panel">
    <div class="chat-header">
      <div>
        <div class="chat-logo">{PlAIceholder}</div>
        <div class="chat-sub">Ask us anything</div>
      </div>
      <button class="chat-close" onclick="toggleChat()" aria-label="Close">&#x2715;</button>
    </div>
    <div class="chat-messages" id="chat-messages">
      <div class="msg msg-ai">Hey! Ask me about our agents, pricing, how we work — or I can help you book a free demo call.</div>
    </div>
    <div class="chat-input-row">
      <input type="text" id="chat-input" placeholder="Ask a question…" autocomplete="off"/>
      <button class="chat-send" id="chat-send">&#x2192;</button>
    </div>
  </div>
</div>
<script>
(function(){
  var panel=document.getElementById('chat-panel');
  var input=document.getElementById('chat-input');
  var msgs=document.getElementById('chat-messages');
  var history=[];
  window.toggleChat=function(){
    panel.classList.toggle('open');
    if(panel.classList.contains('open'))input.focus();
  };
  function addMsg(text,role){
    var d=document.createElement('div');
    d.className='msg msg-'+role;
    d.textContent=text;
    msgs.appendChild(d);
    msgs.scrollTop=msgs.scrollHeight;
    return d;
  }
  function showTyping(){
    var d=document.createElement('div');
    d.className='msg-typing';d.id='chat-typing';
    d.innerHTML='<span class="typing-dot"></span><span class="typing-dot"></span><span class="typing-dot"></span>';
    msgs.appendChild(d);msgs.scrollTop=msgs.scrollHeight;
  }
  function hideTyping(){var t=document.getElementById('chat-typing');if(t)t.remove();}
  async function send(){
    var text=input.value.trim();if(!text)return;
    input.value='';input.disabled=true;
    document.getElementById('chat-send').disabled=true;
    addMsg(text,'user');
    history.push({role:'user',content:text});
    showTyping();
    try{
      var r=await fetch('/.netlify/functions/chat',{
        method:'POST',headers:{'Content-Type':'application/json'},
        body:JSON.stringify({messages:history})
      });
      var data=await r.json();
      hideTyping();
      var reply=data.reply||'I had trouble with that. Try the contact page or book a call directly.';
      addMsg(reply,'ai');
      history.push({role:'assistant',content:reply});
    }catch(e){
      hideTyping();
      addMsg('Something went wrong — visit our contact page to reach us directly.','ai');
    }
    input.disabled=false;
    document.getElementById('chat-send').disabled=false;
    input.focus();
  }
  document.getElementById('chat-send').addEventListener('click',send);
  input.addEventListener('keydown',function(e){if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();send();}});
})();
</script>"""

# ── page wrapper ──────────────────────────────────────────────────────────────
def _sub_icons(s):
    import re
    return re.sub(r'\{ICON\["(\w+)"\]\}', lambda m: ICON.get(m.group(1), m.group(0)), s)

NETLIFY_KILL = """<script>
(function(){
  function killBadge(){
    var f=document.getElementById('nl-badge-frame');
    if(f)f.style.cssText='display:none!important';
    document.querySelectorAll('script[src*="netlify/scripts"]').forEach(function(s){s.remove();});
  }
  var obs=new MutationObserver(function(ml){
    ml.forEach(function(m){m.addedNodes.forEach(function(n){
      if(n.id==='nl-badge-frame')n.style.cssText='display:none!important';
    });});
  });
  obs.observe(document.body,{childList:true});
  document.addEventListener('DOMContentLoaded',killBadge);
  window.addEventListener('load',killBadge);
})();
</script>"""

def page(title, desc, active, body):
    body = _sub_icons(body)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>{title}</title>
  <meta name="description" content="{desc}"/>
{FAVICON}
  <link rel="stylesheet" href="style.css"/>
</head>
<body>
{nav(active)}
{body}
{FOOTER}
{CHAT_WIDGET}
{TRACKER}
{NETLIFY_KILL}
</body>
</html>"""

# ─────────────────────────────────────────────────────────────────────────────
# HOME
# ─────────────────────────────────────────────────────────────────────────────
HOME_BODY = """
<section class="hero-section">
  <div class="hero">
    <div class="badge">Custom-built AI agents for growing companies</div>
    <h1>Your team's slowest weekly task, handed to a custom AI agent in two weeks.</h1>
    <p class="lead">We design, build, and install AI agents tuned to how your business works — inside HubSpot, Salesforce, Zendesk, QuickBooks, and the other tools you already pay for.</p>
    <div class="hero-btns">
      <a href="contact.html" class="btn btn-white">Book a free 30-minute call</a>
      <a href="agents.html" class="btn btn-outline">See the agent catalog</a>
    </div>
  </div>
</section>

<!-- Who it's for -->
<section class="section section-white">
  <div class="inner">
    <span class="tag">Who it's for</span>
    <h2>Built for companies with 10 to 200 employees</h2>
    <p class="sub">You have budget to outsource a project, but not enough to hire a full-time AI engineer. That's exactly the gap we fill.</p>
    <div class="cards">
      <div class="card">
        <div class="icon">{ICON["trending"]}</div>
        <h3>Sales and prospecting</h3>
        <p>Find buying-signal companies, research new leads, prep for meetings, follow up stalled deals — done in minutes, not hours.</p>
      </div>
      <div class="card">
        <div class="icon">{ICON["refresh"]}</div>
        <h3>Customer success</h3>
        <p>Flag renewals at risk before they slip, triage support tickets and track onboarding — with the evidence your team needs.</p>
      </div>
      <div class="card">
        <div class="icon">{ICON["receipt"]}</div>
        <h3>Back office</h3>
        <p>Catch invoice problems before they're paid, screen applicants, write weekly KPI summaries — without adding headcount.</p>
      </div>
    </div>
  </div>
</section>

<!-- 5-step diagram -->
<section class="section section-light">
  <div class="inner">
    <span class="tag">How every agent works</span>
    <h2>Five steps, every time</h2>
    <p class="sub">Every agent follows the same pattern, no matter what job it does.</p>
    <div class="steps">
      <div class="step">
        <div class="step-num">1</div>
        <h3>Pull</h3>
        <p>Gets data from the tools you already pay for — CRM, help desk, accounting, spreadsheets.</p>
      </div>
      <div class="step">
        <div class="step-num">2</div>
        <h3>Think</h3>
        <p>A leading AI model does the research, reading, or judgment a person used to do — we build with whichever fits your stack.</p>
      </div>
      <div class="step">
        <div class="step-num">3</div>
        <h3>Check</h3>
        <p>Rules catch AI mistakes before anyone sees them. No source link means no claim. Hard rules always come first.</p>
      </div>
      <div class="step">
        <div class="step-num">4</div>
        <h3>Write back</h3>
        <p>Results go where your team already works — CRM fields, notes, Slack, or a report.</p>
      </div>
      <div class="step">
        <div class="step-num">5</div>
        <h3>Show and ask</h3>
        <p>A dashboard for the team, and a person says yes before anything is spent or changed.</p>
      </div>
    </div>
  </div>
</section>

<!-- Featured agents -->
<section class="section section-white">
  <div class="inner">
    <span class="tag">Ready now</span>
    <h2>Three agents with live demos</h2>
    <p class="sub">Built, tested, and running on sample data today. The rest of the catalog ships in 1 to 2 extra weeks.</p>
    <div class="cards">
      <div class="card">
        <div class="icon">{ICON["target"]}</div>
        <h3>Signal Prospector</h3>
        <p>Finds companies showing buying signals in the news, explains why now, finds the right contacts, and saves everything to your CRM.</p>
        <p style="margin-top:.75rem;font-size:.8rem;color:var(--blue);font-weight:600;">Sales · Advanced · from $6,000</p>
        <a href="demos/signal-prospector-dashboard.html" class="demo-link" style="display:inline-block;margin-top:.75rem;font-size:.82rem;font-weight:700;color:var(--blue);text-decoration:none;">View sample dashboard →</a>
      </div>
      <div class="card">
        <div class="icon">{ICON["alert"]}</div>
        <h3>Renewal Risk Radar</h3>
        <p>Reads tickets, notes, and usage for accounts renewing soon. Flags risk with evidence and a suggested next step.</p>
        <p style="margin-top:.75rem;font-size:.8rem;color:var(--blue);font-weight:600;">Customer success · Standard · from $3,500</p>
        <a href="demos/renewal-risk-dashboard.html" class="demo-link" style="display:inline-block;margin-top:.75rem;font-size:.82rem;font-weight:700;color:var(--blue);text-decoration:none;">View sample dashboard →</a>
      </div>
      <div class="card">
        <div class="icon">{ICON["receipt"]}</div>
        <h3>Invoice Checker</h3>
        <p>Matches every vendor invoice to its PO before it's paid. Flags duplicates, overbilling, and missing POs with dollars at risk.</p>
        <p style="margin-top:.75rem;font-size:.8rem;color:var(--blue);font-weight:600;">Back office · Standard · from $3,500</p>
        <a href="demos/invoice-checker-dashboard.html" class="demo-link" style="display:inline-block;margin-top:.75rem;font-size:.82rem;font-weight:700;color:var(--blue);text-decoration:none;">View sample dashboard →</a>
      </div>
    </div>
    <p style="margin-top:1.75rem;"><a href="agents.html" class="btn btn-dark">See all 13 agents →</a></p>
  </div>
</section>

<!-- Trust -->
<section class="section section-dark">
  <div class="inner">
    <span class="tag">Built to be trusted</span>
    <h2>Safety is not optional</h2>
    <p class="sub">Every agent ships with the same rules. They're not settings you can turn off.</p>
    <div class="trust-grid">
      <div class="trust-item"><div class="trust-icon">{ICON["flask"]}</div><div><h4>Dry run by default</h4><p>Nothing is written or spent without a yes, one step at a time.</p></div></div>
      <div class="trust-item"><div class="trust-icon">{ICON["clipboard"]}</div><div><h4>Pilot first</h4><p>Every agent proves itself on 20 records before a full run.</p></div></div>
      <div class="trust-item"><div class="trust-icon">{ICON["link"]}</div><div><h4>No made-up facts</h4><p>Every AI finding links to its source. Unsupported findings are thrown out automatically.</p></div></div>
      <div class="trust-item"><div class="trust-icon">{ICON["coin"]}</div><div><h4>Spending caps</h4><p>Limits on AI usage and data credits, set in plain settings.</p></div></div>
      <div class="trust-item"><div class="trust-icon">{ICON["shield"]}</div><div><h4>Never deletes</h4><p>Agents only add or update their own fields, and back up every record before changing it.</p></div></div>
      <div class="trust-item"><div class="trust-icon">{ICON["key"]}</div><div><h4>You own it</h4><p>It runs in your accounts with your keys. We delete our copies at handover.</p></div></div>
      <div class="trust-item"><div class="trust-icon">{ICON["filetext"]}</div><div><h4>Full paper trail</h4><p>Every run keeps a log, the results, and a backup.</p></div></div>
      <div class="trust-item"><div class="trust-icon">{ICON["user"]}</div><div><h4>People decide</h4><p>Agents draft, flag, and score. Your team sends emails, pays invoices, and makes hiring decisions.</p></div></div>
    </div>
  </div>
</section>

<!-- Process timeline -->
<section class="section section-white">
  <div class="inner">
    <div class="two-col">
      <div>
        <span class="tag">The process</span>
        <h2>Live in about two weeks</h2>
        <p class="sub">Fixed price, fixed scope. You see a real result on 20 records before you commit to the full run.</p>
        <div class="timeline">
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">30 min — Free</div><h3>Free call and live demo</h3><p>See a live demo on sample data. Pick the task that hurts most.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">1 to 2 days</div><h3>Proposal</h3><p>Fixed price, scope, and timeline. 50% to start.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">1 hour</div><h3>Discovery interview</h3><p>We interview the people who do the task. Their answers become the agent's settings.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">3 to 5 days</div><h3>Connect and pilot</h3><p>You create access keys. We connect and run 20 records. Your team checks the results.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">1 day</div><h3>Measure and hand over</h3><p>We report the real time saved and cost per record, give 30-minute training. You pay the other 50%.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">Monthly</div><h3>Care plan</h3><p>Monitoring, fixes when tools change, tuning, and a monthly results email.</p></div>
        </div>
      </div>
      <!-- ROI teaser -->
      <div>
        <span class="tag">Estimate your return</span>
        <h2>See your ROI before you commit.</h2>
        <div class="roi-teaser" id="roi-teaser">
          <p style="color:rgba(255,255,255,.65);margin-bottom:0;">Based on a 3-person team running a Standard agent. Adjust the numbers for your situation.</p>
          <div class="roi-stats">
            <div class="roi-stat">
              <div class="rval"><span class="roi-count" data-target="34" data-suffix=" hrs">0</span></div>
              <div class="rlabel">Hours saved / month</div>
            </div>
            <div class="roi-stat">
              <div class="rval"><span class="roi-count" data-target="30600" data-prefix="$" data-suffix="" data-format="currency">0</span></div>
              <div class="rlabel">Value saved / year</div>
            </div>
            <div class="roi-stat">
              <div class="rval"><span class="roi-count" data-target="6" data-suffix=" weeks">0</span></div>
              <div class="rlabel">Payback period</div>
            </div>
          </div>
          <p class="roi-teaser-note">Typical estimate. Your pilot measures the real number.</p>
          <a href="roi.html" class="btn btn-grad">Calculate yours →</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Pricing teaser -->
<section class="section section-light" style="text-align:center;">
  <div class="inner">
    <span class="tag">Pricing</span>
    <h2>Fixed price, fixed scope.</h2>
    <p class="sub" style="margin:0 auto 2rem;">You see a measured result on 20 real records before you commit to the full run. Three tiers — Starter, Standard, and Advanced — based on how many tools the agent touches.</p>
    <a href="pricing.html" class="btn btn-grad">See pricing →</a>
  </div>
</section>

<script>
(function(){
  var counts = document.querySelectorAll('.roi-count');
  var fired = false;
  function animateCounts(){
    if(fired) return;
    fired = true;
    counts.forEach(function(el){
      var target = +el.dataset.target;
      var prefix = el.dataset.prefix || '';
      var suffix = el.dataset.suffix || '';
      var isCurrency = el.dataset.format === 'currency';
      var duration = 1400;
      var start = performance.now();
      function step(now){
        var t = Math.min((now - start) / duration, 1);
        var ease = 1 - Math.pow(1 - t, 3);
        var val = Math.round(target * ease);
        el.textContent = prefix + (isCurrency ? val.toLocaleString() : val) + suffix;
        if(t < 1) requestAnimationFrame(step);
        else el.textContent = prefix + (isCurrency ? target.toLocaleString() : target) + suffix;
      }
      requestAnimationFrame(step);
    });
  }
  var teaser = document.getElementById('roi-teaser');
  if('IntersectionObserver' in window){
    var obs = new IntersectionObserver(function(entries){
      if(entries[0].isIntersecting){ animateCounts(); obs.disconnect(); }
    }, {threshold: 0.3});
    obs.observe(teaser);
  } else {
    animateCounts();
  }
})();
</script>
"""

# ─────────────────────────────────────────────────────────────────────────────
# AGENTS
# ─────────────────────────────────────────────────────────────────────────────
AGENTS = [
  {"name":"Signal Prospector","area":"Sales","tier":"Advanced","status":"ready","setup":"from $6,000","care":"$750/mo","demo":"signal-prospector-dashboard.html",
   "job":"Finds companies showing buying signals in the news — funding, acquisitions, new leaders, expansion — explains why now, finds the right people to contact, and saves it all to your CRM.",
   "connects":["HubSpot","Salesforce","Apollo","AI web search"],
   "you_get":"A score, tier (Hot/Warm/Cold), reasons and source links on every company. Verified contacts. A rep dashboard with talk tracks.",
   "safety":"Every signal links to an article the AI really found. Never touches accounts that already belong to a rep. Credit cap on email reveals."},
  {"name":"Inbound Lead Researcher","area":"Sales","tier":"Standard","status":"available","setup":"from $3,500","care":"$450/mo",
   "job":"Researches every new form lead within minutes, scores fit against your ideal customer, suggests an owner, and drafts a first reply.",
   "connects":["HubSpot","Salesforce","AI web search"],
   "you_get":"A fit score, a research note, and a draft reply on each lead.",
   "safety":"Drafts only. A person sends every email."},
  {"name":"CRM Hygiene","area":"Sales","tier":"Starter","status":"available","setup":"from $1,500","care":"$250/mo",
   "job":"Finds duplicate companies and contacts, missing fields, stale deals and bad data, then proposes fixes for your team to approve.",
   "connects":["HubSpot","Salesforce"],
   "you_get":"A fix list to approve. Only approved fixes are applied.",
   "safety":"Backup before every change. Nothing applied without approval."},
  {"name":"Deal Follow-up Drafter","area":"Sales","tier":"Standard","status":"available","setup":"from $3,500","care":"$450/mo",
   "job":"Spots stalled deals and drafts a follow-up email from the last messages and CRM notes, so reps never lose track of a deal.",
   "connects":["HubSpot","Salesforce","Gmail","Outlook"],
   "you_get":"Draft emails and tasks waiting for the rep.",
   "safety":"Never sends automatically. A person sends every message."},
  {"name":"Meeting Prep Briefs","area":"Sales","tier":"Starter","status":"available","setup":"from $1,500","care":"$250/mo",
   "job":"Writes a one-page brief before every prospect call: who they are, recent news, CRM history, and suggested questions.",
   "connects":["Google Calendar","Microsoft Calendar","CRM","AI web search"],
   "you_get":"A brief in Slack or email an hour before the meeting.",
   "safety":"Every news item links to its source."},
  {"name":"Renewal Risk Radar","area":"Customer success","tier":"Standard","status":"ready","setup":"from $3,500","care":"$450/mo","demo":"renewal-risk-dashboard.html",
   "job":"Reads support tickets, account notes, and product usage for every customer renewing soon. Flags risk with evidence and a suggested next step.",
   "connects":["HubSpot","Salesforce","Zendesk","Slack","Usage exports"],
   "you_get":"Risk score, level, and reasons on each account. CS dashboard showing dollars at risk. Slack alerts for high-risk renewals.",
   "safety":"Every reason cites a real ticket, note, or usage figure. Hard rules the AI can't override."},
  {"name":"Support Ticket Triage","area":"Customer success","tier":"Starter","status":"available","setup":"from $1,500","care":"$250/mo",
   "job":"Tags topic and urgency on new tickets, routes them to the right team, and drafts a reply as an internal note.",
   "connects":["Zendesk","HubSpot"],
   "you_get":"Tags, priority, and a draft reply on each ticket.",
   "safety":"Agents review every reply before it's sent."},
  {"name":"Customer Onboarding Tracker","area":"Customer success","tier":"Starter","status":"available","setup":"from $1,500","care":"$250/mo",
   "job":"Checks new customers against your onboarding checklist and nudges the account owner when one stalls.",
   "connects":["CRM","Help desk","Slack"],
   "you_get":"A stalled-account list and weekly Slack nudges with the blocker.",
   "safety":"Read-only on customer records."},
  {"name":"Invoice Checker","area":"Back office","tier":"Standard","status":"ready","setup":"from $3,500","care":"$450/mo","demo":"invoice-checker-dashboard.html",
   "job":"Matches every vendor invoice to its purchase order before it's paid. Flags duplicates, price overruns, missing POs, and unapproved vendors with dollars at risk.",
   "connects":["CSV exports","QuickBooks Online","Slack"],
   "you_get":"An exceptions report and AP dashboard. Slack summary before the payment run.",
   "safety":"Read-only. Rules find every exception. AI reviews only fuzzy cases and can't clear anything."},
  {"name":"Resume Screener","area":"Back office","tier":"Standard","status":"available","setup":"from $3,500","care":"$450/mo",
   "job":"Compares applicants to the job's must-haves and summarizes each one with quoted evidence from the resume.",
   "connects":["ATS export","Greenhouse"],
   "you_get":"A shortlist with reasons.",
   "safety":"Never auto-rejects. A person makes every decision. Local hiring-AI rules checked first."},
  {"name":"Weekly KPI Writer","area":"Back office","tier":"Starter","status":"available","setup":"from $1,500","care":"$250/mo",
   "job":"Pulls the week's numbers and writes the story behind them — what moved, why, and what to watch.",
   "connects":["CRM","Spreadsheets","Slack","Email"],
   "you_get":"A Monday summary in Slack or email.",
   "safety":"Numbers are calculated in code. AI writes only the words around them."},
  {"name":"Competitor Watch","area":"Marketing","tier":"Starter","status":"available","setup":"from $1,500","care":"$250/mo",
   "job":"Tracks competitor websites, pricing pages, and news. Summarizes what changed and why it matters.",
   "connects":["AI web search","Competitor URLs","Slack","Email"],
   "you_get":"A weekly brief that reports only what's new.",
   "safety":"A link for every claim."},
  {"name":"RFP and Questionnaire Drafter","area":"Marketing","tier":"Advanced","status":"available","setup":"from $6,000","care":"$750/mo",
   "job":"Drafts answers to RFPs and security questionnaires from your library of past approved answers.",
   "connects":["Answer library (docs or spreadsheet)"],
   "you_get":"A draft document with the source of every answer, ready for review.",
   "safety":"Every answer cites a library entry. A person reviews before sending."},
]

def agent_card(a):
    status_pill = '<span class="pill pill-ready">Ready now</span>' if a["status"]=="ready" else '<span class="pill pill-avail">Available</span>'
    demo_link = f'<a href="demos/{a["demo"]}" class="demo-link">View sample dashboard →</a>' if a.get("demo") else ""
    connects = ", ".join(a["connects"])
    return f"""<div class="agent-card" data-area="{a['area']}" data-tier="{a['tier']}" data-status="{a['status']}">
  <div class="agent-meta">
    <span class="pill pill-area">{a['area']}</span>
    <span class="pill pill-tier">{a['tier']}</span>
    {status_pill}
  </div>
  <h3>{a['name']}</h3>
  <p class="job">{a['job']}</p>
  <p class="agent-connects"><strong>Connects to:</strong> {connects}</p>
  <p class="agent-connects" style="margin-top:.4rem;"><strong>You get:</strong> {a['you_get']}</p>
  <p class="agent-connects" style="margin-top:.4rem;"><strong>Safety:</strong> {a['safety']}</p>
  {demo_link}
</div>"""

AGENTS_BODY = """
<div class="page-banner">
  <div class="page-banner-inner">
    <h1>The Agent Catalog</h1>
    <p>13 agents across sales, customer success, back office, and marketing. Three are ready now with live demos.</p>
  </div>
</div>
<section class="section section-light">
  <div class="inner">
    <div class="filter-bar">
      <input type="text" id="agent-search" placeholder="Search agents…" oninput="filterAgents()"/>
      <button class="filter-btn active" data-area="all" onclick="setArea(this,'all')">All</button>
      <button class="filter-btn" data-area="Sales" onclick="setArea(this,'Sales')">Sales</button>
      <button class="filter-btn" data-area="Customer success" onclick="setArea(this,'Customer success')">Customer success</button>
      <button class="filter-btn" data-area="Back office" onclick="setArea(this,'Back office')">Back office</button>
      <button class="filter-btn" data-area="Marketing" onclick="setArea(this,'Marketing')">Marketing</button>
      <span style="width:1px;background:var(--border);align-self:stretch;margin:0 .2rem;"></span>
      <button class="filter-btn active" data-tier="all" onclick="setTier(this,'all')">All tiers</button>
      <button class="filter-btn" data-tier="Starter" onclick="setTier(this,'Starter')">Starter</button>
      <button class="filter-btn" data-tier="Standard" onclick="setTier(this,'Standard')">Standard</button>
      <button class="filter-btn" data-tier="Advanced" onclick="setTier(this,'Advanced')">Advanced</button>
    </div>
    <div class="agent-grid" id="agent-grid">
""" + "\n".join(agent_card(a) for a in AGENTS) + """
    </div>
    <p id="no-results" style="display:none;color:var(--muted);margin-top:1.5rem;">No agents match your filter.</p>
    <div style="background:var(--dark);border-radius:16px;padding:2rem 2.5rem;display:flex;gap:1.5rem;align-items:flex-start;margin-top:2rem;">
      <div class="icon" style="flex-shrink:0;">{ICON["flask"]}</div>
      <div>
        <h3 style="color:#fff;margin-bottom:.4rem;">Don't see your task on the list?</h3>
        <p style="color:rgba(255,255,255,.65);font-size:.9rem;margin-bottom:1.25rem;">We build fully custom agents for any repeatable process your team runs weekly. If a person currently does it by reading, judging, or typing — an agent can likely do it. Same two-week process, same fixed price, same safety rules.</p>
        <a href="contact.html" class="btn btn-grad">Tell us what you need →</a>
      </div>
    </div>
  </div>
</section>

<!-- Quiz -->
<section class="section section-white">
  <div class="inner" style="max-width:680px;">
    <span class="tag">Not sure where to start?</span>
    <h2>Which agent fits you?</h2>
    <p class="sub">Three questions. One or two recommendations.</p>
    <div class="quiz-wrap">
      <div class="quiz-q">1. How big is your team?</div>
      <div class="quiz-opts">
        <label class="quiz-opt"><input type="radio" name="q1" value="small"/> 1 to 15 people</label>
        <label class="quiz-opt"><input type="radio" name="q1" value="mid"/> 16 to 60 people</label>
        <label class="quiz-opt"><input type="radio" name="q1" value="large"/> 61 to 200 people</label>
      </div>
      <div class="quiz-q">2. Which tools do you use?</div>
      <div class="quiz-opts">
        <label class="quiz-opt"><input type="radio" name="q2" value="crm"/> HubSpot or Salesforce</label>
        <label class="quiz-opt"><input type="radio" name="q2" value="desk"/> Zendesk or a help desk</label>
        <label class="quiz-opt"><input type="radio" name="q2" value="finance"/> QuickBooks or accounting CSV exports</label>
        <label class="quiz-opt"><input type="radio" name="q2" value="other"/> Spreadsheets / other</label>
      </div>
      <div class="quiz-q">3. What's your biggest time sink?</div>
      <div class="quiz-opts">
        <label class="quiz-opt"><input type="radio" name="q3" value="prospect"/> Finding and researching prospects</label>
        <label class="quiz-opt"><input type="radio" name="q3" value="churn"/> Spotting customers at risk</label>
        <label class="quiz-opt"><input type="radio" name="q3" value="invoice"/> Checking invoices before payment</label>
        <label class="quiz-opt"><input type="radio" name="q3" value="data"/> Keeping data clean or writing reports</label>
      </div>
      <button class="btn btn-grad" onclick="runQuiz()" style="margin-bottom:1rem;">Get a recommendation</button>
      <div class="quiz-result" id="quiz-result"></div>
    </div>
  </div>
</section>

<script>
var activeArea='all';
var activeTier='all';
function setArea(btn,area){
  document.querySelectorAll('.filter-btn[data-area]').forEach(function(b){b.classList.remove('active');});
  btn.classList.add('active');
  activeArea=area;
  filterAgents();
}
function setTier(btn,tier){
  document.querySelectorAll('.filter-btn[data-tier]').forEach(function(b){b.classList.remove('active');});
  btn.classList.add('active');
  activeTier=tier;
  filterAgents();
}
function filterAgents(){
  var q=document.getElementById('agent-search').value.toLowerCase();
  var cards=document.querySelectorAll('.agent-card');
  var shown=0;
  cards.forEach(function(c){
    var areaMatch=activeArea==='all'||c.dataset.area===activeArea;
    var tierMatch=activeTier==='all'||c.dataset.tier===activeTier;
    var textMatch=!q||c.textContent.toLowerCase().includes(q);
    c.style.display=(areaMatch&&tierMatch&&textMatch)?'':'none';
    if(areaMatch&&tierMatch&&textMatch)shown++;
  });
  document.getElementById('no-results').style.display=shown===0?'block':'none';
}
function runQuiz(){
  var q3=document.querySelector('input[name="q3"]:checked');
  if(!q3){alert('Please answer all three questions.');return;}
  var recs={
    'prospect':'<strong>Signal Prospector</strong> — finds companies showing buying signals and saves the right contacts to your CRM. Advanced tier, from $6,000.',
    'churn':'<strong>Renewal Risk Radar</strong> — flags accounts at risk before renewal with evidence from tickets, notes, and usage. Standard tier, from $3,500.',
    'invoice':'<strong>Invoice Checker</strong> — matches every invoice to its PO and flags problems with dollars at risk before you pay. Standard tier, from $3,500.',
    'data':'<strong>CRM Hygiene</strong> or <strong>Weekly KPI Writer</strong> — clean your data or get a Monday summary of what moved and why. Starter tier, from $1,500.'
  };
  var el=document.getElementById('quiz-result');
  el.innerHTML='We suggest: '+recs[q3.value]+'<br/><br/><a href="contact.html" style="color:var(--blue);font-weight:700;">Book a free call to confirm →</a>';
  el.classList.add('show');
}
</script>
"""

# ─────────────────────────────────────────────────────────────────────────────
# HOW IT WORKS
# ─────────────────────────────────────────────────────────────────────────────
HOW_BODY = """
<div class="page-banner">
  <div class="page-banner-inner">
    <h1>How It Works</h1>
    <p>Two weeks from call to running agent. Here's what happens at each step — and why we do it that way.</p>
  </div>
</div>

<!-- Three options comparison -->
<section class="section section-white">
  <div class="inner">
    <span class="tag">Why not just hire someone?</span>
    <h2>Three ways to get AI doing real work. One that actually delivers.</h2>
    <p class="sub">Most companies try one of three paths. Two of them stall.</p>
    <div class="compare-wrap" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.25rem;margin-top:2rem;">
      <div class="card" style="border-top:3px solid var(--border);">
        <h3 style="color:var(--muted);">Hire an AI person</h3>
        <p style="color:var(--muted);font-size:.88rem;">$120K+ salary. 3–6 months to ramp. Spends half their time learning new tools. If they leave, the agent breaks. You're funding their education.</p>
      </div>
      <div class="card" style="border-top:3px solid var(--border);">
        <h3 style="color:var(--muted);">Buy an off-the-shelf tool</h3>
        <p style="color:var(--muted);font-size:.88rem;">Works for the demo use case, not yours. Doesn't connect to your specific CRM setup. Requires someone to run it. Subscription stacks up fast.</p>
      </div>
      <div class="card" style="border-top:3px solid var(--blue);">
        <h3>Work with {PlAIceholder}</h3>
        <p style="font-size:.88rem;">Fixed price. Two weeks. Built around exactly how your team works. Runs in your own tools. We stay on it so it keeps working when things change.</p>
      </div>
    </div>
  </div>
</section>

<!-- Detailed process -->
<section class="section section-light">
  <div class="inner">
    <div class="two-col">
      <div>
        <span class="tag">The process</span>
        <h2>Every step is fixed price, no surprises.</h2>
        <div class="timeline">
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">30 min — Free</div><h3>Live demo call</h3><p>We show you a working agent on sample data. You tell us the task that costs your team the most time. No pitch deck, no commitment. If we can't help, we'll say so.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">1–2 days</div><h3>Fixed-price proposal</h3><p>We send a scope document: exactly what the agent will do, what it won't do, what it connects to, the price, and the timeline. 50% to start, 50% at handover.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">1 hour</div><h3>Discovery interview</h3><p>We interview the person who currently does the task. Their answers become the agent's settings: which signals matter, what a good result looks like, what edge cases to handle, what to skip. This hour is what makes it yours, not generic.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">3–5 days</div><h3>Connect and pilot</h3><p>You create API keys in your existing tools; we do the rest. We run the agent on 20 real records. Your team reviews the top results and tells us what to tune before the full run.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">1 day</div><h3>Measure and hand over</h3><p>We time the old way against the new way on the same 20 records, write up the real numbers, and run a 30-minute training. You pay the remaining 50%. The agent is yours.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">Ongoing</div><h3>Care plan</h3><p>We monitor the agent, fix it when a connected tool changes its API, apply tuning hours each month, and send a monthly results email. You're not maintaining it alone.</p></div>
        </div>
      </div>
      <div>
        <span class="tag">What we need from you</span>
        <h2>Three things — that's it.</h2>
        <div class="cards" style="grid-template-columns:1fr;">
          <div class="card"><div class="icon">{ICON["key"]}</div><h3>An admin who can create access keys</h3><p>We connect through read-only or scoped API keys in your existing tools. You control the keys and can revoke them at any time. We never ask for more access than the specific task requires.</p></div>
          <div class="card"><div class="icon">{ICON["clock"]}</div><h3>One hour from the person who does the task</h3><p>This is the most important hour. We learn what "good" looks like, what signals matter, what exceptions exist. The discovery interview is what separates an agent that fits your business from one that fits a demo.</p></div>
          <div class="card"><div class="icon">{ICON["chart"]}</div><h3>Clean-enough data</h3><p>Your data doesn't need to be perfect. If it needs cleanup first, we quote that separately — or start with the CRM Hygiene agent to get it in shape before the main build.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Safety -->
<section class="section section-dark">
  <div class="inner">
    <span class="tag">Safety rules</span>
    <h2>Not optional. Not configurable. Built in.</h2>
    <p class="sub">Every agent ships with the same rules. These protect your data, your budget, and your team's trust in the output.</p>
    <div class="trust-grid">
      <div class="trust-item"><div class="trust-icon">{ICON["flask"]}</div><div><h4>Pilot first, always</h4><p>Every agent proves itself on 20 records before touching your full list. If the pilot doesn't meet your bar, we fix it before the full run.</p></div></div>
      <div class="trust-item"><div class="trust-icon">{ICON["link"]}</div><div><h4>No made-up facts</h4><p>Every AI finding requires a source link it actually retrieved. Findings without evidence are discarded before your team sees them — automatically, not by review.</p></div></div>
      <div class="trust-item"><div class="trust-icon">{ICON["coin"]}</div><div><h4>Hard spending caps</h4><p>AI usage costs and data-credit budgets are set in plain settings and enforced before every run. The agent can't overspend.</p></div></div>
      <div class="trust-item"><div class="trust-icon">{ICON["shield"]}</div><div><h4>Never deletes, always backs up</h4><p>Agents only write to their own designated fields. Every record is backed up before any change is made.</p></div></div>
      <div class="trust-item"><div class="trust-icon">{ICON["user"]}</div><div><h4>People make the final call</h4><p>Agents draft, score, and flag. Your team sends the email, pays the invoice, and makes the hire. No fully automated irreversible actions.</p></div></div>
      <div class="trust-item"><div class="trust-icon">{ICON["filetext"]}</div><div><h4>Full audit trail</h4><p>Every run keeps a log: inputs, AI reasoning, rule outcomes, final results. You can replay or audit any run at any time.</p></div></div>
      <div class="trust-item"><div class="trust-icon">{ICON["key"]}</div><div><h4>Your data stays yours</h4><p>The agent runs in your accounts with your keys. We delete our working copies at handover. You own the agent and everything it produces.</p></div></div>
      <div class="trust-item"><div class="trust-icon">{ICON["clipboard"]}</div><div><h4>Dry run before every change</h4><p>Anything that modifies your data runs in read-only mode first. Your team sees the proposed changes before a single record is updated.</p></div></div>
    </div>
  </div>
</section>

<section class="section section-light" style="text-align:center;">
  <div class="inner">
    <h2>See it working before you decide.</h2>
    <p class="sub" style="margin:0 auto 2rem;">The demo call is 30 minutes, free, and runs on sample data. No pitch deck. If we can't help, we'll tell you that too.</p>
    <a href="contact.html" class="btn btn-grad">Book a free call →</a>
  </div>
</section>
"""

# ─────────────────────────────────────────────────────────────────────────────
# PRICING
# ─────────────────────────────────────────────────────────────────────────────
PRICING_BODY = """
<div class="page-banner">
  <div class="page-banner-inner">
    <h1>Simple, Transparent Pricing</h1>
    <p>Fixed price, fixed scope. 50% at kickoff, 50% at handover. Care plans billed monthly and cancelable with 30 days' notice.</p>
  </div>
</div>

<section class="section section-light">
  <div class="inner">
    <div class="plans">
      <div class="plan">
        <span class="founding-badge">Founding-client pricing available</span>
        <div class="pname">Starter</div>
        <div class="price-range">$1,500 – $2,500</div>
        <div class="per">one-time setup · founding price $1,500</div>
        <ul class="feats">
          <li>One tool in, one tool out, no outside data</li>
          <li>Care plan: $250/month</li>
          <li>1 tuning hour/month</li>
          <li>Monitoring + monthly results email</li>
          <li>Fixes when a connected tool changes</li>
          <li>2-business-day response</li>
        </ul>
        <a href="contact.html" class="pbtn pbtn-out">Get started</a>
      </div>
      <div class="plan hot">
        <div class="pbadge">Most popular</div>
        <span class="founding-badge">Founding-client pricing available</span>
        <div class="pname">Standard</div>
        <div class="price-range">$3,500 – $5,000</div>
        <div class="per">one-time setup · founding price $2,500</div>
        <ul class="feats">
          <li>2 to 3 tools, AI research or scoring, a dashboard</li>
          <li>Care plan: $450/month</li>
          <li>2 tuning hours/month</li>
          <li>Monitoring + monthly results email</li>
          <li>Fixes when a connected tool changes</li>
          <li>Quarterly tuning call</li>
          <li>2-business-day response</li>
        </ul>
        <a href="contact.html" class="pbtn">Get started</a>
      </div>
      <div class="plan">
        <span class="founding-badge">Founding-client pricing available</span>
        <div class="pname">Advanced</div>
        <div class="price-range">$6,000 – $7,500</div>
        <div class="per">one-time setup · founding price $4,500</div>
        <ul class="feats">
          <li>Several tools, outside data, batch research</li>
          <li>Spending caps and rep training included</li>
          <li>Care plan: $750 – $900/month</li>
          <li>3 tuning hours/month</li>
          <li>Monitoring + monthly results email</li>
          <li>Fixes when a connected tool changes</li>
          <li>Quarterly tuning call</li>
          <li>2-business-day response</li>
        </ul>
        <a href="contact.html" class="pbtn pbtn-out">Get started</a>
      </div>
    </div>
  </div>
</section>

<!-- Care plan table -->
<section class="section section-white">
  <div class="inner">
    <span class="tag">What every care plan includes</span>
    <h2>Care plan details</h2>
    <div class="table-scroll">
    <table class="care-table">
      <thead><tr><th></th><th>Starter $250</th><th>Standard $450</th><th>Advanced $750+</th></tr></thead>
      <tbody>
        <tr><td>Monitoring and monthly results email</td><td class="yes">Yes</td><td class="yes">Yes</td><td class="yes">Yes</td></tr>
        <tr><td>Fixes when a connected tool changes</td><td class="yes">Yes</td><td class="yes">Yes</td><td class="yes">Yes</td></tr>
        <tr><td>Prompt and scoring tuning</td><td>1 hr/mo</td><td>2 hr/mo</td><td>3 hr/mo</td></tr>
        <tr><td>Response time</td><td>2 business days</td><td>2 business days</td><td>2 business days</td></tr>
        <tr><td>Quarterly tuning call</td><td class="no">No</td><td class="yes">Yes</td><td class="yes">Yes</td></tr>
      </tbody>
    </table>
    </div>
  </div>
</section>

<!-- Pricing rules -->
<section class="section section-light">
  <div class="inner">
    <span class="tag">Pricing rules</span>
    <h2>A few things worth knowing</h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1.25rem;margin-bottom:2.5rem;">
      <div class="card"><h3>Founding-client pricing</h3><p>Available for the first 5 clients in exchange for a written testimonial, a published result, and a 6-month care plan.</p></div>
      <div class="card"><h3>Second agent discount</h3><p>25% off setup for a second agent at the same company. The connections are already in place.</p></div>
      <div class="card"><h3>Annual care plan</h3><p>Pay for 10 months and get 12. Equivalent to 2 months free.</p></div>
      <div class="card"><h3>Usage at cost</h3><p>You pay AI model usage and data credits (e.g. Apollo) directly to those providers. Typical AI usage is a few cents per record. We estimate them up front and measure the real number in the pilot.</p></div>
      <div class="card"><h3>Extra work</h3><p>$125/hour for work outside the care plan, or a new build fee for a brand-new kind of agent.</p></div>
      <div class="card"><h3>Payment</h3><p>50% at kickoff, 50% at handover. Care plans billed monthly and cancelable with 30 days' notice.</p></div>
    </div>

    <!-- Market comparison -->
    <span class="tag">How we compare</span>
    <h2>Market context</h2>
    <p class="sub">Optional context if you're comparing options.</p>
    <div style="overflow-x:auto;">
      <table class="compare-table">
        <thead><tr><th>Option</th><th>Typical cost</th><th>Source</th></tr></thead>
        <tbody>
          <tr><td>Hire an automation engineer</td><td>$90,000 – $140,000/yr salary</td><td><a href="https://evolvaiagents.com/blog/how-much-does-an-ai-automation-agency-cost-in-2026-real-pricing-breakdown/" target="_blank" rel="noopener">Evolv</a></td></tr>
          <tr><td>AI automation agency, single workflow</td><td>$1,500 – $7,500 build + $500 – $1,500/mo</td><td><a href="https://taskip.net/ai-automation-agency-pricing/" target="_blank" rel="noopener">Taskip</a></td></tr>
          <tr><td>Boutique single-agent pilot</td><td>$2,500 – $10,000</td><td><a href="https://cloudmotiv.ai/blog/agentic-ai-consulting-packages-small-business" target="_blank" rel="noopener">Cloudmotiv</a></td></tr>
          <tr><td>GTM / Clay outbound agencies</td><td>$2,500 – $10,000+/mo</td><td><a href="https://www.salesforge.ai/blog/clay-agencies" target="_blank" rel="noopener">Salesforge</a></td></tr>
          <tr><td class="highlight">{PlAIceholder}</td><td class="highlight">from $1,500 + $250/mo</td><td></td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- ROI CTA -->
<section class="section section-dark" style="text-align:center;">
  <div class="inner">
    <span class="tag">Estimate your return</span>
    <h2>See what this costs you today.</h2>
    <p class="sub">Pick your agent, adjust two numbers, and get hours saved, dollar value, and payback period — in under a minute.</p>
    <a href="roi.html" class="btn btn-grad">Open the ROI calculator →</a>
  </div>
</section>

<!-- FAQ -->
<section class="section section-light">
  <div class="inner">
    <span class="tag">FAQ</span>
    <h2>Common questions</h2>
    <div class="faq">
      <details><summary>What exactly is an "AI agent"?</summary><p>A program that does a multi-step task a person used to do — research, reading, judging, and writing up — inside your tools, with rules that check its work before anyone sees it.</p></details>
      <details><summary>Do we need to be technical?</summary><p>No. You need an admin who can create access keys and one hour from the people who currently do the task.</p></details>
      <details><summary>Which AI do you use?</summary><p>We build with the leading models — Claude, GPT-4o, Gemini, and others — and pick whichever fits your stack and budget best. The model runs through your own account so you see and control the usage bill directly.</p></details>
      <details><summary>What does it cost to run?</summary><p>You pay AI usage and data credits directly to those providers at cost — typically a few cents per record. We estimate the number up front and measure the real cost per record in your pilot.</p></details>
      <details><summary>Who owns it?</summary><p>You do. The agent runs in your accounts with your keys. We keep the right to reuse our general templates for other clients, but never your data or settings.</p></details>
      <details><summary>What happens to our data?</summary><p>It stays in your systems. We delete any copies and our access at handover.</p></details>
      <details><summary>What if HubSpot or another tool changes?</summary><p>That's what the care plan covers. Without one, fixes are billed at $125/hour.</p></details>
      <details><summary>Can the AI send emails or pay invoices on its own?</summary><p>No. Agents draft, score, and flag. People approve.</p></details>
      <details><summary>What if the pilot doesn't work?</summary><p>You see the result after 20 records, before the full run. If the result isn't useful, we tune it or stop.</p></details>
      <details><summary>Can we cancel the care plan?</summary><p>Yes, with 30 days' notice.</p></details>
      <details><summary>Our CRM is messy. Is that a problem?</summary><p>It can be. We quote cleanup separately, or you can start with the CRM Hygiene agent.</p></details>
    </div>
  </div>
</section>

"""

# ─────────────────────────────────────────────────────────────────────────────
# CASE STUDY
# ─────────────────────────────────────────────────────────────────────────────
CASE_BODY = """
<div class="page-banner">
  <div class="page-banner-inner">
    <h1>Become a Founding Client</h1>
    <p>Get a discounted build in exchange for letting us document your results as a public case study.</p>
  </div>
</div>

<section class="section section-white">
  <div class="inner">
    <div class="cs-grid">
      <div>
        <span class="tag">The deal</span>
        <h2>Real results are worth more than any ad.</h2>
        <p style="color:var(--muted);margin-bottom:1.25rem;">We're early. We don't have a wall of logos yet, and we're not going to make them up. Instead, we're offering a small number of founding client spots to companies who are willing to let us measure and publish the real numbers once their agent is running.</p>
        <p style="color:var(--muted);margin-bottom:1.25rem;">In exchange, you get a meaningfully discounted build — and we get the proof we can show the next client.</p>
        <p style="color:var(--muted);">You stay in control. We only publish what you approve in writing. If the numbers aren't what we hoped, they don't go public.</p>

        <span class="tag" style="margin-top:2rem;display:block;">What we publish</span>
        <h2>Honest, specific, verifiable.</h2>
        <div class="timeline" style="margin-top:1rem;">
          <div class="tl-item"><div class="tl-dot"></div><h3>Time saved per week</h3><p>Measured before and after. Hours are hours — no vague "efficiency gains."</p></div>
          <div class="tl-item"><div class="tl-dot"></div><h3>Dollar value of that time</h3><p>Based on the hourly cost your team actually carries, not an inflated benchmark.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><h3>How the agent works</h3><p>What it pulls, what it decides, what it writes back — described plainly so readers can judge for themselves.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><h3>What didn't work</h3><p>Anything we had to change during the pilot gets documented too. No airbrushing.</p></div>
        </div>
      </div>
      <div>
        <span class="tag">What you get</span>
        <h2>Founding client terms</h2>
        <div class="cs-stats" style="margin-bottom:1.5rem;">
          <div class="cs-stat"><span class="n">20%</span><span class="l">off the setup fee</span></div>
          <div class="cs-stat"><span class="n">3 mo</span><span class="l">care plan included free</span></div>
          <div class="cs-stat"><span class="n">1st</span><span class="l">priority in the build queue</span></div>
          <div class="cs-stat"><span class="n">Your</span><span class="l">name on the case study (or anonymized)</span></div>
        </div>

        <div class="card" style="margin-top:.5rem;">
          <div class="icon">{ICON["shield"]}</div>
          <h3>You stay in control</h3>
          <p>We measure everything during the pilot. You review the numbers and the write-up before anything goes public. If you don't approve it, it doesn't publish — and your discount stands either way.</p>
        </div>

        <div class="card" style="margin-top:1rem;">
          <div class="icon">{ICON["target"]}</div>
          <h3>What we're looking for</h3>
          <p>A repetitive task your team runs at least weekly, in a tool we can connect to. Sales, CS, finance, HR, or reporting all qualify. We'll tell you in the first call whether your situation is a good fit.</p>
        </div>

        <div style="margin-top:1.5rem;">
          <a href="contact.html" class="btn btn-grad">Apply for a founding client spot →</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-light" style="text-align:center;">
  <div class="inner">
    <span class="tag">Spots available</span>
    <h2>We're keeping this small on purpose.</h2>
    <p class="sub" style="margin:0 auto 2rem;">Founding client builds get more of our time — better discovery, faster iterations, and direct access to us throughout the pilot. We can only take a few at a time.</p>
    <a href="contact.html" class="btn btn-grad">Book a free 30-minute call →</a>
  </div>
</section>
"""

# ─────────────────────────────────────────────────────────────────────────────
# CONTACT
# ─────────────────────────────────────────────────────────────────────────────
TOOLS_LIST = ["HubSpot","Salesforce","Zendesk","QuickBooks","Apollo","Slack","Linear","Notion","Airtable","Other"]
AREAS_LIST = ["Sales & prospecting","Customer success","Finance & ops","HR & recruiting","Reporting & analytics"]
AGENT_LIST = ["Signal Prospector","Inbound Lead Researcher","CRM Hygiene","Deal Follow-up Drafter",
              "Meeting Prep Briefs","Renewal Risk Radar","Support Ticket Triage","Customer Onboarding Tracker",
              "Invoice Checker","Resume Screener","Weekly KPI Writer","Competitor Watch",
              "RFP and Questionnaire Drafter","Not sure yet"]

tools_chips = "\n".join(f'<label class="chip-check"><input type="checkbox" name="tools" value="{t}"/><span>{t}</span></label>' for t in TOOLS_LIST)
areas_chips = "\n".join(f'<label class="chip-check"><input type="checkbox" name="areas" value="{a}"/><span>{a}</span></label>' for a in AREAS_LIST)
agent_opts  = "\n".join(f'<option>{a}</option>' for a in AGENT_LIST)

CONTACT_BODY = f"""
<div class="page-banner">
  <div class="page-banner-inner">
    <h1>Let's Talk</h1>
    <p>Book a free 30-minute call. We'll show you a live demo and pick the task that makes the most sense to start with.</p>
  </div>
</div>
<section class="section section-light">
  <div class="inner">
    <div class="contact-wrap">
      <div class="ci">
        <span class="tag">Get in touch</span>
        <h2>Free call,<br>no commitment</h2>
        <p>In 30 minutes we'll walk you through a live demo on sample data, talk through your biggest time sink, and give you a straight answer on whether an agent can help.</p>
        <div class="ci-chip"><span class="ic">{ICON["clock"]}</span><span><a href="[Booking Link]" style="color:var(--blue);font-weight:600;">Schedule a 30-min call</a></span></div>
        <div class="ci-chip"><span class="ic">{ICON["filetext"]}</span><span>[Contact Email]</span></div>
        <a href="https://www.linkedin.com/company/plaiceholder-io" target="_blank" rel="noopener" class="contact-linkedin">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="li-grad2" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#1A6EF5"/>
                <stop offset="50%" stop-color="#3EC9C9"/>
                <stop offset="100%" stop-color="#2ECC71"/>
              </linearGradient>
            </defs>
            <rect width="24" height="24" rx="5" fill="url(#li-grad2)"/>
            <path d="M7 10h2v7H7v-7zm1-3a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm4 3h1.9v1h.1c.3-.5 1-1.1 2-1.1 2.1 0 2.5 1.4 2.5 3.2V17h-2v-3.5c0-.8 0-1.9-1.2-1.9s-1.3.9-1.3 1.8V17H12v-7z" fill="#fff"/>
          </svg>
          Follow on LinkedIn
        </a>
      </div>
      <form class="contact-form" onsubmit="handleSubmit(event)">
        <div class="frow">
          <input type="text" name="name" placeholder="Your name" required/>
          <input type="email" name="email" placeholder="Work email" required/>
        </div>
        <div class="frow">
          <input type="text" name="company" placeholder="Company name" required/>
          <select name="role">
            <option value="" disabled selected>Your role</option>
            <option>Founder / CEO</option>
            <option>Sales</option>
            <option>Customer success</option>
            <option>Operations</option>
            <option>Finance</option>
            <option>HR / Recruiting</option>
            <option>Marketing</option>
            <option>Other</option>
          </select>
        </div>
        <fieldset>
          <legend>Where would an agent help most? (select all that apply)</legend>
          <div class="chip-group">
            {areas_chips}
          </div>
        </fieldset>
        <fieldset>
          <legend>Tools your team uses (select all that apply)</legend>
          <div class="chip-group">
            {tools_chips}
          </div>
        </fieldset>
        <select name="agent">
          <option value="" disabled selected>Which agent caught your eye?</option>
          {agent_opts}
        </select>
        <textarea name="message" placeholder="Anything else we should know? (optional)"></textarea>
        <!-- honeypot -->
        <input type="text" name="_gotcha" style="display:none;" tabindex="-1" autocomplete="off"/>
        <button type="submit" class="sbtn">Send →</button>
        <div class="form-success" id="form-success">Thanks! We'll be in touch within one business day.</div>
      </form>
    </div>
  </div>
</section>
<script>
function handleSubmit(e){{
  e.preventDefault();
  var hp=e.target.querySelector('input[name="_gotcha"]');
  if(hp&&hp.value)return;
  var btn=e.target.querySelector('.sbtn');
  btn.textContent='Sent ✓';btn.style.opacity='.6';btn.disabled=true;
  document.getElementById('form-success').style.display='block';
}}
</script>
"""

# ─────────────────────────────────────────────────────────────────────────────
# ABOUT
# ─────────────────────────────────────────────────────────────────────────────
ABOUT_BODY = """
<div class="page-banner">
  <div class="page-banner-inner">
    <h1>About {PlAIceholder}</h1>
    <p>We built this because companies kept paying for AI they couldn't use.</p>
  </div>
</div>

<section class="section section-white">
  <div class="inner">
    <div class="two-col">
      <div>
        <span class="tag">The problem we solve</span>
        <h2>You don't need an AI hire. You need AI that already works.</h2>
        <p style="color:var(--muted);margin-bottom:1.25rem;">Most companies sit on AI tools they're not using. Not because AI isn't useful — because using it well takes real experience. Someone has to understand the models, the APIs, the edge cases, and what actually fails in production.</p>
        <p style="color:var(--muted);margin-bottom:1.25rem;">Hiring a full-time AI person costs $120K+ and months of ramp time. And that person is still figuring it out on your dime. What you get is expensive experimentation dressed up as a job title.</p>
        <p style="color:var(--muted);">{PlAIceholder} is the alternative. We've already done the learning. We show up with working agents, not prototypes — and we're done in two weeks, not six months.</p>
      </div>
      <div>
        <span class="tag">What we bring</span>
        <h2>Years of experience, already baked in.</h2>
        <div class="cards" style="grid-template-columns:1fr;">
          <div class="card">
            <div class="icon">{ICON["flask"]}</div>
            <h3>Curated agents, not experiments</h3>
            <p>Our catalog agents have been designed, tested, and refined. The scoring rules, safety checks, and integration patterns are worked out. You're buying the result of that work, not the process of figuring it out.</p>
          </div>
          <div class="card">
            <div class="icon">{ICON["target"]}</div>
            <h3>Custom builds for tasks not on the list</h3>
            <p>Not every task fits a catalog. We build fully custom agents using the same two-week process — discovery interview, fixed price, pilot on 20 records, measure and hand over.</p>
          </div>
          <div class="card">
            <div class="icon">{ICON["shield"]}</div>
            <h3>We stay on it</h3>
            <p>AI tools and business software change constantly. Our care plan means we fix it when something breaks — without you having to file a ticket or find a contractor.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="inner" style="max-width:720px;margin:0 auto;text-align:center;">
    <span class="tag">Our standard</span>
    <h2>No invented results. No star ratings we made up. No logos without permission.</h2>
    <p style="color:rgba(255,255,255,.65);margin-bottom:2rem;">We don't publish ROI claims until a client approves the real numbers in writing. Sample dashboards are labeled as fictional. This page will grow as clients give us permission to quote them — not before.</p>
    <a href="case-study.html" class="btn btn-grad" style="margin-right:1rem;">Become a founding client →</a>
    <a href="contact.html" class="btn btn-white">Book a free call</a>
  </div>
</section>
"""

# ─────────────────────────────────────────────────────────────────────────────
# BLOG
# ─────────────────────────────────────────────────────────────────────────────
# ── To add a new post, append one dict to POSTS and run python3 build_site.py ──
# ── To add a post: append a dict with slug/title/date/tag/preview/body, then run python3 build_site.py ──
POSTS = [
  # posts go here
]

def post_card(p):
    return f"""<a href="blog/{p['slug']}.html" class="post-card">
  <span class="post-tag">{p['tag']}</span>
  <h3>{p['title']}</h3>
  <p class="post-preview">{p['preview']}</p>
  <span class="post-date">{p['date']}</span>
</a>"""

def post_page(p):
    body_html = f"""
<div class="page-banner">
  <div class="page-banner-inner" style="max-width:760px;">
    <span class="tag">{p['tag']}</span>
    <h1 style="margin-top:.75rem;">{p['title']}</h1>
    <p style="margin-top:.5rem;opacity:.7;">{p['date']}</p>
  </div>
</div>
<section class="section section-white">
  <div class="inner" style="max-width:760px;">
    <div class="post-body">
      {p['body']}
    </div>
    <div style="margin-top:3rem;padding-top:2rem;border-top:1.5px solid var(--border);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;">
      <a href="../blog.html" style="color:var(--muted);font-size:.88rem;text-decoration:none;">← All posts</a>
      <a href="../contact.html" class="btn btn-grad">Book a free call →</a>
    </div>
  </div>
</section>"""
    return page(f"{p['title']} — {{PlAIceholder}}", p['preview'], "blog", body_html)

BLOG_BODY = """
<div class="page-banner">
  <div class="page-banner-inner">
    <h1>Blog</h1>
    <p>How AI agents work, what we've learned building them, and what actually delivers results.</p>
  </div>
</div>
<section class="section section-white">
  <div class="inner">
    <div class="post-grid">
""" + (
    "\n".join(post_card(p) for p in POSTS)
    if POSTS else
    '<p style="color:var(--muted);grid-column:1/-1;">Posts coming soon.</p>'
) + """
    </div>
  </div>
</section>
"""

# ─────────────────────────────────────────────────────────────────────────────
# DEMOS placeholder
# ─────────────────────────────────────────────────────────────────────────────
DEMOS_DIR = os.path.join(base, "demos")
os.makedirs(DEMOS_DIR, exist_ok=True)

def demo_placeholder(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>{title} — Sample</title>
{FAVICON}
  <link rel="stylesheet" href="../style.css"/>
</head>
<body>
{nav("agents")}
<div class="page-banner">
  <div class="page-banner-inner">
    <div class="badge">Sample data. These companies are fictional.</div>
    <h1>{title}</h1>
    <p>{desc}</p>
  </div>
</div>
<section class="section section-light" style="text-align:center;">
  <div class="inner">
    <div class="card" style="max-width:520px;margin:0 auto;padding:3rem;">
      <div class="icon" style="margin:0 auto 1.25rem;">{ICON["chart"]}</div>
      <h2 style="font-size:1.3rem;margin-bottom:.75rem;">Live demo dashboard</h2>
      <p style="color:var(--muted);margin-bottom:1.5rem;">The interactive sample dashboard for this agent will appear here once the demo files are installed. Add <code>agent-kit/samples/</code> to this folder to enable it.</p>
      <a href="contact.html" class="btn btn-grad">Book a call to see a live demo →</a>
    </div>
  </div>
</section>
{FOOTER}
{TRACKER}
</body>
</html>"""

# ─────────────────────────────────────────────────────────────────────────────
# ROI CALCULATOR
# ─────────────────────────────────────────────────────────────────────────────
ROI_BODY = """
<div class="page-banner">
  <div class="page-banner-inner">
    <h1>ROI Calculator</h1>
    <p>Pick an agent, adjust two numbers, and see hours saved, dollar value, and payback period.</p>
  </div>
</div>

<section class="section section-light">
  <div class="inner" style="max-width:720px;">

    <div class="calc-wrap">

      <!-- Step 1: Agent selector -->
      <div class="calc-field" style="margin-bottom:1.5rem;">
        <label style="font-weight:700;font-size:.95rem;color:var(--dark);display:block;margin-bottom:.5rem;">Which agent are you considering?</label>
        <select id="roi-agent" style="width:100%;padding:.65rem .9rem;border:1.5px solid var(--border);border-radius:8px;font-size:.95rem;background:#fff;color:var(--ink);">
          <option value="none">— Not sure yet —</option>
          <optgroup label="Sales">
            <option value="6000,750,20">Signal Prospector</option>
            <option value="3500,450,12">Inbound Lead Researcher</option>
            <option value="1500,250,8">CRM Hygiene</option>
            <option value="3500,450,10">Deal Follow-up Drafter</option>
            <option value="1500,250,6">Meeting Prep Briefs</option>
          </optgroup>
          <optgroup label="Customer Success">
            <option value="3500,450,15">Renewal Risk Radar</option>
            <option value="1500,250,18">Support Ticket Triage</option>
            <option value="1500,250,10">Customer Onboarding Tracker</option>
          </optgroup>
          <optgroup label="Back Office">
            <option value="3500,450,12">Invoice Checker</option>
            <option value="3500,450,14">Resume Screener</option>
            <option value="1500,250,6">Weekly KPI Writer</option>
          </optgroup>
          <optgroup label="Marketing">
            <option value="1500,250,8">Competitor Watch</option>
            <option value="6000,750,20">RFP and Questionnaire Drafter</option>
          </optgroup>
        </select>
      </div>

      <!-- Sliders -->
      <div class="calc-grid" style="margin-bottom:1.5rem;">
        <div class="calc-field">
          <label>People doing this task today</label>
          <div class="slider-row">
            <input type="range" id="roi-people" min="1" max="10" value="2" step="1"/>
            <span class="slider-val" id="roi-people-val">2</span>
          </div>
        </div>
        <div class="calc-field">
          <label>Fully-loaded hourly cost (USD)</label>
          <div class="slider-row">
            <input type="range" id="roi-cost" min="50" max="150" value="75" step="5"/>
            <span class="slider-val" id="roi-cost-val">$75</span>
          </div>
        </div>
      </div>

      <!-- Results -->
      <div id="roi-results" class="calc-results" style="display:none;">
        <div class="calc-result"><div class="rval" id="roi-hrs">—</div><div class="rlabel">Hours saved / month</div></div>
        <div class="calc-result"><div class="rval" id="roi-save">—</div><div class="rlabel">Value saved / year</div></div>
        <div class="calc-result"><div class="rval" id="roi-pay">—</div><div class="rlabel">Payback period</div></div>
      </div>

      <!-- Not-sure fallback -->
      <div id="roi-noagent" style="display:none;background:rgba(62,201,201,.08);border:1.5px solid var(--border);border-radius:12px;padding:1.5rem;text-align:center;margin-top:1rem;">
        <p style="color:var(--ink);margin-bottom:.75rem;">These numbers depend on the task. Tell us your biggest time sink and we'll run the real estimate on a 30-minute call.</p>
        <a href="contact.html" class="btn btn-grad">Book a free call →</a>
      </div>

      <p class="calc-note" id="roi-note" style="display:none;">Conservative estimate based on typical deployments. Your pilot measures the actual number before the full run.</p>
      <a href="contact.html" class="btn btn-grad" id="roi-cta" style="display:none;margin-top:1.25rem;">Get the real number for your business →</a>
    </div>

    <p style="font-size:.8rem;color:var(--muted);margin-top:2rem;text-align:center;">Setup cost and care plan are shown transparently so the payback math is clear. Estimates assume the pilot confirms the agent works for your data.</p>
  </div>
</section>

<script>
(function(){
  var agentSel = document.getElementById('roi-agent');
  var peopleIn = document.getElementById('roi-people');
  var costIn   = document.getElementById('roi-cost');
  var peopleVal= document.getElementById('roi-people-val');
  var costVal  = document.getElementById('roi-cost-val');

  peopleIn.addEventListener('input', function(){ peopleVal.textContent = peopleIn.value; run(); });
  costIn.addEventListener('input',   function(){ costVal.textContent   = '$'+costIn.value; run(); });
  agentSel.addEventListener('change', run);

  function run(){
    var v = agentSel.value;
    var results = document.getElementById('roi-results');
    var noagent = document.getElementById('roi-noagent');
    var note    = document.getElementById('roi-note');
    var cta     = document.getElementById('roi-cta');

    if(v === 'none'){
      results.style.display = 'none';
      noagent.style.display = 'block';
      note.style.display    = 'none';
      cta.style.display     = 'none';
      return;
    }

    noagent.style.display = 'none';
    results.style.display = 'grid';
    note.style.display    = 'block';
    cta.style.display     = 'inline-block';

    var parts   = v.split(',');
    var setup   = +parts[0];
    var care    = +parts[1];
    var hrsBase = +parts[2];
    var people  = +peopleIn.value;
    var cost    = +costIn.value;

    var hrsMonth = hrsBase * people;
    var saveYear = hrsMonth * cost * 12;
    var saveMo   = hrsMonth * cost;
    var paybackWks = setup / ((saveMo - care) / 4.33);

    document.getElementById('roi-hrs').textContent  = hrsMonth + ' hrs';
    document.getElementById('roi-save').textContent = '$' + Math.round(saveYear).toLocaleString();
    document.getElementById('roi-pay').textContent  = paybackWks > 0 ? Math.round(paybackWks) + ' weeks' : '—';
  }

  run();
})();
</script>
"""

# ─────────────────────────────────────────────────────────────────────────────
# Build
# ─────────────────────────────────────────────────────────────────────────────
pages = {
    "index.html": page(
        "{PlAIceholder} — AI agents for growing companies",
        "Custom-built AI agents for companies with 10 to 200 employees. Designed, installed, and proven in two weeks.",
        "home", HOME_BODY),
    "agents.html": page(
        "Agent Catalog — {PlAIceholder}",
        "13 custom-built AI agents for sales, customer success, back office, and marketing. Three are ready now with live demos.",
        "agents", AGENTS_BODY),
    "how-it-works.html": page(
        "How It Works — {PlAIceholder}",
        "The five-step process, the two-week timeline, and every safety rule — explained plainly.",
        "how", HOW_BODY),
    "pricing.html": page(
        "Pricing — {PlAIceholder}",
        "Setup from $1,500. Care plan from $250/month. Fixed price, fixed scope. ROI calculator included.",
        "pricing", PRICING_BODY),
    "roi.html": page(
        "ROI Calculator — {PlAIceholder}",
        "Pick your agent, adjust two numbers, and see hours saved, dollar value, and payback period.",
        "roi", ROI_BODY),
    "case-study.html": page(
        "Case Study — {PlAIceholder}",
        "Become a founding client. Get a discounted AI agent build in exchange for letting us document your real results.",
        "case", CASE_BODY),
    "contact.html": page(
        "Book a Call — {PlAIceholder}",
        "Book a free 30-minute call. Live demo, no commitment.",
        "contact", CONTACT_BODY),
    "about.html": page(
        "About — {PlAIceholder}",
        "We help companies replace expensive AI experimentation with working agents, built by experts.",
        "about", ABOUT_BODY),
    "blog.html": page(
        "Blog — {PlAIceholder}",
        "How AI agents work, what we've learned building them, and what actually delivers results.",
        "blog", BLOG_BODY),
}

# Check for real demo files from agent-kit
agent_kit_samples = os.path.join(base, "agent-kit", "samples")
demo_files = {
    "signal-prospector-dashboard.html": ("Signal Prospector Dashboard", "Who to call this week — companies showing buying signals, scored and ready."),
    "renewal-risk-dashboard.html": ("Renewal Risk Dashboard", "Renewals at risk — accounts flagged with evidence and a suggested next step."),
    "invoice-checker-dashboard.html": ("Invoice Checker Dashboard", "Invoices to check before paying — exceptions flagged with dollars at risk."),
}

for fname, (title, desc) in demo_files.items():
    src = os.path.join(agent_kit_samples, fname)
    dst = os.path.join(DEMOS_DIR, fname)
    if os.path.exists(src):
        with open(src) as f: content = f.read()
        # Inject banner
        banner = f'<div style="background:#0d1b2a;color:rgba(255,255,255,.7);text-align:center;padding:.6rem;font-size:.82rem;">Sample data. These companies are fictional. <a href="../agents.html" style="color:#3ec9c9;">Back to agents →</a></div>'
        content = content.replace('<body>', '<body>' + banner, 1)
        content = content.replace('</body>', TRACKER + '\n</body>', 1)
        with open(dst, "w") as f: f.write(content)
        print(f"  demos/{fname} (from agent-kit)")
    else:
        with open(dst, "w") as f: f.write(demo_placeholder(title, desc))
        print(f"  demos/{fname} (placeholder — add agent-kit/samples/ to enable)")

with open(os.path.join(base, "style.css"), "w") as f:
    f.write(CSS)
print("  style.css")

for filename, content in pages.items():
    with open(os.path.join(base, filename), "w") as f:
        f.write(content)
    print(f"  {filename}")

# Blog post pages
blog_dir = os.path.join(base, "blog")
os.makedirs(blog_dir, exist_ok=True)
for p in POSTS:
    fname = os.path.join(blog_dir, f"{p['slug']}.html")
    with open(fname, "w") as f:
        f.write(post_page(p))
    print(f"  blog/{p['slug']}.html")

print("\nDone. Placeholders still to fill:")
print("  PlAIceholder  — company name")
print("  [Founder Name]   — your name (for About section)")
print("  [Contact Email]  — where leads should go")
print("  [Booking Link]   — Calendly or Cal.com link")
print("  [Case Study Client] — 'Praxis Escrow' with their OK, or 'a software escrow company'")
