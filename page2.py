import streamlit as st
import sqlite3


st.title("직원용 페이지")

    # 데이터베이스 연결
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

    # 비밀번호 입력
password = st.text_input("직원 비밀번호를 입력하세요", type="password")
if password == "wlgurrr":  # 실제로는 환경 변수나 더 안전한 방식으로 처리
        st.success("비밀번호가 확인되었습니다.")

        # 모든 주문 데이터 가져오기
        cursor.execute("SELECT rowid, nickname, menu, quantity, completed FROM orders")
        orders = cursor.fetchall()

        # 주문 목록 표시
        for order in orders:
            rowid, nickname, menu, quantity, completed = order
            status = "완료" if completed else "미완료"
            if st.checkbox(f"{nickname} - {menu} ({quantity}개) / 상태: {status}", key=rowid, value=completed):
                cursor.execute("UPDATE orders SET completed = ? WHERE rowid = ?", (True, rowid))
                conn.commit()

conn.close()
