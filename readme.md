# Proof of Work – Generative AI with Gemini API (OpenAI-Compatible)

This project demonstrates a working setup of **Google Gemini models** using the **Gemini API** with **OpenAI-compatible endpoints**.
It includes two example AI applications and a simple server backend.

---

## Project Structure

```
chatbot/
├── model_1.py       # Nutritionist AI with chat history
└── model_2.py       # E-commerce chatbot with tool functionality

server/
├── .env.example     # Environment variables for server
├── dataset.json     # Demo dataset
├── package.json
├── package-lock.json
└── server.js        # Express backend

.env.example         # Environment variables for Python scripts
basic.py             # Minimal Gemini API usage example in Python

```

---

## Gemini Models Used

| Model Name                 | Alias                             | Description                                                                                    | Pricing (per 1M tokens)                                                             |
| -------------------------- | --------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Gemini 2.5 Pro**         | `gemini-2.5-pro`                  | Advanced reasoning model with a **2M token** context window. Best for complex problem solving. | Input: \$1.25 (≤200k), \$2.50 (>200k) <br> Output: \$10.00 (≤200k), \$15.00 (>200k) |
| **Gemini 2.5 Flash**       | `gemini-2.5-flash`                | Best price-performance balance, well-rounded and adaptive. Great for most applications.        | Input: \$0.30 <br> Output: \$2.50                                                   |
| **Gemini 2.5 Flash-Lite**  | `gemini-2.5-flash-lite`           | Fastest & most cost-efficient in 2.5 series, ideal for high-throughput, low-latency tasks.     | Input: \$0.10 <br> Output: \$0.40                                                   |
| **Gemini 2.0 Flash**       | `gemini-2.0-flash-001`            | Next-gen multimodal model with tool use, fast & general-purpose.                               | Input: \$0.10 <br> Output: \$0.40                                                   |
| **Gemini 2.0 Flash-Lite**  | `gemini-2.0-flash-lite-001`       | Ultra-fast and budget-friendly, ideal for quick responses.                                     | Input: \$0.075 <br> Output: \$0.30                                                  |
| **Gemini Embedding**       | `gemini-embedding-001`            | Converts text into embeddings for semantic search, clustering, etc.                            | Input: \$0.15                                                                       |
| **Text Embedding**         | `text-embedding-005`              | Cost-effective text embedding model.                                                           | Input: \$0.10                                                                       |
| **Multilingual Embedding** | `text-multilingual-embedding-002` | Embedding model with multi-language support for global apps.                                   | N/A                                                                                 |

---

## Features

* **Nutritionist AI** – remembers chat history for ongoing conversation.
* **E-commerce Chatbot** – includes tool functionality for dynamic responses.
* **Express Server Backend** – serves data from `dataset.json`.
* **Python Example** – minimal Gemini API usage for quick testing.
* **OpenAI-Compatible Calls** – easy migration from OpenAI API.

---

## Notes

* Pricing is based on **per 1M tokens** and varies for input vs. output.
* `.env.example` files contain placeholders for environment variables—copy and rename to `.env` for actual usage.
* This is a **proof of work** project, intended as a starting point for real-world applications.
