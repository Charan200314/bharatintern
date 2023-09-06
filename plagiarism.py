from difflib import SequenceMatcher

def calculate_similarity(text1, text2):
    matcher = SequenceMatcher(None, text1, text2)
    similarity_ratio = matcher.ratio() * 100
    return similarity_ratio

def check_plagiarism(text1, text2, threshold=70):
    similarity = calculate_similarity(text1, text2)
    if similarity >= threshold:
        return True, similarity
    else:
        return False, similarity

if __name__ == "_main_":
    original_text = "This is a sample text for testing."
    suspicious_text = "This is a text meant for testing purposes."

    is_plagiarized, similarity_percentage = check_plagiarism(original_text, suspicious_text)

    if is_plagiarized:
        print("Plagiarism Detected!")
    else:
        print("No Plagiarism Detected.")

    print("Similarity:", similarity_percentage, "%")