import os, zipfile

# Buat folder kerja
folder = "Dulanova_Portfolio"
os.makedirs(folder, exist_ok=True)

# === README.md ===
readme = """<!-- 🌌 DULANOVA PORTFOLIO README 🌌 -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=180&color=gradient&customColorList=2,20,30&text=DULANOVA%20🌱%20Software%20Engineer&fontAlignY=35&fontSize=40&fontColor=ffffff" />
</p>

<h1 align="center">
  <img src="https://readme-typing-svg.herokuapp.com?size=28&duration=4000&color=00FFF0&center=true&vCenter=true&width=600&lines=👋+Hi,+I'm+Dulanova!;💻+A+Passionate+Software+Engineer;🌟+Building+Creative+and+Powerful+Solutions;🚀+Welcome+to+My+Digital+Space!" alt="Typing SVG">
</h1>

---

## 🧩 About Me

```yaml
name: Dulanova
role: Software Engineer
from: Indonesia 🇮🇩
speciality: Full Stack Development, Automation, and Creative Problem Solving
motto: "Code is an art — and every line tells a story."
````

> 🎯 *I turn ideas into efficient, scalable, and beautiful digital experiences.*

---

## ⚙️ Tech Arsenal

<p align="center">
  <img src="https://skillicons.dev/icons?i=html,css,js,ts,react,nodejs,python,java,mongodb,git,figma,docker" />
</p>

---

## 🧠 What I Love Building

* ⚡ **Dynamic web applications** with smooth UX
* 🧩 **APIs and backend systems** that just work
* 🎨 **Creative digital experiences** with motion and life
* 🤖 **Automation tools** that save time and energy

<p align="center">
  <img src="https://media.giphy.com/media/l0MYEqEzwMWFCg8rm/giphy.gif" width="350" alt="coding animation"/>
</p>

---

## 📊 GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Dulanova&show_icons=true&theme=tokyonight&bg_color=0d1117&title_color=00f0a0&icon_color=00f0ff" height="160px"/>
  <img src="https://github-readme-streak-stats.herokuapp.com?user=Dulanova&theme=tokyonight-duo&date_format=j%20M%5B%20Y%5D&background=0D1117" height="160px"/>
</p>

---

## 🐍 Contribution Animation

<p align="center">
  <img src="https://github.com/Platane/snk/raw/output/github-contribution-grid-snake.svg" alt="snake animation" />
</p>

---

## 🌍 Connect with Me

<p align="center">
  <a href="https://github.com/Dulanova"><img src="https://img.shields.io/badge/GitHub-00F0A0?style=for-the-badge&logo=github&logoColor=white" /></a>
  <a href="https://discord.com/users/acaks._27825"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" /></a>
  <a href="https://instagram.com/dulanran"><img src="https://img.shields.io/badge/Instagram-00B5FF?style=for-the-badge&logo=instagram&logoColor=white" /></a>
</p>

---

<h2 align="center">🌈 “Innovate, Create, Elevate.” 🌈</h2>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=25&duration=4000&color=00F0A0&center=true&vCenter=true&lines=✨+Crafting+Code+With+Purpose;🚀+Learning+Every+Single+Day;💡+Driven+By+Curiosity!" />
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=footer&customColorList=2,20,30" />
</p>
"""
open(os.path.join(folder, "README.md"), "w", encoding="utf-8").write(readme)

# === index.html (Mini Portfolio) ===

html = """<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dulanova | Software Engineer</title>
<style>
body {
  margin: 0;
  font-family: 'Orbitron', sans-serif;
  background: radial-gradient(circle at top, #001f2e, #000);
  color: #00f0a0;
  text-align: center;
}
h1 { color: #00fff2; margin-top: 2rem; }
a { color: #00ffb3; text-decoration: none; }
.container {
  padding: 40px;
}
.avatar {
  border-radius: 50%;
  border: 3px solid #00f0a0;
  width: 150px;
  margin-bottom: 20px;
}
.card {
  background: rgba(0,255,200,0.08);
  border: 1px solid #00f0a0;
  padding: 20px;
  margin: 20px auto;
  width: 60%;
  border-radius: 10px;
  box-shadow: 0 0 10px #00f0a0;
}
</style>
</head>
<body>
  <div class="container">
    <img src="https://github.com/Dulanova.png" class="avatar" alt="Dulanova">
    <h1>👨‍💻 Dulanova</h1>
    <h3>Software Engineer • Creator • Innovator</h3>
    <div class="card">
      <p>Turning ideas into reality through clean, efficient, and creative code.</p>
      <p>💡 Full Stack | 🚀 Automation | 🎨 Interactive Design</p>
    </div>
    <p>
      🌐 <a href="https://github.com/Dulanova">GitHub</a> |
      💬 <a href="https://discord.com/users/acaks._27825">Discord</a> |
      📸 <a href="https://instagram.com/dulanran">Instagram</a>
    </p>
  </div>
</body>
</html>
"""
open(os.path.join(folder, "index.html"), "w", encoding="utf-8").write(html)

# === Dummy GIF Preview (URL placeholder) ===

gif_content = b"GIF89a"  # Placeholder minimal header
with open(os.path.join(folder, "preview.gif"), "wb") as f:
    f.write(gif_content)

# === ZIP File ===

zip_filename = f"{folder}.zip"
with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for file in os.listdir(folder):
        zipf.write(os.path.join(folder, file), arcname=os.path.join(folder, file))

print(f"✅ ZIP file '{zip_filename}' berhasil dibuat!")
