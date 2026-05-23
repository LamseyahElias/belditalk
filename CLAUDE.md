# Belditalk.com — Moroccan Darija Academy

## What This Is
Professional website for Belditalk.com — an online academy teaching Moroccan Darija (Moroccan Arabic dialect) to a global audience. Founded by Elias Lamseyah.

## Tech Stack
- Pure HTML/CSS/JS (NO frameworks, NO npm, NO build tools)
- Single index.html with embedded CSS and JS
- Mobile-first responsive design
- Deployed as static files (Vercel/Netlify/GitHub Pages)

## Design Direction
- Moroccan-inspired: warm colors (terracotta, saffron gold, deep blue, mint green, cream)
- Geometric zellige tile patterns as decorative elements
- Modern, clean, premium feel — NOT cheap or template-looking
- Google Fonts: 'Outfit' for headings, 'Inter' for body
- Dark sections alternating with light for visual rhythm
- Smooth scroll animations on reveal

## Brand Assets
- Logo: public/images/logo.png (1024x1024, with background)
- Logo no-bg: public/images/logo-nobg.png (1024x1024, transparent)
- Brand colors: 
  - Primary: #C75B2F (Moroccan terracotta)
  - Secondary: #1B4965 (Deep Moroccan blue)
  - Accent: #D4A24E (Saffron gold)
  - Success: #2D6A4F (Mint green)
  - Light: #FDF6EC (Warm cream)
  - Dark: #1A1A2E (Night blue)
  - Text: #2D3436

## Pages (ALL IN ONE index.html with smooth scroll sections)

### 1. Hero Section
- Full viewport height
- Background: subtle Moroccan geometric pattern overlay on warm gradient
- Logo centered
- Headline: "Learn Moroccan Darija — Speak Like a Local"
- Subheadline: "Master Morocco's language and culture with native-speaker guidance, interactive lessons, and a global community"
- Two CTAs: "Get the E-Book →" (primary) and "Join Free Community" (outline)
- Scroll indicator at bottom

### 2. About Section
- "Why Learn Darija?" heading
- 3 cards: "For Travelers" (navigate Morocco authentically), "For Heritage Learners" (reconnect with roots), "For Language Enthusiasts" (explore a unique dialect)
- Brief personal story from Elias (2-3 sentences)
- Stats: "197 Pages", "12 Modules", "3 Levels", "1000+ Phrases"

### 3. What You Get Section
- E-Book card: "I ❤️ Moroccan Darija" — comprehensive guide, 197 pages, grammar + vocabulary + culture, QR codes to audio, self-paced
- Live Sessions card: Monthly interactive Zoom classes, cultural storytelling, pronunciation practice, Q&A
- Community card: Free Discord community, daily challenges, peer practice, cultural events
- Each card with icon, description, and subtle hover animation

### 4. Curriculum Preview
- Accordion or tabs showing 3 levels: Beginner (Modules 1-4), Intermediate (5-8), Advanced (9-12)
- Each module: title + 2-3 bullet points of what you'll learn
- "Full curriculum included in the e-book"

### 5. Pricing Section
- Single centered pricing card
- "Complete Darija Package"
- Price: $29 (or placeholder)
- What's included checklist: ✅ 197-page e-book, ✅ Monthly live sessions access, ✅ Free community membership, ✅ Audio pronunciation guides, ✅ Cultural insights, ✅ Lifetime updates
- CTA: "Get Started Now →" (links to #gumroad or placeholder)
- Money-back guarantee badge

### 6. Testimonials
- 3-4 placeholder testimonials with names, countries, star ratings
- Carousel or grid layout
- "Join 500+ learners worldwide" (aspirational)

### 7. Blog/Resources Preview
- "Free Darija Resources" heading
- 3 preview cards: "10 Essential Phrases for Travelers", "Understanding Moroccan Culture", "Your First Day Speaking Darija"
- "Coming soon" or placeholder blog links

### 8. FAQ Section
- Accordion with 6-8 questions:
  - What is Moroccan Darija?
  - Do I need prior Arabic knowledge?
  - How are live sessions structured?
  - What format is the e-book?
  - Can I get a refund?
  - How do I join the community?

### 9. Email Signup Section
- "Stay Connected" 
- Email input + subscribe button
- "Get free weekly Darija lessons and cultural insights"
- Placeholder form (action="#" for now)

### 10. Footer
- Logo + tagline
- Quick links: About, Courses, Community, Blog, Contact
- Social media icons (Instagram, TikTok, YouTube, Discord)
- "© 2026 Belditalk.com — All rights reserved"
- "Made with ❤️ in Morocco"

## Key Requirements
- MUST be a single index.html file with all CSS and JS inline/embedded
- MUST be fully responsive (mobile, tablet, desktop)
- MUST include smooth scroll navigation
- MUST have scroll-reveal animations (CSS only, no libraries)
- MUST use the logo images from public/images/
- Image paths should be relative: images/logo.png, images/logo-nobg.png
- All placeholder links should use # or javascript:void(0)
- Include Open Graph meta tags for social sharing
- Include basic SEO meta tags (title, description, keywords)
- Sticky/fixed navigation bar that changes on scroll
- "Word of the Day" widget in the hero or sidebar
- Moroccan geometric SVG patterns as background decorations (inline SVGs, not external files)

## DO NOT
- Do NOT use React, Vue, or any framework
- Do NOT use npm or any package manager
- Do NOT create multiple HTML files — everything in ONE index.html
- Do NOT use external CSS/JS libraries (no Bootstrap, no jQuery, no Tailwind CDN)
- Do NOT use placeholder images from the internet — use CSS gradients and SVG patterns instead
