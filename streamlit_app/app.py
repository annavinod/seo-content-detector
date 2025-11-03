import streamlit as st
from utils.scorer import analyze_url
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import time

# ---- CONFIG ----
st.set_page_config(
    page_title="SEO Content Quality & Duplicate Detector",
    page_icon="🔍",
    layout="wide",
)

# ---- SIDEBAR ----
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Lead_Walnut_logo.png/120px-Lead_Walnut_logo.png", use_column_width=True)
st.sidebar.title("🔧 Navigation")
st.sidebar.markdown("**Sections:**")
st.sidebar.markdown("- Analyze Content\n- Readability & Keywords\n- Duplicate Detection\n")
st.sidebar.divider()
st.sidebar.info("📘 Built by [Anna Vinod](https://github.com/annavinod) for Lead Walnut Screening")

# ---- MAIN TITLE ----
st.markdown(
    "<h1 style='text-align:center; color:#2c3e50;'>🚀 SEO Content Quality & Duplicate Detector</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center; color:gray;'>Analyze webpage quality, readability, and duplication using NLP and ML</p>",
    unsafe_allow_html=True
)

url = st.text_input("🌐 **Enter a webpage URL to analyze:**", placeholder="https://example.com/article")

if st.button("Run Analysis 🚀"):
    with st.spinner("Analyzing content... Please wait."):
        time.sleep(1)
        result = analyze_url(url)

    st.success("✅ Analysis Complete!")

    # ---- Display Key Results ----
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📄 Title", result.get("title", "N/A"))
    with col2:
        st.metric("🧮 Word Count", result.get("word_count", 0))
    with col3:
        st.metric("🗣️ Sentence Count", result.get("sentence_count", 0))

    col4, col5, col6 = st.columns(3)
    with col4:
        st.metric("📊 Readability (Flesch)", round(result.get("readability", 0), 2))
    with col5:
        st.metric("🎯 Quality Label", result.get("quality", "Medium"))
    with col6:
        st.metric("🕵️ Duplicate Content", "❌ No" if not result.get("duplicate") else "⚠️ Possible Duplicate")

    st.divider()

    # ---- Keyword Cloud ----
    st.subheader("🔤 Keyword Cloud")
    text_content = result.get("content", "")
    if text_content:
        wc = WordCloud(width=900, height=400, background_color="white").generate(text_content)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(plt)

    # ---- Readability & Similarity Summary ----
    st.subheader("📈 Summary Statistics")
    st.write(f"- **Thin Content:** {'✅ No' if result.get('word_count', 0) > 500 else '⚠️ Yes (Low content)'}")
    st.write(f"- **Duplicate Probability:** {round(result.get('similarity', 0)*100, 2)}%")

    st.divider()

    # ---- Download Report ----
    df = pd.DataFrame([result])
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download Analysis Report (CSV)", csv, "seo_analysis.csv", "text/csv")

# ---- FOOTER ----
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>© 2025 Lead Walnut Assignment | Built with ❤️ by <a href='https://github.com/annavinod'>Anna Vinod</a></p>",
    unsafe_allow_html=True
)
