
import streamlit as st
import time

st.set_page_config(
    page_title="AI Bridge 留学生助手",
    page_icon="🌏",
    layout="wide"
)

# 页面样式
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
.stChatMessage {
    border-radius: 15px;
    padding: 10px;
}
.big-title {
    font-size: 42px;
    font-weight: bold;
    color: white;
}
.subtitle {
    font-size: 18px;
    color: #BBBBBB;
}
.feature-box {
    background-color: #1E2430;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# 知识库
knowledge_base = {
    "支付": "马来西亚常用 Visa、MasterCard、Touch'n Go、GrabPay，也支持支付宝和微信支付。",
    "交通": "推荐使用 Grab 打车，类似中国滴滴。",
    "饮食": "校园附近有中餐、马来餐和西餐，价格整体比国内略高。",
    "文化": "马来西亚是多元文化国家，需要尊重穆斯林文化。",
    "语言": "英语是主要交流语言，日常交流问题不大。",
    "学校": "赫瑞瓦特大学马来西亚校区拥有国际化教学环境。",
    "住宿": "建议优先选择学校宿舍或学校附近公寓。",
    "安全": "夜晚尽量避免独自前往偏僻区域，注意保管财物。"
}

# 页面顶部
st.markdown('<div class="big-title">🌏 AI Bridge 留学生助手</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">赴马来西亚交流学生跨文化适应智能助手</div>', unsafe_allow_html=True)

st.write("")

# 功能展示
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-box">
    <h3>💳 支付帮助</h3>
    <p>了解马来西亚支付方式与电子钱包。</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
    <h3>🚕 交通出行</h3>
    <p>Grab 打车、公交与出行建议。</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-box">
    <h3>🍜 留学生活</h3>
    <p>饮食、文化、住宿与安全问题。</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "你好！欢迎来到 AI Bridge，请输入你关于马来西亚留学的问题。"}
    ]

# 展示聊天
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 回答函数
def get_answer(question):
    q = question.lower()

    keyword_map = {
        "支付": ["支付", "花钱", "银行卡", "微信", "支付宝"],
        "交通": ["交通", "打车", "grab", "公交", "地铁"],
        "饮食": ["吃", "饭", "饮食", "餐厅", "外卖"],
        "文化": ["文化", "宗教", "穆斯林"],
        "语言": ["英语", "语言", "交流"],
        "学校": ["学校", "课程", "上课", "大学"],
        "住宿": ["宿舍", "租房", "住宿", "公寓"],
        "安全": ["安全", "危险", "晚上"]
    }

    for key, words in keyword_map.items():
        for w in words:
            if w in q:
                return knowledge_base[key]

    return "这个问题我还在学习中，你可以尝试换一种问法。"

# 输入框
prompt = st.chat_input("请输入你的问题...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    answer = get_answer(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        for chunk in answer:
            full_response += chunk
            time.sleep(0.02)
            message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": answer})
