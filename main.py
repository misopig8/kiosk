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
        background-color: #f0f4fa; /* 배경색 변경 */
        padding: 20px;
    }
    [data-testid="stSidebar"] h1 {
        color: #4CAF50; /* 제목 색상 변경 */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 사이드바 내용
st.sidebar.image("https://via.placeholder.com/150", caption="부스 로고", use_column_width=True)
st.sidebar.title("키오스크 메뉴")

# 페이지 상단 헤더
st.markdown(
    """
    <style>
    .header {
        background-color: #4CAF50;
        padding: 20px;
        text-align: center;
        font-size: 30px;
        color: white;
    }
    </style>
    <div class="header">
        🎉 부스 키오스크 시스템 🎉
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="footer">
        문의: example@email.com | Instagram: @example_kiosk
    </div>
    """,
    unsafe_allow_html=True,
)