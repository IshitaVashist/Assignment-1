# 📌 📖  BACKEND PROJECT


# PubMed Papers CLI 📚🖥️

A command-line tool to fetch recent PubMed research papers based on a search query, parse their metadata, and export the results to a CSV file.

---

## 📦 Features

- Fetch paper metadata using PubMed's Entrez API
- Parse paper details including:
  - PubMed ID
  - Title
  - Publication Date
  - Authors
  - Company affiliations (using simple heuristics)
  - Corresponding author email
- Export parsed data to a clean CSV file
- Debug flag to print paper IDs and parsed data count
- CLI built using Python, Poetry, and `argparse`
- Clean, Poetry-managed dependency setup

---

## 📂 Project Structure

```

project/
├── pyproject.toml
├── README.md
├── project/
│   ├── **init**.py
│   ├── api\_client.py
│   ├── paper\_processor.py
│   ├── csv\_writer.py
│   ├── cli.py

````

---

## 🛠️ Installation & Setup

### 📌 Install Python 3.11+

Download from: [python.org](https://www.python.org/downloads/release/python-3110/)

### 📌 Install Poetry

```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
````

Add Poetry to PATH or run it via its full path if necessary.

---

### 📌 Install Project Dependencies

Inside your project folder:

```Powershell/bash
poetry install
```

---

## 🚀 Usage

From your project directory, run:

```Powershell/bash
poetry run get-papers-list "covid 19" --file papers.csv --debug
```

**Options:**

* `"covid 19"` → your PubMed search query
* `--file papers.csv` → output CSV filename (optional, default is `papers.csv`)
* `--debug` → prints extra information like fetched IDs and number of parsed papers

**Example Output:**

```
Found 20 paper IDs: ['40642811', '40642808', ...]
Parsed 20 papers.
Saved 20 papers to papers.csv
```

---

## 🤖 LLM Usage (Assignment Requirement)

This project was developed with assistance from an LLM (ChatGPT 4o) for:

* Breaking down project requirements into structured development steps
* Generating clean Python code for PubMed API integration
* Handling XML parsing logic
* Structuring the CLI using `argparse`
* Designing the `pyproject.toml` configuration for Poetry
* Troubleshooting environment and package installation issues
* Generating this README template

LLM support streamlined complex steps, clarified API documentation interpretation, and accelerated prototyping while preserving full developer control over decisions and logic.

---

## 📑 License

MIT License (or as per assignment requirements)

---

## 📧 Author

Ishita Vashist

```
