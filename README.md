
# Google Play Store Data Analytics Dashboard 📊

This project is part of my **NullClass Internship**.  
The goal is to analyze Google Play Store data using Python, Plotly, NLP (VADER), and advanced filtering techniques.  
All 6 assigned tasks were implemented as interactive visualizations, following the same patterns used in training — with strict adherence to each task’s instructions.

---

## 📌 **Project Structure**

- **Task 1:** Stacked bar chart of sentiment distribution for user reviews, segmented by rating groups (1–2, 3–4, 4–5 stars) for top 5 categories.
- **Task 2:** Dual-axis chart comparing average installs & revenue for free vs. paid apps in top 3 categories. Includes strict filters (installs, revenue, version, size, content rating, app name length). Time-bound display (1 PM to 2 PM IST only).
- **Task 3:** Grouped bar chart comparing average rating & total review count for top 10 categories by installs. Filters for minimum rating, size, and Jan-month updates. Time-bound display (3 PM to 5 PM IST only).
- **Task 4:** Interactive Choropleth map visualizing global installs by category. Filters for top 5 categories, excludes categories starting with A/C/G/S, highlights 1M+ installs. Time-bound display (6 PM to 8 PM IST only).
- **Task 5:** Bubble chart analyzing app size vs. average rating. Bubble size represents installs. Includes multi-step filters: min rating, specific categories (Game, Beauty, Business, Comics, Communication, Dating, Entertainment, Social, Event), reviews >500, app name must not contain "S", sentiment subjectivity >0.5, installs >50k. Translations: Beauty (Hindi), Business (Tamil), Dating (German). Game category highlighted in pink. Time-bound display (5 PM to 7 PM IST only).
- **Task 6:** Time series line chart showing total installs trend over time by category. Highlights 20%+ month-over-month growth with shaded areas. Filters: app name must not start with X/Y/Z or contain "S"; categories must start with E/C/B; Beauty (Hindi), Business (Tamil), Dating (German) translation. Reviews >500. Time-bound display (6 PM to 9 PM IST only).

---

## ✅ **Key Features**

- **Data Cleaning:** Full pipeline as in training (duplicates, missing values, log transforms, consistent types).
- **Sentiment Analysis:** VADER lexicon for compound sentiment scores.
- **Time Controls:** Each figure is displayed conditionally based on IST.
- **Strict Filters:** Custom filters for installs, reviews, price, content rating, app name, category prefixes.
- **Interactive Dashboard:** Single `index.html` loads all plots with clickable containers & insights.
- **Fully Responsive:** Designed for both desktop & mobile devices.
- **Clean & Modular:** Code is clear, commented & modular for easy review.

---

## 🚀 **How to Run**

1. Download or clone this repository.

2. Keep all the HTML files (`index.html` and all `fig*.html`) in the same folder.

3. Open `index.html` in your web browser.

4. Click on any task to view its visualization and insight.  
   Each chart will appear only within its specified time window.


## 🌐 **Live Demo**
Hosted version on Netlify — (https://playstore-insight-vault.netlify.app)


## 📑 **Author**
**Name:** Ishant Gupta

**Internship:** NullClass 3-month Internship — Real-Time Google Play Store Data Analytics

## 📧 **Contact**
For any queries, reach me at ishantgupta2005@gmail.com

## ⚙️ **License**
📜 For academic internship use only — no commercial reuse.

Thank you for visiting my project! 🚀
