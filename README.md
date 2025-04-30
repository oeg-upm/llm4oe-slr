# LLM4OE-SLR

Large Language Models (LLMs) are increasingly being used to support ontology engineering (OE) tasks, yet a comprehensive understanding of their roles, effectiveness, and application domains remains limited. This project presents a **Systematic Literature Review (SLR)** focused on how LLMs contribute to various phases of ontology development. We analyzed 30 peer-reviewed papers published between 2018 and 2024 and extracted 41 distinct OE tasks where LLMs are applied.  

---

## 📁 Repository Structure

### 📂 `Paper Selection/`

This folder documents the **paper selection process**, with each filtering step tracked in individual Excel sheets for full transparency and reproducibility.

The screening process includes the following steps:

1. **Raw Search**  
   Initial search results retrieved from five major academic databases (Web of Science, ACM Digital Library, IEEE Xplore, Scopus, and Google Scholar), yielding **11,985 records** based on predefined keywords, time range, and language filters.

2. **Duplicate Removal**  
   Automatic deduplication across databases reduced the dataset to **5,275 unique entries**.

3. **Title Screening**  
   Manual title screening was performed, narrowing the pool to **204 potentially relevant papers**.

4. **Abstract & Peer-Review Filtering**  
   We applied two filters:
   - Peer-reviewed status
   - Abstract relevance to LLM-based ontology engineering  
   This resulted in **38 papers**.  
   After further inspection, **8 papers were excluded** due to lack of alignment with our scope (marked with strikethrough in the spreadsheet), leading to **30 final included studies**.

5. **Final Inclusion**  
   These 30 papers form the core dataset for downstream analysis.  
   From them, we extracted **41 LLM-based OE activities**, summarized across the ontology development pipeline.

---

### 📂 `Data Extraction/`

This folder includes **five tables** designed to support analysis for the four research questions (RQs):

- `Full_Data_Extraction_from_30_papers.xlsx`  
  Master dataset including article metadata such as title, authors, year, peer-reviewed status, and language.

- `Data_Extraction_for_RQ1.xlsx`  
  Used to analyze **RQ1** (Ontology development activities supported by LLMs).  
  Includes activity name, task definitions, and corresponding papers.

- `Data_Extraction_for_RQ2.xlsx`  
  Used to analyze **RQ2** (How LLMs support OE activities).  
  Contains roles of LLMs, types of models used, input/output formats, and whether human-in-the-loop was involved.

- `Data_Extraction_for_RQ3.xlsx`  
  Used to analyze **RQ3** (Performance evaluation).  
  Includes experiment existence, evaluation methods (quantitative, qualitative, hybrid), datasets used, metrics, and reported results.

- `Data_Extraction_for_RQ4.xlsx`  
  Used to analyze **RQ4** (Application domains).  
  Lists domains where LLMs have been applied, such as healthcare, education, and finance.

---

### 📂 `Experiment Datasets/`

Furthermore, in this folder we compiled a comprehensive summary of ** experiment datasets** used in the experiments evaluation reported by the included studies.  
For each dataset.

- The dataset summary table is available at:  
  `full_experiment_datasets_summary.xlsx`
  For each dataset, we list:
- Acronym and full name  
- Access URL  
- Application domain (e.g., Medicine, Music, Anatomy)

This enables users and researchers to easily locate the resources used in LLM-based OE evaluations and potentially reuse them for futher benchmark creation.

---

