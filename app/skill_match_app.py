import streamlit as st
import pandas as pd

st.set_page_config(page_title="Marketing Data Analyst Skill Match", page_icon="??")

st.title("How Does Your Skillset Match the Real Job Market?")
st.write("""
Built from real job postings for Marketing/Data Analyst roles.
Primary benchmark: 188 US postings with full job descriptions (Kaggle
LinkedIn dataset). Paste your skills below and see how you stack up
against what employers are actually asking for.
""")

skill_demand = pd.read_csv("data/processed/skill_demand_by_market.csv")
us_demand = skill_demand[skill_demand["source"] == "kaggle_us"].copy()

user_input = st.text_area(
    "List your skills (comma-separated):",
    placeholder="e.g. Python, SQL, Tableau, Excel, Google Analytics"
)

if st.button("Check My Match"):
    if user_input.strip():
        user_skills = set(s.strip().lower() for s in user_input.split(","))
        market_skills = set(us_demand["skill"].str.lower())

        matched = market_skills.intersection(user_skills)
        missing_high_demand = us_demand[
            (~us_demand["skill"].str.lower().isin(user_skills)) &
            (us_demand["pct_of_postings"] > 10)
        ].sort_values("pct_of_postings", ascending=False)

        match_pct = len(matched) / len(market_skills) * 100 if market_skills else 0

        st.metric("Market Match Score", f"{match_pct:.0f}%")

        st.subheader("Skills You Have That Are In Demand:")
        if matched:
            for skill in matched:
                st.write(f"? {skill.title()}")
        else:
            st.write("None of your listed skills matched our tracked skill list.")

        st.subheader("High-Demand Skills You're Missing:")
        if len(missing_high_demand) > 0:
            for _, row in missing_high_demand.head(5).iterrows():
                st.write(f"?? {row['skill']} — appears in {row['pct_of_postings']:.0f}% of postings")
        else:
            st.write("You cover all the major high-demand skills we tracked. ??")
    else:
        st.warning("Enter at least one skill first.")

st.divider()
st.caption("""
Methodology: skills extracted via keyword matching from real job posting
descriptions. US data (primary) uses full descriptions from 188 postings.
Canada/Australia data was also analyzed but excluded from this tool due to
truncated description text in the source API, making skill-mention rates
unreliable for those markets specifically. Full methodology and limitations:
github.com/jbx-p/job-market-skill-analysis
""")
