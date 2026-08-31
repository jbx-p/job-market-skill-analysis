# What Actually Gets You Hired as a Marketing Data Analyst

A data-driven analysis of real job postings for Marketing/Data Analyst
roles, built to answer one question with evidence instead of guesswork:
what skills actually matter, and how do they relate to each other? Includes
a live, interactive tool where anyone can paste their own skills and get a
personalized gap analysis against the real market.

**[Try the live tool](https://job-market-skill-analysis.streamlit.app)**

**Headline finding:** SQL (35.6%) and Excel (30.3%) dominate real US job
postings for these roles, forming a tightly interconnected "technical
core" with Tableau, Python, and Power BI. SQL is the most central skill in
the co-occurrence network -- it connects to nearly every other skill,
functioning as connective tissue rather than a standalone requirement.

## Why This Project

Most "what skills should I learn" content on LinkedIn is opinion, not
evidence. This project extracts skill demand directly from real job
posting text, builds an actual network model of how skills relate to each
other, and turns the whole thing into something people can use on
themselves rather than just read about.

## Data Sources

- **Kaggle: LinkedIn Job Postings (2023-2024)** by arshkon -- the primary
  dataset, filtered to Marketing/Data Analyst roles (188 relevant US
  postings with full job description text).
- **Adzuna API** (free tier) -- used to pull supplementary Canada (316
  postings) and Australia (349 postings) data after finding the Kaggle
  dataset was almost entirely US-centric.

## Methodology

1. Filtered postings to relevant titles (Marketing Analyst, Data Analyst,
   Marketing Data Analyst, etc.).
2. Extracted skills via a curated keyword dictionary, iteratively refined
   by checking postings that matched zero skills.
3. Ranked skill demand by frequency of mention.
4. Attempted salary-skill correlation -- found reliable results only for
   a small US subsample (37 postings, clean annual salary data); reported
   as directional, not statistically confirmed, given small per-skill
   sample sizes.
5. Built a skill co-occurrence network to show which skills are typically
   required together, not just which are individually common.
6. Built and deployed a public Streamlit app where users benchmark their
   own skills against the US findings.

## A Key Data-Quality Finding (Worth Reading Before Trusting Any Cross-Market Number)

Adzuna's API returns short description snippets (~500 characters) vs.
Kaggle's full descriptions (~2,773 characters) -- a 5.5x difference. This
makes Canada/Australia skill-mention rates severely understated and NOT
comparable to the US figures (e.g., SQL: 35.6% US vs. 3.2% Canada / 2.9%
Australia -- an artifact of truncated text, not a real market difference).
Canada and Australia can be fairly compared to each other (same source,
same truncation), and chi-square tests found no statistically significant
skill-demand differences between them. This is why the US data is treated
as the primary analysis throughout, and why the live tool benchmarks
against US data only.

## Repo Structure

job-market-skill-analysis/
├── data/
│ ├── raw/ # source files (not committed - see Setup)
│ └── processed/ # skill_demand_by_market.csv, combined_postings.csv,
│ # salary analysis outputs
├── notebooks/
│ ├── 01_data_acquisition.ipynb # Kaggle load, Adzuna fetch, filtering
│ └── 02_skill_extraction_analysis.ipynb # skill extraction, demand ranking,
│ # salary analysis, co-occurrence network
├── app/
│ └── skill_match_app.py # live Streamlit tool
├── outputs/ # insights memo, charts, network graphs
├── README.md
└── requirements.txt # minimal deps for the deployed Streamlit app


## Reproducing This

1. Download the [LinkedIn Job Postings dataset](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings)
   into `data/raw/`
2. Get free Adzuna API credentials at [developer.adzuna.com](https://developer.adzuna.com),
   create a `config.py` with your `ADZUNA_APP_ID` and `ADZUNA_APP_KEY`
   (never commit this file -- already in `.gitignore`)
3. `python -m venv venv`, activate it, `pip install pandas numpy matplotlib seaborn jupyter requests networkx pyvis scipy`
4. Run notebooks in order: `01_data_acquisition.ipynb` → `02_skill_extraction_analysis.ipynb`
5. To run the app locally: `streamlit run app/skill_match_app.py`

## Insights Memo

See [`outputs/insights_memo.md`](outputs/insights_memo.md) for the full
write-up: skill rankings, salary signal, the Canada/Australia data-quality
finding, and limitations.

## Author

Joel Bumba - [github.com/jbx-p](https://github.com/jbx-p) - [jbx-p.github.io](https://jbx-p.github.io)
