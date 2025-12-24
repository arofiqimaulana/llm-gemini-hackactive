## RAG (Retrieval Augmented Generation)

- RAG  adalah  sebuah  teknik  yang  menggabungkan  retrieval  (pencarian  informasi  eksternal)  dan  generation (pembuatan teks oleh LLM). 
- Teknik ini memungkinkan pengimplementasian LLM hanya untuk tanya jawab pada topik tertentu sesuai dengan dokumen yang diberikan.

## LangChain
- Saat ingin menggunakan Gemini, kita perlu menggunakan package google-genai. Sementara itu, untuk mengakses Groq, kita harus menggunakan groq-python. Pertanyaannya, bagaimana jika kita ingin menggunakan model AI lainnya? Apakah setiap model memiliki konfigurasi dan parameter yang berbeda?

- Perbedaan inilah yang menimbulkan kebutuhan akan sebuah framework yaitu **LangChain** yang mampu mengakomodasi berbagai model AI sekaligus, sehingga pengaturan parameter dapat diseragamkan dan integrasi menjadi lebih sederhana.

## Gateway API
- API yang bisa dipanggil oleh aplikasi lain untuk melakukan inferensi/permintaan terhadap model bahasa besar (LLM).


# Reference
- https://console.groq.com/home
- https://openrouter.ai/ 
