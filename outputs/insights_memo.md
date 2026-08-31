# Insights Memo: What Actually Gets You Hired as a Marketing Data Analyst

**Analyst:** Joel Bumba
**Date:** September 1, 2026

---

## Headline Finding

Across 188 real US job postings for Marketing/Data Analyst roles, SQL
(35.6%) and Excel (30.3%) are the two most commonly required skills by a
wide margin -- both appear in nearly a third or more of postings.
Tableau, Python, and Power BI form a clear second tier (16-18%), and these
five tools together form a tightly interconnected "technical core": the
skill co-occurrence network shows they almost always appear together in
the same posting, not as substitutes for each other.

## Skill Demand Ranking (US, Primary Analysis)

| Rank | Skill | % of Postings |
|---|---|---|
| 1 | SQL | 35.6% |
| 2 | Excel | 30.3% |
| 3 | Tableau | 18.1% |
| 4 | Python | 17.6% |
| 5 | Power BI | 16.5% |
| 6 | Statistics | 13.3% |
| 7 | Data Visualization | 12.2% |
| 8 | Machine Learning | 10.1% |

## Skill Relationships

The co-occurrence network (14 connected skills, 59 pairings) shows SQL as
the most central node -- it co-occurs with nearly every other skill in the
network, functioning as the connective tissue of the whole skillset rather
than a standalone requirement. SQL+Excel and SQL+Tableau are the two
single strongest pairings (24 co-occurrences each). Practical takeaway:
SQL is not optional if you want to be considered for the majority of
adjacent tool requirements.

## Salary Signal (Directional, Not Statistically Confirmed)

Among a small US subsample (37 postings with clean annual salary data),
Tableau, Python, and SQL showed the largest positive salary differences
(+$37,648, +$28,564, +$18,924 respectively vs. postings without each
skill). Given the small per-skill sample sizes (10-22 postings), these are
reported as a directional signal worth further investigation, not a
statistically confirmed finding.

## Canada / Australia: What the Data Could and Couldn't Show

Supplementary data was pulled directly from Adzuna's API for Canada (316
postings) and Australia (349 postings) after finding the primary Kaggle
dataset was almost entirely US-centric. However, Adzuna's API returns
much shorter description snippets (~500 characters vs. Kaggle's ~2,773),
making direct skill-demand comparisons to the US data unreliable and
excluded from headline claims. Canada and Australia showed no
statistically significant skill-demand differences from each other
(chi-square tests on the largest observed gaps: p=0.054-0.614). Average
disclosed salary across both markets combined: $108,708/year.

## What I Did With This Personally

[Fill in: how this analysis changed or confirmed your own skill-building
priorities, e.g. "This confirmed SQL and Excel are non-negotiable table
stakes, and validated my decision to prioritize Tableau/Power BI
certification given their central position in the co-occurrence network
and directional salary signal."]

## Try It Yourself

A live tool is available at [job-market-skill-analysis.streamlit.app] --
paste your own skills and get a personalized match score against this
same US skill-demand data.

## Limitations

- Keyword-based skill extraction, not NLP/semantic matching -- may miss
  skills described in non-standard phrasing.
- US sample (188 postings) reflects one point in time and one job board's
  postings, not the full labor market.
- Canada/Australia findings are directional only, limited by API text
  truncation, and excluded from the primary skill-demand ranking.
- Salary-skill correlations are based on small samples and should be
  treated as suggestive, not conclusive.
