import sys

file_path = r'd:\1. AI\Antigravity\alliance-peinture-76\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Make all bg-white visible beiges
html = html.replace('bg-white', 'bg-[#F4EBE0]')
html = html.replace('bg-slate-50', 'bg-[#Ece2D5]')
html = html.replace('bg-slate-100', 'bg-[#E3D8Cb]')
html = html.replace('bg-slate-200', 'bg-[#D9CDBF]')

# Tailwind config: modify to a beautiful terracotta instead of blue
html = html.replace("primary: '#1D4ED8'", "primary: '#A04D36'") # Terracotta
html = html.replace("primaryLight: '#3B82F6'", "primaryLight: '#B8654B'") # Lighter Terracotta
html = html.replace("accent: '#EAB308'", "accent: '#3C5A4C'") # Forest Sage
html = html.replace("textDark: '#0F172A'", "textDark: '#2B2421'") # Very dark brown/slate instead of dark blue

# Change the base variables as well
html = html.replace("bgLight: '#FDFBF7'", "bgLight: '#F4EBE0'") 
html = html.replace("bgWarm: '#F5F3ED'", "bgWarm: '#EBE2D5'")
html = html.replace("bgMuted: '#EFECE5'", "bgMuted: '#E3D8CB'")
html = html.replace("surface: '#ffffff'", "surface: '#F4EBE0'")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("done")
