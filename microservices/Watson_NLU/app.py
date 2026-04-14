from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def simple_sentiment(text):
    """Simple rule-based sentiment analysis as fallback."""
    text_lower = text.lower()
    positive_words = ['great', 'excellent', 'fantastic', 'amazing', 'good', 'love',
                      'wonderful', 'best', 'happy', 'satisfied', 'perfect', 'awesome']
    negative_words = ['bad', 'terrible', 'awful', 'horrible', 'worst', 'hate',
                      'disappointed', 'poor', 'never', 'problem', 'issue', 'wrong']

    pos_count = sum(1 for word in positive_words if word in text_lower)
    neg_count = sum(1 for word in negative_words if word in text_lower)

    if pos_count > neg_count:
        return "positive"
    elif neg_count > pos_count:
        return "negative"
    return "neutral"


# Task 16 — Analyze review sentiment
@app.route('/analyze/<text>', methods=['GET'])
def analyze_review(text):
    try:
        sentiment = simple_sentiment(text)
        return jsonify({
            "sentiment": sentiment,
            "text": text
        })
    except Exception as e:
        return jsonify({"error": str(e), "sentiment": "neutral"}), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "Sentiment microservice is running"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
