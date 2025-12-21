# Generative AI Using Gemini

## Teknik Prompting
### 1. CoT - Chain-of-Thought
- Chain-of-Thought adalah pola penalaran linear dan berurutan, di mana model memecahkan masalah langkah demi langkah dari awal sampai kesimpulan.
- Cocok untuk: logika, matematika, analisis sebab–akibat, reasoning sederhana–menengah.
- Contoh Masalah: Jika satu server memproses 50 request/detik, berapa request dalam 2 menit?

### 2. ToT - Tree of Thoughts
- Tree of Thoughts memperluas CoT dengan banyak cabang pemikiran. Model:
    - Mengeksplor beberapa alternatif solusi
    - Mengevaluasi tiap cabang
    - Memilih jalur terbaik

- Contoh Masalah:
    - Bagaimana meningkatkan konversi landing page?

- Alur ToT (konseptual):
    - Cabang A: Optimasi copywriting
    - Cabang B: Optimasi UI/UX
    - Cabang C: Social proof & trust
    - Cabang D: Performance & loading speed

- Setiap cabang dianalisis → dibandingkan → dipilih kombinasi terbaik. 👉 Bukan satu jalur, tapi pohon keputusan.

### 3. ReAct (Reason + Act)
- ReAct menggabungkan:
    - Reasoning (berpikir)
    - Action (bertindak ke tools / environment)

- Model tidak hanya berpikir, tapi juga:
    - Memanggil API
    - Query database
    - Search
    - Eksekusi tool lain lalu menggunakan hasilnya untuk reasoning lanjutan.

- Cocok untuk: agent AI, chatbot berbasis tools, RAG, automation.

- Contoh Masalah:
    - Cek apakah domain tersedia dan sarankan alternatif.

- Alur ReAct (konseptual):
    - Reason: perlu cek ketersediaan domain
    - Act: panggil API WHOIS
    - Observe: domain sudah terdaftar
    - Reason: buat variasi nama
    - Act: cek alternatif
    - Final answer. 

- 👉 Ada loop Think → Act → Observe → Think.

### Kapan Pakai yang Mana?

- CoT → soal hitung, analisis lurus, edukasi
- ToT → decision making, brainstorming serius, strategi bisnis
- ReAct → chatbot pintar, agent AI, sistem otomatis (n8n, RAG, API)

## Temperature dan Max Output Tokens
- Temperature  mengontrol tingkat keacakan dalam pemilihan token dan kreativitas teks yang dihasilkan
- Skor Temperature berada pada rentang 0 - 2. 
- Temperature yang lebih tinggi menyebabkan 
    - Hasil yang lebih beragam dan kreatif
    - Terkadang teks yang didapat mungkin kurang relevan
- Temperature yang lebih rendah menyebabkan
    - Teks yang kurang kreatif dan beragam.
    - Temperature  0  bersifat  deterministik,  artinya  respons  dengan  probabilitas  tertinggi selalu dipilih.
- Max  Output  Tokens Menentukan  jumlah  token  maksimum  yang  dapat  dihasilkan  dalam respons.  
    - Untuk model Gemini, satu token terdiri dari sekitar empat karakter. 100 token setara dengan sekitar 6080 kata bahasa Inggris.

## Function Calling
- Function calling di LLM adalah mekanisme yang memungkinkan model tidak hanya menjawab dengan teks, tapi juga memutuskan kapan harus memanggil fungsi (kode / API / tool) beserta parameter yang tepat.Singkatnya
    - LLM = otak (reasoning)
    - Function = tangan (aksi nyata)
- Misal kita ingin membuat beberapa fungsi
    - 1. code_untuk_browsing -> buat deskripsi -> masukkan ke llm
    - 2. code_untuk_matikan_lampu -> buat deskripsi -> masukkan ke llm
    - 3. code_untuk_jalankan_musik -> buat deskripsi -> masukkan ke llm


# Referensi
- EXA : https://exa.ai/ 