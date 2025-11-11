# Solar Irradiance Data Cleaning & Pipeline (Week 0 - Interim Submission)

This repository contains the Week 0 data exploration and cleaning pipeline for the Solar Challenge Project.  
The goal of this stage is to **load, profile, clean, and export** solar irradiance datasets for multiple West African regions.  

---

## Repository Structure

solar-challenge-week0/
│── data/ # Raw and cleaned data outputs
│ ├── cleaned
│ └── raw
│
│── notebooks/
│ └── benin_eda.ipynb # Interactive EDA + transformation steps
│ └── sierraleone_eda.ipynb # Interactive EDA + transformation steps
│ └── togo_eda.ipynb # Interactive EDA + transformation steps
│
│── src/
│ └── data_pipeline.py # Modular data transformation functions
│
│── scripts/
│ └── (future optional CLI utilities)
│
│── tests/
│ └── (placeholder for later unit tests)
│
│── requirements.txt
│── README.md


The **`src/data_pipeline.py`** module contains reusable functions for:
- loading data
- standardizing column names
- converting timestamp fields
- detecting outliers using Z-scores
- imputing missing values with median values
- exporting cleaned datasets

---

## Design & Code Organisation (Why This Matters)

To improve maintainability and reusability, all major processing steps are written as **modular functions** in `src/data_pipeline.py` instead of embedding all logic inside notebooks.

This supports:
- cleaner notebooks
- re-use of processing logic across **Sierra Leone**, **Benin**, and **Togo**
- easier testing later in the project

---

## How to Run the Notebook

1. Clone the repository:

```bash
git clone https://github.com/Robel-fikadu70/solar-challenge-week0.git
cd solar-challenge-week0
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt

```
4. Open Jupyter Notebook:

```bash
jupyter notebook notebooks/sierraleone_eda.ipynb
```