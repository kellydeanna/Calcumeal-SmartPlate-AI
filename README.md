# Calcumeal-SmartPlate-AI

## 🧠 Project Title
**Calcumeal SmartPlate AI: An Intelligent System for Ingredient Recognition and Personalized Healthy Meal Planning**

---

## 📌 Project Description

**Calcumeal SmartPlate AI** is a health-focused AI application that helps users identify ingredients from images and generate personalized, calorie-estimated recipes or weekly meal plans. The system features two core functionalities:

1. **Ingredient Detection:** Upload an image of raw ingredients. A CNN model classifies the items and suggests two healthy recipes for each, with instructions and calorie estimates.
2. **Weekly Meal Planner:** GPT-powered generator that produces a 7-day meal plan (breakfast, lunch, dinner) with nutritional guidance and cooking steps.

Built for people who want to eat healthier, save time, and learn about nutrition effortlessly.

---

## 🚀 Getting Started

### Live Portotypes
Try it on Hugging Face:  
👉 [https://huggingface.co/spaces/Kellydeanna/healthymeal](https://huggingface.co/spaces/Kellydeanna/healthymeal)

### Prerequisites
- Python 3.8+
- TensorFlow / Keras
- OpenAI API Key
- Google Colab (for model training)

### Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/kellydeanna/calcumeal-smartplate-ai.git
cd calcumeal-smartplate-ai
pip install -r requirements.txt
```

Connect to your dataset on Google Drive or Hugging Face and set up your API key for OpenAI.

---

## 📁 File Structure

```
calcumeal-smartplate-ai/
├── model/
│   └── ingredient_classifier.h5
├── data/
│   └── ingredients_dataset/
├── app/
│   ├── app.py
│   ├── gpt_mealplanner.py
│   └── image_upload_handler.py
├── notebooks/
│   └── cnn_training.ipynb
├── media/
│   ├── screenshots/
│   └── demo_video.mov
└── README.md
```

---

## 📊 Analysis & Methods

### 🔍 Ingredient Detection
- Custom CNN model trained on 66 manually labeled ingredient classes.
- Dataset: ~50 images/class, collected by team members.
- Image preprocessing: resize, normalize, augment.

### 🍽️ GPT Meal Planning
- OpenAI's GPT-3.5 model used to generate structured weekly meal plans.
- Each plan includes:
  - Recipe Name
  - How to Cook
  - Estimated Calories

Prompts designed to simulate a health consultant's guidance.

---

## ✅ Results

- High accuracy in ingredient classification using CNN.
- Realistic and diverse meal plan generation using GPT.
- Fully functional app hosted on Hugging Face.
- User feedback confirms potential for personal health use.

---

## 👥 Contributors

| Name                   | Role                                                                                       |
|------------------------|--------------------------------------------------------------------------------------------|
| Kelly Deanna Djaja     | proposal, dataset collection, programming, application design, poster design, presentation |
| Luana Vallejos Morinigo| presentation, dataset collection                                                           |
| Giovanie Tandiono      | dataset collection                                                                         |
| Lac Thi Giang          | presentation, dataset collection                                                           | 
| Mira黃宥宓              | presentation, dataset collection                                                           |

---

## 🙏 Acknowledgments

- Professor Pien Chung-pei
- OpenAI for GPT API
- Hugging Face for app hosting
- Google Colab for training environment

---

## 📚 References

- [OpenAI API](https://platform.openai.com)
- [TensorFlow](https://www.tensorflow.org/)
- [Hugging Face Spaces](https://huggingface.co/spaces)
- Custom dataset by project team
