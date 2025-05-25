import csv
import re
from collections import defaultdict

class KakaoAnalyzer:
    def __init__(self):
        pass

    def analyze_kakao_csv(self, file_path):
        messages = []

        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                if len(row) < 4:
                    continue
                date, speaker, time, message = row[:4]
                messages.append({
                    "date": date,
                    "speaker": speaker,
                    "time": time,
                    "message": message
                })

        return {"messages": messages}

    def extract_keywords(self, messages):
        keyword_count = defaultdict(int)
        for msg in messages:
            for word in msg["message"].split():
                keyword_count[word] += 1
        return sorted(keyword_count.items(), key=lambda x: x[1], reverse=True)
