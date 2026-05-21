# AI Powered Research Proposal Evaluation System

An AI-driven web application that automates the evaluation of scientific research proposals using **Python**, **Flask**, and **Google Gemini AI**. The system analyzes proposal content and generates intelligent summaries, strengths, weaknesses, scores, and recommendations using **Generative AI**, **NLP**, and **Prompt Engineering** techniques.

---

## Features

* Automated research proposal analysis
* AI-generated summaries and evaluations
* Strengths and weaknesses detection
* Intelligent scoring system
* Recommendation generation (Accept / Needs Review / Reject)
* Real-time JSON-based evaluation responses
* User-friendly web interface

---

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### AI & Libraries

* Google Gemini API (`google-genai`)
* dotenv
* json

---

## AI & ML Concepts Used

* Generative AI
* Natural Language Processing (NLP)
* Prompt Engineering
* Large Language Models (LLMs)
* Text Classification
* Intelligent Scoring
* Recommendation Systems
* Contextual Text Analysis

---

## Project Workflow

1. User submits:

   * Proposal Title
   * Research Domain
   * Proposal Content

2. Backend generates a structured AI prompt.

3. Gemini AI analyzes the proposal and generates:

   * Summary
   * Strengths
   * Weaknesses
   * Suggestions
   * Scores
   * Final Recommendation

4. The response is processed into JSON format.

5. Evaluation results are displayed on the frontend.

---

## Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create `.env` File

```env
GEMINI_API_KEY=your_api_key_here
```

### Run the Application

```bash
python app.py
```

The application will run at:

```bash
http://127.0.0.1:5000
```

---

## API Endpoint

### POST `/analyze`

Accepts proposal details and returns AI-generated evaluation results in JSON format.

### Input Fields

```json
{
  "title": "Research Proposal Title",
  "domain": "Research Domain",
  "content": "Detailed research proposal content"
}
```

---

## Example Output

```json
{
  "summary": "AI-generated proposal summary",
  "strengths": ["strength 1", "strength 2"],
  "weaknesses": ["weakness 1", "weakness 2"],
  "suggestions": ["suggestion 1", "suggestion 2"],
  "scores": {
    "innovation": 8,
    "technical_feasibility": 7,
    "research_relevance": 9
  },
  "overall_score": 8.0,
  "recommendation": "Accept"
}
```

---

## Advantages

* Reduces manual evaluation effort
* Saves time for research institutions
* Provides structured and consistent evaluations
* Scalable for large numbers of proposals

---

## Future Enhancements

* PDF proposal upload
* Proposal plagiarism detection
* Multi-language support
* Proposal ranking system
* AI-based funding prediction
* Research trend analysis

---

## Conclusion

This project demonstrates the practical application of **Generative AI**, **NLP**, and **Machine Learning concepts** in automating academic research proposal evaluation. The system helps improve evaluation efficiency, consistency, and decision-making support for research organizations.
