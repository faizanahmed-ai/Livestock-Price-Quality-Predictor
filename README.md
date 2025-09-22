# Livestock Price & Quality Predictor 🐑

A simple Python program to estimate the **price** and **quality** of livestock (cow, goat, sheep, buffalo, camel, etc.) based on age and weight.  
The rules are easy to follow, so even beginners can understand the code.

---

## Features
- Supports multiple animal types  
- Adjusts price by age:
  - Under 1 year → 10% less  
  - 1–2 years → normal price  
  - Over 2 years → 20% more  
- Rates quality by weight:
  - < 50 kg → Fair  
  - 50–70 kg → Good  
  - > 70 kg → Excellent  
- Can add multiple animals in one run  
- Shows total price at the end  

---

## How to Run
1. Install Python (3.x recommended)  
2. Clone or download this project  
3. Run the program:  
   ```bash
   python livestock.py
   
