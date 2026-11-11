

# ==========================================
# AI POWERED NEWS SUMMARIZATION SYSTEM
# STREAMLIT WEB APPLICATION
# ==========================================

import streamlit as st
import trafilatura

from urllib.parse import urlparse


from summarizer import (
    load_model,
    generate_summary,
    calculate_statistics
)



# 1. PAGE CONFIGURATION

st.set_page_config(
    page_title="AI News Summarizer",
    page_icon="📰",
    layout="wide"
)


# 2. CUSTOM DESIGN

st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
}

.main-title {
    font-size: 38px;
    font-weight: bold;
    color: #60A5FA;
}

.subtitle {
    font-size: 17px;
    color: #CBD5E1;
}

.result-box {
    background-color: #192638;
    padding: 20px;
    border-radius: 12px;
    line-height: 1.7;
}

</style>
""", unsafe_allow_html=True)


# 3. LOAD MODEL ONLY ONCE

@st.cache_resource
def get_model():

    return load_model()


# 4. HEADER

st.markdown(
    '<p class="main-title">📰 AI Powered News Summarization System</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Transform lengthy news articles into '
    'meaningful insights using DistilBART and NLP.</p>',
    unsafe_allow_html=True
)

st.divider()


# 5. URL INPUT

st.subheader("🔍 Enter News Article")

url = st.text_input(
    "News Article URL",
    placeholder="https://example.com/news-article"
)

generate_button = st.button(
    "🚀 Generate Summary",
    type="primary",
    use_container_width=True
)


# 6. PROCESS NEWS ARTICLE

if generate_button:

    if not url.strip():

        st.error("Please enter a news article URL.")

    else:

        parsed_url = urlparse(url.strip())

        if parsed_url.scheme not in ("http", "https") or not parsed_url.netloc:

            st.error("Please enter a valid HTTP or HTTPS article URL.")

        else:

            try:

                # Extract article

                with st.spinner("Extracting news article..."):

                    downloaded = trafilatura.fetch_url(url.strip())

                    if not downloaded:
                        st.error(
                            "Unable to access this article. "
                            "The website may be blocking automated requests."
                        )
                        st.stop()

                    article = trafilatura.extract(downloaded)

                    if not article or len(article.split()) < 30:
                        st.error(
                            "Could not extract enough article text. "
                            "Try another publicly accessible news article."
                        )
                        st.stop()


                # Load AI model

                with st.spinner(
                    "Loading DistilBART AI model... "
                    "This may take a few minutes the first time."
                ):

                    tokenizer, model = get_model()


                # Generate summary

                with st.spinner("AI is summarizing your news article..."):

                    summary = generate_summary(
                        article,
                        tokenizer,
                        model
                    )

                    statistics = calculate_statistics(
                        article,
                        summary
                    )


                # SUCCESS

                st.success("News summarization completed successfully!")

                st.divider()

                # Statistics

                st.subheader("📊 Summary Statistics")

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Original Words",
                    statistics["original_word_count"]
                )

                col2.metric(
                    "Summary Words",
                    statistics["summary_word_count"]
                )

                col3.metric(
                    "Compression",
                    f'{statistics["compression_ratio"]}%'
                )

                st.divider()

                # Display results

                st.subheader("📰 Article and AI Summary")

                col1, col2 = st.columns(2)

                with col1:

                    st.markdown("### Original Article")

                    st.text_area(
                        "Extracted Article",
                        article,
                        height=400,
                        disabled=True,
                        label_visibility="collapsed"
                    )

                with col2:

                    st.markdown("### 🤖 AI Generated Summary")

                    st.markdown(
                        f'<div class="result-box">{summary}</div>',
                        unsafe_allow_html=True
                    )

                # Download summary

                st.divider()

                st.download_button(
                    label="📥 Download Summary",
                    data=summary,
                    file_name="news_summary.txt",
                    mime="text/plain"
                )

            except Exception as e:

                st.error(f"An error occurred: {str(e)}")


# 7. FOOTER

st.divider()

st.caption(
    "Powered by DistilBART | PyTorch | Transformers | NLP | Streamlit"
)
