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

# 메뉴 데이터 (임시 URL 사용)
menu_data = {
    "코하쿠토 젤리 (5개입)": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.paris.co.kr%2Fproduct%2F%25EA%25B0%2593%25EA%25B5%25AC%25EC%259A%25B4-%25EC%25AB%2580%25EB%2593%259D%25EB%25B0%2594%25EC%2582%25AD-%25EC%259E%2590%25EC%259D%25B8%25ED%258A%25B8-%25EC%258A%25A4%25EB%25AA%25A8%25EC%2596%25B4%25EC%25BF%25A0%25ED%2582%25A4%2F&psig=AOvVaw3qyiroYWUM9-PmpMo6fZRF&ust=1731911850265000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOiq48fg4okDFQAAAAAdAAAAABAE",
    "베이직 다이제 스모어쿠키": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.paris.co.kr%2Fproduct%2F%25EA%25B0%2593%25EA%25B5%25AC%25EC%259A%25B4-%25EC%25AB%2580%25EB%2593%259D%25EB%25B0%2594%25EC%2582%25AD-%25EC%259E%2590%25EC%259D%25B8%25ED%258A%25B8-%25EC%258A%25A4%25EB%25AA%25A8%25EC%2596%25B4%25EC%25BF%25A0%25ED%2582%25A4%2F&psig=AOvVaw3qyiroYWUM9-PmpMo6fZRF&ust=1731911850265000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOiq48fg4okDFQAAAAAdAAAAABAE",
    "디자인 다이제 스모어쿠키": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.paris.co.kr%2Fproduct%2F%25EA%25B0%2593%25EA%25B5%25AC%25EC%259A%25B4-%25EC%25AB%2580%25EB%2593%259D%25EB%25B0%2594%25EC%2582%25AD-%25EC%259E%2590%25EC%259D%25B8%25ED%258A%25B8-%25EC%258A%25A4%25EB%25AA%25A8%25EC%2596%25B4%25EC%25BF%25A0%25ED%2582%25A4%2F&psig=AOvVaw3qyiroYWUM9-PmpMo6fZRF&ust=1731911850265000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOiq48fg4okDFQAAAAAdAAAAABAE",
}
st.subheader("메뉴 선택")
    
    # 메뉴 이미지와 가격 데이터를 정의합니다.
menu_data = {
        "스모어쿠키": "https://www.paris.co.kr/product/somecookie.jpg",  # 실제 이미지 링크로 교체
        "코하쿠토 젤리": "https://www.paris.co.kr/product/jelly.jpg",
        "디자인 스모어쿠키": "https://www.paris.co.kr/product/designcookie.jpg",
    }

    # 메뉴를 카드 형식으로 나열
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
    "별": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.paris.co.kr%2Fproduct%2F%25EA%25B0%2593%25EA%25B5%25AC%25EC%259A%25B4-%25EC%25AB%2580%25EB%2593%259D%25EB%25B0%2594%25EC%2582%25AD-%25EC%259E%2590%25EC%259D%25B8%25ED%258A%25B8-%25EC%258A%25A4%25EB%25AA%25A8%25EC%2596%25B4%25EC%25BF%25A0%25ED%2582%25A4%2F&psig=AOvVaw3qyiroYWUM9-PmpMo6fZRF&ust=1731911850265000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOiq48fg4okDFQAAAAAdAAAAABAE",
    "경원": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaZ6C0UvsxxSEHPYLZYC53PhcWfAR2GXf45Q&s",
    "이그지니어스": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.paris.co.kr%2Fproduct%2F%25EA%25B0%2593%25EA%25B5%25AC%25EC%259A%25B4-%25EC%25AB%2580%25EB%2593%259D%25EB%25B0%2594%25EC%2582%25AD-%25EC%259E%2590%25EC%259D%25B8%25ED%258A%25B8-%25EC%258A%25A4%25EB%25AA%25A8%25EC%2596%25B4%25EC%25BF%25A0%25ED%2582%25A4%2F&psig=AOvVaw3qyiroYWUM9-PmpMo6fZRF&ust=1731911850265000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOiq48fg4okDFQAAAAAdAAAAABAE",
    "닉네임": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.paris.co.kr%2Fproduct%2F%25EA%25B0%2593%25EA%25B5%25AC%25EC%259A%25B4-%25EC%25AB%2580%25EB%2593%259D%25EB%25B0%2594%25EC%2582%25AD-%25EC%259E%2590%25EC%259D%25B8%25ED%258A%25B8-%25EC%258A%25A4%25EB%25AA%25A8%25EC%2596%25B4%25EC%25BF%25A0%25ED%2582%25A4%2F&psig=AOvVaw3qyiroYWUM9-PmpMo6fZRF&ust=1731911850265000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCOiq48fg4okDFQAAAAAdAAAAABAE",
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
