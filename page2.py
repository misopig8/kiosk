import streamlit as st
import sqlite3

# 데이터베이스 연결 함수
def get_db_connection():
    return sqlite3.connect("orders.db", check_same_thread=False)

# 주문 상태 업데이트 함수
def update_order_status(order_id, completed):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE orders SET completed = ? WHERE rowid = ?",
        (completed, order_id),
    )
    conn.commit()
    conn.close()

# 주문 데이터 조회 함수
def fetch_orders():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, nickname, menu, option, quantity, completed FROM orders")
    orders = cursor.fetchall()
    conn.close()
    return orders

# Streamlit 앱
st.title("직원용 주문 관리 페이지")
st.subheader("현재 주문 목록")

# 주문 데이터 가져오기
orders = fetch_orders()

# 주문 목록 표시
if orders:
    for order in orders:
        order_id, nickname, menu, option, quantity, completed = order

        # 주문 카드 형식으로 표시
        st.markdown(
            f"""
            <div style="border: 1px solid #ccc; border-radius: 5px; padding: 10px; margin-bottom: 10px;">
                <strong>주문자:</strong> {nickname}<br>
                <strong>메뉴:</strong> {menu}<br>
                <strong>옵션:</strong> {option if option else "없음"}<br>
                <strong>수량:</strong> {quantity}<br>
                <strong>상태:</strong> {"완료" if completed else "미완료"}<br>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # 완료 여부 업데이트 버튼
        col1, col2 = st.columns(2)
        with col1:
            if not completed:
                if st.button(f"주문 완료 처리 (ID: {order_id})"):
                    update_order_status(order_id, True)
                    st.success(f"주문 ID {order_id}가 완료 처리되었습니다.")
        with col2:
            if completed:
                if st.button(f"완료 취소 (ID: {order_id})"):
                    update_order_status(order_id, False)
                    st.warning(f"주문 ID {order_id}가 미완료 상태로 변경되었습니다.")
else:
    st.info("현재 주문이 없습니다.")
