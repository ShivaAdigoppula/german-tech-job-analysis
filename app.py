# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# -----------------------
# App Title
# -----------------------
st.title("German Tech Job Market Analysis")
st.write("Explore salary drivers, skill demand, and company characteristics in the German tech job market.")

# -----------------------
# Upload Dataset
# -----------------------
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset loaded successfully!")

    st.header("Dataset Preview")
    st.dataframe(df.head())

    # -----------------------
    # 7️⃣ Top 10 industries by average salary
    # -----------------------
    st.subheader("Top 10 Industries by Average Salary")
    top_industries = df.groupby('Industry')['avg_salary'].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x=top_industries.values, y=top_industries.index, palette='viridis')
    plt.xlabel("Average Salary (€)")
    plt.ylabel("Industry")
    plt.title("Top 10 Industries by Average Salary")
    st.pyplot(plt.gcf())
    plt.clf()

    # -----------------------
    # 8️⃣ Older companies vs startups
    # -----------------------
    st.subheader("Company Age vs Average Salary")
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='age', y='avg_salary', data=df)
    plt.xlabel("Company Age (years)")
    plt.ylabel("Average Salary (€)")
    plt.title("Company Age vs Average Salary")
    st.pyplot(plt.gcf())
    plt.clf()

    # -----------------------
    # 9️⃣ German states with highest salaries
    # -----------------------
    st.subheader("Average Salary by German State")
    state_salary = df.groupby('job_state')['avg_salary'].mean().sort_values(ascending=False)
    plt.figure(figsize=(12,6))
    sns.barplot(x=state_salary.index, y=state_salary.values, palette='magma')
    plt.xlabel("German State")
    plt.ylabel("Average Salary (€)")
    plt.xticks(rotation=45)
    plt.title("Average Salary by German State")
    st.pyplot(plt.gcf())
    plt.clf()

    # -----------------------
    # 🔟 Job description length vs salary
    # -----------------------
    st.subheader("Job Description Length vs Salary")
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='desc_len', y='avg_salary', data=df)
    plt.xlabel("Job Description Length (characters)")
    plt.ylabel("Average Salary (€)")
    st.pyplot(plt.gcf())
    plt.clf()

    # -----------------------
    # 1️⃣1️⃣ Employer-provided vs estimated salaries
    # -----------------------
    st.subheader("Employer-provided vs Estimated Salaries")
    plt.figure(figsize=(8,6))
    sns.barplot(x='employer_provided', y='avg_salary', data=df, ci=None, palette='coolwarm')
    plt.xlabel("Salary Source")
    plt.ylabel("Average Salary (€)")
    st.pyplot(plt.gcf())
    plt.clf()

    # -----------------------
    # 1️⃣2️⃣ Number of competitors vs salary
    # -----------------------
    st.subheader("Number of Competitors vs Average Salary")
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='num_comp', y='avg_salary', data=df)
    plt.xlabel("Number of Competitors")
    plt.ylabel("Average Salary (€)")
    st.pyplot(plt.gcf())
    plt.clf()

    # -----------------------
    # 1️⃣ Salary by job role
    # -----------------------
    st.subheader("Salary Distribution by Job Role")
    plt.figure(figsize=(12,6))
    sns.boxplot(x='job_simp', y='avg_salary', data=df, palette='Set2')
    plt.xlabel("Job Role")
    plt.ylabel("Average Salary (€)")
    plt.xticks(rotation=45)
    st.pyplot(plt.gcf())
    plt.clf()

    # -----------------------
    # 2️⃣ Seniority level vs salary
    # -----------------------
    st.subheader("Salary by Seniority Level")
    plt.figure(figsize=(10,6))
    sns.boxplot(x='seniority', y='avg_salary', data=df, palette='Set3')
    plt.xlabel("Seniority Level")
    plt.ylabel("Average Salary (€)")
    st.pyplot(plt.gcf())
    plt.clf()

    # Optional: Bar chart for average salary per seniority
    st.subheader("Average Salary per Seniority Level")
    avg_salary_seniority = df.groupby('seniority')['avg_salary'].mean().sort_values(ascending=False)
    plt.figure(figsize=(8,5))
    sns.barplot(x=avg_salary_seniority.index, y=avg_salary_seniority.values, palette='Set1')
    plt.xlabel("Seniority Level")
    plt.ylabel("Average Salary (€)")
    st.pyplot(plt.gcf())
    plt.clf()

    # -----------------------
    # 3️⃣ Most demanded skills (% of jobs)
    # -----------------------
    st.subheader("Skill Demand (% of jobs requiring skill)")
    skill_cols = ['python_yn', 'R_yn', 'spark', 'aws', 'excel']
    skill_pct = df[skill_cols].mean() * 100
    plt.figure(figsize=(8,6))
    sns.barplot(x=skill_pct.index, y=skill_pct.values, palette='pastel')
    plt.ylabel("% of Jobs Requiring Skill")
    plt.xlabel("Skill")
    st.pyplot(plt.gcf())
    plt.clf()

    # -----------------------
    # 4️⃣ Skills vs average salary
    # -----------------------
    st.subheader("Average Salary for Jobs Requiring Each Skill")
    skill_avg_salary = {}
    for skill in skill_cols:
        if 1 in df[skill].unique():
            skill_avg_salary[skill] = df.groupby(skill)['avg_salary'].mean().loc[1]
    skill_avg_salary = pd.Series(skill_avg_salary).sort_values(ascending=False)
    plt.figure(figsize=(8,6))
    sns.barplot(x=skill_avg_salary.index, y=skill_avg_salary.values, palette='muted')
    plt.ylabel("Average Salary (€)")
    plt.xlabel("Skill")
    st.pyplot(plt.gcf())
    plt.clf()

    # -----------------------
    # 5️⃣ Company size influence on salary
    # -----------------------
    st.subheader("Salary Distribution by Company Size")
    plt.figure(figsize=(10,6))
    sns.boxplot(x='Size', y='avg_salary', data=df, palette='coolwarm')
    plt.xlabel("Company Size")
    plt.ylabel("Average Salary (€)")
    st.pyplot(plt.gcf())
    plt.clf()

    # -----------------------
    # 6️⃣ Company rating vs salary
    # -----------------------
    st.subheader("Company Rating vs Average Salary")
    plt.figure(figsize=(10,6))
    sns.scatterplot(x='Rating', y='avg_salary', data=df)
    sns.regplot(x='Rating', y='avg_salary', data=df, scatter=False, color='red')
    plt.xlabel("Company Rating")
    plt.ylabel("Average Salary (€)")
    st.pyplot(plt.gcf())
    plt.clf()

else:
    st.info("Please upload a CSV file to get started!")
