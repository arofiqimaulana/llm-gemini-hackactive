## RAG (Retrieval Augmented Generation)

- RAG  adalah  sebuah  teknik  yang  menggabungkan  retrieval  (pencarian  informasi  eksternal)  dan  generation (pembuatan teks oleh LLM). 
- Teknik ini memungkinkan pengimplementasian LLM hanya untuk tanya jawab pada topik tertentu sesuai dengan dokumen yang diberikan.
- Terdapat metode chnunks yang digunakan untuk memecah (split) teks panjang dari sebuah PDF menjadi potongan-potongan kecil (chunks) yang lebih mudah diproses oleh LLM supaya konteks tidak terpotong. 
- Chunk juga biasanya overlapping agar konteks tidak terpotong dan kalimat yang ada di batas chunk tetap bisa “terbaca utuh” oleh model
    - Chunk 1: karakter 1–1000
    - Chunk 2: karakter 801–1800

## LangChain
- Saat ingin menggunakan Gemini, kita perlu menggunakan package google-genai. Sementara itu, untuk mengakses Groq, kita harus menggunakan groq-python. Pertanyaannya, bagaimana jika kita ingin menggunakan model AI lainnya? Apakah setiap model memiliki konfigurasi dan parameter yang berbeda?

- Perbedaan inilah yang menimbulkan kebutuhan akan sebuah framework yaitu **LangChain** yang mampu mengakomodasi berbagai model AI sekaligus, sehingga pengaturan parameter dapat diseragamkan dan integrasi menjadi lebih sederhana.

## Gateway API
- API yang bisa dipanggil oleh aplikasi lain untuk melakukan inferensi/permintaan terhadap model bahasa besar (LLM).


# Reference
- https://console.groq.com/home
- https://openrouter.ai/ 
