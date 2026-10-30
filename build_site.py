import os, urllib.parse

base = os.path.dirname(os.path.abspath(__file__))

# ── favicon ──────────────────────────────────────────────────────────────────
_svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1a6ef5"/><stop offset="100%" stop-color="#3ec9c9"/></linearGradient></defs><circle cx="16" cy="16" r="16" fill="url(#g)"/><text x="16" y="21" text-anchor="middle" font-family="system-ui,sans-serif" font-weight="800" font-size="16" fill="white">A</text></svg>'
FAVICON = f'  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,{urllib.parse.quote(_svg)}"/>'

# ── navigation ────────────────────────────────────────────────────────────────
def nav(active):
    links = [
        ("Home", "index.html", "home"),
        ("Agents", "agents.html", "agents"),
        ("Services", "services.html", "services"),
        ("How It Works", "how-it-works.html", "how"),
        ("Pricing", "pricing.html", "pricing"),
        ("Case Study", "case-study.html", "case"),
    ]
    items = ""
    for label, href, key in links:
        cls = ' class="active"' if active == key else ""
        items += f'    <li><a href="{href}"{cls}>{label}</a></li>\n'
    cta_cls = " active" if active == "contact" else ""
    items += f'    <li><a href="contact.html" class="nav-cta{cta_cls}">Book a Call</a></li>\n'
    return f"""<nav>
  <a href="index.html" class="logo">PlAIceholder</a>
  <ul>
{items}  </ul>
  <button class="hamburger" aria-label="Menu" onclick="this.closest('nav').classList.toggle('open')">&#9776;</button>
</nav>"""

FOOTER = """<footer>
  <div class="footer-inner">
    <div>
      <a href="index.html" class="logo footer-logo">PlAIceholder</a>
      <p class="footer-tag">AI agents that do the busywork inside the tools you already use.</p>
    </div>
    <div class="footer-links">
      <a href="agents.html">Agents</a>
      <a href="services.html">Services</a>
      <a href="how-it-works.html">How It Works</a>
      <a href="pricing.html">Pricing</a>
      <a href="case-study.html">Case Study</a>
      <a href="contact.html">Contact</a>
    </div>
  </div>
  <p class="footer-copy">© 2026 PlAIceholder. All rights reserved.</p>
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
  align-items:center;justify-content:center;font-size:1.3rem;margin-bottom:1rem;flex-shrink:0;}
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
  display:flex;align-items:center;justify-content:center;font-size:.95rem;flex-shrink:0;margin-top:.1rem;}
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
.agent-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:1.25rem;}
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

/* ── ROI calculator ── */
.calc-wrap{background:var(--dark);border-radius:22px;padding:2.5rem;color:#fff;}
.calc-wrap h3{font-size:1.2rem;font-weight:800;margin-bottom:.3rem;}
.calc-wrap .csub{font-size:.85rem;color:rgba(255,255,255,.6);margin-bottom:1.5rem;}
.calc-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:1.5rem;}
.calc-field label{display:block;font-size:.75rem;font-weight:600;color:rgba(255,255,255,.7);
  margin-bottom:.35rem;letter-spacing:.04em;}
.calc-field input,.calc-field select{width:100%;padding:.65rem .9rem;border-radius:9px;
  border:1.5px solid rgba(255,255,255,.15);background:rgba(255,255,255,.07);
  color:#fff;font-size:.9rem;outline:none;transition:border-color .2s;}
.calc-field input:focus,.calc-field select:focus{border-color:var(--sea);}
.calc-field select option{background:var(--dark);}
.calc-results{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:.75rem;margin-bottom:1.5rem;}
.calc-result{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.1);
  border-radius:12px;padding:1rem;}
.calc-result .rval{font-size:1.6rem;font-weight:900;background:var(--grad);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.calc-result .rlabel{font-size:.75rem;color:rgba(255,255,255,.6);margin-top:.1rem;}
.calc-note{font-size:.75rem;color:rgba(255,255,255,.45);margin-bottom:1rem;}
@media(max-width:600px){.calc-grid{grid-template-columns:1fr;}}

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
.chip{display:flex;align-items:center;gap:.65rem;margin-bottom:.9rem;color:var(--muted);font-size:.88rem;}
.chip .ic{width:34px;height:34px;border-radius:8px;background:var(--grad);
  display:flex;align-items:center;justify-content:center;font-size:.88rem;flex-shrink:0;}
form.contact-form{display:flex;flex-direction:column;gap:.8rem;}
.frow{display:grid;grid-template-columns:1fr 1fr;gap:.8rem;}
input,textarea,select{width:100%;padding:.7rem .9rem;border:1.5px solid var(--border);
  border-radius:10px;font-size:.88rem;font-family:inherit;background:#fff;
  color:var(--ink);outline:none;transition:border-color .2s;}
input:focus,textarea:focus,select:focus{border-color:var(--sea);}
textarea{resize:vertical;min-height:110px;}
.cbgroup{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:.4rem;}
.cb-label{display:flex;align-items:center;gap:.45rem;font-size:.83rem;color:var(--muted);cursor:pointer;}
.cb-label input{width:auto;accent-color:var(--blue);}
fieldset{border:1.5px solid var(--border);border-radius:10px;padding:.75rem .9rem;}
legend{font-size:.8rem;font-weight:700;color:var(--muted);padding:0 .4rem;}
.sbtn{background:var(--grad);color:#fff;padding:.78rem 1.75rem;border-radius:100px;
  font-size:.92rem;font-weight:700;border:none;cursor:pointer;
  transition:opacity .2s,transform .2s;align-self:flex-start;}
.sbtn:hover{opacity:.88;transform:translateY(-2px);}
.form-success{display:none;background:rgba(46,204,113,.1);border:1.5px solid var(--green);
  border-radius:12px;padding:1rem 1.25rem;color:#1a7a45;font-size:.9rem;font-weight:600;}

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
.footer-copy{text-align:center;font-size:.78rem;color:rgba(255,255,255,.3);max-width:1080px;margin:0 auto;}

@media(max-width:700px){
  .about-grid,.contact-wrap,.frow,.cs-grid{grid-template-columns:1fr;}
  .footer-inner{flex-direction:column;}
}
"""

# ── page wrapper ──────────────────────────────────────────────────────────────
def page(title, desc, active, body):
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
        <div class="icon">📈</div>
        <h3>Sales and prospecting</h3>
        <p>Find buying-signal companies, research new leads, prep for meetings, follow up stalled deals — done in minutes, not hours.</p>
      </div>
      <div class="card">
        <div class="icon">🔄</div>
        <h3>Customer success</h3>
        <p>Flag renewals at risk before they slip, triage support tickets and track onboarding — with the evidence your team needs.</p>
      </div>
      <div class="card">
        <div class="icon">🧾</div>
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
        <p>Claude (by Anthropic) does the research, reading, or judgment a person used to do.</p>
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
        <div class="icon">🎯</div>
        <h3>Signal Prospector</h3>
        <p>Finds companies showing buying signals in the news, explains why now, finds the right contacts, and saves everything to your CRM.</p>
        <p style="margin-top:.75rem;font-size:.8rem;color:var(--blue);font-weight:600;">Sales · Advanced · from $6,000</p>
        <a href="demos/signal-prospector-dashboard.html" class="demo-link" style="display:inline-block;margin-top:.75rem;font-size:.82rem;font-weight:700;color:var(--blue);text-decoration:none;">View sample dashboard →</a>
      </div>
      <div class="card">
        <div class="icon">⚠️</div>
        <h3>Renewal Risk Radar</h3>
        <p>Reads tickets, notes, and usage for accounts renewing soon. Flags risk with evidence and a suggested next step.</p>
        <p style="margin-top:.75rem;font-size:.8rem;color:var(--blue);font-weight:600;">Customer success · Standard · from $3,500</p>
        <a href="demos/renewal-risk-dashboard.html" class="demo-link" style="display:inline-block;margin-top:.75rem;font-size:.82rem;font-weight:700;color:var(--blue);text-decoration:none;">View sample dashboard →</a>
      </div>
      <div class="card">
        <div class="icon">🧾</div>
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
      <div class="trust-item"><div class="trust-icon">🧪</div><div><h4>Dry run by default</h4><p>Nothing is written or spent without a yes, one step at a time.</p></div></div>
      <div class="trust-item"><div class="trust-icon">📋</div><div><h4>Pilot first</h4><p>Every agent proves itself on 20 records before a full run.</p></div></div>
      <div class="trust-item"><div class="trust-icon">🔗</div><div><h4>No made-up facts</h4><p>Every AI finding links to its source. Unsupported findings are thrown out automatically.</p></div></div>
      <div class="trust-item"><div class="trust-icon">💰</div><div><h4>Spending caps</h4><p>Limits on AI usage and data credits, set in plain settings.</p></div></div>
      <div class="trust-item"><div class="trust-icon">🚫</div><div><h4>Never deletes</h4><p>Agents only add or update their own fields, and back up every record before changing it.</p></div></div>
      <div class="trust-item"><div class="trust-icon">🔑</div><div><h4>You own it</h4><p>It runs in your accounts with your keys. We delete our copies at handover.</p></div></div>
      <div class="trust-item"><div class="trust-icon">📝</div><div><h4>Full paper trail</h4><p>Every run keeps a log, the results, and a backup.</p></div></div>
      <div class="trust-item"><div class="trust-icon">👤</div><div><h4>People decide</h4><p>Agents draft, flag, and score. Your team sends emails, pays invoices, and makes hiring decisions.</p></div></div>
    </div>
  </div>
</section>

<!-- Process timeline -->
<section class="section section-white">
  <div class="inner">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:start;">
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
      <!-- ROI calculator -->
      <div>
        <span class="tag">Estimate your return</span>
        <h2>ROI calculator</h2>
        <div class="calc-wrap" id="calc">
          <h3>How much time is this task costing you?</h3>
          <p class="csub">Estimate. Your pilot measures the real number.</p>
          <div class="calc-grid">
            <div class="calc-field"><label>People doing the task</label><input type="number" id="c-people" value="2" min="1"/></div>
            <div class="calc-field"><label>Hours per week each</label><input type="number" id="c-hours" value="4" min="0.5" step="0.5"/></div>
            <div class="calc-field"><label>Hourly cost (USD)</label><input type="number" id="c-cost" value="45" min="10"/></div>
            <div class="calc-field"><label>Est. time saved</label>
              <select id="c-save"><option value="0.3">30%</option><option value="0.4">40%</option><option value="0.5" selected>50%</option><option value="0.6">60%</option><option value="0.7">70%</option></select></div>
            <div class="calc-field"><label>Tier</label>
              <select id="c-tier">
                <option value="1500,250">Starter ($1,500 setup / $250/mo)</option>
                <option value="3500,450" selected>Standard ($3,500 setup / $450/mo)</option>
                <option value="6000,750">Advanced ($6,000 setup / $750/mo)</option>
              </select>
            </div>
          </div>
          <div class="calc-results">
            <div class="calc-result"><div class="rval" id="r-hrs">—</div><div class="rlabel">Hours saved/month</div></div>
            <div class="calc-result"><div class="rval" id="r-save">—</div><div class="rlabel">Dollars saved/month</div></div>
            <div class="calc-result"><div class="rval" id="r-pay">—</div><div class="rlabel">Payback (weeks)</div></div>
            <div class="calc-result"><div class="rval" id="r-yr">—</div><div class="rlabel">Year-one return</div></div>
          </div>
          <p class="calc-note">Estimate only. Assumes your pilot confirms the time-saved percentage above.</p>
          <a href="contact.html" class="btn btn-white" id="calc-cta">Book a call to get the real number →</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Services teaser -->
<section class="section section-white">
  <div class="inner">
    <span class="tag">More ways we help</span>
    <h2>Beyond agents: courses and consultation</h2>
    <p class="sub">Not every team is ready to hand off a task to an agent. We also teach and advise.</p>
    <div class="cards">
      <div class="card">
        <div class="icon">🎓</div>
        <h3>AI Courses</h3>
        <p>Practical, hands-on courses that teach your team how to use AI tools effectively — from prompting basics to building lightweight automations without code.</p>
        <a href="services.html" style="display:inline-block;margin-top:1rem;font-size:.82rem;font-weight:700;color:var(--blue);text-decoration:none;">Learn more →</a>
      </div>
      <div class="card">
        <div class="icon">🧠</div>
        <h3>AI Consultation</h3>
        <p>Not sure where AI fits in your business? We map your workflows, identify the highest-value automation opportunities, and give you a clear, prioritized roadmap.</p>
        <a href="services.html" style="display:inline-block;margin-top:1rem;font-size:.82rem;font-weight:700;color:var(--blue);text-decoration:none;">Learn more →</a>
      </div>
      <div class="card">
        <div class="icon">🤖</div>
        <h3>Custom AI Agents</h3>
        <p>Have a specific task in mind that isn't in the catalog? We scope, build, and install a custom agent tailored to exactly how your team works.</p>
        <a href="agents.html" style="display:inline-block;margin-top:1rem;font-size:.82rem;font-weight:700;color:var(--blue);text-decoration:none;">See the catalog →</a>
      </div>
    </div>
  </div>
</section>

<!-- Pricing teaser -->
<section class="section section-light" style="text-align:center;">
  <div class="inner">
    <span class="tag">Pricing</span>
    <h2>Setup from $1,500. Care plan from $250/mo.</h2>
    <p class="sub" style="margin:0 auto 2rem;">A US automation engineer costs $90,000 to $140,000 a year. Agencies quoted one comparable custom agent at $9,500. Ours start at $1,500.</p>
    <a href="pricing.html" class="btn btn-grad">See full pricing →</a>
  </div>
</section>

<script>
(function(){
  function calc(){
    var P=+document.getElementById('c-people').value||1;
    var H=+document.getElementById('c-hours').value||1;
    var C=+document.getElementById('c-cost').value||45;
    var S=+document.getElementById('c-save').value||0.5;
    var tv=document.getElementById('c-tier').value.split(',');
    var setup=+tv[0],care=+tv[1];
    var hrs=P*H*S*4.33;
    var save=hrs*C;
    var payback=setup/((save-care)/4.33);
    var yr1=12*(save-care)-setup;
    document.getElementById('r-hrs').textContent=hrs.toFixed(0);
    document.getElementById('r-save').textContent='$'+save.toFixed(0);
    document.getElementById('r-pay').textContent=payback>0?payback.toFixed(1)+'wk':'—';
    document.getElementById('r-yr').textContent=yr1>0?'$'+Math.round(yr1).toLocaleString():'—';
    var cta=document.getElementById('calc-cta');
    cta.href='contact.html?hrs='+hrs.toFixed(0)+'&save='+save.toFixed(0);
  }
  ['c-people','c-hours','c-cost','c-save','c-tier'].forEach(function(id){
    document.getElementById(id).addEventListener('input',calc);
  });
  calc();
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
  {"name":"Custom Agent","area":"Custom","tier":"Custom","status":"available","setup":"Contact us","care":"Contact us",
   "job":"Don't see what you need? We design and build custom agents for any repeatable task your team does. If it involves pulling data, making a judgment, and writing something back, we can automate it.",
   "connects":["Your tools"],
   "you_get":"A scoped proposal, fixed price, and a working agent tailored exactly to how your team operates.",
   "safety":"All custom agents ship with the same safety rules: dry run first, pilot on 20 records, source links on every AI finding, spending caps, full audit log, and human approval before any action."},
]

def agent_card(a):
    status_pill = '<span class="pill pill-ready">Ready now</span>' if a["status"]=="ready" else '<span class="pill pill-avail">Available</span>'
    demo_link = f'<a href="demos/{a["demo"]}" class="demo-link">View sample dashboard →</a>' if a.get("demo") else ""
    connects = ", ".join(a["connects"])
    return f"""<div class="agent-card" data-area="{a['area']}" data-status="{a['status']}">
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
  <p style="margin-top:.9rem;font-size:.8rem;font-weight:700;color:var(--blue);">{a['setup']} setup · {a['care']} care</p>
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
      <button class="filter-btn" data-area="Custom" onclick="setArea(this,'Custom')">Custom</button>
    </div>
    <div class="agent-grid" id="agent-grid">
""" + "\n".join(agent_card(a) for a in AGENTS) + """
    </div>
    <p id="no-results" style="display:none;color:var(--muted);margin-top:1.5rem;">No agents match your filter.</p>
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
function setArea(btn,area){
  document.querySelectorAll('.filter-btn').forEach(function(b){b.classList.remove('active');});
  btn.classList.add('active');
  activeArea=area;
  filterAgents();
}
function filterAgents(){
  var q=document.getElementById('agent-search').value.toLowerCase();
  var cards=document.querySelectorAll('.agent-card');
  var shown=0;
  cards.forEach(function(c){
    var areaMatch=activeArea==='all'||c.dataset.area===activeArea;
    var textMatch=!q||c.textContent.toLowerCase().includes(q);
    c.style.display=(areaMatch&&textMatch)?'':'none';
    if(areaMatch&&textMatch)shown++;
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
    <p>The process, the safety rules, and what we need from you.</p>
  </div>
</div>

<!-- Process -->
<section class="section section-white">
  <div class="inner">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:start;">
      <div>
        <span class="tag">The process</span>
        <h2>Live in about two weeks</h2>
        <p class="sub">Fixed price, fixed scope. You see a measured result on 20 records before you commit to the full run.</p>
        <div class="timeline">
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">30 min — Free</div><h3>Free call and live demo</h3><p>See a live demo on sample data. Pick the task that hurts most. No commitment.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">1 to 2 days</div><h3>Proposal</h3><p>Fixed price, fixed scope, and a timeline. 50% to start, 50% at handover.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">1 hour</div><h3>Discovery interview</h3><p>We interview the people who currently do the task. Their answers become the agent's settings: scoring rules, signals, fields, tone, and exclusions.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">3 to 5 days</div><h3>Connect and pilot</h3><p>You create access keys; we connect and run on 20 records. Your team checks the top results and tells us what to tune.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">1 day</div><h3>Measure and hand over</h3><p>We time the old way against the new way, report the real time saved and cost per record, and give a 30-minute training. You pay the remaining 50%.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">Ongoing</div><h3>Care plan</h3><p>Monitoring, fixes when a connected tool changes, tuning hours (1, 2, or 3 per month by tier), and a monthly results email.</p></div>
        </div>
      </div>
      <div>
        <span class="tag">What we need from you</span>
        <h2>Three things</h2>
        <div class="cards" style="grid-template-columns:1fr;">
          <div class="card"><div class="icon">🔑</div><h3>An admin who can create access keys</h3><p>We connect through your own accounts. You control the keys and can revoke them any time.</p></div>
          <div class="card"><div class="icon">⏱️</div><h3>One hour from the people who do the task</h3><p>We need to understand how they work today — what signals matter, what exceptions they make, and what a good result looks like.</p></div>
          <div class="card"><div class="icon">📊</div><h3>Clean-enough data</h3><p>If your data needs cleanup first, we quote that separately — or start with the CRM Hygiene agent.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Safety -->
<section class="section section-dark">
  <div class="inner">
    <span class="tag">Built to be trusted</span>
    <h2>Every safety rule ships with every agent</h2>
    <p class="sub">These are not settings you can turn off. They're part of how the agent works.</p>
    <div class="trust-grid">
      <div class="trust-item"><div class="trust-icon">🧪</div><div><h4>Dry run by default</h4><p>Nothing is written or spent without a yes from your team, one step at a time.</p></div></div>
      <div class="trust-item"><div class="trust-icon">📋</div><div><h4>Pilot first</h4><p>Every agent proves itself on 20 records before running on your full list.</p></div></div>
      <div class="trust-item"><div class="trust-icon">🔗</div><div><h4>No made-up facts</h4><p>Every AI finding links to its source. Findings with no evidence are thrown out automatically before your team sees them.</p></div></div>
      <div class="trust-item"><div class="trust-icon">💰</div><div><h4>Spending caps</h4><p>Hard limits on AI usage and data credits are set in plain settings and enforced before every run.</p></div></div>
      <div class="trust-item"><div class="trust-icon">🚫</div><div><h4>Never deletes</h4><p>Agents only add or update their own fields. They back up every record before changing it.</p></div></div>
      <div class="trust-item"><div class="trust-icon">🔑</div><div><h4>You own it</h4><p>The agent runs in your accounts with your keys. We delete our copies of your data and keys at handover.</p></div></div>
      <div class="trust-item"><div class="trust-icon">📝</div><div><h4>Full paper trail</h4><p>Every run keeps a log, the results, and a backup. You can replay or audit any run.</p></div></div>
      <div class="trust-item"><div class="trust-icon">👤</div><div><h4>People decide</h4><p>Agents draft, flag, and score. Your team sends emails, pays invoices, and makes hiring decisions.</p></div></div>
    </div>
  </div>
</section>

<!-- 5-step tech detail -->
<section class="section section-white">
  <div class="inner">
    <span class="tag">Under the hood</span>
    <h2>Five steps, every time</h2>
    <p class="sub">Every agent follows the same pattern. Each step has its own safeguards.</p>
    <div class="steps">
      <div class="step">
        <div class="step-num">1</div>
        <h3>Pull</h3>
        <p>Reads data from the tools you already pay for through official APIs or exports. No new databases.</p>
      </div>
      <div class="step">
        <div class="step-num">2</div>
        <h3>Think</h3>
        <p>Claude (by Anthropic), running in your own account, does the research, reading, or judgment — the part a person used to do.</p>
      </div>
      <div class="step">
        <div class="step-num">3</div>
        <h3>Check</h3>
        <p>Rules run automatically after the AI. No source link means no claim. No real ticket means no reason. Hard rules always override the AI.</p>
      </div>
      <div class="step">
        <div class="step-num">4</div>
        <h3>Write back</h3>
        <p>Verified results go where your team already works — CRM fields, notes, Slack, or a dashboard. Only the agent's own fields are touched.</p>
      </div>
      <div class="step">
        <div class="step-num">5</div>
        <h3>Show and ask</h3>
        <p>Your team sees a dashboard and approves actions. Nothing is sent, paid, or changed without a yes.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-light" style="text-align:center;">
  <div class="inner">
    <h2>Ready to see it on your data?</h2>
    <p class="sub" style="margin:0 auto 2rem;">Book a free 30-minute call. We'll show you a live demo on sample data and pick the task that makes the most sense to start with.</p>
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
      <div class="card"><h3>Usage at cost</h3><p>You pay AI (Claude) usage and data credits (e.g. Apollo) directly to those providers. Typical AI usage is a few cents per record. We estimate them up front and measure the real number in the pilot.</p></div>
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
          <tr><td class="highlight">PlAIceholder</td><td class="highlight">from $1,500 + $250/mo</td><td></td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- ROI Calculator -->
<section class="section section-white">
  <div class="inner" style="max-width:800px;">
    <span class="tag">Estimate your return</span>
    <h2>ROI calculator</h2>
    <div class="calc-wrap">
      <h3>How much is this task costing you?</h3>
      <p class="csub">Estimate. Your pilot measures the real number.</p>
      <div class="calc-grid">
        <div class="calc-field"><label>People doing the task</label><input type="number" id="p-people" value="2" min="1"/></div>
        <div class="calc-field"><label>Hours per week each</label><input type="number" id="p-hours" value="4" min="0.5" step="0.5"/></div>
        <div class="calc-field"><label>Hourly cost (USD)</label><input type="number" id="p-cost" value="45" min="10"/></div>
        <div class="calc-field"><label>Est. time saved</label>
          <select id="p-save"><option value="0.3">30%</option><option value="0.4">40%</option><option value="0.5" selected>50%</option><option value="0.6">60%</option><option value="0.7">70%</option></select></div>
        <div class="calc-field"><label>Tier</label>
          <select id="p-tier">
            <option value="1500,250">Starter ($1,500 / $250/mo)</option>
            <option value="3500,450" selected>Standard ($3,500 / $450/mo)</option>
            <option value="6000,750">Advanced ($6,000 / $750/mo)</option>
          </select>
        </div>
      </div>
      <div class="calc-results">
        <div class="calc-result"><div class="rval" id="pr-hrs">—</div><div class="rlabel">Hours saved/month</div></div>
        <div class="calc-result"><div class="rval" id="pr-save">—</div><div class="rlabel">Dollars saved/month</div></div>
        <div class="calc-result"><div class="rval" id="pr-pay">—</div><div class="rlabel">Payback (weeks)</div></div>
        <div class="calc-result"><div class="rval" id="pr-yr">—</div><div class="rlabel">Year-one return</div></div>
      </div>
      <p class="calc-note">Estimate only. Assumes your pilot confirms the percentage above.</p>
      <a href="contact.html" class="btn btn-white">Book a call to get the real number →</a>
    </div>
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
      <details><summary>Which AI do you use?</summary><p>Claude, by Anthropic, running through your own account. You see and control the usage bill directly.</p></details>
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

<script>
(function(){
  function calc2(){
    var P=+document.getElementById('p-people').value||1;
    var H=+document.getElementById('p-hours').value||1;
    var C=+document.getElementById('p-cost').value||45;
    var S=+document.getElementById('p-save').value||0.5;
    var tv=document.getElementById('p-tier').value.split(',');
    var setup=+tv[0],care=+tv[1];
    var hrs=P*H*S*4.33;
    var save=hrs*C;
    var payback=setup/((save-care)/4.33);
    var yr1=12*(save-care)-setup;
    document.getElementById('pr-hrs').textContent=hrs.toFixed(0);
    document.getElementById('pr-save').textContent='$'+save.toFixed(0);
    document.getElementById('pr-pay').textContent=payback>0?payback.toFixed(1)+'wk':'—';
    document.getElementById('pr-yr').textContent=yr1>0?'$'+Math.round(yr1).toLocaleString():'—';
  }
  ['p-people','p-hours','p-cost','p-save','p-tier'].forEach(function(id){
    document.getElementById(id).addEventListener('input',calc2);
  });
  calc2();
})();
</script>
"""

# ─────────────────────────────────────────────────────────────────────────────
# SERVICES
# ─────────────────────────────────────────────────────────────────────────────
SERVICES_BODY = """
<div class="page-banner">
  <div class="page-banner-inner">
    <h1>Services</h1>
    <p>AI agents, courses, and consultation — whatever stage your team is at, we have a way to help.</p>
  </div>
</div>

<section class="section section-white">
  <div class="inner">
    <span class="tag">What we offer</span>
    <h2>Three ways to work with us</h2>
    <p class="sub">Start with a consultation, upskill your team with a course, or go straight to a custom agent. Most clients do more than one.</p>
    <div class="cards" style="grid-template-columns:repeat(auto-fit,minmax(300px,1fr));">
      <div class="card">
        <div class="icon">🤖</div>
        <h3>Custom AI Agents</h3>
        <p>We design, build, and install a custom AI agent that automates a specific repeatable task inside the tools you already use. Fixed price, two-week delivery, pilot on 20 records before full deployment.</p>
        <ul class="checklist" style="margin-top:.75rem;">
          <li>From $1,500 setup</li>
          <li>Care plans from $250/month</li>
          <li>HubSpot, Salesforce, Zendesk, QuickBooks, and more</li>
          <li>14 agents in the catalog, or fully custom</li>
        </ul>
        <a href="agents.html" class="btn btn-grad" style="display:inline-block;margin-top:1.25rem;">See the catalog →</a>
      </div>
      <div class="card">
        <div class="icon">🎓</div>
        <h3>AI Courses</h3>
        <p>Practical, hands-on training that teaches your team how to use AI tools in their actual daily work — not theory, not hype. We focus on what saves real time.</p>
        <ul class="checklist" style="margin-top:.75rem;">
          <li>Prompting fundamentals for non-technical staff</li>
          <li>Using AI inside your CRM, help desk, and spreadsheets</li>
          <li>Building lightweight automations without code</li>
          <li>Live workshops (remote or on-site) or self-paced modules</li>
        </ul>
        <a href="contact.html" class="btn btn-dark" style="display:inline-block;margin-top:1.25rem;">Book a call to learn more →</a>
      </div>
      <div class="card">
        <div class="icon">🧠</div>
        <h3>AI Consultation</h3>
        <p>Not sure where AI fits in your business? We spend time with your team, map your workflows, and deliver a clear, prioritized roadmap — with honest advice on what's worth automating and what isn't.</p>
        <ul class="checklist" style="margin-top:.75rem;">
          <li>Workflow mapping and opportunity audit</li>
          <li>Prioritized automation roadmap</li>
          <li>Tool and vendor recommendations</li>
          <li>Ongoing advisory retainer available</li>
        </ul>
        <a href="contact.html" class="btn btn-dark" style="display:inline-block;margin-top:1.25rem;">Book a call to learn more →</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-light">
  <div class="inner">
    <span class="tag">AI Courses</span>
    <h2>What we teach</h2>
    <p class="sub">Every course is built around real tasks — things your team actually does every week.</p>
    <div class="cards">
      <div class="card">
        <div class="icon">✍️</div>
        <h3>Prompting Fundamentals</h3>
        <p>How to write instructions that get consistent, useful results from AI tools. Covers structure, tone, examples, and common mistakes. Half-day workshop.</p>
      </div>
      <div class="card">
        <div class="icon">📊</div>
        <h3>AI for Sales Teams</h3>
        <p>Using AI to research prospects, draft follow-ups, prep for meetings, and write CRM notes. Built around HubSpot and Salesforce workflows.</p>
      </div>
      <div class="card">
        <div class="icon">🎧</div>
        <h3>AI for Customer Success</h3>
        <p>Triaging tickets, summarizing customer history, spotting risk signals, and drafting renewal conversations — all with AI assistance.</p>
      </div>
      <div class="card">
        <div class="icon">⚙️</div>
        <h3>No-Code Automations</h3>
        <p>Building simple automations with tools like Make, Zapier, and Claude — without writing code. For ops and admin staff who want to connect the tools they already use.</p>
      </div>
    </div>
    <p style="margin-top:1.75rem;color:var(--muted);font-size:.9rem;">All courses available as remote workshops, on-site sessions, or self-paced recorded modules. <a href="contact.html" style="color:var(--blue);font-weight:600;">Contact us for scheduling and pricing →</a></p>
  </div>
</section>

<section class="section section-white">
  <div class="inner">
    <span class="tag">AI Consultation</span>
    <h2>What a consultation looks like</h2>
    <p class="sub">We spend time understanding your business before we recommend anything.</p>
    <div class="timeline" style="max-width:680px;">
      <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">Week 1</div><h3>Workflow interviews</h3><p>We interview the people doing the work — sales, ops, CS, finance. We learn what they actually do each week, where time goes, and what frustrates them most.</p></div>
      <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">Week 2</div><h3>Opportunity mapping</h3><p>We map every repeatable task against three criteria: time cost, AI suitability, and implementation risk. This becomes your automation opportunity map.</p></div>
      <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">Delivery</div><h3>Prioritized roadmap</h3><p>A written report with your top 3 to 5 automation opportunities ranked by expected ROI, an honest assessment of complexity, and a recommended starting point.</p></div>
      <div class="tl-item"><div class="tl-dot"></div><div class="tl-label">Optional</div><h3>Ongoing advisory</h3><p>Monthly retainer for teams that want a dedicated AI advisor to evaluate new tools, review prompt quality, and help prioritize the roadmap as the business changes.</p></div>
    </div>
  </div>
</section>

<section class="section section-dark" style="text-align:center;">
  <div class="inner">
    <h2>Not sure which service fits?</h2>
    <p class="sub" style="margin:0 auto 2rem;">Book a free 30-minute call. We'll ask a few questions and give you a straight answer on what makes the most sense to start with.</p>
    <a href="contact.html" class="btn btn-white">Book a free call →</a>
  </div>
</section>
"""

# ─────────────────────────────────────────────────────────────────────────────
# CASE STUDY
# ─────────────────────────────────────────────────────────────────────────────
CASE_BODY = """
<div class="page-banner">
  <div class="page-banner-inner">
    <h1>Case Study: Signal Engine</h1>
    <p>The first build. A sales prospecting agent for a software escrow company. Pilot in progress.</p>
  </div>
</div>

<section class="section section-white">
  <div class="inner">
    <div class="cs-grid">
      <div>
        <span class="tag">The project</span>
        <h2>A prospecting agent built in four days</h2>
        <p style="color:var(--muted);margin-bottom:1rem;">Client: [Case Study Client], a software and IP escrow company.</p>
        <p style="color:var(--muted);margin-bottom:1rem;">An agency quoted $9,500 for 60 hours of custom development plus $1,500 for a month of support, over five weeks.</p>
        <p style="color:var(--muted);margin-bottom:1.5rem;">We built a working, packaged agent in four days. The client sets it up with four commands.</p>

        <span class="tag">What it does</span>
        <h2>How the agent works</h2>
        <div class="timeline" style="margin-top:1rem;">
          <div class="tl-item"><div class="tl-dot"></div><h3>Pulls target companies from Apollo</h3><p>Filtered by industry, size, and other criteria set in the discovery interview.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><h3>Researches recent news at half price</h3><p>AI batch processing cuts the cost of researching hundreds of companies at once.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><h3>Throws out unverified links</h3><p>Any news link the AI didn't actually find is discarded automatically before scoring.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><h3>Scores companies with editable rules</h3><p>The scoring criteria — which signals matter most — are set by the client and can be changed without code.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><h3>Finds verified contacts within a credit cap</h3><p>Apollo email reveals are capped per run, set in plain settings.</p></div>
          <div class="tl-item"><div class="tl-dot"></div><h3>Writes to HubSpot and builds a rep dashboard</h3><p>Score, tier, reasons, source links, and contacts go straight into HubSpot. Reps see a "who to call this week" dashboard.</p></div>
        </div>
      </div>
      <div>
        <span class="tag">Status</span>
        <h2>Pilot in progress</h2>
        <div class="cs-stats">
          <div class="cs-stat"><span class="n">4</span><span class="l">days to build</span></div>
          <div class="cs-stat"><span class="n">4</span><span class="l">commands to set up</span></div>
          <div class="cs-stat"><span class="n">$9,500</span><span class="l">agency quote for the same agent</span></div>
          <div class="cs-stat"><span class="n">$6,000</span><span class="l">our price (Advanced tier)</span></div>
        </div>

        <div class="pending-block">
          <strong>Results: coming after the pilot.</strong><br/><br/>
          The agent is running on real accounts. We will publish time saved per week, cost per verified lead, and the before/after comparison once the client has approved the numbers in writing.<br/><br/>
          We do not show percentages or time saved until real numbers are measured.
        </div>

        <div class="card" style="margin-top:1.25rem;">
          <div class="icon">🔍</div>
          <h3>Try the sample dashboard</h3>
          <p>The demo shows how reps see the output — score, tier, reasons, and talk tracks — on fictional companies.</p>
          <a href="demos/signal-prospector-dashboard.html" style="display:inline-block;margin-top:.9rem;font-size:.85rem;font-weight:700;color:var(--blue);text-decoration:none;">View sample dashboard →</a>
        </div>

        <div class="card" style="margin-top:1rem;">
          <h3>Want a similar agent?</h3>
          <p>Book a free 30-minute call. We'll demo Signal Prospector live on sample data and talk through whether it fits your sales motion.</p>
          <a href="contact.html" class="btn btn-grad" style="margin-top:1rem;display:inline-block;">Book a free call →</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-light" style="text-align:center;">
  <div class="inner">
    <span class="tag">Proof policy</span>
    <h2>We don't invent results</h2>
    <p class="sub" style="margin:0 auto;">No invented testimonials, star ratings, or client logos. Sample dashboards are labeled with fictional data. Real results and quotes are added only once a client approves them in writing.</p>
  </div>
</section>
"""

# ─────────────────────────────────────────────────────────────────────────────
# CONTACT
# ─────────────────────────────────────────────────────────────────────────────
TOOLS_LIST = ["HubSpot","Salesforce","Apollo","Zendesk","Slack","QuickBooks","Other"]
AGENT_LIST = ["Signal Prospector","Inbound Lead Researcher","CRM Hygiene","Deal Follow-up Drafter",
              "Meeting Prep Briefs","Renewal Risk Radar","Support Ticket Triage","Customer Onboarding Tracker",
              "Invoice Checker","Resume Screener","Weekly KPI Writer","Competitor Watch",
              "RFP and Questionnaire Drafter","Not sure yet"]

tools_cbs = "\n".join(f'<label class="cb-label"><input type="checkbox" name="tools" value="{t}"/> {t}</label>' for t in TOOLS_LIST)
agent_opts = "\n".join(f'<option>{a}</option>' for a in AGENT_LIST)

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
        <h2>Free call, no commitment</h2>
        <p>In 30 minutes we'll show you a live demo on sample data, talk through your biggest time sink, and give you a straight answer on whether an agent can help.</p>
        <div class="chip"><span class="ic">📅</span><span><a href="[Booking Link]" style="color:var(--blue);font-weight:600;">[Booking Link]</a></span></div>
        <div class="chip"><span class="ic">📧</span><span>[Contact Email]</span></div>
      </div>
      <form class="contact-form" onsubmit="handleSubmit(event)">
        <div class="frow">
          <input type="text" name="name" placeholder="Your name" required/>
          <input type="email" name="email" placeholder="Work email" required/>
        </div>
        <div class="frow">
          <input type="text" name="company" placeholder="Company name" required/>
          <select name="size">
            <option value="" disabled selected>Company size</option>
            <option>1 to 10</option>
            <option>11 to 50</option>
            <option>51 to 200</option>
            <option>200+</option>
          </select>
        </div>
        <fieldset>
          <legend>Tools you use</legend>
          <div class="cbgroup">
            {tools_cbs}
          </div>
        </fieldset>
        <textarea name="task" placeholder="What slow task would you hand to an agent?" required></textarea>
        <select name="agent">
          <option value="" disabled selected>Which agent are you interested in?</option>
          {agent_opts}
        </select>
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
      <div class="icon" style="margin:0 auto 1.25rem;">📊</div>
      <h2 style="font-size:1.3rem;margin-bottom:.75rem;">Live demo dashboard</h2>
      <p style="color:var(--muted);margin-bottom:1.5rem;">The interactive sample dashboard for this agent will appear here once the demo files are installed. Add <code>agent-kit/samples/</code> to this folder to enable it.</p>
      <a href="contact.html" class="btn btn-grad">Book a call to see a live demo →</a>
    </div>
  </div>
</section>
{FOOTER}
</body>
</html>"""

# ─────────────────────────────────────────────────────────────────────────────
# Build
# ─────────────────────────────────────────────────────────────────────────────
pages = {
    "index.html": page(
        "PlAIceholder — AI agents for growing companies",
        "Custom-built AI agents for companies with 10 to 200 employees. Designed, installed, and proven in two weeks.",
        "home", HOME_BODY),
    "agents.html": page(
        "Agent Catalog — PlAIceholder",
        "13 custom-built AI agents for sales, customer success, back office, and marketing. Three are ready now with live demos.",
        "agents", AGENTS_BODY),
    "services.html": page(
        "Services — PlAIceholder",
        "AI courses, consultation, and custom agents. Three ways to help your team get more from AI.",
        "services", SERVICES_BODY),
    "how-it-works.html": page(
        "How It Works — PlAIceholder",
        "The five-step process, the two-week timeline, and every safety rule — explained plainly.",
        "how", HOW_BODY),
    "pricing.html": page(
        "Pricing — PlAIceholder",
        "Setup from $1,500. Care plan from $250/month. Fixed price, fixed scope. ROI calculator included.",
        "pricing", PRICING_BODY),
    "case-study.html": page(
        "Case Study: Signal Engine — PlAIceholder",
        "A sales prospecting agent built in four days for a software escrow company. Pilot in progress.",
        "case", CASE_BODY),
    "contact.html": page(
        "Book a Call — PlAIceholder",
        "Book a free 30-minute call. Live demo, no commitment.",
        "contact", CONTACT_BODY),
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

print("\nDone. Placeholders still to fill:")
print("  PlAIceholder  — company name")
print("  [Founder Name]   — your name (for About section)")
print("  [Contact Email]  — where leads should go")
print("  [Booking Link]   — Calendly or Cal.com link")
print("  [Case Study Client] — 'Praxis Escrow' with their OK, or 'a software escrow company'")
