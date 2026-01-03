import streamlit as st
import os
from PIL import Image

# 1. 페이지 설정
st.set_page_config(
    page_title="Tether Back Premium Calculator",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 고급 CSS 적용
st.markdown("""
    <style>
    /* Base Fonts & Colors */
    .stApp { background-color: #0E1117; color: #FAFAFA; font-family: 'Inter', sans-serif; }
    h1, h2, h3, h4 { letter-spacing: -0.5px; }
    
    /* Card Design */
    .css-card {
        background: linear-gradient(180deg, #161B22 0%, #0D1117 100%);
        border: 1px solid rgba(48, 54, 61, 0.6);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
    }
    .css-card:hover {
        transform: translateY(-2px);
        border-color: rgba(46, 160, 67, 0.5);
        box-shadow: 0 14px 40px rgba(46, 160, 67, 0.15);
    }

    /* Partner Box Styling */
    .partner-box {
        background-color: rgba(33, 38, 45, 0.5);
        border: 1px solid rgba(48, 54, 61, 0.8);
        border-radius: 12px;
        padding: 18px;
        margin-top: 10px;
    }
    
    /* 파트너 링크 스타일 */
    .partner-link {
        text-decoration: none;
        color: #E6EDF3;
        font-weight: 500;
        display: block;
        margin-bottom: 8px;
        transition: color 0.2s ease, transform 0.2s ease;
    }
    .partner-link:hover {
        color: #2EA043; /* Tether Back Green */
        transform: translateX(5px);
    }

    /* Link Button Styling */
    .stLinkButton > a {
        width: 100%;
        background: linear-gradient(90deg, #238636 0%, #2EA043 100%);
        color: white !important;
        border: none;
        border-radius: 12px;
        height: 56px;
        font-size: 18px;
        font-weight: 700;
        box-shadow: 0 4px 12px rgba(46, 160, 67, 0.4);
        transition: all 0.2s ease;
        text-decoration: none;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .stLinkButton > a:hover {
        filter: brightness(1.1);
        transform: scale(1.01);
        box-shadow: 0 6px 16px rgba(46, 160, 67, 0.6);
        color: white !important;
    }
    .stLinkButton > a:active { transform: translateY(1px); }

    /* Metric Value Colors */
    div[data-testid="stMetricValue"] { font-size: 26px; font-weight: 700; }
    
    /* Input Fields adjustment */
    .stNumberInput input { background-color: #0D1117; }
    </style>
""", unsafe_allow_html=True)

# 3. 헤더 영역
st.divider()

col_logo, col_title = st.columns([1, 4])
logo_filename = 'logo.png' 

with col_logo:
    if os.path.exists(logo_filename):
        try:
            image = Image.open(logo_filename)
            st.image(image, use_container_width=True)
        except:
            st.empty()
    else:
        st.empty()

with col_title:
    st.title("Tether Back Calculator")
    st.markdown("""
    <p style='font-size: 18px; color: #8B949E; margin-top: -10px;'>
    "Phí giao dịch là chi phí vô hình. Tối ưu đúng cách, nó trở thành lợi nhuận." 
    <br><span style='font-size: 14px; opacity: 0.8;'>(Transaction fees are invisible costs. Optimized correctly, they become profit.)</span>
    </p>
    """, unsafe_allow_html=True)

st.divider()

# 4. 메인 레이아웃
col_input, col_result = st.columns([1, 1.4], gap="large")

# --- 좌측: 입력 (Inputs) ---
with col_input:
    st.markdown('<div class="css-card">', unsafe_allow_html=True)
    st.subheader("⚙️ Thiết lập giao dịch (Settings)")
    st.caption("Nhập thông tin giao dịch của bạn để tính toán.")
    
    seed_money = st.number_input("💰 Vốn ban đầu (USDT)", value=1000, step=100, min_value=100)
    leverage = st.slider("⚡ Đòn bẩy (Leverage)", 1, 125, 10)
    
    c1, c2 = st.columns(2)
    with c1:
        trade_count = st.number_input("🔄 Số lệnh/ngày", value=2, min_value=1)
    with c2:
        fee_rate = st.number_input("📉 Phí (%) - (Ví dụ: 0.04)", value=0.04, format="%.4f", step=0.01)
    
    if fee_rate > 1:
        st.warning("⚠️ Chú ý: 1% là mức phí rất cao. Hãy kiểm tra lại (0.04% = 0.04).")
    
    st.markdown("<br>", unsafe_allow_html=True)
    exchange_rate = st.number_input("🇻🇳 Tỷ giá (VND/USDT)", value=25450, step=50, help="Tỷ giá thị trường hiện tại")

    st.markdown("---")
    
    # [수정 완료] 파트너 링크 업데이트
    st.markdown("##### 🤝 Đối tác chiến lược (Strategic Partners)")
    st.markdown("""
    <div class="partner-box">
        <div style="margin-bottom: 10px;">
            <a href="https://www.binance.com/join?ref=TETHERBACK20" target="_blank" class="partner-link">
                🔶 Binance Official <span style="font-size: 12px; color: #8B949E;">(Click)</span>
            </a>
            <a href="https://partner.bybit.com/b/TETHERBACK" target="_blank" class="partner-link">
                ⚫ Bybit Official <span style="font-size: 12px; color: #8B949E;">(Click)</span>
            </a>
            <a href="https://partner.bitget.com/bg/TBack20" target="_blank" class="partner-link">
                🔵 Bitget Official <span style="font-size: 12px; color: #8B949E;">(Click)</span>
            </a>
            <a href="https://okx.com/join/TETHERBACK" target="_blank" class="partner-link">
                ⚫ OKX Official <span style="font-size: 12px; color: #8B949E;">(Click)</span>
            </a>
        </div>
        <div style="margin-top: 15px; font-size: 13px; color: #2EA043; font-weight: bold; background: rgba(46,160,67,0.1); padding: 8px; border-radius: 6px; text-align: center;">
            ✨ Verified VIP Partner Link
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- 계산 로직 ---
one_trade_volume = seed_money * leverage
standard_fee_per_trade = one_trade_volume * (fee_rate / 100)
monthly_standard_fee = standard_fee_per_trade * trade_count * 30

discount_amount = monthly_standard_fee * 0.20
real_fee_paid = monthly_standard_fee - discount_amount
payback_amount_usdt = real_fee_paid * 0.20

total_benefit_usdt = discount_amount + payback_amount_usdt
total_benefit_vnd = total_benefit_usdt * exchange_rate

# --- 우측: 결과 ---
with col_result:
    st.markdown('<div class="css-card">', unsafe_allow_html=True)
    
    st.subheader("📊 Báo cáo lợi nhuận (Profit Report)")
    st.markdown("Nếu tham gia **Tether Back**, bạn sẽ nhận được:")
    st.markdown("<br>", unsafe_allow_html=True)

    c_fee, c_disc, c_pay = st.columns(3)
    with c_fee:
        st.metric(label="Phí tiêu chuẩn (Tháng)", value=f"{monthly_standard_fee:,.0f} USDT")
    with c_disc:
        st.metric(label="Giảm phí (20%)", value=f"-{discount_amount:,.1f} USDT", delta="Tiết kiệm ngay")
    with c_pay:
        st.metric(label="Hoàn tiền (20%)", value=f"+{payback_amount_usdt:,.1f} USDT", delta="Hoàn trả ví")
    
    st.markdown("---")
    
    c_total_usdt, c_total_vnd = st.columns(2)
    with c_total_usdt:
        st.metric(label="🔥 Tổng lợi ích (USDT)", value=f"{total_benefit_usdt:,.2f} USDT")
        st.caption("Discount + Payback")
    with c_total_vnd:
        st.markdown(f"""
        <p style="margin-bottom: 0px; font-size: 14px; color: #8B949E;">Tổng lợi ích (Quy đổi VND)</p>
        <p style="font-size: 32px; font-weight: 800; color: #2EA043; margin: 0;">{total_benefit_vnd:,.0f} ₫</p>
        <p style="font-size: 12px; color: #2EA043;">(Mỗi tháng)</p>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="css-card" style="text-align: center; border-color: #238636;">', unsafe_allow_html=True)
    st.markdown("""
    <h3 style="margin-bottom: 10px;">🚀 Bắt đầu tối ưu hóa lợi nhuận ngay</h3>
    <p style="color: #8B949E; margin-bottom: 20px;">Đừng để phí giao dịch ăn mòn tài khoản của bạn.</p>
    """, unsafe_allow_html=True)
    
    st.link_button("👉 Đăng ký tài khoản Partner (Nhận ưu đãi VIP)", "https://t.me/Tether_Back_Official")
    
    st.markdown('</div>', unsafe_allow_html=True)
