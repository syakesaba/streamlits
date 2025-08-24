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
ソースコード⇢ [https://github.com/syakesaba/streamlits](https://github.com/syakesaba/streamlits)

---
## こんにちは！ 👋 syakesaba です！

お金が無くても、時間が無くても、スキルさえなくても
アイデア一つで誰でもイノベーションを起こせるような
オープンなIT技術で作られた民主的なIT社会に夢見てます！

### プログラミング言語

Shell, C, Java, Pythonを経てGo, Rustを勉強中！

### IT系職歴

ネットワークエンジニア⇒インフラエンジニア⇒セキュリティエンジニア⇒データエンジニア

### IT系保有資格

- 情報処理推進機構
  - 基本情報技術者試験（FW）
  - 応用情報技術者試験（AP）
  - ネットワークスペシャリスト（NW）
  - セキュリティスペシャリスト（SC）

### Contact
🌍️ [https://www.syakesaba.com](https://www.syakesaba.com)
  
ITに関してであれば、何でもお仕事ご依頼ください！
"""
)
