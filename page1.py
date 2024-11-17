import streamlit as st
import sqlite3

# 데이터베이스 연결 함수
def get_db_connection():
    return sqlite3.connect("orders.db", check_same_thread=False)

# 테이블 생성 함수
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            nickname TEXT,
            menu TEXT,
            option TEXT DEFAULT '',
            quantity INTEGER,
            completed BOOLEAN
        )
    ''')
    conn.commit()
    conn.close()

# 테이블 생성 실행
create_table()

# Streamlit 앱 제목 및 서브타이틀
st.title("고객용 페이지")
st.subheader("메뉴 안내")

# 메뉴 데이터
menu_data = {
    "코하쿠토 젤리 (5개입)": "https://www.example.com/jelly.jpg",  # 이미지 URL을 실제 링크로 교체
    "베이직 다이제 스모어쿠키": "https://www.example.com/basic_cookie.jpg",
    "디자인 다이제 스모어쿠키": "https://www.example.com/design_cookie.jpg",
}

# 메뉴를 카드 형식으로 표시
st.subheader("메뉴 선택")
for menu_name, image_url in menu_data.items():
    st.markdown(
        f"""
        <div style="border: 2px solid #f0f4fa; border-radius: 10px; padding: 10px; margin-bottom: 10px; display: flex; align-items: center;">
            <img src="{image_url}" style="width: 100px; height: auto; margin-right: 20px;">
            <div>
                <h4 style="margin: 0;">{menu_name}</h4>
                <p style="color: #777;">가격: 3,000원</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# 주문 관련 입력
order_details = []  # 주문 정보 저장
nickname = st.text_input("닉네임을 입력하세요")

# 코하쿠토 젤리 주문
st.subheader("코하쿠토 젤리 (5개입)")
jelly_quantity = st.number_input("수량 입력", min_value=0, step=1, key="jelly")
if jelly_quantity > 0:
    order_details.append(("코하쿠토 젤리 (5개입)", None, jelly_quantity))

# 베이직 다이제 스모어쿠키 주문
st.subheader("베이직 다이제 스모어쿠키")
basic_quantity = st.number_input("수량 입력", min_value=0, step=1, key="basic")
if basic_quantity > 0:
    order_details.append(("베이직 다이제 스모어쿠키", None, basic_quantity))

# 디자인 다이제 스모어쿠키 주문
st.subheader("디자인 다이제 스모어쿠키 옵션 선택")
design_options = {
    "별": "https://www.example.com/star_option.jpg",
    "하트": "https://www.example.com/heart_option.jpg",
    "닉네임": "https://www.example.com/flower_option.jpg",
}

selected_design = st.selectbox("디자인 선택", list(design_options.keys()))
st.image(design_options[selected_design], caption=f"디자인: {selected_design}")

design_quantity = st.number_input(
    f"{selected_design} 수량", min_value=0, step=1, key="design"
)
if design_quantity > 0:
    order_details.append(("디자인 다이제 스모어쿠키", selected_design, design_quantity))

# 주문 저장
if st.button("주문하기"):
    if nickname:
        conn = get_db_connection()
        cursor = conn.cursor()
        for menu, option, quantity in order_details:
            cursor.execute(
                "INSERT INTO orders (nickname, menu, option, quantity, completed) VALUES (?, ?, ?, ?, ?)",
                (nickname, menu, option if option else "", quantity, False),
            )
        conn.commit()
        conn.close()
        st.success("주문이 저장되었습니다.")
    else:
        st.error("닉네임을 입력해 주세요.")
