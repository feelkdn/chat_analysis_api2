from flask import Blueprint, request, jsonify, make_response
from app.services.nlp04 import KakaoAnalyzer
from app.services.word_frequency_analyzer import WordFrequencyAnalyzer
import os
import tempfile

analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/analyze-file', methods=['POST', 'OPTIONS'])
def analyze_file():
    # 👉 OPTIONS 요청 처리 (CORS preflight)
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
        return response, 204

    file = request.files.get('chat_file')
    if not file:
        return jsonify({'error': '파일이 없습니다.'}), 400

    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
        file.save(tmp.name)
        temp_path = tmp.name

    try:
        analyzer = KakaoAnalyzer()
        word_analyzer = WordFrequencyAnalyzer()

        results = analyzer.analyze_kakao_csv(temp_path)
        word_freq = word_analyzer.analyze_file(temp_path)

        top_words = word_freq[:10]
        user_words = [{"word": w["word"], "count": w["count"]} for w in top_words[:5]]
        partner_words = [{"word": w["word"], "count": w["count"]} for w in top_words[5:]]

        return jsonify({
            "wordFrequency": {
                "user": user_words,
                "partner": partner_words
            },
            "topics": [
                {"name": "일상", "percentage": 0.4, "color": "#3B82F6"},
                {"name": "감정", "percentage": 0.3, "color": "#EF4444"},
                {"name": "취미", "percentage": 0.3, "color": "#6366F1"}
            ],
            "topicTimeline": {
                "timestamps": ["월", "화", "수", "목", "금", "토", "일"],
                "topics": {
                    "일상": [10, 20, 15, 30, 25, 10, 5],
                    "감정": [5, 10, 20, 15, 10, 30, 40],
                    "취미": [10, 5, 10, 15, 20, 25, 30]
                }
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        os.remove(temp_path)
