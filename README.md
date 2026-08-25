# 📰 AI Content Intelligence

An LLM-powered platform for analyzing and comparing news articles, social media posts, forum posts, comments, and other online content.

The project combines **Python, LLM-based NLP, structured outputs, semantic embeddings, similarity analysis, and interactive data visualization** to transform unstructured content into structured and comparable insights.

> **AI · NLP · Semantic Analysis · Content Intelligence · Computational Media**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?style=flat-square)
![LLM](https://img.shields.io/badge/LLM-DeepSeek%20API-green?style=flat-square)
![Pandas](https://img.shields.io/badge/Data-Pandas-purple?style=flat-square)
![Scikit-learn](https://img.shields.io/badge/ML-scikit--learn-orange?style=flat-square)
![Sentence Transformers](https://img.shields.io/badge/NLP-Sentence%20Transformers-yellow?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 🌟 Overview

Online content is increasingly fragmented across news websites, social media platforms, forums, and user-generated discussions.

Analyzing these sources manually can make it difficult to identify recurring topics, differences in framing, and broader patterns across multiple pieces of content.

This project explores an AI-assisted approach to content intelligence.

Users can analyze a single piece of content or compare **2–10 pieces of content** simultaneously.

The system converts unstructured text into structured analytical dimensions and uses semantic embeddings to identify related topics across different pieces of content.

```text
                 Online Content
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     Article      Social Post     Forum / Comment
        │              │              │
        └──────────────┼──────────────┘
                       ▼
              LLM Content Analysis
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Content      Metadata      Framing
      Intelligence  Analysis      Analysis
          │
          ▼
     Topic Extraction
          │
          ▼
   Semantic Embeddings
          │
          ▼
    Similarity Analysis
          │
          ▼
    Topic Grouping
          │
          ▼
  Cross-Content Insights
```

---

## 🚀 Core Features

### 1. 📌 Single Content Analysis

The platform supports analysis of individual pieces of online content.

Supported content types include:

- News Article
- Social Media Post
- Forum Post
- Comment
- Other

For each piece of content, the system can generate:

- Summary
- Key Points
- Topic
- Sentiment
- Target Audience
- Audience Needs
- Primary Keywords
- Secondary Keywords
- Search Intent
- Content Framing

The system also detects the primary language of the input and generates natural-language analytical results in the same language.

Standardized classification labels such as sentiment and search intent remain in English to support cross-content comparison.

---

### 2. 📊 Multi-Content Comparison

Users can analyze between **2 and 10 pieces of content** in a single analysis session.

Each piece of content can include:

- Content Type
- Source
- Publication Date
- Content Text

The platform generates a structured comparison table containing analytical dimensions such as:

- Topic
- Sentiment
- Search Intent
- Primary Frame
- Generic Frames
- Issue-Specific Frames
- Primary Keywords

This makes it possible to compare how different sources or platforms discuss related issues.

---

### 3. 📈 Sentiment Distribution

The system aggregates sentiment classifications across multiple pieces of content.

Possible sentiment categories are:

```text
Positive
Neutral
Negative
```

The distribution is visualized interactively to provide a quick overview of the overall emotional orientation of the analyzed content set.

---

### 4. 🔍 Search Intent Analysis

The platform classifies the likely search intent associated with the content.

The current classification scheme includes:

```text
Informational
Navigational
Commercial
Transactional
```

This provides an additional perspective on how users may seek or interact with information related to the analyzed content.

---

### 5. 🧩 Content Framing Analysis

The platform incorporates a structured framing analysis inspired by concepts from communication and media research.

Rather than treating content only as a collection of keywords, the system examines which interpretive frames are emphasized.

#### Generic News Frames

The current categories include:

```text
Responsibility
Conflict
Human Interest
Economic Consequences
Morality
```

#### Issue-Specific Frames

The current categories include:

```text
Technology & Innovation
Risk & Threat
Policy & Regulation
Social Impact
```

For each piece of content, the system identifies:

- Primary Frame
- Generic Frames
- Issue-Specific Frames

Only frames supported by the content are selected.

The system does not force a frame when sufficient evidence is unavailable.

---

### 6. 📊 Cross-Content Frame Analysis

When multiple pieces of content are analyzed, framing results can be aggregated across the dataset.

This allows users to examine how frequently different frames occur and compare framing patterns across sources or content types.

For example:

```text
Economic Consequences
████████████████

Technology & Innovation
██████████

Social Impact
██████

Risk & Threat
████
```

This provides a bridge between qualitative framing concepts and quantitative content analysis.

---

## 🧠 Semantic Topic Analysis

One of the core NLP components of the project is semantic topic grouping.

Simple keyword matching can fail when different pieces of content describe the same idea using different vocabulary.

For example:

```text
Economic pressure on marriage

Housing costs affecting marriage decisions

Changing attitudes toward marriage

Choosing to remain single
```

These expressions do not share identical keywords, but some of them describe closely related concepts.

The platform therefore uses sentence embeddings to represent topics in a semantic vector space.

```text
Content
   │
   ▼
LLM Topic Extraction
   │
   ▼
Sentence Embedding
   │
   ▼
Semantic Vector
   │
   ▼
Cosine Similarity
   │
   ▼
Similarity-based Grouping
   │
   ▼
Representative Topic
```

The current implementation uses **Sentence Transformers** to generate embeddings and **cosine similarity** to measure semantic relatedness.

Related topics can then be grouped together and represented by a representative topic.

Example:

```text
Topic Group 1

Representative:
Economic pressure on marriage

- Economic pressure on marriage
- Housing costs affecting marriage decisions
- Changing attitudes toward marriage


Topic Group 2

Representative:
Choosing to remain single

- Choosing to remain single
```

This component enables the system to move beyond surface-level keyword matching toward semantic comparison.

---

## 📊 Cross-Content Insights

After analyzing multiple pieces of content, the platform provides several aggregate views.

These currently include:

- Article / Content Comparison
- Primary Frame Distribution
- Sentiment Distribution
- Search Intent Distribution
- Shared Topics
- Semantic Topic Groups

The goal is to identify patterns that may not be obvious when examining individual pieces of content separately.

---

## 🏗️ System Architecture

```text
                         User
                          │
                          ▼
                ┌──────────────────┐
                │  Streamlit Web UI │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Content Input    │
                │ & Metadata       │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Prompt Engineering│
                │ & Analysis Rules │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │     LLM API      │
                │ Structured JSON  │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Content Analysis │
                └────────┬─────────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
    Sentiment         Framing          Keywords
        │                │                │
        └────────────────┼────────────────┘
                         │
                         ▼
                  Topic Extraction
                         │
                         ▼
                Sentence Embeddings
                         │
                         ▼
                 Cosine Similarity
                         │
                         ▼
                 Semantic Grouping
                         │
                         ▼
              Cross-Content Analysis
                         │
                         ▼
                 Streamlit Dashboard
```

---

## 🔬 Technical Approach

The project combines several layers of AI and data processing.

### LLM-based NLP

The LLM is responsible for extracting structured information from unstructured content.

The system uses prompt engineering to define:

- Output fields
- Classification categories
- Language behavior
- Framing categories
- Output constraints

The model returns structured JSON that can be processed programmatically.

### Structured Outputs

Instead of relying on free-form responses, the analysis pipeline requests a JSON object with predefined fields.

A simplified output structure is:

```json
{
  "summary": "...",
  "key_points": ["...", "..."],
  "topic": "...",
  "sentiment": "Neutral",
  "target_audience": "...",
  "audience_needs": ["...", "..."],
  "primary_keywords": ["...", "..."],
  "secondary_keywords": ["...", "..."],
  "search_intent": "Informational",
  "primary_frame": "...",
  "generic_frames": ["..."],
  "issue_specific_frames": ["..."]
}
```

This makes model-generated information easier to:

- Process
- Compare
- Aggregate
- Visualize
- Reuse in downstream applications

---

### Semantic Embeddings

Topic strings are transformed into dense vector representations using a Sentence Transformer model.

Semantic similarity is then calculated using cosine similarity.

Conceptually:

```text
Topic A → Embedding A
Topic B → Embedding B

             ↓

       Cosine Similarity

             ↓

   Semantic Relatedness
```

This allows the system to identify conceptually similar topics even when they use different wording.

---

## 🧪 Example Use Case

The platform can be used to explore how a social issue is discussed across different types of online content.

For example, a researcher could provide several pieces of content discussing marriage and demographic change:

```text
News Article
       │
       ├── Economic pressure
       │
       └── Demographic change

Social Media Post
       │
       └── Individual choice

Forum Discussion
       │
       ├── Housing costs
       └── Marriage expectations

Comment
       │
       └── Changing attitudes
```

The system can then compare:

- Topics
- Sentiment
- Search intent
- Frames
- Keywords
- Semantic topic relationships

The marriage topic is used as a **case study**, while the underlying platform is designed to support broader content-analysis tasks.

---

## 💻 Technology Stack

### Programming

- Python

### AI / NLP

- LLM API
- Prompt Engineering
- Structured JSON Outputs
- Sentence Transformers
- Semantic Embeddings
- Cosine Similarity

### Data Analysis

- Pandas
- Scikit-learn

### Web Application

- Streamlit

### Development

- Git
- GitHub
- PyCharm

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
└── src/
    ├── __init__.py
    ├── data.py
    ├── llm.py
    ├── prompts.py
    └── semantic.py
```

### Module Responsibilities

`app.py`

Main Streamlit application and user interface.

`src/llm.py`

Handles communication with the LLM API and structured JSON responses.

`src/prompts.py`

Contains the analysis prompt and classification rules.

`src/semantic.py`

Handles semantic embeddings, similarity calculation, and topic grouping.

`src/data.py`

Contains data-processing functionality used by the application.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YingyunWu/ai-content-intelligence.git
cd ai-content-intelligence
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on macOS / Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
DEEPSEEK_API_KEY=your_api_key_here
```

The API key should never be committed to GitHub.

---

## ▶️ Usage

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in a browser.

Users can then select between:

```text
Single Content
```

or

```text
Multi-Content Comparison
```

and provide the corresponding content for analysis.

---

## 🗺️ Roadmap

The current version focuses on the core content intelligence and semantic analysis pipeline.

Potential future development includes:

- [ ] Human-annotated evaluation dataset
- [ ] Quantitative evaluation of classification performance
- [ ] Precision / Recall / F1 evaluation
- [ ] Improved semantic clustering algorithms
- [ ] Topic evolution across time
- [ ] Cross-platform comparison
- [ ] Source-level analysis
- [ ] Improved visualization
- [ ] Batch data ingestion
- [ ] Automated data collection from public sources

The roadmap is intentionally separate from the current implementation so that future capabilities can be evaluated independently.

---

## 🎯 Project Goals

The project has two complementary goals.

### Engineering

To develop practical experience with:

```text
Python
  ↓
APIs
  ↓
Structured Data
  ↓
LLM Applications
  ↓
NLP
  ↓
Semantic Embeddings
  ↓
Data Analysis
  ↓
Interactive Visualization
```

### Computational Analysis

To explore how AI and computational methods can support the analysis of large-scale online content.

The project focuses on transforming qualitative textual information into structured representations that can be compared, grouped, and visualized.

---

## 🌱 Motivation

The project grew from an interdisciplinary background spanning **Journalism & Communication, engineering, and public-sector governance**.

This combination motivates an interest in applying computational methods to real-world information and social problems.

The project therefore sits at the intersection of:

```text
Artificial Intelligence
        +
Natural Language Processing
        +
Data Analysis
        +
Computational Media
        +
Interdisciplinary Research
```

Rather than building a domain-specific classifier for a single topic, the goal is to develop a reusable **content intelligence framework** that can be applied to different subjects and content environments.

---

## 📌 Current Status

**Version: v0.2**

The current version supports:

- Single-content analysis
- Multiple content types
- 2–10 content comparison
- Structured LLM analysis
- Multilingual output matching
- Sentiment analysis
- Search intent classification
- Content framing
- Semantic topic grouping
- Cross-content visualization

The project is actively being developed.

---

## 📄 License

This project is licensed under the MIT License.