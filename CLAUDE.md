# Belditalk.com — Moroccan Darija Academy

## What This Is
Professional website for Belditalk.com — an online academy teaching Moroccan Darija (Moroccan Arabic dialect) to a global audience. Founded by Elias Lamseyah.

## Tech Stack
- Pure HTML/CSS/JS (NO frameworks, NO npm, NO build tools)
- Single index.html with embedded CSS and JS
- Mobile-first responsive design
- Deployed as static files on Vercel

## Design Direction
- Moroccan-inspired: warm colors (terracotta, saffron gold, deep blue, mint green, cream)
- Geometric zellige tile patterns as decorative elements (inline SVGs)
- Modern, clean, premium feel — NOT cheap or template-looking
- Google Fonts: 'Outfit' for headings, 'Inter' for body
- Dark sections alternating with light for visual rhythm
- Smooth scroll-reveal animations (IntersectionObserver, no libraries)
- Subtle micro-interactions on hover (cards lift, buttons glow, patterns pulse)

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

## INTEGRATIONS TO WIRE UP

### Lemon Squeezy (Payments)
- Store URL: https://belditalk.lemonsqueezy.com
- Products need to be created in dashboard. For now, link "Buy" buttons to: https://belditalk.lemonsqueezy.com/buy
- Discount code WELCOME20 exists (20% off)
- Embed checkout overlay script: <script src="https://assets.lemonsqueezy.com/lemon.js" defer></script>
- Use class="lemonsqueezy-button" on buy links for overlay checkout

### Mailchimp (Email Signup)
- Form action URL: https://gmail.us10.list-manage.com/subscribe/post?u=39cfc39714e24c2f1e80bd2d5&id=7317b7b5dd
- Fields: EMAIL (required), FNAME (optional), LNAME (optional)
- Hidden honeypot field: <input type="text" name="b_39cfc39714e24c2f1e80bd2d5_7317b7b5dd" tabindex="-1" value="" style="position:absolute;left:-5000px">
- Use AJAX submission with fetch() to avoid page redirect
- Show success/error messages inline

## Pages (ALL IN ONE index.html with smooth scroll sections)

### 1. Navigation Bar (Fixed)
- Logo + "BeldiTalk" text on left
- Links: About, Courses, Curriculum, Pricing, Community, Blog, FAQ
- CTA button: "Start Learning →" links to #pricing
- Mobile hamburger menu
- Transparent initially, solid dark background on scroll
- Smooth transition

### 2. Hero Section
- Full viewport height
- Background: dark gradient with subtle Moroccan zellige pattern overlay
- Floating logo with drop-shadow animation
- Badge: "🟢 NOW ENROLLING — Limited Spots"
- Headline: "Learn Moroccan Darija — Speak Like a Local"
- Subheadline: "Master Morocco's language and culture with native-speaker guidance, interactive lessons, and a global community"
- Two CTAs: "Get Started — $29 →" (primary, links to #pricing) and "Try Free Lesson" (outline, links to #free-lesson)
- Stats row: "197 Pages" | "12 Modules" | "3 Levels" | "1000+ Phrases"
- Scroll indicator at bottom
- "Word of the Day" widget showing a random Darija phrase

### 3. About Section ("Why Learn Darija?")
- Section label: "WHY DARIJA"
- 3 feature cards with icons:
  - "For Travelers" — Navigate Morocco authentically. Order in cafes, bargain in souks, take taxis with confidence.
  - "For Heritage Learners" — Reconnect with your Moroccan roots. Understand family conversations and cultural traditions.
  - "For Language Enthusiasts" — Explore a unique Arabic dialect that blends Arabic, Amazigh, French, and Spanish.
- Founder card: Photo placeholder (CSS gradient), "Meet Elias Lamseyah" — born and raised in Morocco, teaching Darija to help the world connect with Moroccan culture.

### 4. Free Lesson Section (id="free-lesson")
- Section label: "FREE LESSON"
- Title: "Your First Darija Lesson — Right Now"
- Interactive mini-lesson with 5 phrases:
  1. Salam — Hello
  2. Labas? — How are you?
  3. Hamdullah — Thank God / I'm good
  4. Shukran — Thank you
  5. Bslama — Goodbye
- Each phrase: Darija word (large), pronunciation guide, English meaning
- Click-to-reveal style interaction (click a card to flip it)
- Mini dialogue practice:
  "Person A: Salam, labas?"
  "Person B: Labas, hamdullah. Nta?"
  "Person A: Bikhir, shukran."
- CTA: "Want more? Get the full 12-module course →" links to #pricing
- Below: Email signup form (Mailchimp) — "Get free weekly Darija lessons" with FNAME + EMAIL fields

### 5. What You Get Section
- Section label: "WHAT'S INCLUDED"
- 3 product cards:
  
  **Card 1: E-Book** (icon: 📘)
  "I ❤️ Moroccan Darija" — 197-page comprehensive guide
  - 12 structured modules from greeting to fluent conversation
  - 1000+ vocabulary words with transliteration
  - Real dialogues, not textbook phrases
  - Cultural context for every lesson
  - Self-paced, keep forever
  
  **Card 2: Live Sessions** (icon: 🎥)
  Monthly interactive Zoom classes with Elias
  - Pronunciation practice with native speaker
  - Cultural storytelling sessions
  - Q&A and personalized feedback
  - Recorded for later viewing
  
  **Card 3: Community** (icon: 🌍)
  Free global Discord community
  - Daily Darija challenges
  - Pronunciation practice channels
  - Peer learning and support
  - Cultural events and discussions

### 6. Curriculum Preview Section
- Section label: "CURRICULUM"
- Title: "12 Modules — From 'Salam' to Real Conversations"
- Accordion/collapsible list showing all 12 modules:
  
  Module 1: First Words — Greetings & Politeness
  Module 2: Introducing Yourself
  Module 3: Numbers & Money
  Module 4: Food & Drinks
  Module 5: Getting Around
  Module 6: Shopping & Bargaining
  Module 7: Family & People
  Module 8: Time & Days
  Module 9: Feelings & Opinions
  Module 10: Problem Solving
  Module 11: Culture & Customs
  Module 12: Real Conversations — Full Dialogues
  
- Each module shows 3-4 bullet points of what you'll learn (use content from content/beginner-course/ files)
- "Full curriculum included in the course"
- Visual progress path (module 1 at top connected by dotted line to module 12 at bottom)

### 7. Pricing Section (id="pricing")
- Section label: "PRICING"
- Title: "Start Your Darija Journey Today"
- 3 pricing cards side by side:

  **Free Starter Pack** — $0
  - 20 essential Darija phrases PDF
  - Pronunciation guide
  - Cultural tips
  - Community access
  - CTA: "Download Free →" (links to Lemon Squeezy free product or email signup)

  **Beginner Course** — $29 (MOST POPULAR badge)
  - Everything in Free +
  - 197-page e-book
  - 12 structured modules
  - 1000+ vocabulary words
  - Audio pronunciation guides
  - Real conversation dialogues
  - Cultural deep dives
  - Lifetime updates
  - CTA: "Get the Course →" (links to Lemon Squeezy checkout)
  
  **Premium Bundle** — $49
  - Everything in Beginner +
  - Monthly live Zoom sessions
  - Private Discord channels
  - Personal pronunciation feedback
  - Priority support
  - Future courses included
  - CTA: "Go Premium →" (links to Lemon Squeezy checkout)

- Below cards: "Use code WELCOME20 for 20% off your first purchase!"
- Money-back guarantee badge: "30-Day Money Back Guarantee — No questions asked"
- Trust indicators: secure payment icons, "Powered by Lemon Squeezy"

### 8. Testimonials Section
- Section label: "WHAT LEARNERS SAY"
- 4 testimonial cards:
  1. Sarah M., United States — "I finally understood what my Moroccan mother-in-law was saying! The cultural notes are incredibly helpful." ⭐⭐⭐⭐⭐
  2. Pierre L., France — "As someone who speaks French, I thought I'd understand Darija easily. I was wrong! This course bridges the gap perfectly." ⭐⭐⭐⭐⭐
  3. Fatima K., Canada — "I'm Moroccan-Canadian and wanted to reconnect with my roots. Belditalk made it feel natural, not like homework." ⭐⭐⭐⭐⭐
  4. James T., UK — "Went to Marrakech and actually bargained in the souk in Darija. The look on the vendor's face was priceless!" ⭐⭐⭐⭐⭐
- "Join 500+ learners worldwide" (aspirational)

### 9. Blog/Resources Preview
- Section label: "FREE RESOURCES"
- 3 blog preview cards with gradient backgrounds:
  1. "10 Essential Darija Phrases for Travelers" — The phrases you need for your first day in Morocco
  2. "Darija vs Arabic: What's the Difference?" — Why Moroccan Arabic is unique
  3. "Your First Day Speaking Darija" — A practical guide to using what you learn
- "Coming soon — more free lessons and guides"

### 10. FAQ Section
- Section label: "FAQ"
- Accordion with 8 questions:
  1. What is Moroccan Darija? — Darija is the Moroccan dialect of Arabic, spoken by 30+ million people. It blends Arabic, Amazigh, French, and Spanish. It's the language of daily life in Morocco — cafes, souks, families, and friendships.
  2. Do I need to know Arabic first? — Not at all! This course starts from zero. We use Latin transliteration so you don't need to read Arabic script. You'll learn to speak and understand, not read formal Arabic.
  3. How is this different from learning Modern Standard Arabic (MSA)? — MSA is the formal language of news and literature. Darija is what Moroccans actually speak daily. They're related but different — like Portuguese and Spanish. If you want to connect with real people in Morocco, you need Darija.
  4. What format is the course? — A downloadable PDF e-book with 12 modules, 197 pages. Plus optional live Zoom sessions (Premium) and a free Discord community.
  5. How long does it take to complete? — Most students complete the beginner course in 4-8 weeks studying 20-30 minutes daily. But it's self-paced — go at your own speed.
  6. Can I get a refund? — Yes! 30-day money-back guarantee, no questions asked. If the course isn't right for you, email us for a full refund.
  7. How do I join the community? — The Discord community is free for everyone! You'll get an invite link after signing up or purchasing.
  8. Will there be more courses? — Yes! Intermediate and Advanced courses are in development. Premium Bundle members get all future courses included.

### 11. Final CTA Section
- Dark background with zellige pattern
- Title: "Ready to Speak Darija?"
- Subtitle: "Join 500+ learners from 40+ countries. Start with a free lesson or dive into the full course."
- Two CTAs: "Get Started — $29 →" and "Download Free Starter Pack"
- Email signup form (same Mailchimp form): "Or get free weekly lessons →" with EMAIL field

### 12. Footer
- Dark background
- 4 columns:
  - Column 1: Logo + "Learn Moroccan Darija with native-speaker guidance. Your journey to speaking like a local starts here."
  - Column 2: Quick Links — About, Courses, Community, Blog, FAQ, Contact
  - Column 3: Resources — Free Lesson, Phrase Guide, Pronunciation Tips, Discord Community
  - Column 4: Connect — Instagram, TikTok, YouTube, Facebook, Email: belditalk212@gmail.com
- Bottom bar: "© 2026 Belditalk.com — All rights reserved" | "Made with ❤️ in Morocco" | Privacy Policy | Terms of Service
- Lemon Squeezy checkout script tag at bottom

## Technical Requirements

### Must Have
- Single index.html file with ALL CSS and JS inline/embedded
- Fully responsive (mobile, tablet, desktop) — test all breakpoints
- Smooth scroll navigation with active link highlighting
- Scroll-reveal animations using IntersectionObserver (no libraries)
- Sticky/fixed nav that changes opacity/background on scroll
- All images referenced from public/images/ (relative paths: images/logo.png)
- Open Graph + Twitter Card meta tags
- SEO meta tags (title, description, keywords)
- Moroccan zellige SVG patterns as inline background decorations
- Functional Mailchimp signup forms (2 locations: free lesson section + footer)
- Lemon Squeezy checkout overlay script
- Accessible: proper contrast, alt text, aria labels, keyboard navigation
- Fast: no external JS libraries, minimal external requests
- FAQ and Curriculum accordions with smooth expand/collapse
- Card flip animation on the free lesson section
- Mobile hamburger menu with slide-in animation

### Nice to Have
- Animated counter for stats (counts up when scrolled into view)
- Typing animation on hero subtitle
- Parallax effect on hero background pattern
- Dark mode toggle (save preference to localStorage)
- "Back to top" floating button

## DO NOT
- Do NOT use React, Vue, Next.js, or any framework
- Do NOT use npm, webpack, or any build tools
- Do NOT create multiple HTML files — EVERYTHING in ONE index.html
- Do NOT use external CSS/JS libraries (no Bootstrap, no jQuery, no Tailwind, no AOS.js)
- Do NOT use placeholder images from the internet — use CSS gradients, SVG patterns, and emoji
- Do NOT make it look like a generic template — it should feel uniquely Moroccan and premium
- Do NOT leave any broken links or non-functional buttons
- Do NOT use Lorem Ipsum — all text must be real content
