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