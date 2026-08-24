# 📰 AI Content Intelligence & Computational Media Platform

An LLM-powered web application that transforms unstructured articles into structured content insights, generated copy, and computational media analysis.

By combining **Natural Language Processing (NLP)**, **structured LLM outputs**, and **communication theory**, this project explores how large language models can support both practical content workflows and computational analysis of media texts.

The platform is designed as an interdisciplinary AI application at the intersection of:

**Artificial Intelligence · NLP · Data Analysis · Computational Media · Communication Research**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?style=flat-square)
![OpenAI API](https://img.shields.io/badge/LLM-OpenAI%20API-green?style=flat-square)
![Pandas](https://img.shields.io/badge/Data-Pandas-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 🌟 Project Overview

Traditional content analysis often requires manually reading, coding, categorizing, and comparing large amounts of text.

This project explores whether an LLM-powered pipeline can automate parts of this workflow while maintaining **structured, interpretable, and evaluable outputs**.

The system takes an article as input and generates multiple layers of analysis:

```text
Article
   │
   ▼
LLM Analysis Pipeline
   │
   ├── Summary
   ├── Key Points
   ├── Topic Classification
   ├── Sentiment Analysis
   ├── Target Audience
   ├── SEO Keywords
   ├── Social Media Copy
   │
   └── Computational Media Analysis
           ├── Framing
           ├── Key Actors
           └── Perspective / Source Analysis
```

---

## 🚀 Core Features

### 1. 📌 Content Intelligence

The platform extracts structured information from unstructured articles.

* **Automated Summarization**
  Generates concise summaries of long-form articles.

* **Key Point Extraction**
  Identifies the main arguments, facts, and takeaways.

* **Topic Classification**
  Categorizes articles into predefined or dynamically identified topics.

* **Sentiment Analysis**
  Analyzes the overall emotional tone of the content.

* **Target Audience Analysis**
  Estimates the primary audience based on topic, language, and content characteristics.

* **SEO Keyword Extraction**
  Identifies primary, secondary, and long-tail keywords.

* **Cross-Platform Copy Generation**
  Adapts the same source content for different communication contexts, such as LinkedIn or Xiaohongshu/RED.

---

## 🔬 Computational Media Analysis

A key component of this project is the application of computational methods to concepts from **communication and media studies**.

### News Framing Analysis

The system explores news framing using concepts derived from **Robert Entman's framing theory**.

Rather than treating an article as a collection of keywords, the analysis examines how an issue is constructed through different framing dimensions:

```text
Problem Definition
        │
        ▼
Causal Interpretation
        │
        ▼
Moral Evaluation
        │
        ▼
Treatment / Policy Recommendation
```

The system aims to identify:

* Primary and secondary frames
* Problem definitions
* Causal interpretations
* Evaluative language
* Suggested or implied responses
* Key actors and institutions

Example frame categories may include:

```text
Economic Impact
Public Policy
Public Safety
Social Impact
Environmental Impact
Technological Innovation
```

### Frame Distribution

For multiple analyzed articles, the system can aggregate framing results and visualize the distribution of different frames.

For example:

```text
Economic Impact       ████████████ 40%
Public Policy         ████████     27%
Social Impact         █████        18%
Public Safety         ████         15%
```

This creates a bridge between qualitative communication concepts and quantitative computational analysis.

### Source & Perspective Analysis

A later module will examine how different actors and institutions are represented within media texts.

Potential dimensions include:

* Government representation
* Expert representation
* Business representation
* Citizen perspectives
* Institutional source diversity
* Potential perspective patterns

The system will treat these outputs as **analytical indicators rather than definitive judgments of media bias**.

---

## 🏗️ System Architecture

```text
                    User Input
               Article / News Text
                         │
                         ▼
              ┌────────────────────┐
              │  Streamlit Web UI  │
              └──────────┬─────────┘
                         │
                         ▼
              ┌────────────────────┐
              │ Prompt Engineering │
              │ & Analysis Pipeline│
              └──────────┬─────────┘
                         │
                         ▼
              ┌────────────────────┐
              │     LLM API        │
              │  Structured Output │
              └──────────┬─────────┘
                         │
                         ▼
              ┌────────────────────┐
              │   JSON Parsing     │
              │ & Validation       │
              └──────────┬─────────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
     Content Intelligence    Media Analysis
          Module                  Module
              │                     │
              │                     ├── Framing
              │                     ├── Actors
              │                     └── Perspective
              │
              ├── Summary
              ├── Topics
              ├── Sentiment
              ├── Audience
              ├── Keywords
              └── Copy Generation
              │
              └──────────┬──────────┘
                         ▼
              ┌────────────────────┐
              │ Interactive         │
              │ Streamlit Dashboard │
              └────────────────────┘
```

---

## 📊 Structured Output

A major design principle of this project is to avoid relying solely on free-form LLM responses.

The analysis pipeline is designed to transform model output into structured JSON that can be processed programmatically.

Example:

```json
{
  "summary": "...",
  "key_points": [
    "...",
    "...",
    "..."
  ],
  "topic": "Technology",
  "sentiment": "Neutral",
  "target_audience": [
    "Technology professionals",
    "Students"
  ],
  "seo_keywords": [
    "artificial intelligence",
    "large language models",
    "NLP"
  ],
  "framing": {
    "primary_frame": "Technological Innovation",
    "secondary_frames": [
      "Economic Impact",
      "Social Impact"
    ]
  }
}
```

This structured approach makes the output easier to:

* Store
* Analyze
* Visualize
* Compare
* Evaluate
* Reuse in downstream applications

---

## 🧪 Evaluation

An important goal of this project is to investigate not only **what an LLM can generate**, but also **how reliably it can perform structured content analysis**.

A manually annotated sample dataset will be developed to compare human annotations with model-generated outputs.

Potential evaluation tasks include:

* Topic classification
* Sentiment classification
* Frame classification

Planned evaluation metrics:

```text
Accuracy
Precision
Recall
F1 Score
```

The evaluation component will help identify where LLM-based analysis performs well and where human review remains necessary.

---

## 🛠️ Tech Stack

**Programming**

`Python`

**Data Processing**

`Pandas` · `JSON` · `NumPy`

**AI / NLP**

`LLM APIs` · `Prompt Engineering` · `Structured Outputs` · `NLP`

**Web Application**

`Streamlit`

**Database / Data**

`SQLite` · `CSV`

**Development**

`Git` · `GitHub` · `PyCharm`

---

## 📁 Project Structure

```text
ai-content-intelligence/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── analyzer.py
│   ├── llm.py
│   ├── prompts.py
│   └── utils.py
│
├── data/
│   └── sample_articles/
│
└── tests/
    └── test_analyzer.py
```

The project structure will evolve as additional analysis modules and evaluation components are implemented.

---

## 🗺️ Roadmap

### Phase 1 — Core LLM Pipeline

* [ ] Article input
* [ ] LLM API integration
* [ ] Structured JSON output
* [ ] Summary generation
* [ ] Key point extraction
* [ ] Topic classification
* [ ] Sentiment analysis

### Phase 2 — Content Intelligence

* [ ] Target audience analysis
* [ ] SEO keyword extraction
* [ ] Cross-platform copy generation
* [ ] Streamlit dashboard

### Phase 3 — Computational Media Analysis

* [ ] News framing analysis
* [ ] Frame classification
* [ ] Key actor extraction
* [ ] Frame distribution visualization
* [ ] Source & perspective analysis

### Phase 4 — Evaluation

* [ ] Build manually annotated dataset
* [ ] Human vs. LLM comparison
* [ ] Accuracy / Precision / Recall / F1
* [ ] Error analysis

### Phase 5 — Multi-Article Analysis

* [ ] Batch article processing
* [ ] Cross-article comparison
* [ ] Topic distribution
* [ ] Frame distribution
* [ ] Keyword trends
* [ ] Comparative media analysis

---

## 🎯 Project Goals

This project has two complementary goals.

**Engineering Goal**

To build practical experience in:

> Python → APIs → JSON → Data Processing → LLM Applications → Web Applications → Evaluation

**Research Goal**

To explore how computational methods and LLMs can support the analysis of:

> Media Content → Framing → Perspectives → Information Patterns

Ultimately, the project aims to demonstrate how **AI and computational methods can be applied to problems traditionally studied through communication and social science approaches**.

---

## 📚 Background & Motivation

This project is informed by my academic background in **Journalism & Communication** and **Agricultural Water Resources Engineering**, as well as professional experience in public-sector governance.

The combination of communication theory, engineering thinking, and computational methods motivates my interest in **AI applications, computational media, and interdisciplinary data analysis**.

---

## 📄 License

This project is licensed under the MIT License.

我会特别建议你现在就用这一版作为“项目蓝图”，但**不要把所有代码结构一次性照着建出来**。

你现在实际上只有：

```text
app.py
README.md
requirements.txt
```

完全没问题。

我们接下来可以按照 README 的 Roadmap 一步一步实现。第一阶段只做：

```text
Article
  ↓
Python
  ↓
LLM API
  ↓
Structured JSON
  ↓
Summary + Key Points + Topic + Sentiment
```

等这个真正跑通以后，再创建 `src/`、`data/`、`tests/`。

这样最终 GitHub 上的 README、代码和 commit history 会彼此对应，项目会显得非常真实。
