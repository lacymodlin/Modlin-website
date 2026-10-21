#!/usr/bin/env python3
"""Builds the Modlin Designs site into ../site from the parts in this folder.
Run: python3 build.py   (then deploy the site/ folder)."""
import os, re, shutil, json, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from projects import PROJECTS
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(HERE,'..','site')
P=lambda n: open(os.path.join(HERE,n)).read()
A=os.path.join(HERE,'assets')

DISCOVERY='https://calendar.app.google/HnmJ462Fce4tVTCG9'
SITE='https://modlindesigns.com'
INSTAGRAM='https://www.instagram.com/modlindesigns/'

def page(title, desc, body, path='/', image='/assets/img/og-image.jpg', jsonld=None, noindex=False, og_type='website'):
    ld=''.join(f'<script type="application/ld+json">{json.dumps(j,ensure_ascii=False)}</script>\n' for j in (jsonld or []))
    robots='<meta name="robots" content="noindex">\n' if noindex else ''
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{robots}<link rel="canonical" href="{SITE}{path}">
<meta name="theme-color" content="#1B2A4A">
<meta property="og:site_name" content="Modlin Designs">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}{image}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}{image}">
{ld}
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito+Sans:ital,opsz,wght@0,6..12,400;0,6..12,600;0,6..12,700;0,6..12,800;1,6..12,400&display=swap">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
{P('part-sprite.html')}
<header>
  <div class="wrap nav">
    <a class="brand" href="/" aria-label="Modlin Designs home"><svg><use href="#logo"/></svg>Modlin Designs</a>
    <ul>
      <li><a href="/#work">Work</a></li>
      <li><a href="/#services">Services</a></li>
      <li><a href="/#about">About</a></li>
      <li><a href="/#reviews">Reviews</a></li>
    </ul>
    <a class="btn btn-fill" href="/#inquire">Start your inquiry</a>
  </div>
</header>
{body}
<footer class="foot">
  <svg class="sprig" width="100%" height="100%" aria-hidden="true" style="position:absolute;inset:0;opacity:.12"><rect width="100%" height="100%" fill="url(#sprig)"/></svg>
  <div class="wrap">
    <a class="brand" href="/"><svg><use href="#logo"/></svg>Modlin Designs</a>
    <nav><a href="/#work">Work</a><a href="/#services">Services</a><a href="/#about">About</a><a href="/#inquire">Inquire</a><a href="{INSTAGRAM}" rel="noopener me" target="_blank">Instagram</a></nav>
    <small>lacy@modlindesigns.com · © 2026 Modlin Designs</small>
  </div>
</footer>
</body>
</html>
'''

FORM='''<form name="inquiry" method="POST" action="/thanks/" data-netlify="true" netlify-honeypot="company_website">
        <input type="hidden" name="form-name" value="inquiry">
        <p class="hp"><label>Leave this empty <input name="company_website" tabindex="-1" autocomplete="off"></label></p>
        <div class="f"><label for="name">Your name</label><input id="name" name="Contact Name" autocomplete="name" required></div>
        <div class="f"><label for="email">Email</label><input id="email" name="Email" type="email" autocomplete="email" required></div>
        <div class="f"><label for="biz">Business name</label><input id="biz" name="Business name" autocomplete="organization" required></div>
        <div class="f"><label for="phone">Phone number <span style="font-weight:400">(optional)</span></label><input id="phone" name="Phone number" type="tel" autocomplete="tel"></div>
        <div class="f full"><label for="about-biz">Tell me about your business</label><textarea id="about-biz" name="Tell me about your business" required></textarea></div>
        <div class="f full"><label for="services">What services do you need?</label><input id="services" name="What services do you need?" required></div>
        <div class="f full"><span class="lbl">Budget</span>
          <div class="chips">
            <label><input type="checkbox" name="Budget" value="$2800 – $4000">$2800 – $4000</label>
            <label><input type="checkbox" name="Budget" value="$4000 – $6000">$4000 – $6000</label>
            <label><input type="checkbox" name="Budget" value="$6000 – $9000">$6000 – $9000</label>
          </div>
        </div>
        <div class="f full"><span class="lbl">How did you hear about me?</span>
          <div class="chips">
            <label><input type="radio" name="How did you hear about me?" value="Social media ad">Social media ad</label>
            <label><input type="radio" name="How did you hear about me?" value="Instagram">Instagram</label>
            <label><input type="radio" name="How did you hear about me?" value="TikTok">TikTok</label>
            <label><input type="radio" name="How did you hear about me?" value="Facebook">Facebook</label>
            <label><input type="radio" name="How did you hear about me?" value="Google search">Google search</label>
            <label><input type="radio" name="How did you hear about me?" value="My website">My website</label>
            <label><input type="radio" name="How did you hear about me?" value="Referral / word of mouth">Referral / word of mouth</label>
            <label><input type="radio" name="How did you hear about me?" value="Other">Other</label>
          </div>
        </div>
        <button class="btn btn-fill" type="submit">Send inquiry</button>
      </form>'''

def esc(t): return html.escape(t, quote=True)

def project_page(p, nxt):
    img = lambda f: f"/assets/projects/{p['slug']}/{f}"
    meta = ''.join(f'<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k, v in p['meta'])
    story = ''.join(f'<div class="story-row"><h2>{esc(h)}</h2><p>{esc(t)}</p></div>' for h, t in p['story'])
    gal = ''.join(f'<div class="shot {lay}"><img src="{img(f)}" alt="{esc(a)}" loading="lazy"></div>' for f, a, lay in p['gallery'])
    quote = ''
    if p.get('review'):
        q, who = p['review']
        quote = f'<section class="case-quote"><div class="stars" aria-label="5 stars">★★★★★</div><blockquote>{esc(q)}</blockquote><footer>{esc(who)}</footer></section>'
    nxt_link = f'<a href="/projects/{nxt["slug"]}/" style="text-align:right"><span>Next project</span>{esc(nxt["title"])}</a>' if nxt else ''
    return f"""<main><div class="wrap">
    <section class="case-hero">
      <p class="crumb"><a href="/#work">Work</a><span>/</span><span>{esc(p['title'])}</span></p>
      <p class="eyebrow">{esc(p['category'])}</p>
      <h1>{esc(p['title'])}</h1>
      <p class="lede">{esc(p['summary'])}</p>
      <dl class="meta">{meta}</dl>
    </section>
    <div class="shot wide"><img src="{img(p['cover'][0])}" alt="{esc(p['cover'][1])}"></div>
    <section class="story">{story}</section>
    <div class="gallery">{gal}</div>
    {quote}
    <section class="cta-band" style="margin-top:clamp(48px,7vw,88px)">
      <svg class="sprig" width="100%" height="100%" aria-hidden="true"><rect width="100%" height="100%" fill="url(#sprig)"/></svg>
      <p class="eyebrow" style="color:var(--ivory)">Your brand next</p>
      <h2>Love how this turned out? Let's make yours next.</h2>
      <p>Tell me about your brand and I'll get back to you personally. If we're a fit, you'll get a link to a free 15-minute discovery call.</p>
      <div class="btns"><a class="btn" href="/#inquire">Start your inquiry</a><a class="btn ghost" href="/#services">See packages</a></div>
    </section>
    <nav class="next" aria-label="More projects"><a href="/#work"><span>Back</span>All work</a>{nxt_link}</nav>
  </div></main>"""

def work_cards(total=0):
    cards = [f'<a class="proj" href="/projects/{p["slug"]}/"><div class="cover"><img src="/assets/projects/{p["slug"]}/{p["card"]}" alt="{esc(p["title"])} project cover" loading="lazy"></div><h3>{esc(p["title"])}</h3><span>{esc(p["card_tags"])}</span></a>' for p in PROJECTS]
    while len(cards) < total:
        cards.append('<div class="proj"><div class="cover"><div class="slot">Project cover</div></div><h3>Project title</h3><span>Coming soon</span></div>')
    return '\n        '.join(cards)

def build():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT+'/assets/fonts'); os.makedirs(OUT+'/assets/img')
    shutil.copy(os.path.join(HERE,'site.css'),OUT+'/assets/site.css')
    shutil.copy(A+'/MontHeavy.otf',OUT+'/assets/fonts/MontHeavy.otf')
    shutil.copy(A+'/email-header.png',OUT+'/assets/img/email-header.png')
    for f in os.listdir(A+'/img'): shutil.copy(A+'/img/'+f,OUT+'/assets/img/'+f)
    logo=open(A+'/logo.svg').read().replace('stroke: #000;','stroke: #B5543A; fill: #B5543A;')
    open(OUT+'/assets/img/favicon.svg','w').write(logo)

    home=P('part-home.html')
    home=re.sub(r'<form id="inq".*?</form>',FORM,home,flags=re.S)
    home=re.sub(r'<div class="work-grid">.*?</div>\n    </div>\n  </section>', lambda m: '<div class="work-grid">\n        '+work_cards()+'\n      </div>\n    </div>\n  </section>', home, count=1, flags=re.S)
    home=home.replace(' <a href="#case" style="color:var(--terra);font-weight:700">See the project page</a>','')
    home=home.replace('<a class="btn" href="#reviews">Read all reviews on Google</a>','<a class="btn" href="GOOGLE_REVIEWS_URL" rel="noopener">Read all reviews on Google</a>')
    home=home.replace('href="#inquire"','href="/#inquire"').replace('href="#work"','href="/#work"')
    home='<main id="top">'+home+'</main>'
    w=lambda rel,html: (os.makedirs(os.path.dirname(OUT+'/'+rel),exist_ok=True), open(OUT+'/'+rel,'w').write(html))
    biz={"@context":"https://schema.org","@type":"ProfessionalService","@id":SITE+"/#business","name":"Modlin Designs","url":SITE+"/",
        "logo":SITE+"/assets/img/favicon.svg","image":SITE+"/assets/img/og-image.jpg","email":"lacy@modlindesigns.com",
        "description":"Brand identity and packaging design for natural skincare, cosmetics and wellness brands.",
        "address":{"@type":"PostalAddress","addressLocality":"Newbury Park","addressRegion":"CA","addressCountry":"US"},
        "areaServed":"United States","priceRange":"$$$","founder":{"@id":SITE+"/#lacy"},"sameAs":[INSTAGRAM],
        "knowsAbout":["Brand identity design","Packaging design","Logo design","Skincare branding","Cosmetics branding","Brand strategy"]}
    person={"@context":"https://schema.org","@type":"Person","@id":SITE+"/#lacy","name":"Lacy Modlin","jobTitle":"Brand Designer","worksFor":{"@id":SITE+"/#business"},"url":SITE+"/#about","sameAs":[INSTAGRAM]}
    site={"@context":"https://schema.org","@type":"WebSite","name":"Modlin Designs","url":SITE+"/"}
    w('index.html',page('Modlin Designs | Brand & Packaging Designer for Natural Beauty Brands',
        'Lacy Modlin designs brand identities and packaging for natural skincare, cosmetics and wellness brands. Strategy-led branding packages from $2,700.',home,
        jsonld=[biz,person,site]))

    for i,p in enumerate(PROJECTS):
        shutil.copytree(os.path.join(A,'projects',p['slug']),OUT+'/assets/projects/'+p['slug'])
        nxt=PROJECTS[(i+1)%len(PROJECTS)] if len(PROJECTS)>1 else None
        path=f"/projects/{p['slug']}/"
        desc=p['summary'] if len(p['summary'])<=158 else p['summary'][:155].rsplit(' ',1)[0]+'…'
        work={"@context":"https://schema.org","@type":"CreativeWork","name":p['title'],"headline":f"{p['title']}: {p['category']}","description":p['summary'],
              "url":SITE+path,"image":SITE+f"/assets/projects/{p['slug']}/{p['cover'][0]}","genre":p['category'],
              "creator":{"@type":"Person","name":"Lacy Modlin","url":SITE+"/#about"},"publisher":{"@type":"Organization","name":"Modlin Designs","url":SITE+"/"}}
        crumbs={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
              {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
              {"@type":"ListItem","position":2,"name":"Work","item":SITE+"/#work"},
              {"@type":"ListItem","position":3,"name":p['title'],"item":SITE+path}]}
        w(f"projects/{p['slug']}/index.html",page(f"{p['title']} {p.get('seo_title','Brand Design')} | Modlin Designs",desc,project_page(p,nxt),
            path=path,image=f"/assets/projects/{p['slug']}/{p['cover'][0]}",jsonld=[work,crumbs],og_type='article'))

    thanks=f'''<main><div class="wrap"><section class="simple">
<p class="eyebrow">Inquiry received</p><h1>Thank you! I'll be in touch soon.</h1>
<p>Keep an eye on your inbox for a note from lacy@modlindesigns.com. In the meantime, feel free to look through more of my work.</p>
<a class="btn btn-fill" href="/#work">See my work</a></section></div></main>'''
    w('thanks/index.html',page('Thank you | Modlin Designs','Your inquiry was sent.',thanks,path='/thanks/',noindex=True))
    nf='''<main><div class="wrap"><section class="simple"><p class="eyebrow">Page not found</p><h1>This page wandered off.</h1>
<p>Let's get you back on track.</p><a class="btn btn-fill" href="/">Go to the home page</a></section></div></main>'''
    w('404.html',page('Page not found | Modlin Designs','Page not found.',nf,noindex=True))
    w('robots.txt','User-agent: *\nAllow: /\nSitemap: https://modlindesigns.com/sitemap.xml\n')
    import datetime; today=datetime.date.today().isoformat()
    urls=['/']+[f"/projects/{p['slug']}/" for p in PROJECTS]
    w('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{SITE}{u}</loc><lastmod>{today}</lastmod></url>\n' for u in urls)+'</urlset>\n')

if __name__=='__main__': build(); print('built',OUT)
