---
name: Meta Ads Tracker Excel Formatting
description: Exact visuele en structurele formatting standaarden voor de Meta Ads Tracker Excel/Sheets. Gebruikt bij genereren, updaten of aanmaken van het STX EU ad tracking bestand.
trigger: Bij genereren/updaten van Meta_Ads_Tracker_Sempertex.xlsx of schrijven naar Google Sheet tracker
---

# Meta Ads Tracker — Excel Formatting Skill

## Purpose

Ensure the Meta Ads Tracker Excel file is always professionally formatted, matching the established template standards. This skill defines the exact visual and structural requirements for every sheet in the tracker.

## When to Use

- When generating or updating the Meta Ads Tracker Excel file
- When writing weekly report data to the tracker
- When creating a new tracker from scratch
- Any time Claude Code outputs an .xlsx file for STX EU ad tracking

## File Name

`Meta_Ads_Tracker_Sempertex.xlsx`

## Google Sheet (if applicable)

Write to: https://docs.google.com/spreadsheets/d/1kMtMXBYxFYStVxop_yjkWaB5mfh7Y2tgmpYcjf2ytHs/edit

---

## Global Formatting Rules

### Colors (HEX RGB for openpyxl)

```python
HEADER_DARK = "1A1A2E"      # Dark navy — sheet titles, table headers row 1
HEADER_BLUE = "0F3460"      # Deep blue — primary metric column headers
HEADER_TEAL = "16213E"      # Dark teal — secondary metric column headers
HEADER_GREEN = "0D7377"     # Teal green — section headers (e.g., Excel Reference)
HEADER_RED = "2C3E50"       # Dark slate — UTM/tracking column headers
ROW_ALT_1 = "F5F5F5"        # Light gray — alternating row background
ROW_ALT_2 = "FFFFFF"        # White — alternating row background
KPI_BG = "EBF5FB"           # Light blue — KPI value cells on dashboard
WARNING_BG = "FFF3CD"       # Yellow — warning/target banners
HIGHLIGHT_BLUE = "D6EAF8"   # Light blue — total/summary rows
FUNNEL_GREEN = "D5E8D4"     # Soft green — top/mid funnel events
FUNNEL_YELLOW = "FFF2CC"    # Soft yellow — low funnel events
FUNNEL_ORANGE = "FFE6CC"    # Soft orange — conversion events
WHITE_TEXT = "FFFFFF"        # White — text on dark headers
```

### Font

- All cells: Arial, size 10
- Headers: Arial, size 10, Bold, White text on dark background
- Sheet titles: Arial, size 12, Bold, White text on HEADER_DARK background
- KPI values on dashboard: Arial, size 14, Bold

### Row Styling

- Alternating row colors: ROW_ALT_1 / ROW_ALT_2 (zebra striping)
- Row height: 20px for data rows, 30px for header rows
- Freeze panes: freeze row 1 (title) and row 3 (column headers) on all data sheets

### Column Widths

- Auto-fit to content with minimum 12 characters
- Campaign/Ad Name columns: minimum 25 characters
- Notes/Feedback columns: minimum 35 characters
- Numeric columns (Spend, CPC, etc.): 15 characters
- Date columns: 15 characters

### Number Formatting

- Currency: `€#,##0.00` (e.g., €421.28)
- Percentages: `0.00%` (e.g., 4.93%)
- Integers: `#,##0` (e.g., 205,335)
- ROAS: `0.00x` (e.g., 8.30x)
- Dates: `YYYY-MM-DD`

### Conditional Formatting

- CPC > €0.50 → Red background on CPC cell
- CTR < 1.0% → Red background on CTR cell
- ROAS < 1.0x → Red background on ROAS cell
- Status = "PAUSED" → Gray text
- Status = "Active" → Green text

---

## Sheet Structure

### Sheet 1: Dashboard

**Purpose:** High-level KPI overview, auto-updated from other sheets.

**Layout:**

- **Row 1:** Title "META ADS TRACKER · Sempertex Europe" (merged A1:P1, HEADER_DARK bg)
- **Row 3-4:** KPI Cards (8 cards, 2 columns each)
  - A3-B4: Total Budget Spent
  - C3-D4: Total Campaigns
  - E3-F4: Total Ads Live
  - I3-J4: Avg CPC (€)
  - K3-L4: Avg ROAS
  - M3-N4: Total Sales
  - O3-P4: Avg AOV (€)
  - Row 3: Labels (HEADER_BLUE bg, white bold text)
  - Row 4: Values (KPI_BG bg, size 14 bold)
- **Row 6:** Warning banner "⚠️ TARGET: Keep CPC below €0.50 | Rows highlighted RED if CPC > €0.50" (WARNING_BG bg)
- **Row 8:** Split section
  - A8: "TOP 5 ADS BY ROAS" (HEADER_GREEN bg)
  - J8: "BUDGET OVERVIEW BY CAMPAIGN" (HEADER_BLUE bg)
- **Row 9:** Sub-headers for both tables
- **Row 10-14:** Data rows (formulas pulling from other sheets)
- **Row 16+:** "HOW TO USE THIS TRACKER" instruction box (KPI_BG bg)

### Sheet 2: Weekly Report

**Purpose:** Weekly performance data per ad variant. Main data entry sheet.

**Layout:**

- **Row 1:** Title "WEEKLY PERFORMANCE REPORT · Meta Ads" (merged, HEADER_DARK bg)
- **Row 3:** Column headers (24 columns + PostHog):

| Col | Header | Category |
|-----|--------|----------|
| A | Week (YYYY-WW) | ID |
| B | Period (Mon - Sun) | ID |
| C | Campaign Name | ID |
| D | Ad Set Name | ID |
| E | Ad ID | ID |
| F | Amount Spent (€) | Primary (HEADER_BLUE) |
| G | Impressions | Primary |
| H | Reach | Primary |
| I | Video Views | Primary |
| J | Views 3s+ | Primary |
| K | Views Until End | Primary |
| L | CPM (€) | Primary |
| M | CPC (€) | Primary |
| N | CTR (%) | Primary |
| O | Link Clicks | Primary |
| P | Engagement Rate (%) | Secondary (HEADER_TEAL) |
| Q | LP Video Views | Secondary |
| R | Sales (#) | Secondary |
| S | ROAS | Secondary |
| T | CPS (€) | Secondary |
| U | AOV (€) | Secondary |
| V | Frequency (per profile) | Secondary |
| W | Meta Quality Ranking | Secondary |
| X | Feedback / Notes | Secondary |
| Y | LP Bounce Rate (%) | PostHog (HEADER_GREEN) |
| Z | LP Avg Scroll Depth (%) | PostHog |
| AA | LP Avg Session Duration (s) | PostHog |
| AB | LP CTA Click Rate (%) | PostHog |
| AC | LP /booking Visits | PostHog |

- **Row 4+:** Data rows with zebra striping
- One row per ad variant per week
- Group rows by week (all ads for week X together)

### Sheet 3: Ad Master List

**Purpose:** Complete inventory of all ads with creative links and UTM tracking.

**Layout:**

- **Row 1:** Title "AD MASTER LIST · All Ads Overview" (HEADER_DARK bg)
- **Row 2:** Total ad budget spent (HIGHLIGHT_BLUE bg)
- **Row 3:** Column headers (22 columns):

| Col | Header | Category |
|-----|--------|----------|
| A | Ad ID | ID |
| B | Ad Name | ID |
| C | Campaign | ID |
| D | Ad Set | ID |
| E | Ad Format (Video/Image/Carousel) | Primary (HEADER_BLUE) |
| F | Start Date | Primary |
| G | End Date | Primary |
| H | Status (Live/Paused/Ended) | Primary |
| I | Total Spend (€) | Primary |
| J | Total Sales (#) | Primary |
| K | Total ROAS | Primary |
| L | CPS (€) | Primary |
| M | AOV (€) | Primary |
| N | Meta Quality Ranking | Secondary (HEADER_TEAL) |
| O | Your Score (1-10) | Secondary |
| P | UTM Source | Tracking (HEADER_RED) |
| Q | UTM Medium | Tracking |
| R | UTM Campaign | Tracking |
| S | UTM Content | Tracking |
| T | Pixel Event | Tracking |
| U | Drive Link | Tracking |
| V | Feedback / Notes | Tracking |

### Sheet 4: Campaign Overview

**Purpose:** Aggregated metrics per campaign.

**Layout:**

- **Row 1:** Title "CAMPAIGN OVERVIEW · Aggregated Metrics per Campaign" (HEADER_DARK bg)
- **Row 3:** Column headers (18 columns):

| Col | Header |
|-----|--------|
| A | Campaign Name |
| B | Campaign Objective |
| C | Start Date |
| D | End Date |
| E | Status |
| F | Total Budget (€) |
| G | Total Spent (€) |
| H | # Ad Sets |
| I | # Ads |
| J | Total Sales |
| K | Total ROAS |
| L | Avg CPC (€) |
| M | Avg CPM (€) |
| N | Avg CTR (%) |
| O | Total Impressions |
| P | Avg Frequency |
| Q | Best Ad Format |
| R | Notes / Strategy |

### Sheet 5: UTM & Pixel Reference

**Purpose:** Reference sheet for UTM conventions and Meta Pixel funnel events.

**Layout:**

- **Row 1:** Title "UTM BUILDER & META PIXEL FUNNEL REFERENCE" (HEADER_DARK bg)
- **Row 3:** "UTM PARAMETER BUILDER" (HEADER_BLUE bg)
- **Row 4-9:** UTM parameter table (Parameter, Description, Example Value, Notes)
- **Row 11:** "UTM NAMING CONVENTION TEMPLATE" (HEADER_TEAL bg)
- **Row 12:** Full UTM template string (KPI_BG bg)
- **Row 14:** "META PIXEL FUNNEL EVENTS" (HEADER_GREEN bg)
- **Row 15-20:** Funnel events table with color-coded stages:
  - ViewContent, AddToCart: FUNNEL_GREEN bg
  - InitiateCheckout, AddPaymentInfo: FUNNEL_YELLOW bg
  - Purchase: FUNNEL_ORANGE bg

---

## Data Entry Rules

**When adding weekly data:**

- Always append new rows BELOW existing data
- Maintain zebra striping on new rows
- Fill ALL columns: use 0 or "-" for missing data, never leave blank
- Week number format: ISO week (1-52)
- Period format: "Mon - Sun" with abbreviated day names
- Group all ad variants for the same week together

**When updating Dashboard:**

- KPI values should use formulas referencing other sheets
- Top 5 table pulls from Ad Master List, sorted by ROAS descending
- Budget Overview pulls from Campaign Overview

---

## Implementation Notes

### openpyxl Code

When creating or updating this file in Claude Code, always:

- Use openpyxl (not pandas) for formatting control
- Apply all colors using PatternFill with fgColor (not start_color for older versions)
- Set column widths explicitly after adding data
- Apply conditional formatting rules after all data is written
- Freeze panes at row 4 (below headers) on data sheets
- Use number_format strings for proper display
- Run `scripts/recalc.py` after saving to ensure formula values are calculated

### PostHog Data Columns

- The PostHog columns (Y-AC) on the Weekly Report are filled from the PostHog MCP data
- Match PostHog data to ad variants using the `utm_content` parameter
- If PostHog has no data for a specific ad variant (e.g., campaign is paused), enter "-"
