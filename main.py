import streamlit as st
from page1 import customer_page
from page2 import staff_page

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

#     if page == "고객용 페이지":
#         customer_page()
#     elif page == "직원용 페이지":
#         staff_page()

# if __name__ == "__main__":
#     main()
