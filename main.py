import streamlit as st


st.set_page_config(
    page_title = "공돌제과🍬",
    page_icon = "🍪"
)
pages ={
    "주문" :[
        st.Page("page1.py", title="고객용"),
        st.Page("page2.py", title = "직원용")
    ]
}

pg = st.navigation(pages)
pg.run()

st.sidebar.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #CC9B50; /* 민트 그린 */
        padding: 20px;
    }
    [data-testid="stSidebar"] h1 {
        color: #6E4B3A; /* 제목 색상 변경 */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

backgroundColor="#FFECAE"
# 사이드바 내용
st.sidebar.image("https://via.placeholder.com/150", caption="부스 로고", use_column_width=True)
st.sidebar.title("키오스크 메뉴")

st.markdown(
    """
    <style>
    body {
        background-color: #F5F5DC;  /* 밀가루색 */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 페이지 상단 헤더
st.markdown(
    """
    <style>
    .header {
        background-color: #602b23;
        padding: 20px;
        text-align: center;
        font-size: 30px;
        color: black;
        font-family: 'Dohyeon', sans-serif;  /* 상단 헤더에만 Dohyeon 글꼴 적용 */
        font-weight: bold;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Dohyeon&display=swap" rel="stylesheet">  <!-- Dohyeon 글꼴 -->
    <div class="header">
        🍪 공돌제과 🍪
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="footer">
         Instagram: @wlgurrr | @igg_gineers
    </div>
    """,
    unsafe_allow_html=True,
)