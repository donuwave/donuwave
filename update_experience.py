from datetime import datetime

start_date = datetime(2023, 8, 28)
today = datetime.now()

delta = today - start_date
years = delta.days // 365
months = (delta.days % 365) // 30

experience_text = f"💼 Опыт работы: {years} лет {months} месяцев"

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_content = content.replace(
    "{{experience}}", experience_text
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)
