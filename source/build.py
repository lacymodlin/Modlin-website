#!/usr/bin/env python3
"""Builds the Modlin Designs site into ../site from the parts in this folder.
Run: python3 build.py   (then deploy the site/ folder)."""
import os, re, shutil, json
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(HERE,'..','site')
P=lambda n: open(os.path.join(HERE,n)).read()
A=os.path.join(HERE,'assets')

DISCOVERY='https://calendar.app.google/HnmJ462Fce4tVTCG9'

def page(title, desc, body, path_depth=0):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
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
    <nav><a href="/#work">Work</a><a href="/#services">Services</a><a href="/#about">About</a><a href="/#inquire">Inquire</a><a href="BEHANCE_URL" rel="noopener">Behance</a><a href="INSTAGRAM_URL" rel="noopener">Instagram</a></nav>
    <small>lacy@modlindesigns.com · © 2026 Modlin Designs</small>
  </div>
</footer>
</body>
</html>
'''

FORM='''<form name="inquiry" method="POST" action="/thanks/" data-netlify="true" netlify-honeypot="company_website">
        <input type="hidden" name="form-name" value="inquiry">
        <p class="hp"><label>Leave this empty <input name="company_website" tabindex="-1" autocomplete="off"></label></p>
        <div class="f"><label for="name">Your name</label><input id="name" name="name" autocomplete="name" required></div>
        <div class="f"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
        <div class="f full"><label for="biz">Business name</label><input id="biz" name="business_name" required></div>
        <div class="f full"><label for="about-biz">Tell me about your business</label><textarea id="about-biz" name="about_business" required></textarea></div>
        <div class="f full"><span class="lbl">What services do you need?</span>
          <div class="chips">
            <label><input type="checkbox" name="services[]" value="Brand identity">Brand identity</label>
            <label><input type="checkbox" name="services[]" value="Packaging design">Packaging design</label>
            <label><input type="checkbox" name="services[]" value="Launch campaign">Launch campaign</label>
            <label><input type="checkbox" name="services[]" value="Website">Website</label>
            <label><input type="checkbox" name="services[]" value="Not sure yet">Not sure yet</label>
          </div>
        </div>
        <div class="f full"><label for="why">What's prompting you to reach out now?</label><textarea id="why" name="reason"></textarea></div>
        <div class="f full"><span class="lbl">Budget</span>
          <div class="chips">
            <label><input type="radio" name="budget" value="Under $2700">Under $2,700</label>
            <label><input type="radio" name="budget" value="$2700 to $4800">$2,700 to $4,800</label>
            <label><input type="radio" name="budget" value="$4800 to $8000">$4,800 to $8,000</label>
            <label><input type="radio" name="budget" value="$8000+">$8,000+</label>
          </div>
        </div>
        <div class="f full"><label for="heard">How did you hear about me?</label><input id="heard" name="heard_about"></div>
        <button class="btn btn-fill" type="submit">Send inquiry</button>
      </form>'''

def build():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT+'/assets/fonts'); os.makedirs(OUT+'/assets/img')
    shutil.copy(os.path.join(HERE,'site.css'),OUT+'/assets/site.css')
    shutil.copy(A+'/MontHeavy.otf',OUT+'/assets/fonts/MontHeavy.otf')
    shutil.copy(A+'/email-header.png',OUT+'/assets/img/email-header.png')
    logo=open(A+'/logo.svg').read().replace('stroke: #000;','stroke: #B5543A; fill: #B5543A;')
    open(OUT+'/assets/img/favicon.svg','w').write(logo)

    home=P('part-home.html')
    home=re.sub(r'<form id="inq".*?</form>',FORM,home,flags=re.S)
    home=home.replace('href="#case"','href="/projects/sample-project/"')
    home=home.replace('<a class="btn" href="#reviews">Read all reviews on Google</a>','<a class="btn" href="GOOGLE_REVIEWS_URL" rel="noopener">Read all reviews on Google</a>')
    home=home.replace('href="#inquire"','href="/#inquire"').replace('href="#work"','href="/#work"')
    home='<main id="top">'+home+'</main>'
    w=lambda rel,html: (os.makedirs(os.path.dirname(OUT+'/'+rel),exist_ok=True), open(OUT+'/'+rel,'w').write(html))
    w('index.html',page('Modlin Designs | Branding & Packaging for Natural Beauty Brands',
        'Brand identity and packaging design for clean skincare, cosmetics and wellness founders. Packages from $2,700.',home))

    case=P('part-case.html').replace('href="#inquire"','href="/#inquire"').replace('href="#services"','href="/#services"').replace('href="#work"','href="/#work"').replace('href="#case"','href="/#work"')
    w('projects/sample-project/index.html',page('Project name | Modlin Designs','Brand identity and packaging case study by Modlin Designs.','<main>'+case+'</main>'))

    thanks=f'''<main><div class="wrap"><section class="simple">
<p class="eyebrow">Inquiry received</p><h1>Thank you! I'll be in touch soon.</h1>
<p>Keep an eye on your inbox for a note from lacy@modlindesigns.com. In the meantime, feel free to look through more of my work.</p>
<a class="btn btn-fill" href="/#work">See my work</a></section></div></main>'''
    w('thanks/index.html',page('Thank you | Modlin Designs','Your inquiry was sent.',thanks))
    nf='''<main><div class="wrap"><section class="simple"><p class="eyebrow">Page not found</p><h1>This page wandered off.</h1>
<p>Let's get you back on track.</p><a class="btn btn-fill" href="/">Go to the home page</a></section></div></main>'''
    w('404.html',page('Page not found | Modlin Designs','Page not found.',nf))
    w('robots.txt','User-agent: *\nAllow: /\nSitemap: https://modlindesigns.com/sitemap.xml\n')
    w('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n<url><loc>https://modlindesigns.com/</loc></url>\n</urlset>\n')

if __name__=='__main__': build(); print('built',OUT)
