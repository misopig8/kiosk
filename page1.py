
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
    "코하쿠토 젤리 (5개입)": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.paris.co.kr%2Fproduct%2F%25EA%25B0%2593%25EA%25B5%25AC%25EC%259A%25B4-%25EC%25AB%2580%25EB%2593%259D%25EB%25B0%2594%25EC%2582%25AD-%25EC%259E%2590%25EC%259D%25B4%25EC%2596%25B8%25ED%258A%25B8-%25EC%258A%25A4%25EB%25AA%25A8%25EC%2596%25B4%25EC%25BF%25A0%25ED%2582%25A4%2F&psig=AOvVaw3qyiroYWUM9-PmpMo6fZRF&ust=1731911850265000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOiq48fg4okDFQAAAAAdAAAAABAE.jpg",
    "베이직 다이제 스모어쿠키": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.paris.co.kr%2Fproduct%2F%25EA%25B0%2593%25EA%25B5%25AC%25EC%259A%25B4-%25EC%25AB%2580%25EB%2593%259D%25EB%25B0%2594%25EC%2582%25AD-%25EC%259E%2590%25EC%259D%25B4%25EC%2596%25B8%25ED%258A%25B8-%25EC%258A%25A4%25EB%25AA%25A8%25EC%2596%25B4%25EC%25BF%25A0%25ED%2582%25A4%2F&psig=AOvVaw3qyiroYWUM9-PmpMo6fZRF&ust=1731911850265000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOiq48fg4okDFQAAAAAdAAAAABAE.jpg",
    "디자인 다이제 스모어쿠키": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.paris.co.kr%2Fproduct%2F%25EA%25B0%2593%25EA%25B5%25AC%25EC%259A%25B4-%25EC%25AB%2580%25EB%2593%259D%25EB%25B0%2594%25EC%2582%25AD-%25EC%259E%2590%25EC%259D%25B4%25EC%2596%25B8%25ED%258A%25B8-%25EC%258A%25A4%25EB%25AA%25A8%25EC%2596%25B4%25EC%25BF%25A0%25ED%2582%25A4%2F&psig=AOvVaw3qyiroYWUM9-PmpMo6fZRF&ust=1731911850265000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOiq48fg4okDFQAAAAAdAAAAABAE.jpg",
}

cols = st.columns(len(menu_data))
for i, (menu_name, image_url) in enumerate(menu_data.items()):
    with cols[i]:
        st.image(image_url, caption=menu_name, use_column_width=True)

# 메뉴 선택
st.subheader("메뉴 선택")

main_menu = st.selectbox("메뉴를 선택하세요", list(menu_data.keys()))

# 디자인 다이제 스모어쿠키의 옵션 추가
design_options = [
    "별",
    "경원",
    "이그지니어스",
    "닉네임",
]

order_details = []
if main_menu == "디자인 다이제 스모어쿠키":
    st.write("디자인 옵션을 선택하고 수량을 설정하세요.")
    for option in design_options:
        quantity = st.number_input(
            f"{option} 수량", min_value=0, max_value=3, step=1, key=option
        )
        if quantity > 0:
            order_details.append((main_menu, option, quantity))
else:
    # 다른 메뉴는 옵션 없이 수량만 선택
    quantity = st.number_input(
        "수량을 입력하세요", min_value=1, step=1, key=main_menu
    )
    order_details.append((main_menu, None, quantity))

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
