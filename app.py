import streamlit as st
from modules import ui, logic, data

st.set_page_config(
    page_title="VARK Expert AI", 
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if 'page_index' not in st.session_state: st.session_state['page_index'] = 0 
if 'answers' not in st.session_state: st.session_state['answers'] = {}
if 'finished' not in st.session_state: st.session_state['finished'] = False

engine = logic.InferenceEngine()
ui.inject_custom_css()
selected_menu = ui.render_navbar(default_idx=st.session_state['page_index'])
menu_map = {"Dashboard": 0, "Assessment": 1, "Analytics": 2}

if menu_map[selected_menu] != st.session_state['page_index']:
    st.session_state['page_index'] = menu_map[selected_menu]
    st.rerun()
st.markdown("<div style='margin-bottom: 24px;'></div>", unsafe_allow_html=True)

if st.session_state['page_index'] == 0:
    ui.render_dashboard_hero()
    
    col1, col2, col3 = st.columns(3)
    features = [
        ("🧠", "Analisis Kognitif", "Memetakan pola pikir unik Anda dalam menyerap informasi."),
        ("📊", "Visualisasi Data", "Hasil disajikan dalam bentuk grafik radar interaktif & presisi."),
        ("⚡", "Strategi Instan", "Tips belajar konkret yang bisa langsung diterapkan hari ini.")
    ]
    
    for i, (icon, title, desc) in enumerate(features):
        with [col1, col2, col3][i]:
            st.markdown(f"""<div class="saas-card h-full text-center"><div class="text-4xl mb-3">{icon}</div><h3 class="font-bold text-slate-800 text-lg">{title}</h3><p class="text-sm text-slate-500 mt-2 leading-relaxed">{desc}</p></div>""", unsafe_allow_html=True)

    col_c = st.columns([1, 2, 1])
    with col_c[1]:
        if st.button("Mulai Tes Sekarang 🚀", type="primary", use_container_width=True):
            st.session_state['page_index'] = 1
            st.rerun()

elif st.session_state['page_index'] == 1:
    col_l, col_main, col_r = st.columns([1, 4, 1]) 
    with col_main:
        q_idx = len(st.session_state['answers'])
        total_q = len(data.QUESTIONS)
        ui.render_progress_bar(q_idx, total_q)

        if q_idx < total_q:
            q_curr = data.QUESTIONS[q_idx]
            ui.render_question_card(q_curr['question'])
            opts_map = {v: k for k, v in q_curr['options'].items()}
            choice = st.radio(
                "Pilihan", 
                list(q_curr['options'].values()), 
                label_visibility="collapsed", 
                key=f"q_{q_curr['id']}"
            )
            
            st.markdown("<div class='mt-8'></div>", unsafe_allow_html=True)
            if st.button("Lanjut ➔", type="primary", use_container_width=True):
                st.session_state['answers'][q_curr['id']] = opts_map[choice]
                st.rerun()
        else:
            st.session_state['finished'] = True
            st.markdown("""<div class="saas-card text-center py-8"><div class="text-6xl mb-4">🎉</div><h2 class="text-2xl font-bold text-slate-800">Analisis Selesai!</h2><p class="text-slate-500">Algoritma AI telah berhasil memproses profil belajar Anda.</p></div>""", unsafe_allow_html=True)
            
            if st.button("Lihat Hasil Analisis 📊", type="primary", use_container_width=True):
                st.session_state['page_index'] = 2
                st.rerun()

elif st.session_state['page_index'] == 2:
    if not st.session_state['finished']:
        st.warning("⚠️ Data belum tersedia. Silakan selesaikan Assessment terlebih dahulu.")
        if st.button("Ke Menu Assessment", type="primary"):
            st.session_state['page_index'] = 1
            st.rerun()
    else:
        raw_ans = list(st.session_state['answers'].values())
        scores = engine.process_answers(raw_ans)
        pcts = engine.calculate_percentages()
        p_name, p_data = engine.determine_profile()
        radar_fig = engine.create_radar_chart()

        ui.render_result_hero(p_data['archetype'], p_data['desc'])
        ui.render_metrics_grid(scores, pcts)
        
        c1, c2 = st.columns([1, 1.2]) 
        
        with c1:
            st.markdown("<h4 class='font-bold text-center mb-6 text-slate-800 text-lg'>Peta Potensi Kognitif</h4>", unsafe_allow_html=True)
            st.plotly_chart(radar_fig, use_container_width=True, config={'displayModeBar': False})
            st.markdown('</div>', unsafe_allow_html=True)
            
        with c2:
            st.markdown(f"<h4 class='font-bold mb-6 text-slate-800 text-lg'>Rekomendasi Strategi: <span class='text-indigo-600'>{p_name}</span></h4>", unsafe_allow_html=True)
            
            for tip in p_data['tips']:
                st.markdown(f"""<div class="flex gap-4 mb-4 border-b border-slate-50 pb-3 last:border-0 hover:bg-slate-50 p-2 rounded-lg transition-colors"><div class="mt-0.5 text-xl">💡</div><p class="text-sm text-slate-600 leading-relaxed font-medium">{tip}</p></div>""", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        col_res = st.columns([1, 2, 1])
        with col_res[1]:
            st.markdown("<div class='mt-8'></div>", unsafe_allow_html=True)
            if st.button("🔄 Reset & Mulai Ulang", type="secondary", use_container_width=True):
                st.session_state['answers'] = {}
                st.session_state['finished'] = False
                st.session_state['page_index'] = 0
                st.rerun()
                