## 📌 Ülevaade  
**KKK Generaator** on veebirakendus, mis võimaldab ettevõtetel, e-poodidel või teenusepakkujatel luua korduma kippuvaid küsimusi (FAQ) automaatselt, kasutades **ChatGPT (OpenAI GPT-3.5-turbo)**. Administraator saab genereeritud küsimusi eelvaadata, vajadusel redigeerida, kinnitada ja kuvada need avalikus vaates.

---

## 🛠️ Kasutatud tehnoloogiad

| Tehnoloogia       | Kirjeldus |
|-------------------|-----------|
| Python 3.10       | Põhikeel |
| Django 5.1.7      | Veebiraamistik |
| Django-admin      | Adminliides KKK halduseks |
| Bootstrap 4       | Kujundus ja mobiilisõbralik UI |
| OpenAI API        | FAQ-de genereerimine AI abil |
| Python-dotenv     | API võtmete turvaline haldus |
| Pillow            | Piltide üleslaadimine FAQ juurde |

---

## ⚙️ Funktsionaalsused

### 🌐 Avalik kasutajavaade
- Kasutaja saab genereerida KKK-sid sisestades toote või teenuse kirjelduse
- Kuvatakse ainult kinnitatud (approved) KKK-d
- Iga küsimuse juurde saab kuvada pildi

### 👤 Kasutajate haldus
- **Konto loomine** (`signup.html`)
- **Sisselogimine / väljalogimine** (`login.html`, `logout`)
- Automaatselt suunamine peale registreerimist

### 🧠 FAQ genereerimine (AI)
- ChatGPT (gpt-3.5-turbo) analüüsib sisestatud kirjeldust ja loob 5 küsimuse-vastuse paari
- Generatsioon toimub turvaliselt `.env` failist saadud võtmega

### 📋 FAQ eelvaade ja kinnitamine
- Admin saab vaadata kinnitamata küsimusi
- **Mitmik-kinnitamine** checkboxide kaudu
- **„Vali kõik“** funktsioon ühe klikiga
- FAQ saab kustutada või redigeerida

---

## 📂 Olulised failid ja mallid

| Fail            | Roll |
|------------------|------|
| `base.html`      | Ühine kujundus kõigile lehtedele |
| `home.html`      | Kuvab kinnitatud KKK-d |
| `generate_faq.html` | FAQ genereerimisvorm |
| `admin_review_faqs.html` | Kinnitamata KKK eelvaade ja mitmik-kinnitamine |
| `signup.html`    | Konto loomise vorm |
| `login.html`     | Sisselogimisvorm |

---

## 🧾 Tüüpiline töövoog

1. Kasutaja logib sisse või loob konto
2. Sisestab toote/teenuse kirjelduse
3. ChatGPT tagastab 5 KKK-d (ei ole kohe nähtavad avalikus vaates)
4. Administraator logib sisse, avab kinnitamata KKK-d
5. Märgib soovitud KKK-d ja kinnitab need
6. Kinnitatud küsimused ilmuvad avalikku `home.html` vaatesse

---

## 🔐 Turvalisus ja korraldus

- API võtmed hoitakse `.env` failis
- Ainult superkasutaja pääseb kinnitamata KKK eelvaatesse
- CSRF-kaitse kõikidel vormidel
- Django `messages` kasutatakse tagasisideks

---

## 🔧 Arendatavus

Potentsiaal tuleviku jaoks:

- ✅ PDF/CSV eksport kinnitatud KKK-dest
- 📸 Piltide lisamine kinnitamisel
- 📧 Meiliteavitused kinnitamisel
- 🌍 Mitmekeelsus (i18n)

---

Kui soovid, võin selle resümee eksportida ka **PDF-failina** või aidata kirjutada **README.md** GitHubi jaoks. Soovid?
