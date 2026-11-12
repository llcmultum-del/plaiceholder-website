import os

base = os.path.dirname(os.path.abspath(__file__))

# ── favicon ──────────────────────────────────────────────────────────────────
FAVICON = '  <link rel="icon" type="image/png" sizes="64x64" href="favicon.png"/>\n  <link rel="shortcut icon" href="favicon.png"/>'

TRACKER = '<script src="https://multum-site-analytics.netlify.app/track.js" data-site="plaiceholder" defer></script>'

# ── SVG icons (solid brand colors, no gradient) ───────────────────────────────
# Usage: ICON["key"], drop straight into HTML as the icon div's content
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
    def a(label, href, key):
        cls = ' class="active"' if active == key else ""
        return f'<a href="{href}"{cls}>{label}</a>'

    agents_cls  = ' class="active"' if active in ("agents","how") else ""
    res_cls     = ' class="active"' if active in ("case","blog","roi","faq") else ""
    cta_cls     = " nav-cta-active" if active == "contact" else ""

    return f"""<nav>
  <a href="index.html" class="logo">{{PlAIceholder}}</a>
  <ul>
    <li>{a("Home","index.html","home")}</li>
    <li class="has-drop">
      <a href="agents.html"{agents_cls}>Agents <span class="drop-arrow">&#9662;</span></a>
      <ul class="dropdown">
        <li>{a("How It Works","how-it-works.html","how")}</li>
        <li>{a("Catalog","agents.html","agents")}</li>
      </ul>
    </li>
    <li>{a("Pricing","pricing.html","pricing")}</li>
    <li class="has-drop">
      <a href="blog.html"{res_cls}>Resources <span class="drop-arrow">&#9662;</span></a>
      <ul class="dropdown">
        <li>{a("Case Studies","case-study.html","case")}</li>
        <li>{a("Blog","blog.html","blog")}</li>
        <li>{a("ROI Calculator","roi.html","roi")}</li>
        <li>{a("FAQ","faq.html","faq")}</li>
      </ul>
    </li>
    <li>{a("About","about.html","about")}</li>
    <li>{a("Contact Us","contact.html","contact")}</li>
  </ul>
  <a href="contact.html" class="nav-cta{cta_cls}">Book a Call</a>
  <button class="hamburger" aria-label="Menu" onclick="this.closest('nav').classList.toggle('open')">&#9776;</button>
</nav>""" + """<script>
document.querySelectorAll('.has-drop>a').forEach(function(a){
  a.addEventListener('click',function(e){
    e.preventDefault();
    if(window.innerWidth<=900){
      this.closest('.has-drop').classList.toggle('open');
    }
  });
});
</script>"""

FOOTER = """<footer>
  <div class="footer-inner">
    <div class="footer-brand">
      <a href="index.html" class="logo footer-logo">{PlAIceholder}</a>
      <p class="footer-tag">AI agents that do the busywork inside the tools you already use.</p>
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
    <div class="footer-col">
      <p class="footer-col-label">Agents</p>
      <a href="how-it-works.html">How It Works</a>
      <a href="agents.html">Catalog</a>
      <a href="pricing.html">Pricing</a>
    </div>
    <div class="footer-col">
      <p class="footer-col-label">Resources</p>
      <a href="case-study.html">Case Studies</a>
      <a href="blog.html">Blog</a>
      <a href="roi.html">ROI Calculator</a>
      <a href="faq.html">FAQ</a>
    </div>
    <div class="footer-col">
      <p class="footer-col-label">Company</p>
      <a href="about.html">About</a>
      <a href="contact.html">Contact Us</a>
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
nav{position:sticky;top:0;z-index:200;display:flex;align-items:center;gap:2rem;
  padding:.7rem 2.5rem;background:rgba(255,255,255,.97);backdrop-filter:blur(10px);
  border-bottom:1px solid var(--border);}
.logo{font-size:1.2rem;font-weight:800;background:var(--grad);-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;background-clip:text;text-decoration:none;white-space:nowrap;}
nav>ul{list-style:none;display:flex;gap:1.4rem;align-items:center;flex:1;}
nav a{text-decoration:none;color:var(--ink);font-weight:500;font-size:.88rem;transition:color .2s;}
nav a:hover,nav a.active{color:var(--blue);}
.drop-arrow{font-size:.65rem;opacity:.5;margin-left:.15rem;}
/* dropdowns */
.has-drop{position:relative;}
.has-drop>a{display:flex;align-items:center;gap:.1rem;}
.has-drop{padding-bottom:.6rem;margin-bottom:-.6rem;}
.dropdown{display:none;position:absolute;top:100%;left:0;min-width:170px;
  background:#fff;border:1px solid var(--border);border-radius:12px;
  box-shadow:0 8px 28px rgba(0,0,0,.1);padding:.5rem 0;list-style:none;z-index:300;}
.dropdown li a{display:block;padding:.55rem 1.1rem;font-size:.85rem;color:var(--ink);white-space:nowrap;}
.dropdown li a:hover{color:var(--blue);background:var(--light);}
.has-drop:hover .dropdown,.has-drop:focus-within .dropdown{display:block;}
.has-drop>a{cursor:default;}
/* cta */
nav>.nav-cta{background:var(--grad);color:#fff !important;padding:.38rem 1.1rem;
  border-radius:100px;-webkit-text-fill-color:#fff !important;font-size:.85rem !important;
  white-space:nowrap;flex-shrink:0;}
nav>.nav-cta:hover{opacity:.85;}
.hamburger{display:none;background:none;border:none;font-size:1.4rem;cursor:pointer;color:var(--ink);}
@media(max-width:900px){
  nav>ul{display:none;flex-direction:column;align-items:flex-start;position:absolute;top:100%;left:0;right:0;
    background:#fff;border-bottom:1px solid var(--border);padding:1rem 2rem 1.5rem;gap:.9rem;z-index:300;}
  nav.open>ul{display:flex;}
  nav>.nav-cta{display:none;}
  .hamburger{display:block;}
  .dropdown{position:static;box-shadow:none;border:none;padding:.25rem 0 .25rem 1rem;display:none;}
  .has-drop.open .dropdown{display:block;}
  .has-drop>a{justify-content:space-between;}
  .has-drop>a .drop-arrow{display:inline;}
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
.hero-trust{display:flex;gap:1.5rem;justify-content:center;flex-wrap:wrap;margin-top:1.75rem;
  padding-top:1.5rem;border-top:1px solid rgba(255,255,255,.18);}
.hero-trust span{display:flex;align-items:center;gap:.45rem;font-size:.8rem;color:rgba(255,255,255,.65);}
.hero-trust span svg{opacity:.7;}

/* ── how-teaser steps ── */
.how-teaser-steps{display:flex;flex-direction:column;gap:1rem;margin-top:1.5rem;}
.hts{display:flex;align-items:flex-start;gap:1rem;}
.hts-num{width:28px;height:28px;border-radius:50%;background:var(--blue);color:#fff;
  font-size:.8rem;font-weight:800;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:.1rem;}
.hts strong{color:#fff;font-size:.95rem;display:block;margin-bottom:.2rem;}
.hts p{color:rgba(255,255,255,.55);font-size:.84rem;margin:0;}

/* ── card with demo (hover lift) ── */
.card.card-demo{transition:transform .22s,box-shadow .22s;cursor:pointer;}
.card.card-demo:hover{transform:translateY(-4px);box-shadow:0 12px 32px rgba(26,110,245,.13);}

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
  transition:box-shadow .25s;display:flex;flex-direction:column;}
.agent-card:hover{box-shadow:0 4px 18px rgba(0,0,0,.07);}
.agent-card.has-demo{transition:transform .25s,box-shadow .25s;cursor:pointer;}
.agent-card.has-demo:hover{transform:translateY(-4px);box-shadow:0 12px 32px rgba(26,110,245,.1);}
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
.chat-btn{width:62px;height:62px;border-radius:50%;
  background:rgba(255,255,255,.72);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
  border:1px solid rgba(255,255,255,.55);box-shadow:0 4px 20px rgba(0,0,0,.18);
  color:var(--blue);font-size:1.35rem;font-weight:900;line-height:1;
  display:flex;align-items:center;justify-content:center;
  cursor:pointer;transition:opacity .2s,transform .2s;font-family:inherit;}
.chat-btn:hover{opacity:.9;transform:scale(1.06);}
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
footer{background:var(--dark);padding:3rem 2rem 1.5rem;}
.footer-inner{max-width:1080px;margin:0 auto;display:flex;flex-wrap:wrap;gap:3rem;margin-bottom:2.5rem;}
.footer-brand{flex:1 1 200px;min-width:180px;}
.footer-logo{font-size:1.2rem !important;-webkit-text-fill-color:#fff !important;display:inline-block;margin-bottom:.4rem;}
.footer-tag{font-size:.82rem;color:rgba(255,255,255,.45);max-width:220px;margin-top:.3rem;line-height:1.5;}
.footer-linkedin{display:inline-flex;align-items:center;line-height:1;margin-top:1.1rem;}
.footer-linkedin:hover{opacity:.8;}
.footer-col{display:flex;flex-direction:column;gap:.6rem;min-width:120px;}
.footer-col-label{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:rgba(255,255,255,.35);margin-bottom:.2rem;}
.footer-col a{text-decoration:none;color:rgba(255,255,255,.6);font-size:.88rem;transition:color .2s;}
.footer-col a:hover{color:var(--sea);}
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
  .hero-trust{flex-direction:column;gap:.5rem;align-items:flex-start;}
  .hts{flex-direction:column;gap:.35rem;}
  .how-teaser-steps{gap:1.25rem;}

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
      <div class="msg msg-ai">Hey! Ask me about our agents, pricing, how we work, or I can help you book a free demo call.</div>
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
      addMsg('Something went wrong, visit our contact page to reach us directly.','ai');
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
    <div class="badge">Custom-built AI agents</div>
    <h1>Your team's slowest weekly task, automated in two weeks.</h1>
    <p class="lead">We build AI agents for any repeatable process your team runs on a schedule, inside the tools you already pay for.</p>
    <div class="hero-btns">
      <a href="contact.html" class="btn btn-white">Book a free 30-minute call</a>
      <a href="agents.html" class="btn btn-outline">See the agent catalog</a>
    </div>
    <div class="hero-trust">
      <span>{ICON["clipboard"]} Pilot on 20 real records before you commit</span>
      <span>{ICON["link"]} Every AI finding cites its source</span>
      <span>{ICON["user"]} People approve all actions</span>
    </div>
  </div>
</section>

<!-- What we automate -->
<section class="section section-white">
  <div class="inner">
    <span class="tag">What we automate</span>
    <h2>If a person does it every week, an agent can do it for them.</h2>
    <p class="sub">Any repeatable task that involves reading, judging, or writing is a candidate. Here are the most common types.</p>
    <div class="cards">
      <div class="card">
        <div class="icon">{ICON["target"]}</div>
        <h3>Reading and research</h3>
        <p>Prospect research, buying-signal monitoring, meeting prep briefs, competitor tracking. The agent reads, summarizes, and surfaces only what matters.</p>
      </div>
      <div class="card">
        <div class="icon">{ICON["alert"]}</div>
        <h3>Scoring and flagging</h3>
        <p>Lead fit scoring, renewal risk, invoice exceptions, ticket priority. The agent runs the same judgment call every time and flags anything that needs a human look.</p>
      </div>
      <div class="card">
        <div class="icon">{ICON["filetext"]}</div>
        <h3>Writing and reporting</h3>
        <p>Draft follow-up emails, weekly KPI summaries, RFP answers, applicant shortlists. The agent writes the first version; your team reviews and sends.</p>
      </div>
    </div>
    <p style="margin-top:2rem;text-align:center;"><a href="agents.html" class="btn btn-dark">Browse the full catalog of 13 agents</a></p>
  </div>
</section>

<!-- Process + ROI -->
<section class="section section-dark">
  <div class="inner">
    <div class="two-col">
      <div>
        <span class="tag">The process</span>
        <h2>Two weeks from yes to handover.</h2>
        <p style="color:rgba(255,255,255,.65);margin-bottom:1.5rem;">Fixed price, fixed scope. You see the agent run on 20 of your real records before you pay the second half. No surprises.</p>
        <div class="how-teaser-steps">
          <div class="hts"><div class="hts-num">1</div><div><strong>Free call and demo</strong><p>Pick the task. See a sample result. No prep needed.</p></div></div>
          <div class="hts"><div class="hts-num">2</div><div><strong>Build and pilot</strong><p>We connect to your tools and run 20 real records. You check the output before anything goes further.</p></div></div>
          <div class="hts"><div class="hts-num">3</div><div><strong>Measure and hand over</strong><p>Real time saved on your data. 30-minute training. Monthly care plan to keep it running.</p></div></div>
        </div>
        <a href="how-it-works.html" class="btn btn-outline" style="margin-top:1.5rem;">Full process and safety rules</a>
      </div>
      <div>
        <span class="tag" style="color:rgba(255,255,255,.5);">Estimate your return</span>
        <h2 style="color:#fff;margin-bottom:1rem;">See your ROI before you commit.</h2>
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
          <a href="roi.html" class="btn btn-grad">Calculate yours</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- CTA bar -->
<section class="section section-light" style="text-align:center;">
  <div class="inner" style="max-width:580px;">
    <h2>Start with a free call. No commitment.</h2>
    <p style="color:var(--muted);margin-top:1rem;">We'll walk you through a live demo, talk through your biggest time sink, and tell you straight whether an agent is the right fit.</p>
    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-top:2rem;">
      <a href="contact.html" class="btn btn-grad">Book a free call</a>
      <a href="how-it-works.html" class="btn btn-dark">See how it works</a>
    </div>
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
   "job":"Finds companies showing buying signals in the news, funding, acquisitions, new leaders, expansion, explains why now, finds the right people to contact, and saves it all to your CRM.",
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
   "job":"Pulls the week's numbers and writes the story behind them, what moved, why, and what to watch.",
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
    has_demo_cls = " has-demo" if a.get("demo") else ""
    return f"""<div class="agent-card{has_demo_cls}" data-area="{a['area']}" data-tier="{a['tier']}" data-status="{a['status']}">
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
    <p>Catalog agents start at $1,500. Custom agents are scoped to your process. Every build is fixed price.</p>
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
        <p style="color:rgba(255,255,255,.65);font-size:.9rem;margin-bottom:1.25rem;">We build fully custom agents for any repeatable process your team runs weekly. If a person currently does it by reading, judging, or typing, an agent can likely do it. Same two-week process, same fixed price, same safety rules.</p>
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
    'prospect':'<strong>Signal Prospector</strong>, finds companies showing buying signals and saves the right contacts to your CRM. Advanced tier, from $6,000.',
    'churn':'<strong>Renewal Risk Radar</strong>, flags accounts at risk before renewal with evidence from tickets, notes, and usage. Standard tier, from $3,500.',
    'invoice':'<strong>Invoice Checker</strong>, matches every invoice to its PO and flags problems with dollars at risk before you pay. Standard tier, from $3,500.',
    'data':'<strong>CRM Hygiene</strong> or <strong>Weekly KPI Writer</strong>, clean your data or get a Monday summary of what moved and why. Starter tier, from $1,500.'
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
    <p>Two weeks from call to running agent. Here's what happens at each step, and why we do it that way.</p>
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
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">30 min, Free</div><h3>Live demo call</h3><p>We show you a working agent on sample data. You tell us the task that costs your team the most time. No pitch deck, no commitment. If we can't help, we'll say so.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">1–2 days</div><h3>Fixed-price proposal</h3><p>We send a scope document: exactly what the agent will do, what it won't do, what it connects to, the price, and the timeline. 50% to start, 50% at handover.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">1 hour</div><h3>Discovery interview</h3><p>We interview the person who currently does the task. Their answers become the agent's settings: which signals matter, what a good result looks like, what edge cases to handle, what to skip. This hour is what makes it yours, not generic.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">3–5 days</div><h3>Connect and pilot</h3><p>You create API keys in your existing tools; we do the rest. We run the agent on 20 real records. Your team reviews the top results and tells us what to tune before the full run.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">1 day</div><h3>Measure and hand over</h3><p>We time the old way against the new way on the same 20 records, write up the real numbers, and run a 30-minute training. You pay the remaining 50%. The agent is yours.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">Ongoing</div><h3>Care plan</h3><p>We monitor the agent, fix it when a connected tool changes its API, apply tuning hours each month, and send a monthly results email. You're not maintaining it alone.</p></div>
        </div>
      </div>
      <div>
        <span class="tag">What we need from you</span>
        <h2>Three things, that's it.</h2>
        <div class="cards" style="grid-template-columns:1fr;">
          <div class="card"><div class="icon">{ICON["key"]}</div><h3>An admin who can create access keys</h3><p>We connect through read-only or scoped API keys in your existing tools. You control the keys and can revoke them at any time. We never ask for more access than the specific task requires.</p></div>
          <div class="card"><div class="icon">{ICON["clock"]}</div><h3>One hour from the person who does the task</h3><p>This is the most important hour. We learn what "good" looks like, what signals matter, what exceptions exist. The discovery interview is what separates an agent that fits your business from one that fits a demo.</p></div>
          <div class="card"><div class="icon">{ICON["chart"]}</div><h3>Clean-enough data</h3><p>Your data doesn't need to be perfect. If it needs cleanup first, we quote that separately, or start with the CRM Hygiene agent to get it in shape before the main build.</p></div>
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
      <div class="trust-item"><div class="trust-icon">{ICON["link"]}</div><div><h4>No made-up facts</h4><p>Every AI finding requires a source link it actually retrieved. Findings without evidence are discarded before your team sees them, automatically, not by review.</p></div></div>
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
    <p class="sub">Pick your agent, adjust two numbers, and get hours saved, dollar value, and payback period, in under a minute.</p>
    <a href="roi.html" class="btn btn-grad">Open the ROI calculator →</a>
  </div>
</section>

<!-- FAQ -->
<section class="section section-light">
  <div class="inner">
    <span class="tag">FAQ</span>
    <h2>Common questions</h2>
    <div class="faq">
      <details><summary>What exactly is an "AI agent"?</summary><p>A program that does a multi-step task a person used to do, research, reading, judging, and writing up, inside your tools, with rules that check its work before anyone sees it.</p></details>
      <details><summary>Do we need to be technical?</summary><p>No. You need an admin who can create access keys and one hour from the people who currently do the task.</p></details>
      <details><summary>Which AI do you use?</summary><p>We build with the leading models, Claude, GPT-4o, Gemini, and others, and pick whichever fits your stack and budget best. The model runs through your own account so you see and control the usage bill directly.</p></details>
      <details><summary>What does it cost to run?</summary><p>You pay AI usage and data credits directly to those providers at cost, typically a few cents per record. We estimate the number up front and measure the real cost per record in your pilot.</p></details>
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
        <p style="color:var(--muted);margin-bottom:1.25rem;">In exchange, you get a meaningfully discounted build, and we get the proof we can show the next client.</p>
        <p style="color:var(--muted);">You stay in control. We only publish what you approve in writing. If the numbers aren't what we hoped, they don't go public.</p>

        <span class="tag" style="margin-top:2rem;display:block;">What we publish</span>
        <h2>Honest, specific, verifiable.</h2>
        <div class="timeline" style="margin-top:1rem;">
          <div class="tl-item"><div class="tl-dot"></div><h3>Time saved per week</h3><p>Measured before and after. Hours are hours, no vague "efficiency gains."</p></div>
          <div class="tl-item"><div class="tl-dot"></div><h3>Dollar value of that time</h3><p>Based on the hourly cost your team actually carries, not an inflated benchmark.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><h3>How the agent works</h3><p>What it pulls, what it decides, what it writes back, described plainly so readers can judge for themselves.</p></div>
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
          <p>We measure everything during the pilot. You review the numbers and the write-up before anything goes public. If you don't approve it, it doesn't publish, and your discount stands either way.</p>
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
    <p class="sub" style="margin:0 auto 2rem;">Founding client builds get more of our time, better discovery, faster iterations, and direct access to us throughout the pilot. We can only take a few at a time.</p>
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
    <h1>Book a Call</h1>
    <p>Free 30-minute call. Live demo, straight answers, no commitment.</p>
  </div>
</div>
<section class="section section-light">
  <div class="inner">
    <div class="contact-wrap">
      <div class="ci">
        <span class="tag">Get in touch</span>
        <h2>Free call,<br>no commitment</h2>
        <p>In 30 minutes we'll walk you through a live demo on sample data, talk through your biggest time sink, and give you a straight answer on whether an agent can help.</p>
        <div class="ci-chip"><span class="ic">{ICON["filetext"]}</span><span><a href="mailto:ben@plaiceholder.io" style="color:var(--blue);font-weight:600;">ben@plaiceholder.io</a></span></div>
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
      <form class="contact-form" name="contact" method="POST" data-netlify="true" onsubmit="handleSubmit(event)">
        <input type="hidden" name="form-name" value="contact"/>
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
        <select name="source" required>
          <option value="" disabled selected>Where did you find us?</option>
          <option>Google search</option>
          <option>LinkedIn</option>
          <option>Word of mouth / referral</option>
          <option>AI search (ChatGPT, Perplexity, etc.)</option>
          <option>Social media</option>
          <option>Blog or article</option>
          <option>Other</option>
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
  btn.textContent='Sending…';btn.disabled=true;
  var data=new FormData(e.target);
  fetch('/',{{method:'POST',headers:{{'Content-Type':'application/x-www-form-urlencoded'}},
    body:new URLSearchParams(data).toString()}})
    .then(function(){{
      btn.textContent='Sent ✓';btn.style.opacity='.6';
      document.getElementById('form-success').style.display='block';
      e.target.reset();
    }})
    .catch(function(){{
      btn.textContent='Send →';btn.disabled=false;
      alert('Something went wrong. Email us directly at ben@plaiceholder.io');
    }});
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
        <p style="color:var(--muted);margin-bottom:1.25rem;">Most companies sit on AI tools they're not using. Not because AI isn't useful, because using it well takes real experience. Someone has to understand the models, the APIs, the edge cases, and what actually fails in production.</p>
        <p style="color:var(--muted);margin-bottom:1.25rem;">Hiring a full-time AI person costs $120K+ and months of ramp time. And that person is still figuring it out on your dime. What you get is expensive experimentation dressed up as a job title.</p>
        <p style="color:var(--muted);">{PlAIceholder} is the alternative. We've already done the learning. We show up with working agents, not prototypes, and we're done in two weeks, not six months.</p>
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
            <p>Not every task fits a catalog. We build fully custom agents using the same two-week process, discovery interview, fixed price, pilot on 20 records, measure and hand over.</p>
          </div>
          <div class="card">
            <div class="icon">{ICON["shield"]}</div>
            <h3>We stay on it</h3>
            <p>AI tools and business software change constantly. Our care plan means we fix it when something breaks, without you having to file a ticket or find a contractor.</p>
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
    <p style="color:rgba(255,255,255,.65);margin-bottom:2rem;">We don't publish ROI claims until a client approves the real numbers in writing. Sample dashboards are labeled as fictional. This page will grow as clients give us permission to quote them, not before.</p>
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
  {
    "slug": "how-to-tell-if-an-ai-agent-is-working",
    "title": "How to Tell If an AI Agent Is Actually Working",
    "date": "2026-11-12",
    "tag": "ROI",
    "preview": "Most companies running AI can't say whether it paid off, usually because nobody wrote down what \"before\" looked like.",
    "body": """
<p>Ask a company whether its AI tools are working and you will usually get a feeling, not a number. People say it seems faster, or that the team likes it. That is not nothing, but it is not an answer either. MIT's NANDA initiative reported in 2025 that only about 5% of the generative AI pilots it studied produced rapid revenue gains, with the rest showing little or no measurable effect on profit and loss. Futurum Group's 2026 survey of 830 IT decision-makers found 43% still unsure how to measure the business value of their AI. Some of those tools may well be helping. The trouble is that nobody can show it.</p>
<h2>Write down "before" first</h2>
<p>Most measurement problems start before the tool is switched on. If nobody records how long the task takes today, how often it goes wrong, and how much of it sits in a queue, there is nothing to compare against later. A month in, "it feels quicker" is the only evidence left.</p>
<p>The baseline does not need to be elaborate. For a single repeatable task, three numbers usually cover it: how many items go through in a week, how long each one takes a person, and how many get sent back or corrected. Count them for two or three weeks before anything changes. A spreadsheet is fine.</p>
<h2>Measure the task, not the tool</h2>
<p>A common mistake is tracking what the software does instead of what the business gets. Number of prompts run, number of messages drafted, number of logins: these show activity, and activity is easy to produce. What matters is whether the task itself got cheaper, faster, or more accurate.</p>
<p>This is one reason narrow agents are easier to judge than broad assistants. An agent that checks supplier invoices against purchase orders has an obvious scoreboard: invoices checked, mismatches caught, mismatches missed, hours a person no longer spends on it. A general chat tool spread across a whole department has no single scoreboard, so its value turns into an argument. The MIT report made a related point: back-office work like this showed some of the clearest measured returns, even though most AI budgets went to sales and marketing.</p>
<h2>Check accuracy, not only speed</h2>
<p>Speed is the number everyone reaches for, because it improves straight away. But an agent that finishes in seconds and is wrong one time in ten can cost more than the manual process it replaced, since someone now has to find and fix the errors downstream.</p>
<p>So keep a sample under review. For the first few weeks, have a person check a fixed share of the agent's output, record what it got wrong, and sort the errors into types. After that the sample can shrink, but it should not disappear. Inputs change: suppliers redesign their invoices, a CRM field gets renamed, a new product line appears. An agent that was accurate at launch can drift without anyone noticing unless someone keeps looking.</p>
<p>None of this is complicated, and most of it is done before or after the build rather than during it. That is why we set it up this way. Each PlAIceholder agent handles one defined task, so there is one set of numbers to watch. The pilot runs on a small batch of real records, so accuracy is checked against actual work before anything scales up. And the care plan exists partly to keep watching those numbers after launch, when drift tends to show up. If an agent is working, the figures will show it. If it is not, it is better to find that out in week three than in month nine.</p>
"""
  },
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
    return page(f"{p['title']}, {{PlAIceholder}}", p['preview'], "blog", body_html)

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
  <title>{title}, Sample</title>
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
          <option value="none">,  Not sure yet , </option>
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
        <div class="calc-result"><div class="rval" id="roi-hrs">, </div><div class="rlabel">Hours saved / month</div></div>
        <div class="calc-result"><div class="rval" id="roi-save">, </div><div class="rlabel">Value saved / year</div></div>
        <div class="calc-result"><div class="rval" id="roi-pay">, </div><div class="rlabel">Payback period</div></div>
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
    document.getElementById('roi-pay').textContent  = paybackWks > 0 ? Math.round(paybackWks) + ' weeks' : ', ';
  }

  run();
})();
</script>
"""

FAQ_BODY = """
<section class="section" style="padding-top:3.5rem;">
  <div class="inner" style="max-width:860px;">
    <h1 style="font-size:2.2rem;margin-bottom:.6rem;">Frequently Asked Questions</h1>
    <p style="color:var(--muted);font-size:1.05rem;margin-bottom:3rem;">Straight answers about what AI agents are, how they work, and whether one is right for you.</p>

    <div class="faq-toc">
      <a href="#what-it-is">What it is &amp; who it's for</a>
      <a href="#sales">Sales</a>
      <a href="#customer-success">Customer Success</a>
      <a href="#back-office">Back Office</a>
      <a href="#integrations">Integrations &amp; Tech</a>
      <a href="#safety">Safety &amp; Trust</a>
      <a href="#pricing">Pricing &amp; ROI</a>
      <a href="#process">Process &amp; Timeline</a>
    </div>

    <div class="faq-group" id="what-it-is">
      <h2 class="faq-group-title">What it is &amp; who it's for</h2>

      <details class="faq-item" open>
        <summary>What is a custom AI agent for business?</summary>
        <div class="faq-answer">
          <p>A custom AI agent is software that handles one specific, repeatable task your team does regularly, without a human doing it manually. It reads from your systems, makes decisions based on rules you approve, writes or flags the output, and hands the result back to your team. It's not a general assistant and it's not a chatbot. It does one job, inside the tools you already use, on a schedule you control.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>How is an AI agent different from a chatbot or Zapier automation?</summary>
        <div class="faq-answer">
          <p>A chatbot responds to questions in a conversation window. A Zapier automation moves data from point A to point B when a trigger fires. An AI agent reasons. It reads unstructured text, weighs multiple signals, makes a judgment, and produces a structured output. For example: a Zap can copy a lead into your CRM when a form is submitted. An AI agent can read that lead's LinkedIn profile, their company's recent news, and their job title, then score the opportunity and write a personalized outreach draft. The judgment is what makes it an agent.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>Is PlAIceholder a good fit for a small or mid-sized business?</summary>
        <div class="faq-answer">
          <p>Yes. We work best with companies that have a clear repeatable task taking meaningful staff hours every week, a team willing to review outputs in the first few weeks, and an appetite to actually use the results. If you can describe the task in a paragraph and name the person who currently does it, we can probably automate a large part of it. We don't require a large IT team or existing AI infrastructure.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>Do I need an in-house AI engineer to use an AI agent?</summary>
        <div class="faq-answer">
          <p>No. We handle the build, the integration, and the initial tuning. Once deployed, the agent runs automatically and your team just reviews the outputs in the same tools they already use. If something needs adjustment, you contact us and we handle it. The care plan exists specifically so you don't need to maintain it yourself.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>What's the difference between hiring an AI agency and building in-house?</summary>
        <div class="faq-answer">
          <p>Building in-house means hiring an ML engineer or AI developer, spending months on trials, and owning all the maintenance. It makes sense if AI is core to your product. For a business task like lead scoring or invoice review, you're paying for a capability, not building a platform. We deliver a working agent in roughly two weeks at a fixed price, with a care plan that keeps it working. No recruiting, no six-month build cycle, no internal expertise required.</p>
        </div>
      </details>
    </div>

    <div class="faq-group" id="sales">
      <h2 class="faq-group-title">Sales</h2>

      <details class="faq-item">
        <summary>Can AI find companies that are ready to buy?</summary>
        <div class="faq-answer">
          <p>It can surface companies showing signals that often precede a buying decision: job postings that suggest a problem you solve, news mentions of relevant events, funding announcements, leadership changes, or other observable indicators. It won't predict the future, but it narrows a large list to the accounts most worth calling this week. That's what our Signal Prospector does.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>How does AI lead research work?</summary>
        <div class="faq-answer">
          <p>The agent takes a list of companies or contacts, pulls publicly available information from web sources, company sites, LinkedIn, and news feeds, then synthesizes a brief on each one: who they are, why they might be a fit, what to reference in an outreach. The output lands in your CRM or a spreadsheet, structured and ready to use. Research that takes a rep 30 minutes per account can be done in under a minute per account at scale.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>Can an AI agent follow up on stalled deals in HubSpot or Salesforce?</summary>
        <div class="faq-answer">
          <p>Yes. The agent scans deals that have gone quiet based on the last activity date, drafts a personalized follow-up for each one based on the deal context and contact history, and queues the drafts for your rep to review and send. It doesn't send automatically unless you specifically want that. The rep stays in the loop; they just stop starting from a blank page.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>What is a buying signal, and how does the Signal Prospector find them?</summary>
        <div class="faq-answer">
          <p>A buying signal is any observable event that suggests a company may be in a position to buy. Common examples: a job posting for a role that implies they need what you sell, a press release about a problem you solve, a funding round that gives them budget, or a leadership hire who has bought similar solutions before. The Signal Prospector monitors sources you define, extracts these events, scores them against your ideal customer profile, and delivers a ranked list each week.</p>
        </div>
      </details>
    </div>

    <div class="faq-group" id="customer-success">
      <h2 class="faq-group-title">Customer Success</h2>

      <details class="faq-item">
        <summary>Can AI predict which customers won't renew?</summary>
        <div class="faq-answer">
          <p>It can flag accounts showing risk indicators before the renewal conversation. These signals include declining usage, unresolved support tickets, reduced stakeholder engagement, or CRM notes that mention competitor evaluation. It won't be right every time, but it surfaces the accounts most worth a proactive conversation while there's still time to act. That's what the Renewal Risk Radar does.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>How does AI triage support tickets in Zendesk?</summary>
        <div class="faq-answer">
          <p>The agent reads incoming tickets, classifies them by issue type and urgency, routes them to the right queue or team, and drafts an initial response for the agent to review. It can also link tickets to known issues or documentation. The goal is to cut first-response time and reduce the number of tickets your team has to read in full before knowing what to do with them.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>What does the Renewal Risk Radar actually flag?</summary>
        <div class="faq-answer">
          <p>Accounts where one or more risk signals are present: low product usage relative to their contract, open support issues past a certain age, no recorded activity with the account team in the last 60 days, NPS below a threshold, or notes mentioning dissatisfaction or competitor evaluation. Each flag includes the evidence so your CSM can make a judgment call, not just a warning light with no context.</p>
        </div>
      </details>
    </div>

    <div class="faq-group" id="back-office">
      <h2 class="faq-group-title">Back Office</h2>

      <details class="faq-item">
        <summary>Can AI check invoices against purchase orders automatically?</summary>
        <div class="faq-answer">
          <p>Yes. The Invoice Checker reads incoming invoices, matches them against the corresponding purchase orders, and flags discrepancies: amounts that don't match, vendors not on your approved list, line items that don't appear on the PO, or invoices submitted more than once. Each flagged invoice includes the specific mismatch so your AP team can resolve it rather than hunt for it. Clean invoices pass through without manual review.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>Does the Invoice Checker work with QuickBooks?</summary>
        <div class="faq-answer">
          <p>We've built integrations with QuickBooks, as well as email-based invoice workflows where PDFs or attachments arrive in a shared inbox. The specific integration depends on how you currently receive and process invoices. We cover this on the discovery call and confirm the integration before we build anything.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>Can AI screen job applicants fairly?</summary>
        <div class="faq-answer">
          <p>The Resume Screener scores applicants against criteria you define: required skills, experience level, specific qualifications. It doesn't make hiring decisions and it doesn't have opinions about names, photos, or background. Every score includes the reasoning so a human reviewer can agree or disagree. We recommend treating it as a first-pass tool that reduces the volume your team reads in full, not as a replacement for human judgment in hiring.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>Can an AI agent write weekly KPI reports?</summary>
        <div class="faq-answer">
          <p>Yes. The Weekly KPI Writer pulls your numbers from connected sources, compares them to the prior period and targets, writes the narrative summary, and delivers a formatted report to your inbox or Slack on a schedule. The report is ready to send or present with minimal editing. It's one of our most popular agents because it saves 1 to 3 hours every single week without any change to how you collect your data.</p>
        </div>
      </details>
    </div>

    <div class="faq-group" id="integrations">
      <h2 class="faq-group-title">Integrations &amp; Tech</h2>

      <details class="faq-item">
        <summary>What software do your AI agents integrate with?</summary>
        <div class="faq-answer">
          <p>We've built integrations with HubSpot, Salesforce, Zendesk, QuickBooks, Google Sheets, Slack, Gmail, Outlook, Notion, Airtable, and most tools with an API or a shared inbox. If your tool isn't on this list, tell us what it is on the discovery call. If it has an API or sends email, we can almost certainly connect to it.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>Which AI model do your agents use?</summary>
        <div class="faq-answer">
          <p>We build on Claude, made by Anthropic. We chose Claude for its strong reasoning on business tasks, its low rate of confident wrong answers, and Anthropic's serious approach to safe deployment. We use the model that best fits each task's needs. You don't need an Anthropic account; API access is included in your care plan.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>Will an AI agent work with my existing CRM?</summary>
        <div class="faq-answer">
          <p>Almost certainly. If your CRM has an API, a Zapier integration, or a CSV export, we can read from it and write back to it. HubSpot and Salesforce are the most common and are fully supported. For less common CRMs, we'll confirm feasibility on the discovery call. We've never had to turn a project away because of the CRM.</p>
        </div>
      </details>
    </div>

    <div class="faq-group" id="safety">
      <h2 class="faq-group-title">Safety &amp; Trust</h2>

      <details class="faq-item">
        <summary>Is it safe to let AI touch my company's data?</summary>
        <div class="faq-answer">
          <p>We take this seriously. The agent only accesses the specific data needed for the task. We use encrypted connections, don't store your data beyond what's needed to run the agent, and don't use your data to train any AI model. Every integration is scoped to the minimum permissions required. We'll walk you through exactly what the agent reads and writes before anything goes live.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>Can the AI agent delete or overwrite my records?</summary>
        <div class="faq-answer">
          <p>By default, no. Every agent we build is configured to write new records or add fields, not to delete or overwrite existing data. If your use case genuinely requires overwriting a field, we discuss it explicitly and document it in the proposal. Auto-delete is never on by default and requires a deliberate decision on your part.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>How do you stop AI from hallucinating or making things up?</summary>
        <div class="faq-answer">
          <p>We design agents to work from sources, not from memory. Every output cites the specific text or record it was based on. The agent is not asked to generate facts; it's asked to extract, classify, or summarize from real inputs. For tasks where accuracy is critical, we also include a confidence score so reviewers know when to double-check. No agent we build makes an unsourced claim as if it were fact.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>What is dry-run mode?</summary>
        <div class="faq-answer">
          <p>Dry-run mode lets the agent process real data and produce its full output without writing anything back to your systems. You see exactly what it would have done without any of it actually happening. We use dry-run on the pilot: the agent runs on 20 real records, you review the results, and you decide whether the quality meets your bar before we flip it to live. It's how we prove the agent works before you rely on it.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>Who owns the AI agent after it's built?</summary>
        <div class="faq-answer">
          <p>You do. We hand over the agent, the configuration, and documentation of how it works. If you cancel the care plan and want to run it independently, you can. We don't lock you into our infrastructure. The care plan is a service, not a lease.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>Do you keep a copy of my company's data?</summary>
        <div class="faq-answer">
          <p>No. We don't retain your records after the agent has processed them. Logs used for debugging are kept for a limited period and then deleted. We don't use your data to train models, build datasets, or improve our general product. What you share with us stays in the agent and your systems.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>How do I control how much the AI spends?</summary>
        <div class="faq-answer">
          <p>Every agent runs with a spending cap. You set a maximum number of records per run, a maximum number of API calls, or both. The agent stops and alerts you if it's about to exceed the limit. The API cost for a typical agent run is small and predictable. We'll give you an estimate of monthly API cost as part of the proposal, and the care plan includes monitoring to catch any unexpected spikes.</p>
        </div>
      </details>
    </div>

    <div class="faq-group" id="pricing">
      <h2 class="faq-group-title">Pricing &amp; ROI</h2>

      <details class="faq-item">
        <summary>How much does a custom AI agent cost?</summary>
        <div class="faq-answer">
          <p>Setup is a one-time fixed price. Care (hosting, maintenance, updates) is a monthly flat fee. Prices range depending on the complexity of the agent and the integrations required. We publish three tiers on our <a href="pricing.html">pricing page</a> and every proposal is fixed-price with no hidden fees. You'll know the full cost before you commit to anything.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>What's included in the monthly care plan?</summary>
        <div class="faq-answer">
          <p>Hosting, monitoring, and keeping the agent running as the tools it connects to change. When a CRM updates its API or Anthropic releases a better model, we update the agent. If the agent starts producing lower quality outputs, we diagnose and fix it. You get a working agent, not just the code for one. The care plan is what keeps it working six months after launch, not just on day one.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>What's the ROI of an AI agent for a small business?</summary>
        <div class="faq-answer">
          <p>It depends on the task and how often your team does it. A realistic starting point: if the agent saves five hours per week at a fully loaded cost of $50 per hour, that's $1,000 per week in recovered capacity. Most agents deliver much more than that once fully adopted. Use our <a href="roi.html">ROI calculator</a> to put in your own numbers. We also don't take on projects where we can't make a reasonable case for positive ROI within the first year.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>How long until an AI agent pays for itself?</summary>
        <div class="faq-answer">
          <p>For most projects, between one and four months. The payback period depends on how many hours the agent saves per week and what those hours cost. The ROI calculator on our pricing page will give you a specific estimate for your situation. We're straightforward about cases where the numbers don't work: if the task is too infrequent or the volume too low, we'll say so on the first call.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>Why do you charge a fixed price instead of hourly?</summary>
        <div class="faq-answer">
          <p>Because hourly billing puts the risk on you. If the build takes longer than expected, you pay more. Fixed-price means we bear the risk of scope changes and estimation errors. You know what you're paying before we start. It also forces us to scope clearly upfront, which produces better agents than open-ended development does.</p>
        </div>
      </details>
    </div>

    <div class="faq-group" id="process">
      <h2 class="faq-group-title">Process &amp; Timeline</h2>

      <details class="faq-item">
        <summary>How long does it take to build an AI agent?</summary>
        <div class="faq-answer">
          <p>About two weeks from signed proposal to pilot results. Week one is the discovery interview, integration setup, and build. Week two is the pilot run on 20 real records, your review, and any tuning needed before full deployment. The two-week timeline assumes reasonable access to your systems and one point of contact on your side. Unusually complex integrations can extend this to three to four weeks.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>What happens on the free 30-minute call?</summary>
        <div class="faq-answer">
          <p>We'll ask you to describe the task you want to automate: what currently happens, who does it, what systems are involved, and what a good output looks like. We'll show you a live demo of the most relevant agent in our catalog. Then we'll tell you honestly whether we think an agent is a good fit, what it would cost, and what the timeline would look like. No prepared pitch. No pressure. If it's not the right fit, we'll tell you that too.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>What is a pilot run, and why 20 records?</summary>
        <div class="faq-answer">
          <p>The pilot is the agent running on 20 real records from your data, in dry-run mode so nothing is written back yet. You review the outputs alongside the actual records and tell us whether the quality is acceptable. Twenty is enough to catch edge cases and calibration issues without requiring a large sample. If the pilot meets your bar, we flip to live. If it doesn't, we adjust and run again. You don't pay the second half of the setup until the pilot passes.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>What happens if the agent stops working or needs changes?</summary>
        <div class="faq-answer">
          <p>Contact us. That's what the care plan covers. Tool APIs change, models improve, and your business needs evolve. We monitor for failures and usually catch problems before you notice them. For changes to scope or new functionality, we quote those separately. Bug fixes, maintenance, and keeping the existing agent running are covered in the monthly fee.</p>
        </div>
      </details>

      <details class="faq-item">
        <summary>Can I start with one agent and add more later?</summary>
        <div class="faq-answer">
          <p>Yes, and that's how most clients start. Pick the task that takes the most time or creates the most risk, automate that first, and then assess. The integrations we set up for the first agent often make subsequent agents faster to build. There's no requirement to commit to multiple agents upfront.</p>
        </div>
      </details>
    </div>

  </div>
</section>

<section class="section section-dark" style="text-align:center;">
  <div class="inner" style="max-width:580px;">
    <h2>Still have questions?</h2>
    <p style="color:rgba(255,255,255,.65);margin-top:1rem;">Book a free 30-minute call. We'll answer everything and show you a live demo of the agent that fits your team.</p>
    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-top:2rem;">
      <a href="contact.html" class="btn btn-white">Book a free call</a>
      <a href="agents.html" class="btn btn-outline">Browse the catalog</a>
    </div>
  </div>
</section>

<style>
.faq-toc{display:flex;flex-wrap:wrap;gap:.5rem;margin-bottom:3rem;}
.faq-toc a{font-size:.82rem;padding:.35rem .85rem;border-radius:100px;border:1px solid var(--border);color:var(--muted);text-decoration:none;transition:color .15s,border-color .15s;}
.faq-toc a:hover{color:var(--blue);border-color:var(--blue);}
.faq-group{margin-bottom:3rem;}
.faq-group-title{font-size:1.1rem;font-weight:700;color:var(--blue);text-transform:uppercase;letter-spacing:.06em;margin-bottom:1rem;padding-bottom:.5rem;border-bottom:1px solid var(--border);}
.faq-item{border:1px solid var(--border);border-radius:12px;margin-bottom:.6rem;overflow:hidden;}
.faq-item summary{padding:1rem 1.25rem;font-weight:600;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:1rem;font-size:.97rem;}
.faq-item summary::-webkit-details-marker{display:none;}
.faq-item summary::after{content:'+';font-size:1.3rem;font-weight:300;color:var(--muted);flex-shrink:0;transition:transform .2s;}
.faq-item[open] summary::after{content:'-';}
.faq-item[open] summary{color:var(--blue);}
.faq-answer{padding:.75rem 1.25rem 1.25rem;color:var(--muted);line-height:1.7;font-size:.93rem;border-top:1px solid var(--border);}
.faq-answer p{margin-bottom:.75rem;}
.faq-answer p:last-child{margin-bottom:0;}
.faq-answer a{color:var(--blue);}
</style>
"""

# ─────────────────────────────────────────────────────────────────────────────
# Build
# ─────────────────────────────────────────────────────────────────────────────
pages = {
    "index.html": page(
        "{PlAIceholder}, AI agents for growing companies",
        "Custom-built AI agents for companies with 10 to 200 employees. Designed, installed, and proven in two weeks.",
        "home", HOME_BODY),
    "agents.html": page(
        "Agent Catalog, {PlAIceholder}",
        "13 custom-built AI agents for sales, customer success, back office, and marketing. Three are ready now with live demos.",
        "agents", AGENTS_BODY),
    "how-it-works.html": page(
        "How It Works, {PlAIceholder}",
        "The five-step process, the two-week timeline, and every safety rule, explained plainly.",
        "how", HOW_BODY),
    "pricing.html": page(
        "Pricing, {PlAIceholder}",
        "Setup from $1,500. Care plan from $250/month. Fixed price, fixed scope. ROI calculator included.",
        "pricing", PRICING_BODY),
    "roi.html": page(
        "ROI Calculator, {PlAIceholder}",
        "Pick your agent, adjust two numbers, and see hours saved, dollar value, and payback period.",
        "roi", ROI_BODY),
    "case-study.html": page(
        "Case Study, {PlAIceholder}",
        "Become a founding client. Get a discounted AI agent build in exchange for letting us document your real results.",
        "case", CASE_BODY),
    "contact.html": page(
        "Contact Us, {PlAIceholder}",
        "Send us a message or book a free 30-minute demo call. We reply within one business day.",
        "contact", CONTACT_BODY),
    "about.html": page(
        "About, {PlAIceholder}",
        "We help companies replace expensive AI experimentation with working agents, built by experts.",
        "about", ABOUT_BODY),
    "blog.html": page(
        "Blog, {PlAIceholder}",
        "How AI agents work, what we've learned building them, and what actually delivers results.",
        "blog", BLOG_BODY),
    "faq.html": page(
        "FAQ, {PlAIceholder}",
        "Answers to common questions about AI agents for business: how they work, what they cost, and whether one is right for you.",
        "faq", FAQ_BODY),
}

# Check for real demo files from agent-kit
agent_kit_samples = os.path.join(base, "agent-kit", "samples")
demo_files = {
    "signal-prospector-dashboard.html": ("Signal Prospector Dashboard", "Who to call this week, companies showing buying signals, scored and ready."),
    "renewal-risk-dashboard.html": ("Renewal Risk Dashboard", "Renewals at risk, accounts flagged with evidence and a suggested next step."),
    "invoice-checker-dashboard.html": ("Invoice Checker Dashboard", "Invoices to check before paying, exceptions flagged with dollars at risk."),
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
        print(f"  demos/{fname} (placeholder, add agent-kit/samples/ to enable)")

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
print("  PlAIceholder , company name")
print("  [Founder Name]  , your name (for About section)")
print("  [Contact Email] , where leads should go")
print("  [Booking Link]  , Calendly or Cal.com link")
print("  [Case Study Client], 'Praxis Escrow' with their OK, or 'a software escrow company'")
