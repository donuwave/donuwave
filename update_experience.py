from datetime import datetime

start_date = datetime(2023, 8, 28)
today = datetime.now()

delta_days = (today - start_date).days

years = delta_days // 365
months = (delta_days % 365) // 30

if years == 0 and months == 0:
    experience_text = "Less than a month"
elif years == 0:
    experience_text = f"{months} months"
elif months == 0:
    experience_text = f"{years} years"
else:
    experience_text = f"{years} years {months} months"

try:
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()  # Читаем файл построчно

    updated_lines = []
    for line in lines:
        if line.strip().startswith("- 🗓 **Work experience:**"):
            line = f"- 🗓 **Work experience:** {experience_text}\n"
        updated_lines.append(line)

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(updated_lines)

except FileNotFoundError:
    print("README.md not found!")
except Exception as e:
    print(f"An error occurred: {e}")
