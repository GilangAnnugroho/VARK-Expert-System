import streamlit as st
from streamlit_option_menu import option_menu

def inject_custom_css():
    """
    Menyuntikkan Tailwind CSS, Font Google, dan CSS Overrides
    untuk tampilan Dashboard modern (SaaS Style), responsif, dan 100% lebar layar.
    """
    st.markdown("""
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
        
        <style>
            /* --- GLOBAL VARIABLES & RESET --- */
            :root {
                --bg-app: #f8fafc;
                --primary: #4f46e5;
                --text-main: #0f172a;
            }
            
            html, body, [class*="css"] {
                font-family: 'Poppins', sans-serif;
                color: var(--text-main);
                background-color: var(--bg-app);
            }

            /* --- LAYOUT 100% WIDTH FIX --- */
            .block-container {
                max-width: 100% !important;
                padding-top: 1.5rem !important;
                padding-bottom: 3rem !important;
                padding-left: 2rem !important;
                padding-right: 2rem !important;
            }
            
            @media (max-width: 640px) {
                .block-container {
                    padding-left: 1rem !important;
                    padding-right: 1rem !important;
                }
            }

            /* Background App */
            .stApp {
                background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%);
                background-attachment: fixed;
            }

            /* --- CUSTOM COMPONENTS --- */
            
            /* Navbar Shadow */
            iframe[title="streamlit_option_menu.option_menu"] {
                border-radius: 12px;
                box-shadow: 0 4px 10px -2px rgba(0, 0, 0, 0.05);
            }

            /* SAAS Card (Modern Clean) */
            .saas-card {
                background: rgba(255, 255, 255, 0.95);
                backdrop-filter: blur(16px);
                border: 1px solid #e2e8f0;
                border-radius: 16px;
                padding: 1.5rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
                margin-bottom: 1.5rem;
                transition: transform 0.2s ease;
            }
            .saas-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
                border-color: #6366f1;
            }

            .hero-title {
                background: linear-gradient(to right, #4f46e5, #0ea5e9);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            /* --- METRIC CARD MODERN (Icon + Text) --- */
            .metric-box {
                background: white;
                border: 1px solid #e2e8f0;
                border-radius: 14px;
                padding: 1.25rem;
                display: flex;
                align-items: center;
                gap: 1rem;
                box-shadow: 0 2px 4px rgba(0,0,0,0.02);
                transition: all 0.2s;
            }
            .metric-box:hover {
                box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.08);
                border-color: #6366f1;
                transform: translateY(-2px);
            }
            
            .metric-icon {
                width: 48px;
                height: 48px;
                border-radius: 12px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 24px;
                flex-shrink: 0;
            }
            
            .metric-content {
                display: flex;
                flex-direction: column;
            }

            /* CSS GRID Fix - Responsif */
            .metric-container {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 1.25rem;
                width: 100%;
                margin-bottom: 2rem;
            }

            /* Radio Buttons Compact Style */
            div.row-widget.stRadio > div { gap: 10px; }
            div.row-widget.stRadio > div[role="radiogroup"] > label {
                background: white; padding: 1rem; border-radius: 12px;
                border: 1px solid #e2e8f0; transition: all 0.2s;
                box-shadow: 0 1px 2px rgba(0,0,0,0.03);
            }
            div.row-widget.stRadio > div[role="radiogroup"] > label:hover {
                border-color: #6366f1; background: #f8fafc;
            }
            
            /* Hide Streamlit Default Elements */
            header {visibility: hidden;}
            footer {visibility: hidden;}
            .stDeployButton {display:none;}
            
            .stButton > button {
                border-radius: 10px;
                font-weight: 600;
                padding: 0.5rem 1rem;
            }
        </style>
    """, unsafe_allow_html=True)

def render_navbar(default_idx=0):
    return option_menu(
        menu_title=None,
        options=["Dashboard", "Assessment", "Analytics"],
        icons=["grid-fill", "cpu-fill", "pie-chart-fill"],
        default_index=default_idx,
        orientation="horizontal",
        styles={
            "container": {"padding": "6px", "background-color": "white", "border-radius": "14px", "box-shadow": "0 2px 8px rgba(0,0,0,0.05)"},
            "nav-link": {"font-size": "14px", "margin": "0px 4px", "padding": "10px", "border-radius": "10px"},
            "nav-link-selected": {"background-color": "#4f46e5", "color": "white", "font-weight": "600"},
        }
    )

def render_dashboard_hero():
    st.markdown("""
        <div class="saas-card text-center py-12">
            <h1 class="text-4xl md:text-6xl font-extrabold mb-4 tracking-tight text-slate-900 leading-tight">
                VARK <span class="hero-title">Expert System</span>
            </h1>
            <p class="text-lg text-slate-600 max-w-3xl mx-auto mb-8 leading-relaxed">
                Temukan gaya belajar ideal Anda melalui sistem pakar berbasis AI untuk strategi belajar yang lebih efektif dan personal.
            </p>
            <div class="flex flex-wrap justify-center gap-4 text-sm font-bold text-slate-500">
                <span class="flex items-center gap-2 px-4 py-2 bg-white rounded-full border border-slate-200">⚡ AI Inference</span>
                <span class="flex items-center gap-2 px-4 py-2 bg-white rounded-full border border-slate-200">🎯 Personalized</span>
                <span class="flex items-center gap-2 px-4 py-2 bg-white rounded-full border border-slate-200">⏱️ 2 Menit</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_question_card(text):
    """
    Menampilkan header pertanyaan dengan style Card SaaS.
    Fungsi inilah yang dicari oleh app.py Anda.
    """
    st.markdown(f"""
        <div class="saas-card text-center mb-6">
            <h3 class="text-xl md:text-2xl font-bold text-slate-800 leading-snug">{text}</h3>
        </div>
    """, unsafe_allow_html=True)

def render_progress_bar(current, total):
    pct = int((current/total)*100)
    st.markdown(f"""
        <div class="flex justify-between text-xs font-bold text-slate-500 uppercase tracking-widest mb-2">
            <span>Progress Analisis</span>
            <span>{current} / {total}</span>
        </div>
        <div class="w-full bg-slate-200 rounded-full h-2.5 mb-6 overflow-hidden">
            <div class="bg-gradient-to-r from-indigo-500 to-cyan-400 h-2.5 rounded-full transition-all duration-500 ease-out" style="width: {pct}%"></div>
        </div>
    """, unsafe_allow_html=True)

def render_result_hero(archetype, desc):
    st.markdown(f"""
        <div class="saas-card text-center border-t-4 border-indigo-600 py-8">
            <div class="inline-block p-3 rounded-full bg-indigo-50 text-indigo-600 mb-4">
                <span class="text-4xl">🏆</span>
            </div>
            <div class="text-indigo-600 font-bold uppercase tracking-widest text-xs mb-2">Hasil Analisis Final</div>
            <h2 class="text-3xl md:text-5xl font-black text-slate-900 mb-4">{archetype}</h2>
            <p class="text-lg text-slate-600 max-w-2xl mx-auto leading-relaxed">{desc}</p>
        </div>
    """, unsafe_allow_html=True)

def render_metrics_grid(scores, percentages):
    """
    Render Metrik dengan Layout Modern (Icon + Text).
    FIX FINAL: String HTML digabungkan satu baris untuk menghindari bug Markdown Code Block.
    """
    html_content = '<div class="metric-container">'
    config = {
        "V": {"color": "blue", "icon": "👁️", "label": "Visual"},
        "A": {"color": "amber", "icon": "👂", "label": "Aural"},
        "R": {"color": "emerald", "icon": "📖", "label": "Read/Write"},
        "K": {"color": "rose", "icon": "✋", "label": "Kinesthetic"}
    }
    
    for key, val in scores.items():
        pct = percentages[key]
        c_name = config[key]["color"]
        icon = config[key]["icon"]
        label = config[key]["label"]
        bg_icon = f"bg-{c_name}-100 text-{c_name}-600"
        bg_pill = f"bg-{c_name}-50 text-{c_name}-700"
        card_html = f'<div class="metric-box"><div class="metric-icon {bg_icon}">{icon}</div><div class="metric-content"><span class="text-2xl font-black text-slate-800">{val}</span><span class="text-xs font-bold text-slate-400 uppercase tracking-wide">{label}</span><span class="inline-block mt-1 px-2 py-0.5 rounded-full text-[10px] font-bold {bg_pill}">{pct}% Dominasi</span></div></div>'
        html_content += card_html
    html_content += '</div>'
    st.markdown(html_content, unsafe_allow_html=True)
    