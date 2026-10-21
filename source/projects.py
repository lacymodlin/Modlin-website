"""Portfolio projects. Each one becomes /projects/<slug>/ and a card in the Work section.
Images live in source/assets/projects/<slug>/.
gallery items: (file, alt text, "wide" or "half")."""

PROJECTS = [
    {
        "slug": "a-purple-house",
        "seo_title": "Logo Design",
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
        "seo_title": "Nonprofit Rebrand",
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
    {
        "slug": "sylva",
        "seo_title": "Skincare Brand Concept",
        "title": "Sylva",
        "category": "Concept brand · Natural skincare",
        "card_tags": "Skincare · Logo & packaging",
        "summary": "A concept identity for a plant-based skincare line. The goal was a brand that feels calm, clean and rooted in nature, without falling back on the rustic kraft-paper look so many natural brands share.",
        "meta": [
            ("Client", "Concept project, natural skincare"),
            ("Services", "Logo suite, color palette, brand pattern"),
            ("Deliverables", "Wordmark, leaf mark, packaging mockup"),
        ],
        "cover": ("cover.jpg", "A Sylva face cream jar with a silver lid on a tree stump surrounded by moss and leaves"),
        "card": "card.jpg",
        "story": [
            ("The brief", "Sylva is a small-batch line of botanical creams and serums for people who want simple, plant-based skincare. The brand had to look gentle and trustworthy next to big-name jars on a shelf, feel natural without looking homemade, and leave room to grow into new products."),
            ("The approach", "The name comes from the Latin word for forest, so the leaf became the heart of the identity. I built the mark from faceted segments in three greens, like sunlight breaking through leaves, and tucked it into the wordmark so the leaf grows right out of the \"v.\" Wide, airy letter spacing keeps the type calm and modern, and the palette runs from deep moss to soft mint so every piece feels fresh but grounded."),
            ("The result", "A complete logo suite with a wordmark and a standalone leaf mark, a three-green palette, and a leaf pattern for tissue paper, boxes and social posts. The mark holds up from a jar label down to a favicon, and it's flexible enough to color-code future products."),
        ],
        "gallery": [
            ("logo-suite.jpg", "The Sylva wordmark and leaf mark in four versions on white, deep green, cream and sage", "wide"),
            ("palette.jpg", "The Sylva color palette of moss, sage, mint and white", "half"),
            ("business-cards.jpg", "Sylva business cards, one deep green with a white leaf and one white with the green wordmark", "half"),
            ("scale-test.jpg", "The leaf mark and wordmark shown from large sizes down to a 16 pixel favicon", "half"),
            ("pattern.jpg", "A repeating leaf pattern on deep green with the Sylva wordmark on a white label", "half"),
        ],
        "review": None,
    },
]
