"""Portfolio projects. Each one becomes /projects/<slug>/ and a card in the Work section.
Images live in source/assets/projects/<slug>/.
gallery items: (file, alt text, "wide" or "half")."""

PROJECTS = [
    {
        "slug": "a-purple-house",
        "title": "A Purple House",
        "category": "Logo suite & brand identity",
        "card_tags": "Logo suite · Brand identity",
        "summary": "A Bay Area maker of crochet patterns and curious handmade goods, named after her very real, very purple house. She needed a brand that looked professional at markets and schools without losing its playful streak.",
        "meta": [
            ("Client", "Crochet patterns & handmade goods"),
            ("Services", "Logo suite, color palette, font pairing"),
            ("Deliverables", "Brand sheet, files in every format"),
            ("Year", "2026"),
        ],
        "cover": ("cover.jpg", "The A Purple House wordmark in lilac on deep plum"),
        "card": "card.jpg",
        "story": [
            ("The challenge", "The business started with crochet pieces for friends and family and grew into markets and work with local schools and businesses. Its old logo was a traced photo of the purple house itself. It needed something professional that still felt a little unexpected, stayed timeless instead of trendy, read clearly at favicon size, and could stretch to new product lines later."),
            ("The approach", "I started with the symbol, since the mark had to work without words. The house roofline doubles as a lidded jar, a nod to the curated oddities the shop is known for, and negative space forms the door. For the type, I chose a bold, all-caps serif that is easy to read and feels a bit like a vintage poster. The palette keeps it to two colors: lilac on deep plum, with black for sticker-style outlines."),
            ("The result", "A complete logo suite in four color versions, plus a palette, a font pairing and a one-page brand sheet. Every file came in JPG, PNG, SVG and AI, ready for pattern PDFs, product labels, market signage and Instagram."),
        ],
        "gallery": [
            ("product-mockup.jpg", "A Purple House branding on an apothecary jar label, a crochet pattern sleeve and a business card", "half"),
            ("stickers.jpg", "The logo mark and wordmark as die-cut stickers with black outlines", "half"),
            ("logo-suite.jpg", "The logo suite in four versions: wordmark on plum, mark on black, mark on lilac and wordmark on white", "wide"),
            ("palette-type.jpg", "The color palette of lilac, deep plum and black, with DM Serif Display type samples", "half"),
            ("scale-test.jpg", "The house mark shown from 320 pixels down to a 16 pixel favicon", "half"),
        ],
        "review": None,  # ("quote", "Name, Business")
    },
    {
        "slug": "the-road-continues",
        "title": "The Road Continues",
        "category": "Nonprofit rebrand & print collateral",
        "card_tags": "Website · Print · Presentations",
        "summary": "A 501(c)(3) that gives women professional clothing for interviews, court dates, new jobs and fresh starts. Over several projects I pulled its website, print pieces and presentations into one consistent look built around a single image: an open road at sunrise.",
        "meta": [
            ("Client", "Nonprofit, Women Helping Women"),
            ("Services", "Website refresh, print design, presentations"),
            ("Deliverables", "Website, postcards, table sign, business cards, donation receipts, slide decks"),
        ],
        "cover": ("cover.jpg", "The Road Continues postcard and tabletop sign, both featuring a sunlit open road with gold type"),
        "card": "card.jpg",
        "story": [
            ("The challenge", "The founder didn't want a logo. She wanted one photo, a quiet road heading into the sunrise, to carry the brand, because it says exactly what the organization does: helps women keep going. Her materials had grown piece by piece, so the website, handouts and decks didn't feel like they came from the same place."),
            ("The approach", "With no logo to lean on, consistency had to come from everything else. I let the road photo do the heavy lifting on every printed piece and paired it with two colors pulled from it, a warm gold and a deep charcoal, plus the same clean sans-serif type throughout. The mission line, \"When a woman looks confident, she feels confident,\" shows up wherever there is room for it, and QR codes connect each print piece back to the website and donations."),
            ("The result", "A refreshed website and a full family of materials that read as one organization: postcards, a tabletop sign for donation drives, business cards, a branded donation receipt with the tax ID donors need, and presentation decks for events like National Women's History Month, all ready as it expands beyond California."),
        ],
        "gallery": [
            ("website.jpg", "The Road Continues website homepage with an Empowering Women headline beside the road photo", "wide"),
            ("web-about.jpg", "The About Us and Who We Serve sections of the website in charcoal and gold", "half"),
            ("web-national.jpg", "The website's Going National map showing locations in California, Washington, Arizona and South Dakota", "half"),
            ("postcards.jpg", "Front and back of The Road Continues postcard, with the mission statement and a donation QR code", "wide"),
            ("sign.jpg", "A tabletop sign with a QR code inviting people to scan, learn more and give", "half"),
            ("business-cards.jpg", "Front and back of the business card with the road photo, gold type and a QR code", "half"),
            ("receipt.jpg", "The branded donation receipt with spaces for date, items donated and dollar value", "half"),
            ("deck.jpg", "Six slides from the presentation deck in charcoal and gold", "half"),
        ],
        "review": None,
    },
]
