import os
import openai
from dotenv import load_dotenv

# Lae .env failist OpenAI API võti
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_faqs(description):
    """
    Genereerib korduma kippuvad küsimused ja vastused sisestatud kirjelduse põhjal.
    Tagastab listi (question, answer) paaridest.
    """
    if not openai.api_key:
        print("❌ OpenAI API võti puudub!")
        return []

    prompt = f"""
Loo 5 korduma kippuvat küsimust ja vastust järgmise toote või teenuse põhjal:

"{description}"

Kasuta täpselt järgmist formaati iga elemendi jaoks:
Küsimus: ...
Vastus: ...
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sa oled abivalmis assistent, kes koostab professionaalseid KKK küsimusi ja vastuseid."},
                {"role": "user", "content": prompt.strip()}
            ],
            temperature=0.7,
            max_tokens=700
        )

        raw_text = response.choices[0].message['content'].strip()
        return parse_faq_text(raw_text)

    except openai.error.OpenAIError as e:
        print(f"⚠️ OpenAI viga: {str(e)}")
        return []

def parse_faq_text(raw_text):
    """
    Parsib OpenAI poolt tagastatud toorandmed.
    Otsib 'Küsimus:' ja 'Vastus:' mustreid ning loob tuple-listi.
    """
    faqs = []
    blocks = raw_text.split("\n\n")

    for block in blocks:
        if "Küsimus:" in block and "Vastus:" in block:
            try:
                question = block.split("Küsimus:")[1].split("Vastus:")[0].strip()
                answer = block.split("Vastus:")[1].strip()
                if question and answer:
                    faqs.append((question, answer))
            except (IndexError, ValueError):
                continue

    return faqs
