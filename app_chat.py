# ============================================================
# app_chat.py - 카톡 같은 채팅 화면 (AI 없이 따라 말하는 앵무새 봇, 사용료 0원!)
# ============================================================
import streamlit as st

st.title("채팅 앱")

# 사물함(session_state)에 '대화 기록장' 만들기 - 다시 실행돼도 대화가 남아요
if "messages" not in st.session_state:
    st.session_state.messages = []

# 화면 맨 아래 입력창 (엔터를 치면 text 에 글이 들어오고, 안 치면 None 이에요)
text = st.chat_input("메시지를 입력하세요")
if text:
    st.session_state.messages.append({"role": "user", "text": text})                        # 내 말 적기
    st.session_state.messages.append({"role": "assistant", "text": f"{text} (따라 말하기!)"})   # 봇 대답 적기

# 기록장의 대화를 처음부터 차례대로 말풍선으로 그려요 (다시 실행될 때마다 새로 그려요)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):      # role: "user" = 나, "assistant" = 봇 (말풍선 아이콘이 달라져요)
        st.write(msg["text"])
