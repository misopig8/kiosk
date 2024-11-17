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

st.sidebar.title("키오스크 메뉴")
page = st.sidebar.selectbox("페이지 선택", ["고객용 페이지", "직원용 페이지"])
pg = st.navigation(pages)
pg.run()