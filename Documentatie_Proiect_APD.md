# Documentație Proiect APD: E-commerce Web Scraper

Acest document conține specificațiile, cerințele și rezultatele analizelor de performanță pentru proiectul de Algoritmi Paraleli și Distribuiți (APD).

---

## 1. Tema Proiectului / Cerințe

**Obiectiv:** Implementarea unui Web Scraper pentru extragerea de date (produse, prețuri) de pe o platformă de E-commerce (eMAG), demonstrând diferențele de performanță între o execuție secvențială și diverse abordări de paralelizare.

**Metode Implementate:**
1. **Secvențial (`sequential/seq_scraper.py`)**: Extragerea datelor pagină cu pagină pe un singur fir de execuție.
2. **Paralel cu Threads (`parallel/scraper_threads.py`)**: Folosind `concurrent.futures.ThreadPoolExecutor` pentru paralelizarea cererilor HTTP (eficient pentru operații I/O-bound).
3. **Paralel cu Multiprocessing (`parallel/scraper_multiprocess.py`)**: Folosind `concurrent.futures.ProcessPoolExecutor` pentru distribuirea procesării pe mai multe nuclee ale procesorului.

**Tehnologii și Limbaje Folosite:**
* **Limbaj:** Python 3.13
* **Parsare HTML:** `BeautifulSoup4` (din biblioteca `bs4`)
* **Cereri HTTP:** `curl_cffi` (pentru a evita blocajele de tip Cloudflare/anti-bot) cu fallback pe `requests`.
* **Procesare Date:** `pandas` (sau CSV standard prin `csv`)
* **Analiză & Grafice:** `matplotlib`, `numpy`

---

## 2. Informații despre Mașina de Test

Testele de performanță și rularea algoritmilor au fost efectuate pe un sistem cu următoarele specificații:
* **Sistem de Operare:** Windows 11 (AMD64)
* **Procesor:** AMD Ryzen (Family 23, Model 96)
* **Nuclee:** 16 Nuclee Logice (Threads)
* **Mediu de Execuție:** Mediul virtual Python (venv) izolat, conexiune stabilă la internet.

---

## 3. Rezultate Experimentale (Timpi de Rulare și Speedup)

Extragerea a fost testată pentru 3 seturi de date diferite (Small, Medium, Large) pe categoria "laptopuri". Din cauza mecanismelor de limitare a traficului (Rate Limiting) impuse de serverele eMAG, setul "Large" a fost setat la 30 de pagini (aprox. 1800 de produse) pentru a păstra consistența datelor.

| Set de Date | Pagini Extrase | Timp Secvențial | Timp Threads | Timp Multiprocess | Speedup Threads | Speedup Multiprocess |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Small** | 3 | 9.89 sec | 5.44 sec | 8.09 sec | **1.82x** | 1.22x |
| **Medium** | 10 | 33.83 sec | 11.45 sec | 17.84 sec | **2.96x** | 1.90x |
| **Large** | 30 | 98.67 sec | 26.26 sec | 47.16 sec | **3.76x** | 2.09x |

### Concluzii și Analiza Performanței:
1. **Modelul Multi-Threading** a oferit **cel mai bun Speedup (până la 3.76x)**. Motivul este că operația de Web Scraping este dominată de timpul de așteptare pentru răspunsul rețelei (**I/O-bound**). Thread-urile permit programului să inițieze mai multe conexiuni HTTP simultan fără penalizări mari de memorie.
2. **Modelul Multiprocessing** a fost mai lent decât Multi-Threading (Speedup maxim 2.09x), deși a fost mai rapid decât execuția secvențială. Explicația este reprezentată de costul ridicat de creare a proceselor noi (overhead) și comunicarea inter-proces (IPC), lucruri care nu sunt justificate pe deplin pentru task-uri I/O-bound. Multiprocessing-ul excelează la operații CPU-bound (cum ar fi procesare grea de imagine sau ecuații matematice).
3. Ambele metode paralele scalează bine odată cu creșterea volumului de muncă, dovedind necesitatea tehnicilor APD în extragerea datelor din mediul online.
