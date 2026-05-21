import os
import json
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the client
client = genai.Client(api_key=GEMINI_API_KEY)


def build_prompt(title: str, domain: str, content: str) -> str:
    return f"""You are an expert scientific research evaluator at a prestigious R&D funding institution.

Carefully analyze the following research proposal and provide a structured evaluation.

---
PROPOSAL TITLE: {title}
RESEARCH DOMAIN: {domain}
PROPOSAL CONTENT:
{content}
---

Evaluate this proposal on the following criteria and respond ONLY with a valid JSON object (no markdown, no explanation outside the JSON):

{{
  "summary": "A concise 2-3 sentence summary of the proposal's core idea and objectives.",
  "strengths": ["strength 1", "strength 2", "strength 3"],
  "weaknesses": ["weakness 1", "weakness 2", "weakness 3"],
  "suggestions": ["suggestion 1", "suggestion 2", "suggestion 3"],
  "scores": {{
    "innovation": <integer 1-10>,
    "technical_feasibility": <integer 1-10>,
    "research_relevance": <integer 1-10>,
    "methodology": <integer 1-10>,
    "clarity": <integer 1-10>,
    "expected_impact": <integer 1-10>
  }},
  "overall_score": <float, average of all scores, one decimal place>,
  "recommendation": "<exactly one of: Accept, Needs Review, Reject>",
  "recommendation_rationale": "A 1-2 sentence explanation for the recommendation."
}}

Be rigorous, fair, and constructive. Base scores only on the provided text."""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data received."}), 400

        title = data.get("title", "").strip()
        domain = data.get("domain", "").strip()
        content = data.get("content", "").strip()

        if not title:
            return jsonify({"error": "Proposal title is required."}), 400
        if not domain:
            return jsonify({"error": "Research domain is required."}), 400
        if not content:
            return jsonify({"error": "Proposal content is required."}), 400
        if len(content) < 100:
            return jsonify({"error": "Proposal content is too short. Please provide at least 100 characters."}), 400
        if len(content) > 20000:
            return jsonify({"error": "Proposal content exceeds the 20,000 character limit."}), 400

        prompt = build_prompt(title, domain, content)
        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
)
        raw_text = response.text.strip()

        if raw_text.startswith("```"):
            raw_text = raw_text.split("```")[1]
            if raw_text.startswith("json"):
                raw_text = raw_text[4:]
        raw_text = raw_text.strip()

        result = json.loads(raw_text)

        valid_recs = {"Accept", "Needs Review", "Reject"}
        if result.get("recommendation") not in valid_recs:
            result["recommendation"] = "Needs Review"

        return jsonify({"success": True, "evaluation": result})

    except json.JSONDecodeError:
        return jsonify({"error": "The AI returned an unexpected format. Please try again."}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
