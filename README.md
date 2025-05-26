# 📊 Portfolio Project: End-to-End Data Pipeline with Python

> 👩‍💻 Author: jiw0n0107  
> 🗓️ Started: 2025  
> 📁 Repository: `portfolio-data`

---

## 🎯 Project Overview

This project demonstrates a fundamental yet production-relevant **end-to-end data pipeline**, designed to simulate real-world data engineering workflows. It covers the essential steps of a pipeline: **data ingestion, cleaning, transformation, and export**, all using Python with `pandas`.

The pipeline architecture is intentionally modular and scalable, intended for extension into automated batch jobs or real-time processing.

---

## 🧱 Project Structure

```
portfolio-data/
├── raw_data/              # Unprocessed source files (e.g., downloaded CSVs or API pulls)
├── cleaned_data/          # Cleaned and transformed data
├── scripts/               # ETL (Extract, Transform, Load) scripts
│   └── basic_pipeline.py  # Main processing script
├── README.md              # Documentation
```

---

## 🛠️ Technologies Used

- **Python 3.10+**
- `pandas`: data manipulation and cleaning
- `os`, `glob`: basic file management
- `csv`, `datetime`: raw data formatting
- (Optionally expandable to `Airflow`, `DBMS`, or `API` ingestion later)

---

## 🔁 Pipeline Process Description

| Step | Description |
|------|-------------|
| **1. Ingestion** | Reads raw `.csv` files from the `raw_data/` directory. This mimics fetching data from an API, FTP, or other source. |
| **2. Cleaning** | Handles missing values, removes duplicates, renames columns for schema consistency. |
| **3. Transformation** | Applies date formatting, aggregates user actions by period (e.g., 3-day bins). |
| **4. Export** | Writes a cleaned version to the `cleaned_data/` directory in `.csv` format. |

Each stage is modular and can be extended to support database storage, error logging, and validation layers.

---

## ✅ Usage Instructions

```bash
# Step 1: Move into scripts directory
cd scripts/

# Step 2: Run the pipeline
python basic_pipeline.py
```

Make sure you have the necessary dependencies installed (`pandas`, `datetime`, etc.). All outputs will be placed in the `cleaned_data/` folder.

---

## 📈 Extension Ideas

This project is designed for growth:

- Add **logging** and **exception handling** to monitor failures
- Integrate with **Apache Airflow** for production-level orchestration
- Store cleaned data into **PostgreSQL** or a **cloud warehouse**
- Implement **unit tests** using `pytest`
- Visualize output using **Power BI** or `seaborn`

---

## 📚 Learning Outcomes

- Mastered data pipeline architecture and implementation flow
- Practiced real-world file processing and transformation logic
- Built a maintainable project folder and commit history for future portfolios

---

## 📬 Contact

Feel free to reach out if you're reviewing this as part of a recruitment or collaboration opportunity.

📧 jiw0n0107@yahoo.com  
🌐 GitHub: [github.com/jiw0n0107](https://github.com/jiw0n0107)

---

> *This project is a part of my continuous journey in data engineering and pipeline automation. Thank you for reading!* 🙏
