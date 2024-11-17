import streamlit as st
import sqlite3

st.set_page_config(
    page_title = "공돌제과🍬",
    page_icon = "🍪"
)

def customer_page():
    st.title("고객용 페이지")

    # 데이터베이스 연결
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders 
                      (nickname TEXT, menu TEXT, quantity INTEGER, completed BOOLEAN)''')
    conn.commit()

    # 메뉴와 가격을 나열
    st.subheader("메뉴 선택")
    menu_items = {
        "스모어쿠키": 3000,
        "초코쿠키": 2500,
        "오트밀쿠키": 2000
    }

    selected_menu = st.selectbox("메뉴를 선택하세요", list(menu_items.keys()))
    quantity = st.number_input("수량을 입력하세요", min_value=1, step=1)

    # 닉네임 설정
    nickname = st.text_input("닉네임을 입력하세요")

    if st.button("주문하기"):
        if nickname:
            cursor.execute("INSERT INTO orders (nickname, menu, quantity, completed) VALUES (?, ?, ?, ?)",
                           (nickname, selected_menu, quantity, False))
            conn.commit()
            st.success("주문이 저장되었습니다.")
        else:
            st.error("닉네임을 입력해 주세요.")

    conn.close()
