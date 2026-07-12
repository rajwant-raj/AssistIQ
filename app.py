

import streamlit as st
import time
from datetime import datetime


# ─────────────────────────────────────────────
# PAGE CONFIGURATION
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="AssistIQ",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ─────────────────────────────────────────────
# CUSTOM CSS — Premium Dark Glassmorphism Theme
# ─────────────────────────────────────────────
def load_css():
    """Inject custom CSS for a premium dark glassmorphism UI."""
    st.markdown(
        """
        <style>
        /* ── Google Fonts ── */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

        /* ── Global Reset ── */
        * { font-family: 'Inter', sans-serif; box-sizing: border-box; }

        /* ── Animated Background ── */
        .stApp {
            background: #0d0d1a;
            background-image:
                radial-gradient(ellipse at 20% 20%, rgba(124,58,237,0.18) 0%, transparent 50%),
                radial-gradient(ellipse at 80% 80%, rgba(6,182,212,0.14) 0%, transparent 50%),
                radial-gradient(ellipse at 50% 50%, rgba(16,16,40,1) 0%, #0d0d1a 100%);
            min-height: 100vh;
        }

        /* ── Hide Streamlit Branding ── */
        #MainMenu, footer, header { visibility: hidden; }

        /* ── Scrollbar ── */
        ::-webkit-scrollbar { width: 5px; }
        ::-webkit-scrollbar-track { background: rgba(255,255,255,0.03); }
        ::-webkit-scrollbar-thumb { background: rgba(124,58,237,0.4); border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: rgba(124,58,237,0.7); }

        /* ── Sidebar ── */
        [data-testid="stSidebar"] {
            background: rgba(13,13,26,0.95) !important;
            border-right: 1px solid rgba(124,58,237,0.2) !important;
            backdrop-filter: blur(20px);
        }
        [data-testid="stSidebar"] * { color: #e2e8f0 !important; }
        [data-testid="stSidebar"] .stMarkdown h1,
        [data-testid="stSidebar"] .stMarkdown h2,
        [data-testid="stSidebar"] .stMarkdown h3 { color: #f1f5f9 !important; }
        [data-testid="stSidebar"] hr { border-color: rgba(124,58,237,0.25) !important; }

        /* ── Main area text defaults ── */
        .stMarkdown, .stMarkdown p, .stMarkdown li { color: #e2e8f0 !important; }
        h1, h2, h3, h4 { color: #f1f5f9 !important; }

        /* ── Main Header Card ── */
        .header-card {
            background: linear-gradient(135deg,
                rgba(124,58,237,0.9) 0%,
                rgba(109,40,217,0.85) 40%,
                rgba(6,182,212,0.8) 100%);
            border-radius: 24px;
            padding: 32px 40px;
            margin-bottom: 28px;
            text-align: center;
            box-shadow:
                0 0 0 1px rgba(124,58,237,0.3),
                0 20px 60px rgba(124,58,237,0.35),
                0 0 80px rgba(6,182,212,0.1) inset;
            position: relative;
            overflow: hidden;
        }
        .header-card::before {
            content: '';
            position: absolute;
            top: -60px; right: -60px;
            width: 220px; height: 220px;
            background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 70%);
            border-radius: 50%;
            animation: orb-float 6s ease-in-out infinite;
        }
        .header-card::after {
            content: '';
            position: absolute;
            bottom: -40px; left: -40px;
            width: 160px; height: 160px;
            background: radial-gradient(circle, rgba(6,182,212,0.15) 0%, transparent 70%);
            border-radius: 50%;
            animation: orb-float 8s ease-in-out infinite reverse;
        }
        @keyframes orb-float {
            0%, 100% { transform: translateY(0px) scale(1); }
            50% { transform: translateY(-12px) scale(1.05); }
        }
        .header-card h1 {
            font-family: 'Outfit', sans-serif;
            color: #ffffff !important;
            font-size: 2.2rem;
            font-weight: 800;
            margin: 0;
            letter-spacing: -0.5px;
            text-shadow: 0 2px 20px rgba(124,58,237,0.5);
        }
        .header-card p {
            color: rgba(255,255,255,0.8);
            font-size: 1rem;
            margin: 8px 0 0 0;
            font-weight: 300;
            letter-spacing: 0.3px;
        }
        .logo-circle {
            width: 76px; height: 76px;
            background: rgba(255,255,255,0.15);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.2rem;
            margin: 0 auto 16px auto;
            border: 2px solid rgba(255,255,255,0.3);
            backdrop-filter: blur(10px);
            box-shadow: 0 0 30px rgba(124,58,237,0.4);
            animation: logo-pulse 3s ease-in-out infinite;
        }
        @keyframes logo-pulse {
            0%, 100% { box-shadow: 0 0 20px rgba(124,58,237,0.4); }
            50% { box-shadow: 0 0 40px rgba(6,182,212,0.5), 0 0 20px rgba(124,58,237,0.3); }
        }

        /* ── Section Headings ── */
        .section-heading {
            font-family: 'Outfit', sans-serif;
            font-size: 1rem;
            font-weight: 600;
            color: #c4b5fd !important;
            letter-spacing: 0.3px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        /* ── Chat Container ── */
        .chat-container {
            background: rgba(255,255,255,0.03);
            border-radius: 20px;
            padding: 24px;
            min-height: 420px;
            max-height: 520px;
            overflow-y: auto;
            box-shadow: 0 0 0 1px rgba(124,58,237,0.15), 0 8px 32px rgba(0,0,0,0.4);
            border: 1px solid rgba(124,58,237,0.12);
            margin-bottom: 18px;
            scroll-behavior: smooth;
            backdrop-filter: blur(12px);
        }

        /* ── Chat Bubbles ── */
        .chat-msg-row {
            display: flex;
            margin-bottom: 16px;
            align-items: flex-end;
            gap: 10px;
        }
        .chat-msg-row.user { flex-direction: row-reverse; }

        .avatar {
            width: 38px; height: 38px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.1rem;
            flex-shrink: 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
        .avatar-bot {
            background: linear-gradient(135deg, #0891b2, #06b6d4);
            border: 2px solid rgba(6,182,212,0.4);
        }
        .avatar-user {
            background: linear-gradient(135deg, #7c3aed, #6d28d9);
            border: 2px solid rgba(124,58,237,0.4);
        }

        .bubble-wrapper { max-width: 74%; }
        .bubble-wrapper.user { align-items: flex-end; }
        .bubble-wrapper.bot  { align-items: flex-start; }

        .bubble {
            padding: 13px 17px;
            border-radius: 20px;
            font-size: 0.91rem;
            line-height: 1.6;
            word-wrap: break-word;
            position: relative;
        }
        .bubble.bot {
            background: rgba(6,182,212,0.1);
            color: #e2e8f0;
            border-bottom-left-radius: 5px;
            border: 1px solid rgba(6,182,212,0.2);
            box-shadow: 0 4px 16px rgba(6,182,212,0.08);
        }
        .bubble.user {
            background: linear-gradient(135deg, #7c3aed, #6d28d9);
            color: #ffffff;
            border-bottom-right-radius: 5px;
            box-shadow: 0 4px 20px rgba(124,58,237,0.35);
        }
        .timestamp {
            font-size: 0.67rem;
            color: #64748b;
            margin-top: 5px;
            display: block;
            letter-spacing: 0.2px;
        }
        .user .timestamp { text-align: right; color: #8b7cb3; }
        .bot  .timestamp { text-align: left; }

        /* ── Typing Indicator ── */
        .typing-indicator {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 10px 16px;
            background: rgba(6,182,212,0.08);
            border-radius: 20px;
            border-bottom-left-radius: 5px;
            width: fit-content;
            margin-bottom: 14px;
            border: 1px solid rgba(6,182,212,0.18);
        }
        .typing-dots { display: flex; gap: 4px; align-items: center; }
        .typing-dots span {
            width: 7px; height: 7px;
            border-radius: 50%;
            background: #06b6d4;
            animation: bounce 1.2s infinite;
        }
        .typing-dots span:nth-child(2) { animation-delay: 0.2s; }
        .typing-dots span:nth-child(3) { animation-delay: 0.4s; }
        @keyframes bounce {
            0%, 60%, 100% { transform: translateY(0); opacity: 0.5; }
            30% { transform: translateY(-7px); opacity: 1; }
        }

        /* ── Quick Actions Title ── */
        .quick-actions-title {
            font-family: 'Outfit', sans-serif;
            font-size: 0.75rem;
            font-weight: 600;
            color: #a78bfa !important;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            margin-bottom: 12px;
        }
        /* ── Help Topics heading ── */
        .help-topics-heading {
            font-family: 'Outfit', sans-serif;
            font-size: 1.05rem;
            font-weight: 700;
            color: #e2e8f0 !important;
            margin-bottom: 12px;
            padding-bottom: 8px;
            border-bottom: 1px solid rgba(124,58,237,0.25);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        /* ── Quick Action Buttons ── */
        .stButton > button {
            background: rgba(255,255,255,0.04) !important;
            color: #c4b5fd !important;
            border: 1px solid rgba(124,58,237,0.3) !important;
            border-radius: 12px;
            font-size: 0.84rem;
            font-weight: 500;
            padding: 10px 14px;
            width: 100%;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
            text-align: left;
            backdrop-filter: blur(8px);
        }
        .stButton > button:hover {
            background: linear-gradient(135deg, rgba(124,58,237,0.35), rgba(109,40,217,0.3)) !important;
            color: #ffffff !important;
            border-color: rgba(124,58,237,0.7) !important;
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(124,58,237,0.3), 0 0 0 1px rgba(124,58,237,0.4) !important;
        }
        .stButton > button:active { transform: translateY(0); }

        /* ── Clear Chat button ── */
        .clear-btn button {
            background: rgba(239,68,68,0.08) !important;
            color: #fca5a5 !important;
            border: 1px solid rgba(239,68,68,0.3) !important;
        }
        .clear-btn button:hover {
            background: rgba(239,68,68,0.25) !important;
            color: #ffffff !important;
            border-color: rgba(239,68,68,0.6) !important;
            box-shadow: 0 6px 20px rgba(239,68,68,0.25) !important;
        }

        /* ── Send button ── */
        [data-testid="stFormSubmitButton"] > button {
            background: linear-gradient(135deg, #7c3aed, #6d28d9) !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 12px !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 18px rgba(124,58,237,0.45) !important;
            transition: all 0.25s ease !important;
        }
        [data-testid="stFormSubmitButton"] > button:hover {
            background: linear-gradient(135deg, #6d28d9, #5b21b6) !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 28px rgba(124,58,237,0.55) !important;
        }

        /* ── Text Input ── */
        [data-testid="stTextInput"] input {
            background: rgba(255,255,255,0.05) !important;
            border: 1px solid rgba(124,58,237,0.25) !important;
            border-radius: 12px !important;
            color: #e2e8f0 !important;
            font-size: 0.9rem !important;
            transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
        }
        [data-testid="stTextInput"] input:focus {
            border-color: rgba(124,58,237,0.6) !important;
            box-shadow: 0 0 0 3px rgba(124,58,237,0.15) !important;
        }
        [data-testid="stTextInput"] input::placeholder { color: #475569 !important; }

        /* ── Info Cards (sidebar) ── */
        .info-card {
            background: rgba(124,58,237,0.08);
            border-radius: 14px;
            padding: 14px 16px;
            margin-bottom: 12px;
            border: 1px solid rgba(124,58,237,0.2);
            backdrop-filter: blur(8px);
            transition: border-color 0.2s ease;
        }
        .info-card:hover { border-color: rgba(124,58,237,0.4); }
        .info-card h4 { margin: 0 0 6px 0; font-size: 0.84rem; font-weight: 600; color: #c4b5fd !important; }
        .info-card p  { margin: 0; font-size: 0.79rem; color: #94a3b8 !important; line-height: 1.55; }

        /* ── Status Badge ── */
        .status-badge {
            display: inline-flex;
            align-items: center;
            gap: 7px;
            background: rgba(16,185,129,0.1);
            border-radius: 20px;
            padding: 5px 14px;
            font-size: 0.77rem;
            font-weight: 500;
            color: #6ee7b7;
            border: 1px solid rgba(16,185,129,0.3);
        }
        .status-dot {
            width: 7px; height: 7px;
            background: #10b981;
            border-radius: 50%;
            box-shadow: 0 0 8px #10b981;
            animation: pulse-dot 2s ease-in-out infinite;
        }
        @keyframes pulse-dot {
            0%, 100% { opacity: 1; box-shadow: 0 0 6px #10b981; }
            50%       { opacity: 0.7; box-shadow: 0 0 14px #10b981; }
        }

        /* ── Footer ── */
        .footer {
            text-align: center;
            font-size: 0.78rem;
            color: #334155;
            padding: 16px;
            margin-top: 8px;
            letter-spacing: 0.2px;
        }

        /* ── FAQ Card ── */
        .faq-item {
            background: rgba(6,182,212,0.06);
            border-radius: 12px;
            padding: 10px 14px;
            margin-bottom: 8px;
            border-left: 3px solid #06b6d4;
            border: 1px solid rgba(6,182,212,0.15);
            border-left: 3px solid #06b6d4;
        }
        .faq-q { font-weight: 600; color: #67e8f9; font-size: 0.84rem; }
        .faq-a { color: #94a3b8; font-size: 0.81rem; margin-top: 4px; }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────
# BOT RESPONSE ENGINE
# ─────────────────────────────────────────────
def get_bot_response(topic: str) -> str:
    """
    Rule-based response engine.
    Maps topic keys to predefined, helpful responses.
    Returns a formatted HTML string rendered inside the chat bubble.
    """
    responses = {
        "order_status": (
            "📦 <b>Order Status</b><br><br>"
            "Please share your <b>Order ID</b> and we'll look it up for you!<br><br>"
            "🔄 Your order is currently being <b>processed</b> and will be shipped "
            "within <b>24 hours</b>.<br><br>"
            "📩 You'll receive a confirmation email with tracking details once dispatched."
        ),
        "shipping": (
            "🚚 <b>Shipping Information</b><br><br>"
            "We offer the following delivery options:<br><br>"
            "📦 <b>Standard Delivery</b> — 5–7 business days<br>"
            "⚡ <b>Express Delivery</b> — 2–3 business days<br>"
            "🏙️ <b>Same-Day Delivery</b> — Available in selected cities<br><br>"
            "🆓 Free standard shipping on orders above ₹499!"
        ),
        "payment": (
            "💳 <b>Payment Methods</b><br><br>"
            "We support a wide range of payment options:<br><br>"
            "📱 UPI (GPay, PhonePe, Paytm)<br>"
            "💳 Credit Card & Debit Card<br>"
            "🏦 Net Banking<br>"
            "💵 Cash on Delivery (COD)<br>"
            "🎁 Gift Cards & Vouchers<br><br>"
            "🔒 All transactions are secured with 256-bit SSL encryption."
        ),
        "returns": (
            "🔄 <b>Return & Refund Policy</b><br><br>"
            "📅 Products can be <b>returned within 7 days</b> of delivery.<br><br>"
            "✅ <b>Eligibility:</b> Item must be unused and in original packaging.<br>"
            "💰 <b>Refunds</b> are processed within <b>5–7 business days</b> to the original payment method.<br><br>"
            "📝 To initiate a return, visit <i>My Orders → Return Request</i> or contact support."
        ),
        "hours": (
            "🕒 <b>Working Hours</b><br><br>"
            "Our customer support team is available:<br><br>"
            "📅 <b>Monday – Saturday</b>: 9:00 AM – 6:00 PM<br>"
            "🚫 <b>Sunday</b>: Closed<br><br>"
            "💬 You can still leave us a message anytime and we'll respond on the next business day."
        ),
        "contact": (
            "📞 <b>Contact Support</b><br><br>"
            "Reach us through any of these channels:<br><br>"
            "📧 <b>Email:</b> support@example.com<br>"
            "📱 <b>Phone:</b> +91-987654XXXX<br>"
            "💬 <b>Live Chat:</b> Available on our website (Mon–Sat)<br>"
            "🐦 <b>Twitter:</b> @SupportExample<br><br>"
            "⏱️ Average response time: <b>under 2 hours</b>"
        ),
        "faq": (
            "❓ <b>Frequently Asked Questions</b><br><br>"
            "🔍 <b>How can I track my order?</b><br>"
            "Visit <i>My Orders</i> and click 'Track' next to your order, or use the tracking link in your email.<br><br>"
            "❌ <b>Can I cancel an order?</b><br>"
            "Yes! Orders can be cancelled within <b>2 hours</b> of placement from the 'My Orders' section.<br><br>"
            "💰 <b>When will I receive my refund?</b><br>"
            "Refunds are credited within <b>5–7 business days</b> after the return is picked up.<br><br>"
            "📞 <b>How do I contact support?</b><br>"
            "Call <b>+91-987654XXXX</b> or email <b>support@example.com</b> (Mon–Sat, 9 AM–6 PM)."
        ),
        "exit": (
            "🚪 <b>Goodbye!</b><br><br>"
            "Thank you for visiting AssistIQ! 😊<br><br>"
            "Have a <b>wonderful day</b> ahead! If you ever need help, we're just a click away. 👋"
        ),
    }
    return responses.get(topic, "I'm sorry, I didn't understand that. Please choose an option below.")


# ─────────────────────────────────────────────
# SESSION STATE INITIALISATION
# ─────────────────────────────────────────────
def init_session():
    """Initialise all session-state keys on first load."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Greeting from bot
        st.session_state.messages.append(
            {
                "role": "bot",
                "content": (
                    "Hello! 👋 <b>Welcome to AssistIQ — Your Smart Support Assistant.</b><br><br>"
                    "I'm here to help you with orders, shipping, payments, returns, and more. "
                    "How can I assist you today? Select an option below or type your query!"
                ),
                "time": datetime.now().strftime("%I:%M %p"),
            }
        )
    if "typing" not in st.session_state:
        st.session_state.typing = False


# ─────────────────────────────────────────────
# CHAT HISTORY RENDERER
# ─────────────────────────────────────────────
def render_chat():
    """Render all chat messages as styled HTML bubbles."""
    html_parts = ['<div class="chat-container" id="chat-end">']

    for msg in st.session_state.messages:
        role = msg["role"]
        content = msg["content"]
        ts = msg.get("time", "")

        if role == "bot":
            html_parts.append(
                f"""
                <div class="chat-msg-row bot">
                    <div class="avatar avatar-bot">🤖</div>
                    <div class="bubble-wrapper bot">
                        <div class="bubble bot">{content}</div>
                        <span class="timestamp bot">🕐 {ts} · Support Bot</span>
                    </div>
                </div>"""
            )
        else:
            html_parts.append(
                f"""
                <div class="chat-msg-row user">
                    <div class="avatar avatar-user">👤</div>
                    <div class="bubble-wrapper user">
                        <div class="bubble user">{content}</div>
                        <span class="timestamp user">{ts} · You</span>
                    </div>
                </div>"""
            )

    # Scroll anchor — placed inside the container so scrollIntoView
    # scrolls the overflow div rather than the whole page
    html_parts.append('<div id="chat-scroll-anchor" style="height:1px;"></div>')
    html_parts.append("</div>")

    # Auto-scroll JS — uses scrollIntoView with a short delay to ensure
    # the DOM has finished painting before we scroll (fixes the Streamlit
    # rerun timing issue that prevented scrolling after the first message)
    html_parts.append(
        """
        <script>
            function scrollToBottom() {
                var anchor = document.getElementById('chat-scroll-anchor');
                if (anchor) {
                    anchor.scrollIntoView({ behavior: 'smooth', block: 'end' });
                }
            }
            scrollToBottom();
            setTimeout(scrollToBottom, 120);
            setTimeout(scrollToBottom, 350);
        </script>"""
    )

    st.markdown("".join(html_parts), unsafe_allow_html=True)


# ─────────────────────────────────────────────
# TYPING INDICATOR
# ─────────────────────────────────────────────
def show_typing():
    """Display an animated 'Bot is typing...' indicator."""
    placeholder = st.empty()
    placeholder.markdown(
        """
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
            <div class="avatar avatar-bot" style="width:38px;height:38px;border-radius:50%;
                background:linear-gradient(135deg,#0891b2,#06b6d4);display:flex;
                align-items:center;justify-content:center;font-size:1.1rem;
                border:2px solid rgba(6,182,212,0.4);
                box-shadow:0 4px 12px rgba(0,0,0,0.3);">🤖</div>
            <div class="typing-indicator">
                <span style="font-size:0.81rem;color:#67e8f9;">Bot is typing</span>
                <div class="typing-dots">
                    <span></span><span></span><span></span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    time.sleep(1.2)   # Simulate typing delay
    placeholder.empty()


# ─────────────────────────────────────────────
# ADD MESSAGE HELPER
# ─────────────────────────────────────────────
def add_message(role: str, content: str):
    """Append a message dict to session state."""
    st.session_state.messages.append(
        {
            "role": role,
            "content": content,
            "time": datetime.now().strftime("%I:%M %p"),
        }
    )


# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
def render_sidebar():
    """Build the left sidebar with branding and information."""
    with st.sidebar:
        # Logo / Branding
        st.markdown(
            """
            <div style="text-align:center;padding:24px 0 12px 0;">
                <div style="width:84px;height:84px;
                    background:linear-gradient(135deg,rgba(124,58,237,0.3),rgba(6,182,212,0.2));
                    border-radius:50%;display:flex;align-items:center;justify-content:center;
                    font-size:2.6rem;margin:0 auto 14px auto;
                    border:2px solid rgba(124,58,237,0.5);
                    box-shadow:0 0 24px rgba(124,58,237,0.3)">
                    🤖
                </div>
                <h2 style="margin:0;font-size:1.25rem;font-weight:700;
                    font-family:'Outfit',sans-serif;color:#e2e8f0;
                    background:linear-gradient(135deg,#c4b5fd,#67e8f9);
                    -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                    background-clip:text;">AssistIQ</h2>
                <p style="margin:5px 0 0 0;font-size:0.78rem;color:#64748b;">Smart Support Assistant</p>
                <div class="status-badge" style="margin:12px auto;display:inline-flex;">
                    <div class="status-dot"></div> Online
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")

        # Info Cards
        st.markdown(
            """
            <div class="info-card">
                <h4>🕒 Support Hours</h4>
                <p>Mon–Sat: 9:00 AM – 6:00 PM<br>Sunday: Closed</p>
            </div>
            <div class="info-card">
                <h4>📞 Quick Contact</h4>
                <p>📱 +91-987654XXXX<br>📧 support@example.com</p>
            </div>
            <div class="info-card">
                <h4>⚡ Response Time</h4>
                <p>Live Chat: Instant<br>Email: Under 2 hours</p>
            </div>
            <div class="info-card">
                <h4>🔒 Secure & Private</h4>
                <p>All conversations are encrypted and confidential.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")

        # Message count stat
        msg_count = len([m for m in st.session_state.messages if m["role"] == "user"])
        bot_count = len([m for m in st.session_state.messages if m["role"] == "bot"])
        st.markdown(
            f"""
            <div style="text-align:center;padding:8px 0;">
                <p style="font-size:0.72rem;color:#475569;margin:0;text-transform:uppercase;letter-spacing:0.8px;">Session Statistics</p>
                <div style="display:flex;justify-content:space-around;margin-top:12px;gap:8px;">
                    <div style="text-align:center;background:rgba(124,58,237,0.1);
                        border:1px solid rgba(124,58,237,0.2);border-radius:12px;padding:10px 16px;flex:1;">
                        <div style="font-size:1.6rem;font-weight:700;font-family:'Outfit',sans-serif;
                            background:linear-gradient(135deg,#c4b5fd,#a78bfa);
                            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                            background-clip:text;">{msg_count}</div>
                        <div style="font-size:0.68rem;color:#64748b;margin-top:2px;">Your Messages</div>
                    </div>
                    <div style="text-align:center;background:rgba(6,182,212,0.08);
                        border:1px solid rgba(6,182,212,0.2);border-radius:12px;padding:10px 16px;flex:1;">
                        <div style="font-size:1.6rem;font-weight:700;font-family:'Outfit',sans-serif;
                            background:linear-gradient(135deg,#67e8f9,#22d3ee);
                            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                            background-clip:text;">{bot_count}</div>
                        <div style="font-size:0.68rem;color:#64748b;margin-top:2px;">Bot Replies</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")

        # Clear Chat
        st.markdown('<div class="clear-btn">', unsafe_allow_html=True)
        if st.button("🗑️ Clear Chat History", key="clear_btn", use_container_width=True):
            st.session_state.messages = []
            add_message(
                "bot",
                "Chat cleared! 🧹 Hello again! How can I help you today?",
            )
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# QUICK ACTION BUTTONS
# ─────────────────────────────────────────────
QUICK_ACTIONS = [
    ("📦 Order Status",           "order_status"),
    ("🚚 Shipping Information",    "shipping"),
    ("💳 Payment Methods",         "payment"),
    ("🔄 Return & Refund Policy",  "returns"),
    ("🕒 Working Hours",           "hours"),
    ("📞 Contact Support",         "contact"),
    ("❓ FAQ",                     "faq"),
    ("🚪 Exit Chat",               "exit"),
]


def render_quick_actions():
    """Render the 2-column grid of quick-action buttons."""
    st.markdown('<p class="quick-actions-title">⚡ Quick Actions — Select a topic</p>', unsafe_allow_html=True)

    cols = st.columns(2)
    for idx, (label, key) in enumerate(QUICK_ACTIONS):
        col = cols[idx % 2]
        with col:
            if st.button(label, key=f"btn_{key}", use_container_width=True):
                # 1. Record user's choice as a message
                add_message("user", label)
                # 2. Show typing animation then bot reply
                show_typing()
                response = get_bot_response(key)
                add_message("bot", response)
                st.rerun()


# ─────────────────────────────────────────────
# TEXT INPUT HANDLER
# ─────────────────────────────────────────────
KEYWORD_MAP = {
    "order": "order_status",
    "track": "order_status",
    "ship": "shipping",
    "deliver": "shipping",
    "pay": "payment",
    "payment": "payment",
    "upi": "payment",
    "card": "payment",
    "return": "returns",
    "refund": "returns",
    "cancel": "returns",
    "hour": "hours",
    "time": "hours",
    "open": "hours",
    "contact": "contact",
    "phone": "contact",
    "email": "contact",
    "faq": "faq",
    "question": "faq",
    "help": "faq",
    "exit": "exit",
    "bye": "exit",
    "goodbye": "exit",
    "quit": "exit",
}


def classify_message(text: str) -> str:
    """
    Simple keyword-based intent classifier.
    Returns the matched topic key or 'unknown'.
    """
    text_lower = text.lower()
    for keyword, topic in KEYWORD_MAP.items():
        if keyword in text_lower:
            return topic
    return "unknown"


def is_order_id(text: str) -> bool:
    """
    Detect if the user's input looks like an Order ID.
    Accepts: pure numbers (e.g. 24514521) or
             alphanumeric codes (e.g. ORD-1234, ABC123).
    """
    import re
    stripped = text.strip()
    # Pure digits of length 4-20
    if re.fullmatch(r'\d{4,20}', stripped):
        return True
    # Alphanumeric with optional dash/hyphen (e.g. ORD-12345, ABC123)
    if re.fullmatch(r'[A-Za-z0-9]{4,20}(-[A-Za-z0-9]+)?', stripped):
        return True
    return False


def get_last_bot_topic() -> str:
    """
    Check the last bot message to determine conversation context.
    Returns 'order_status' if the bot last talked about orders,
    otherwise returns an empty string.
    """
    bot_messages = [
        m for m in st.session_state.get('messages', []) if m['role'] == 'bot'
    ]
    if not bot_messages:
        return ''
    last_content = bot_messages[-1].get('content', '').lower()
    if 'order' in last_content and 'order id' in last_content:
        return 'order_status'
    return ''


def handle_text_input():
    """Render a text input box and process free-form user queries."""
    with st.form(key="chat_form", clear_on_submit=True):
        cols = st.columns([5, 1])
        with cols[0]:
            user_input = st.text_input(
                label="Type your message",
                placeholder="💬 Type your message here… (e.g. 'How do I return an item?')",
                label_visibility="collapsed",
            )
        with cols[1]:
            submitted = st.form_submit_button("Send 🚀", use_container_width=True)

    if submitted and user_input.strip():
        text = user_input.strip()
        add_message("user", text)

        show_typing()

        # ── Context-aware: Order ID entered after Order Status reply ──
        if is_order_id(text) and get_last_bot_topic() == 'order_status':
            order_id = text.upper()
            bot_reply = (
                f"✅ <b>Order ID <code>{order_id}</code> received!</b><br><br>"
                "🔍 We've located your order in our system. Here's the latest update:<br><br>"
                "📦 <b>Status:</b> Processing — your order is being prepared for dispatch.<br>"
                "🚚 <b>Estimated Dispatch:</b> Within the next <b>24 hours</b>.<br>"
                "📩 <b>Tracking:</b> A shipping confirmation with a live tracking link will "
                "be sent to your registered email once dispatched.<br><br>"
                "Is there anything else I can help you with? 😊"
            )
        else:
            topic = classify_message(text)
            if topic == "unknown":
                bot_reply = (
                    "🤔 I'm not sure I understood that.<br><br>"
                    "I can help you with <b>orders, shipping, payments, returns, working hours, "
                    "contact info, and FAQs</b>. Please select one of the quick actions below "
                    "or rephrase your query!"
                )
            else:
                bot_reply = get_bot_response(topic)

        add_message("bot", bot_reply)
        st.rerun()


# ─────────────────────────────────────────────
# MAIN APPLICATION
# ─────────────────────────────────────────────
def main():
    """Entry point — orchestrates all UI components."""
    load_css()
    init_session()
    render_sidebar()

    # ── Header ──
    st.markdown(
        """
        <div class="header-card">
            <div class="logo-circle">🏢</div>
            <h1>🤖 AssistIQ</h1>
            <p>Your Smart Virtual Support Assistant</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Two-column layout: Chat | Actions ──
    chat_col, actions_col = st.columns([3, 2], gap="large")

    with chat_col:
        st.markdown('<p class="help-topics-heading">💬 Chat Window</p>', unsafe_allow_html=True)
        render_chat()
        handle_text_input()

    with actions_col:
        st.markdown('<p class="help-topics-heading">🎯 Help Topics</p>', unsafe_allow_html=True)
        render_quick_actions()

        # Divider + tip box
        st.markdown(
            """
            <div style="background:rgba(124,58,237,0.08);
                border-radius:16px;padding:16px 18px;margin-top:16px;
                border:1px solid rgba(124,58,237,0.2);
                backdrop-filter:blur(8px);">
                <p style="margin:0;font-size:0.82rem;color:#c4b5fd;font-weight:600;
                    font-family:'Outfit',sans-serif;">
                    💡 Pro Tip
                </p>
                <p style="margin:8px 0 0 0;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
                    You can also <b style='color:#e2e8f0;'>type your question</b> in the chat box on the left
                    and our bot will instantly understand and respond!
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ── Footer ──
    st.markdown(
        """
        <div class="footer">
            Made with ❤️ using Streamlit &nbsp;·&nbsp;
            🔒 Secure &nbsp;·&nbsp;
            📞 +91-987654XXXX &nbsp;·&nbsp;
            © 2026 AssistIQ
        </div>
        """,
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────
# RUN
# ─────────────────────────────────────────────
if __name__ == "__main__":
    main()
