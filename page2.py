# import streamlit as st
# import sqlite3

# # 데이터베이스 연결 함수
# def get_db_connection():
#     return sqlite3.connect("orders.db", check_same_thread=False)

# # 주문 상태 업데이트 함수
# def update_order_status(order_id, completed):
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute(
#         "UPDATE orders SET completed = ? WHERE rowid = ?",
#         (completed, order_id),
#     )
#     conn.commit()
#     conn.close()

# # 주문 데이터 조회 함수
# def fetch_orders():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT rowid, nickname, menu, option, quantity, completed FROM orders")
#     orders = cursor.fetchall()
#     conn.close()
#     return orders

# # Streamlit 앱
# st.title("직원용 주문 관리 페이지")
# st.subheader("현재 주문 목록")

# # 주문 데이터 가져오기
# orders = fetch_orders()

# # 주문 목록 표시
# if orders:
#     for order in orders:
#         order_id, nickname, menu, option, quantity, completed = order

#         # 주문 카드 형식으로 표시
#         st.markdown(
#             f"""
#             <div style="border: 1px solid #ccc; border-radius: 5px; padding: 10px; margin-bottom: 10px;">
#                 <strong>주문자:</strong> {nickname}<br>
#                 <strong>메뉴:</strong> {menu}<br>
#                 <strong>옵션:</strong> {option if option else "없음"}<br>
#                 <strong>수량:</strong> {quantity}<br>
#                 <strong>상태:</strong> {"완료" if completed else "미완료"}<br>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#         # 완료 여부 업데이트 버튼
#         col1, col2 = st.columns(2)
#         with col1:
#             if not completed:
#                 if st.button(f"주문 완료 처리 (ID: {order_id})"):
#                     update_order_status(order_id, True)
#                     st.success(f"주문 ID {order_id}가 완료 처리되었습니다.")
#         with col2:
#             if completed:
#                 if st.button(f"완료 취소 (ID: {order_id})"):
#                     update_order_status(order_id, False)
#                     st.warning(f"주문 ID {order_id}가 미완료 상태로 변경되었습니다.")
# else:
#     st.info("현재 주문이 없습니다.")

import streamlit as st
import sqlite3

# 비밀번호 설정
ADMIN_PASSWORD = "wlgurrr123"

# 데이터베이스 초기화 함수
def initialize_db():
    with sqlite3.connect("orders.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS orders 
                          (nickname TEXT, menu TEXT, option TEXT, quantity INTEGER, completed BOOLEAN)''')
        conn.commit()

# 주문 상태 업데이트 함수
def update_order_status(order_id, status):
    with sqlite3.connect("orders.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE orders SET completed = ? WHERE rowid = ?",
            (status, order_id),
        )
        conn.commit()

# 데이터베이스 초기화
initialize_db()

# 비밀번호 입력
st.title("직원용 페이지")
password = st.text_input("비밀번호를 입력하세요", type="password")

if password == ADMIN_PASSWORD:
    st.success("접속 성공! 주문 내역을 확인하세요.")
    
    # 데이터베이스에서 주문 내역 가져오기
    with sqlite3.connect("orders.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT rowid, nickname, menu, option, quantity, completed FROM orders")
        orders = cursor.fetchall()

    # 주문 내역 표시
    if orders:
        for order in orders:
            rowid, nickname, menu, option, quantity, completed = order
            st.markdown(f"**주문번호:** {rowid}")
            st.markdown(f"**닉네임:** {nickname}")
            st.markdown(f"**메뉴:** {menu}")
            st.markdown(f"**옵션:** {option if option else '없음'}")
            st.markdown(f"**수량:** {quantity}")
            status = "완료" if completed else "미완료"
            st.markdown(f"**상태:** {status}")

            # 완료 여부 수정
            new_status = st.checkbox(
                "주문 완료 표시", value=completed, key=f"completed_{rowid}"
            )
            if new_status != completed:
                update_order_status(rowid, new_status)
                st.experimental_rerun()

            st.markdown("---")
    else:
        st.info("현재 저장된 주문 내역이 없습니다.")
else:
    if password:
        st.error("비밀번호가 틀렸습니다.")
    else:
        st.info("비밀번호를 입력하세요.")
