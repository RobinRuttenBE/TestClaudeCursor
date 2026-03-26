# Abandoned Cart Email Flow

**Segment:** Abandoned Cart
**Trigger:** Winkelwagen verlaten zonder checkout (Wix → Zapier)
**Totaal emails:** 3
**Tijdlijn:** 1 uur, dag 3, dag 7
**Doel:** Cart recovery (target: 10% recovery rate)

**Belangrijk:** Stop de flow zodra de aankoop alsnog voltooid wordt.

---

## Email 1: Gentle Reminder

**Timing:** 1 uur na cart abandonment
**Doel:** Zachte herinnering, eventuele technische issues oplossen

**Subject Line A:** You left something behind
**Subject Line B:** Still thinking it over?
**Preview Text:** Your cart is saved — pick up right where you left off.

---

Hi {{first_name}},

Looks like you were browsing our shop and left a few items in your cart. No worries — it happens!

**Your cart:**
{{cart_items}}

We've saved everything for you, so you can pick up right where you left off.

If you ran into any issues during checkout — a technical hiccup, a question about shipping, or anything else — just reply to this email. Our team is happy to help.

Fun fact: every Sempertex balloon is made from 100% natural latex, FSC-certified, and produced without fillers or plasticisers. What you add to your cart is what professionals around the world rely on every day.

Your cart is waiting.

The Sempertex Europe Team

---

**CTA Button:** Complete Your Order
**CTA Link:** {{cart_url}}

---

## Email 2: Social Proof + Value

**Timing:** Dag 3
**Doel:** Vertrouwen opbouwen, waarde benadrukken, twijfel wegnemen

**Subject Line A:** Why 10,000+ decorators choose Sempertex
**Subject Line B:** The difference is in the details
**Preview Text:** Here's what professionals say about the products in your cart.

---

Hi {{first_name}},

We noticed you haven't completed your order yet. Before you decide, here's something worth knowing:

**What makes Sempertex different from every other balloon brand:**

- **Colour consistency** — the colour you see online is the colour you get. Every batch, every time. No surprises at 6am on installation day.
- **9 unique finishes** — from Pastel Matte to Reflex Chrome. No other brand offers this range.
- **Professional durability** — our balloons hold their shape and colour longer, which means your installations look perfect for the entire event.
- **Link-O-Loon** — we invented it. Others copied it. The quality difference is significant.

Don't just take our word for it:

> *"I switched to Sempertex two years ago and haven't looked back. The consistency alone saves me hours of stress."*
> — Professional decorator, Belgium

The items in your cart are still reserved. Ready when you are.

The Sempertex Europe Team

---

**CTA Button:** Return to Your Cart
**CTA Link:** {{cart_url}}

---

## Email 3: Last Chance

**Timing:** Dag 7
**Doel:** Laatste herinnering met zachte urgentie

**Subject Line A:** Your cart expires soon
**Subject Line B:** Last chance to grab your selection
**Preview Text:** We can't hold your items forever — here's a final reminder.

---

Hi {{first_name}},

This is a friendly heads-up: the items in your cart won't be saved much longer.

**Your selection:**
{{cart_items}}

We understand — sometimes the timing just isn't right. But if you were planning to order, now is the moment.

**A few things to keep in mind:**
- Free shipping on orders above {{free_shipping_threshold}}
- Colour charts available to help you plan your next project
- Our team is always here if you have questions about sizing, colours, or finishes

As a professional working with balloons, the quality of your materials directly impacts the quality of your work — and how your clients perceive you. Sempertex gives you that confidence.

If you've decided not to order this time, no hard feelings at all. We'll be here whenever you're ready.

Warm regards,
The Sempertex Europe Team

---

**CTA Button:** Complete Your Order
**CTA Link:** {{cart_url}}

---

## Flow Complete

**Na conversie:** Contact verplaatst uit `Abandoned Cart` segment en start de Post-Purchase flow.
**Na dag 7 zonder conversie:** Flow eindigt. Contact blijft in regulier segment (Newsletter of bestaand).

**Metrics te tracken:**
- Email 1 open rate (target: >50% — high intent audience)
- Overall recovery rate (target: 10%)
- Revenue recovered
- Welke email converteert het meest (optimaliseer timing)
