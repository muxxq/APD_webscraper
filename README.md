# 📚 Books to Scrape — Web Scraper (Sequential & Parallel)

Proiect realizat în cadrul cursului **APD (Algoritmi Paraleli și Distribuiți)**.  
Target: [books.toscrape.com](https://books.toscrape.com) — site de test dedicat web scraping-ului.

---

## 🎯 Obiectiv

Implementarea unui web scraper în **3 variante** cu scopul de a compara performanța:

| Variantă | Metodă | Termen |
|---|---|---|
| Secvențială | `requests` + `BeautifulSoup` | S5 |
| Paralelă #1 | `ThreadPoolExecutor` / `asyncio` | S8 |
| Paralelă #2 | `multiprocessing` / `Scrapy` | S10 |

---

## 🛠️ Tehnologii folosite

- **Limbaj:** Python 3.11+
- **HTTP:** `requests`, `httpx`, `aiohttp`
- **Parsing HTML:** `BeautifulSoup4`, `lxml`
- **Paralelism:** `concurrent.futures`, `asyncio`, `multiprocessing`
- **Date:** `pandas`, `openpyxl`
- **Benchmarking:** `matplotlib`, `psutil`, `memory-profiler`
- **Progress:** `tqdm`

---

## 📁 Structura proiectului

```
web-scraper/
├── sequential/
│   └── scraper_seq.py          # Varianta secventiala
├── parallel/
│   ├── scraper_threads.py      # Varianta paralela #1 — Threads
│   └── scraper_multiprocess.py # Varianta paralela #2 — Multiprocessing
├── utils/
│   ├── parser.py               # Logica de parsare HTML
│   ├── storage.py              # Salvare date CSV/Excel
│   └── metrics.py              # Masurare timp, CPU, RAM
├── data/
│   └── output/                 # Rezultate scraping (ignorat de git)
├── benchmarks/
│   └── compare.py              # Grafice comparative
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup

### 1. Clonează repo-ul
```bash
git clone https://github.com/USERNAME/web-scraper.git
cd web-scraper
```

### 2. Creează și activează virtual environment
```bash
# Creare
python -m venv venv

# Activare — Windows
venv\Scripts\activate

# Activare — macOS/Linux
source venv/bin/activate
```

### 3. Instalează dependențele
```bash
pip install -r requirements.txt
```

---

## 🚀 Rulare

```bash
# Varianta secventiala
python sequential/scraper_seq.py

# Varianta paralela #1
python parallel/scraper_threads.py

# Benchmark comparativ
python benchmarks/compare.py
```

---

## 📊 Date extrase

Din fiecare carte de pe `books.toscrape.com`:

- Titlu
- Preț
- Rating (stele)
- Disponibilitate (In stock / Out of stock)
- URL pagina carte

---

## 📈 Metrici de performanță

- ⏱️ Timp total de execuție
- 📄 Pagini procesate / secundă (throughput)
- ⚡ Speedup față de varianta secvențială
- 💾 Utilizare RAM
- 🖥️ Utilizare CPU

---

## ⚠️ Note

- Site-ul `books.toscrape.com` este creat **special pentru practică** de web scraping — nicio restricție legală.
- Totuși, adăugat delay între request-uri pentru a nu supraîncărca serverul.
- Se respectă bunele practici: `User-Agent` header, retry logic, rate limiting.

---

## 👤 Autor

**Maximilian Andrei**  

Facultatea de Automatică Calculatoare și Electronică

An universitar 2025–2026
