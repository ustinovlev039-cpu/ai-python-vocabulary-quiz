import openai  


openai.api_key = "your-openai-api-key-here"  


def generate_words_via_ai(level, num_words=5):
    """
    Генерирует слова через ChatGPT API для выбранного уровня.
    Пример: Для 'easy' генерирует простые слова с переводами.
    """
    prompt = f"Generate {num_words} English words for {level} vocabulary level, with Russian translations. Format as dict: {{'word': 'translation', ...}}. Examples: easy - family:семья; medium - believe:верить; hard - rural:деревенский."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[{"role": "user", "content": prompt}]
    )
    
    
    try:
        generated = eval(response.choices[0].message.content.strip())
        return generated
    except:
        print("Ошибка генерации слов через AI. Используем статические.")
        return {}


words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}


def choose_difficulty():
    print("Выберите уровень сложности.")
    print("Легкий, средний, сложный.")
    choice = input().strip().lower()
    
    if "легк" in choice:
        words = words_easy
        level_str = "easy"
    elif "средн" in choice:
        words = words_medium
        level_str = "medium"
    elif "сложн" in choice:
        words = words_hard
        level_str = "hard"
    else:
        print("Некорректный уровень. Используем средний.")
        words = words_medium
        level_str = "medium"
    
    
    try:
        ai_words = generate_words_via_ai(level_str, num_words=2)  
        words.update(ai_words)
        print("Добавлены слова, сгенерированные через ChatGPT для разнообразия!")
    except:
        pass  
    
    return words




def main():
    words = choose_difficulty()
    answers = play_game(words)
    display_results(answers)
    calculate_rank(answers)

if __name__ == "__main__":
    main()