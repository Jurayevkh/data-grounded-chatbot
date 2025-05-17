import json

with open("structured_hogwarts_chatbot_data.json", "r", encoding="utf-8") as f:
    data_chunks = json.load(f)

KEYWORD_GROUPS = {
    "free": ["free", "cost", "price", "funding", "payment", "charge", "self-funding", "sponsors"],
    "capacity": ["capacity", "slots", "availability", "seats", "places", "max capacity", "participants"],
    "application": ["apply", "application", "how to join", "enroll", "essay", "cv", "interview", "admission", "selection", "process"],
    "contact": ["contact", "phone", "email", "social media", "telegram", "website"],
    "program": ["program", "schedule", "timeline", "milestones", "camp", "sessions", "activities"],
    "support": ["support", "university", "sponsors", "help", "transportation", "dormitories"],
}

def find_best_answers(user_input, top_n=3):
    user_input_lower = user_input.lower()

    matched_groups = []
    for group, keywords in KEYWORD_GROUPS.items():
        if any(kw in user_input_lower for kw in keywords):
            matched_groups.append(group)

    if not matched_groups:
        return None

    scored_chunks = []

    for item in data_chunks:
        combined_text = " ".join([
            item.get("title", "").lower(),
            " ".join(item.get("tags", [])).lower(),
            item.get("content", "").lower(),
        ])

        matched_keywords = set()
        for group in matched_groups:
            for kw in KEYWORD_GROUPS[group]:
                if kw in combined_text:
                    matched_keywords.add(kw)

        score = len(matched_keywords)

        if score > 0:
            scored_chunks.append((score, item["content"], item.get("title", "No Title")))

    if not scored_chunks:
        return None

    scored_chunks.sort(key=lambda x: x[0], reverse=True)

    return [(title, content) for _, content, title in scored_chunks[:top_n]]

if __name__ == "__main__":
    print("Hogwarts Summer School Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        answers = find_best_answers(user_input)
        if answers:
            for title, content in answers:
                print(f"**{title}**\n{content}\n{'-'*40}")
        else:
            print("Sorry, I couldn't find an answer to that question.")
