"""
Knowledge Base: Menyimpan pertanyaan VARK dan Strategi Belajar.
Database ini digunakan oleh Logic Engine untuk menentukan profil pengguna
dan oleh UI Engine untuk menampilkan pertanyaan serta rekomendasi.
"""
QUESTIONS = [
    {
        "id": 1,
        "question": "Anda ingin belajar menggunakan software baru yang kompleks. Apa yang Anda lakukan?",
        "options": {
            "V": "Melihat diagram alur atau gambar screenshot antarmuka.",
            "A": "Bertanya pada teman yang sudah bisa atau mendengarkan podcast tutorial.",
            "R": "Membaca buku panduan manual atau dokumentasi tertulis.",
            "K": "Langsung membuka software dan mencoba fitur-fiturnya (trial & error)."
        }
    },
    {
        "id": 2,
        "question": "Anda perlu memberikan petunjuk arah ke rumah Anda kepada teman. Anda akan...",
        "options": {
            "V": "Menggambar peta denah lokasi.",
            "A": "Menjelaskan rute secara lisan melalui telepon.",
            "R": "Menuliskan instruksi langkah demi langkah (belok kiri, lurus 100m).",
            "K": "Menjemput mereka atau memandu sambil berjalan/berkendara bersama."
        }
    },
    {
        "id": 3,
        "question": "Anda berencana liburan ke tempat baru. Apa yang paling menarik bagi Anda?",
        "options": {
            "V": "Melihat foto-foto pemandangan dan peta wisata.",
            "A": "Mendengarkan cerita teman atau review vlog tentang tempat itu.",
            "R": "Membaca brosur, artikel blog, atau itinerari tertulis.",
            "K": "Merasakan pengalaman fisik (hiking, kuliner, aktivitas) di sana nanti."
        }
    },
    {
        "id": 4,
        "question": "Dosen/Guru menggunakan kata 'energi'. Apa yang muncul di pikiran Anda?",
        "options": {
            "V": "Bayangan gambar diagram alur energi atau grafik.",
            "A": "Suara penjelasan dosen tentang definisi energi.",
            "R": "Tulisan teks definisi 'Energi' di buku teks.",
            "K": "Sensasi fisik bergerak, bekerja, atau kelelahan."
        }
    },
    {
        "id": 5,
        "question": "Ketika Anda tidak yakin bagaimana cara mengeja sebuah kata, Anda akan...",
        "options": {
            "V": "Membayangkan tampilan kata tersebut di pikiran.",
            "A": "Mengucapkan kata tersebut keras-keras untuk mendengar bunyinya.",
            "R": "Mencarinya di kamus atau Google.",
            "K": "Menuliskan kata tersebut berulang kali untuk merasakan gerakan tangannya."
        }
    },
    {
        "id": 6,
        "question": "Anda paling suka dosen/pengajar yang...",
        "options": {
            "V": "Menggunakan banyak diagram, grafik, dan slide berwarna.",
            "A": "Menjelaskan dengan diskusi, tanya jawab, dan ceramah yang jelas.",
            "R": "Memberikan handout, buku teks, dan bacaan referensi lengkap.",
            "K": "Mengadakan demonstrasi, praktik lab, atau studi lapangan."
        }
    },
    {
        "id": 7,
        "question": "Anda membeli perabot yang harus dirakit sendiri. Anda akan...",
        "options": {
            "V": "Melihat gambar hasil jadi dan diagram langkah-langkah.",
            "A": "Meminta orang lain membacakan instruksi atau menonton video youtube.",
            "R": "Membaca instruksi perakitan dengan teliti dari awal sampai akhir.",
            "K": "Langsung mulai merakit dan mencari tahu seiring berjalannya waktu."
        }
    },
    {
        "id": 8,
        "question": "Saat menghadapi masalah teknis pada komputer, Anda lebih suka...",
        "options": {
            "V": "Melihat indikator visual atau pesan error di layar.",
            "A": "Menelepon support center atau bertanya pada rekan kerja.",
            "R": "Mencari artikel 'Troubleshooting' di internet.",
            "K": "Memeriksa kabel, membongkar casing, atau merestart komputer."
        }
    },
    {
        "id": 9,
        "question": "Anda ingin mempelajari sejarah peristiwa masa lalu. Anda lebih suka...",
        "options": {
            "V": "Melihat peta sejarah, timeline visual, dan foto dokumenter.",
            "A": "Mendengarkan podcast sejarah atau pidato tokoh.",
            "R": "Membaca buku biografi atau artikel sejarah.",
            "K": "Pergi ke museum untuk melihat artefak asli secara langsung."
        }
    },
    {
        "id": 10,
        "question": "Cara terbaik bagi Anda untuk mempersiapkan ujian adalah...",
        "options": {
            "V": "Membuat mind-map dan diagram alur dari materi.",
            "A": "Diskusi kelompok atau menjelaskan materi pada orang lain.",
            "R": "Meringkas catatan dan membaca ulang buku teks.",
            "K": "Melakukan latihan soal (mock exam) atau simulasi praktik."
        }
    }
]

STRATEGIES = {
    "V": {
        "archetype": "The Visionary (Si Visual)",
        "desc": "Otak Anda memproses informasi spasial dengan sangat cepat. Anda berpikir dalam gambar, grafik, dan simbol, bukan sekadar kata-kata.",
        "tips": [
            "Gunakan **Mind Mapping** berwarna-warni.",
            "Tandai materi penting dengan stabilo (color-coding).",
            "Ubah teks panjang menjadi diagram alur.",
            "Gunakan flashcard bergambar.",
            "Tonton video animasi penjelasan."
        ],
        "color": "#6366f1" 
    },
    "A": {
        "archetype": "The Listener (Si Auditorial)",
        "desc": "Kekuatan Anda ada pada pendengaran dan komunikasi. Anda menyerap informasi paling efektif melalui suara, diskusi, dan debat.",
        "tips": [
            "Rekam perkuliahan dan dengarkan ulang (podcast mode).",
            "Baca materi keras-keras (read aloud).",
            "Ikuti Study Group untuk berdiskusi.",
            "Jelaskan materi kepada orang lain (Feynman Technique).",
            "Hindari kebisingan saat fokus."
        ],
        "color": "#f59e0b" 
    },
    "R": {
        "archetype": "The Analyst (Si Baca/Tulis)",
        "desc": "Anda adalah tipe akademisi klasik. Kata-kata, daftar, dan definisi teks adalah senjata utama Anda dalam menguasai materi.",
        "tips": [
            "Tulis ulang catatan dengan kata-kata sendiri.",
            "Buat daftar poin (bullet points) yang terstruktur.",
            "Baca banyak buku referensi.",
            "Ubah diagram menjadi deskripsi paragraf.",
            "Gunakan sticky notes untuk kata kunci."
        ],
        "color": "#10b981" 
    },
    "K": {
        "archetype": "The Doer (Si Kinestetik)",
        "desc": "Anda belajar dengan melakukan (*learning by doing*). Teori abstrak akan membosankan bagi Anda tanpa adanya praktik nyata.",
        "tips": [
            "Praktik langsung (Hands-on labs).",
            "Gunakan studi kasus nyata (Real-world examples).",
            "Belajar sambil bergerak (jalan kaki, fidgeting).",
            "Ambil jeda istirahat singkat (Pomodoro technique).",
            "Kunjungi lokasi terkait materi (Museum, Lapangan)."
        ],
        "color": "#ef4444" 
    },
    "Multimodal": {
        "archetype": "The Synergist (Multimodal)",
        "desc": "Anda adalah pembelajar adaptif. Anda memiliki 'kotak peralatan' lengkap dan fleksibel untuk berpindah strategi sesuai situasi.",
        "tips": [
            "Switch metode saat bosan (misal: Baca -> Gambar).",
            "Kombinasikan input: Dengar podcast sambil menggambar map.",
            "Gunakan variasi media belajar.",
            "Ajarkan orang lain (A) lalu buatkan diagramnya (V).",
            "Eksplorasi strategi mana yang paling efektif per mata kuliah."
        ],
        "color": "#8b5cf6" 
    }
}
