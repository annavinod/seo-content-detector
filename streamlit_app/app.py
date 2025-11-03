import streamlit as st
from utils.scorer import analyze_url

st.set_page_config(page_title="SEO Content Quality Detector", layout="centered")

st.title("🔍 SEO Content Quality & Duplicate Detector")
st.markdown("Analyze webpage content quality, readability, and duplication.")

url = st.text_input("Enter a URL to analyze:")
if st.button("Analyze") and url:
    with st.spinner("Analyzing... please wait ⏳"):
        result = analyze_url(url)
    st.success("✅ Analysis Complete!")

    st.write("### 📄 Title:", result["title"])
    st.write("**Word Count:**", result["word_count"])
    st.write("**Sentence Count:**", result["sentence_count"])
    st.write("**Readability (Flesch):**", round(result["readability"], 2))
    st.write("**Quality Label:**", result["quality_label"])
    st.write("**Thin Content:**", "⚠️ Yes" if result["is_thin"] else "✅ No")

    if result["similar_to"]:
        st.subheader("🔁 Similar Pages Detected")
        for sim in result["similar_to"]:
            st.write(f"- [{sim['url']}]({sim['url']}) — Similarity: **{sim['similarity']:.2f}**")
    else:
        st.info("No significant duplicate content found.")
