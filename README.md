# LLM4OE-SLR [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15313672.svg)](https://doi.org/10.5281/zenodo.15313672)

Large Language Models (LLMs) are increasingly being used to support ontology engineering (OE) tasks, yet a comprehensive understanding of their roles, effectiveness, and application domains remains limited. This project presents a **Systematic Literature Review (SLR)** focused on how LLMs contribute to various phases of ontology development. We analyzed 34 peer-reviewed papers published between 2018 and May 2025 and extracted 46 distinct OE tasks where LLMs are applied. 

---

## Repository Structure

### `Paper Selection/`

This folder documents the **paper selection process**, with each filtering step tracked in individual Excel sheets for full transparency and reproducibility.

The screening process includes the following steps:

1. **Raw Search**  
   Initial search results retrieved from five major academic databases (Web of Science, ACM Digital Library, IEEE Xplore, Scopus, and Google Scholar), yielding **15,688 papers** based on predefined keywords, time range, and language filters.

2. **Duplicate Removal**  
   Automatic deduplication across databases reduced the dataset to **7,179 unique papers**.

3. **Title Screening**  
   Manual title screening was performed, narrowing the pool to **271 potentially relevant papers**.

4. **Abstract & Peer-Review Filtering**  
   We applied two filters:
   - Peer-reviewed status
   - Abstract relevance to LLM-based ontology engineering  
    This resulted in **46 papers**.  
    After further inspection, **10 papers were excluded** due to lack of alignment with our scope (marked with strike through in the spreadsheet), leading to **36 final included papers**.

5. **Final Inclusion**  
   These **36 papers** form the core dataset for downstream analysis.  
   From them, we extracted **49 LLM-based OE studies**, summarized across the ontology development pipeline.

---

### `Data Extraction/`

This folder includes **five tables** designed to support analysis our research questions (RQs):

- `Full_Data_Extraction_from_49_papers.xlsx`(https://github.com/oeg-upm/llm4oe-slr/blob/main/Data%20Extraction/Full_Data_Extraction_from_49_papers.xlsx) 
  Dataset including article metadata such as title, authors, year, peer-reviewed status, and language.

- `Data_Extraction_for_RQ1.xlsx`(https://github.com/oeg-upm/llm4oe-slr/blob/main/Data%20Extraction/Data_Extraction_for_RQ1.xlsx)
  Used to analyze **RQ1** (Ontology development activities supported by LLMs).  
  Includes activity name, task definitions, and corresponding papers.

- `Data_Extraction_for_RQ2.xlsx`(https://github.com/oeg-upm/llm4oe-slr/blob/main/Data%20Extraction/Data_Extraction_for_RQ2.xlsx)
  Used to analyze **RQ2** (How LLMs support OE activities).  
  Contains roles of LLMs, types of models used, prompt techniques, input/output formats, and whether human-in-the-loop was involved.

- `Data_Extraction_for_RQ3.xlsx`(https://github.com/oeg-upm/llm4oe-slr/blob/main/Data%20Extraction/Data_Extraction_for_RQ3.xlsx)
  Used to analyze **RQ3** (Performance evaluation).  
  Includes experiment existence, evaluation methods (quantitative, qualitative, hybrid), datasets used, metrics, and reported results.

- `Data_Extraction_for_RQ4.xlsx`  
  Used to analyze **RQ4** (Application domains).(https://github.com/oeg-upm/llm4oe-slr/blob/main/Data%20Extraction/Data_Extraction_for_RQ4.xlsx) 
  Lists domains where LLMs have been applied, such as healthcare, education, and finance.

---

### `Experiment Datasets/`

Furthermore, in this folder, we compiled a comprehensive summary of ** experiment datasets** used in the experiments evaluation reported by the included studies.  
For each dataset.(https://github.com/oeg-upm/llm4oe-slr/blob/main/Experiment%20Datasets/full_experiment_datasets_summary.xlsx)

- The dataset summary table is available at:  
  `full_experiment_datasets_summary.xlsx`
  
For each dataset, we list:
- Acronym and full name  
- Access URL  
- Application domain (e.g., Medicine, Music, Anatomy)

---

### `Figures/`

This directory contains the figures included in the survey, along with the source files and scripts used to generate them.

**Paper Selection Process**  
- `Figures/LLM4OE_SLR_search_pipeline.pdf`(https://github.com/oeg-upm/llm4oe-slr/blob/main/Figures/LLM4OE_SLR_search_pipeline.pdf)

**Research Question RQ1 – LLM-Supported Ontology Engineering Activities**  
- `Figures/Figure_for_RQ1.pdf`(https://github.com/oeg-upm/llm4oe-slr/blob/main/Figures/Figure_for_RQ1.pdf)

**Overview of LLM-supported ontology engineering tasks based on 46 experiments from 34 papers**  
- `Figures/Taxonomic framework of LLM-supported ontology engineering tasks.svg`(https://github.com/oeg-upm/llm4oe-slr/blob/main/Figures/Taxonomic%20framework%20of%20LLM-supported%20ontology%20engineering%20tasks.svg)


