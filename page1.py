import streamlit as st
import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS orders 
                  (nickname TEXT, menu TEXT, option TEXT, quantity INTEGER, completed BOOLEAN)''')
conn.commit()

# 상단에 모든 메뉴 나열 (이름과 사진)
st.title("고객용 페이지")
st.subheader("메뉴 안내")

menu_data = {
    "코하쿠토 젤리 (5개입)": "url_to_image1.jpg",
    "베이직 다이제 스모어쿠키": "url_to_image2.jpg",
    "디자인 다이제 스모어쿠키": "url_to_image3.jpg",
}

cols = st.columns(len(menu_data))
for i, (menu_name, image_url) in enumerate(menu_data.items()):
    with cols[i]:
        st.image(image_url, caption=menu_name, use_column_width=True)

# 주문 데이터 저장용 리스트
order_details = []

# 코하쿠토 젤리
st.subheader("코하쿠토 젤리 (5개입)")
jelly_quantity = st.number_input("수량 입력", min_value=0, step=1, key="jelly")
if jelly_quantity > 0:
    order_details.append(("코하쿠토 젤리 (5개입)", None, jelly_quantity))

# 베이직 다이제 스모어쿠키
st.subheader("베이직 다이제 스모어쿠키")
basic_quantity = st.number_input("수량 입력", min_value=0, step=1, key="basic")
if basic_quantity > 0:
    order_details.append(("베이직 다이제 스모어쿠키", None, basic_quantity))

# 디자인 다이제 스모어쿠키
st.subheader("디자인 다이제 스모어쿠키 옵션 선택")
design_options = {
    "별": "url_to_star_image.jpg",
    "경원": "url_to_kyungwon_image.jpg",
    "이그지니어스": "url_to_engineer_image.jpg",
    "닉네임": "url_to_custom_image.jpg",
}

selected_design = st.selectbox("디자인 선택", list(design_options.keys()))
st.image(design_options[selected_design], caption=f"디자인: {selected_design}")

design_quantity = st.number_input(
    f"{selected_design} 수량", min_value=0, max_value=3, step=1, key="design"
)
if design_quantity > 0:
    order_details.append(("디자인 다이제 스모어쿠키", selected_design, design_quantity))

# 닉네임 입력
nickname = st.text_input("닉네임을 입력하세요")

# 주문 저장
if st.button("주문하기"):
    if nickname:
        for menu, option, quantity in order_details:
            cursor.execute(
                "INSERT INTO orders (nickname, menu, option, quantity, completed) VALUES (?, ?, ?, ?, ?)",
                (nickname, menu, option, quantity, False),
            )
        conn.commit()
        st.success("주문이 저장되었습니다.")
    else:
        st.error("닉네임을 입력해 주세요.")

conn.close()
