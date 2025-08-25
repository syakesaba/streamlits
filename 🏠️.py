import pathlib
import streamlit as st

st.set_page_config(page_title="HOME", page_icon="🏠️")
st.title("syakesaba.streamlit.app")
st.sidebar.markdown("ホームページです。各種Appが検索できます")

with st.spinner(text="検索画面を表示中..."):
    pages_dir = pathlib.Path(__file__).parent / "pages"
    pages = sorted([page.name for page in pages_dir.glob("*.py")])
    selected_page = st.selectbox(
        "🔎 Appを検索",
        options=pages,
        index=None,
        placeholder="検索文字列を入力...",
    )
    if selected_page is not None:
        st.switch_page(pages_dir / selected_page)

st.markdown(
    """
-----
- Source code: [https://github.com/syakesaba/streamlits](https://github.com/syakesaba/streamlits)
- Bussiness Contact: [https://www.syakesaba.com](https://www.syakesaba.com)
"""
)
