# 🛒 E-commerce Web Scraper (Sequential & Parallel)

Proiect realizat în cadrul cursului **APD (Algoritmi Paraleli și Distribuiți)**.  
Target: Magazinul online [eMAG](https://www.emag.ro) — extragerea datelor pentru o categorie specifică de produse (ex. laptopuri).

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
│   └── seq_scraper.py          # Varianta secventiala
├── parallel/
│   ├── scraper_threads.py      # Varianta paralela #1 — Threads
│   └── scraper_multiprocess.py # Varianta paralela #2 — Multiprocessing
├── utils/
│   ├── __init__.py             # Exporturi comune
│   ├── fetcher.py              # Logica de descarcare pagini HTTP
│   ├── scraper.py              # Logica de extragere si retries
│   ├── writer.py               # Salvare date in format CSV
│   └── parsers/                
│       └── emag_parser.py      # Logica de parsare HTML (BeautifulSoup)
├── data/
│   └── output/                 # Rezultate scraping impartite pe metode
│       ├── secvential/
│       ├── threads/
│       └── multiprocess/
├── benchmarks/
│   └── run_benchmarks.py       # Script pentru rulare benchmark-uri si generare grafice
├── requirements.txt
├── .gitignore
├── Tema_Proiect.md
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
python sequential/seq_scraper.py

# Varianta paralela #1 (Threads)
python parallel/scraper_threads.py

# Varianta paralela #2 (Multiprocess)
python parallel/scraper_multiprocess.py

# Rulare teste de performanta (Benchmark comparativ)
python benchmarks/run_benchmarks.py
```

---

## 📊 Date extrase

Pentru fiecare produs extras de pe eMAG:

- Magazinul sursă (Store)
- Denumire produs
- Preț curent

---

## 📈 Metrici de performanță

- ⏱️ Timp total de execuție
- 📄 Pagini procesate / secundă (throughput)
- ⚡ Speedup față de varianta secvențială
- 💾 Utilizare RAM
- 🖥️ Utilizare CPU

---

## ⚠️ Note

- Scraping-ul este realizat exclusiv în **scop educațional**, pentru a demonstra diferențele de performanță între execuția secvențială și cea paralelă din cadrul cursului APD.
- S-a adăugat delay între request-uri pentru a nu supraîncărca serverul eMAG și pentru a evita pe cât posibil blocajele (ex. CAPTCHA, Rate Limiting).
- Se recomandă folosirea de headere corespunzătoare (`User-Agent`) la rulare.

---

## 👤 Autor

**Maximilian Andrei**  

Facultatea de Automatică Calculatoare și Electronică

An universitar 2025–2026
