# 🧠 Business News Monitoring Agent

## 📋 Overview

This project presents an AI agent capable of analyzing business news and identifying its impact on clients.  
It leverages large language models and tool-based reasoning to automate what is typically a manual, time-consuming task for business analysts.

The system is built as a functional prototype demonstrating agentic behavior, tool usage, and structured business reasoning.

---

## 🎯 Objective

The goal is to create an intelligent assistant that helps institutions monitor news that could affect their clients.

By reading any business article, the agent:
- Detects companies mentioned  
- Checks if they are clients of the institution 
- Finds links between mentioned companies and existing clients  
- Summarizes the potential business impact for each affected client  

---

## 🧩 Use Case

### The Problem
Business analysts and relationship managers receive hundreds of news items daily.  
Manually filtering relevant articles and determining which clients could be impacted is inefficient and prone to error.

### The Solution
An autonomous AI agent that reads a piece of news, reasons about which companies are affected, and uses internal tools to identify existing clients or their related partners.  
It outputs a concise, structured summary of business impacts in JSON format.

### The Business Value
- **Saves time:** Automates repetitive information extraction and client mapping  
- **Improves accuracy:** Ensures no major client-related event is overlooked  
- **Supports reactivity:** Enables faster outreach and decision-making for relationship managers  

---

## 🧠 Agent Design

### Architecture Principles
- **LLM Reasoning** – The agent uses a large language model to interpret the news and plan actions  
- **Tool Usage** – It can call predefined tools to check client status or relationships  
- **Structured Output** – Results are formatted as JSON objects, ready for integration with dashboards or alerts  

### Tools
- **Check Client Status** – Determines if a company is one of the bank’s clients  
- **Check Client Relation** – Identifies whether a company has commercial or strategic ties to a client  

---

## 📰 Example Scenario

### News Example
> Renault announced a major expansion of its partnership with Google Cloud to accelerate the integration of artificial intelligence across its manufacturing and supply chain operations.  
> By leveraging Google’s advanced data analytics and machine learning platforms, Renault aims to significantly improve efficiency and reduce costs.  
> Analysts view this collaboration as a major milestone in Renault’s digital transformation, potentially giving the company a competitive edge in the European market.  
> Meanwhile, Stellantis could struggle to keep up as its digital capabilities remain several years behind Renault’s new AI-driven model.

### Expected Agent Behavior
- Identify companies: **Renault**, **Google Cloud**, **Stellantis**  
- Recognize **Google Cloud** as a client  
- Detect that **Stellantis** is the owner of the client **Peugeot** 
- Summarize the event as an **opportunity for Renault** and a **threat for Peugeot**

---

## ⚙️ Technical Overview

| Component | Description |
|------------|-------------|
| **Model** | `gpt-4o-mini` (OpenAI) – performs reasoning and text understanding |
| **Framework** | SmolAgents – handles tool definition and orchestration |
| **Environment** | Python + dotenv for key management |

---

## 📈 Results & Benefits
- **Automation:** Transforms manual reading into an automated pipeline  
- **Scalability:** Can handle continuous streams of news in real time  
- **Business Insight:** Delivers structured impact analysis to decision-makers  
- **Integrability:** Output format can be easily ingested by dashboards or alert systems  
