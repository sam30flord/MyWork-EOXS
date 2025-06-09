# MyWork-EOXS

# AI-Powered Blog Generator for Building Materials Content

This project was built to solve a real and repetitive problem: writing hundreds (even thousands) of product- and industry-specific blog posts by hand.

Our team needed to generate detailed blog content for a building materials company — covering topics like cement types, roofing options, pricing tools, supply chain tech, and more. Manually writing all of them wasn’t just time-consuming — it was draining. So, we built a tool to do the heavy lifting.

---

##  What It Does

This Python script takes an Excel sheet of blog topics and automatically generates content for each one using Together.ai’s API. It:

- Reads blog topics from `blog_topics.xlsx`
- Sends each topic to the Mixtral-8x7B language model via API
- Receives engaging, brand-aligned content
- Saves everything back to `blog_with_content.xlsx`

Simple, fast, and scalable.

---

##  How We Did It

1. Built a lightweight Python script using `pandas` and `requests`
2. Signed up for [Together.ai](https://www.together.ai/) and grabbed a free API key
3. Used the `mistralai/Mixtral-8x7B-Instruct-v0.1` model for blog generation
4. Prompted the model to follow a friendly, professional writing tone
5. Let the script automate hundreds of content pieces in minutes

No servers. No frontend. Just one file and a huge time-saver.

---

## How to Use

1. Clone the repo or download the files
2. Add your blog topics to a file named: `blog_topics.xlsx`
   - Column A: Blog titles
3. Open `blog_generator.py` and paste your Together.ai API key:
   ```python
   api_key = "your_api_key_here"

---

### RUN THE SCRIPT:

python blog_generator.py

## Output will be saved to: 

blog_with_content.xlsx

---

## Why It Matters
This tool saved our content team hundreds of hours.
Writers can now focus on reviewing and polishing instead of starting from scratch.
It brought consistency, speed, and a massive productivity boost to our content process.

---

# Dependencies
Python 3.x
pandas
openpyxl
requests

---

# Install dependencies (if needed):
pip install pandas openpyxl requests

---

# Model Used
mistralai/Mixtral-8x7B-Instruct-v0.1

---

Served through Together.ai’s chat completion API


