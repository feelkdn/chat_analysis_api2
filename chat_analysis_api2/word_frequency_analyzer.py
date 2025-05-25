import re
from collections import Counter

class WordFrequencyAnalyzer:
    def __init__(self):
        pass

    def analyze_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        # 한글과 띄어쓰기만 남기고 제거
        cleaned = re.sub(r"[^\uAC00-\uD7A3a-zA-Z0-9\s]", "", text)
        words = cleaned.split()
        counter = Counter(words)

        return [{"word": word, "count": count} for word, count in counter.most_common(50)]
