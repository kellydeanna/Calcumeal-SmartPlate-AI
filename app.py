import os
print(os.getcwd())

print("Files in current directory:", os.listdir())


import importlib
import gpt_integration


from gpt_integration import generate_recipe_from_ingredients, generate_weekly_plan

from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import tensorflow as tf

from model_predict import predict as predict_ingredients

import streamlit as st

st.set_page_config(page_title="🥗 Healthy Meal Planner", layout="centered")
st.title(" 📊🥗Calcumeal SmartPlate AI")

st.markdown("Healthy recipe and meal suggestions based on your ingredients using AI.")

st.write("Upload images of your ingredients or Get 1-Week Meal Plan:")

# Feature selection
option = st.radio("What would you like to do?", [
    "📷 Detect Ingredients from Image",
    "🗓️ Get 1-Week Healthy Meal Plan"
])

# ---- OPTION 1: Ingredient Detection ----
if option == "📷 Detect Ingredients from Image":
    st.markdown("### 📤 Upload Images or Use Camera")
    
    uploaded_files = st.file_uploader("Upload one or more images of your ingredients:", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

    all_detected = []

    images_to_process = []

    if uploaded_files: 
        for idx, file in enumerate(uploaded_files):
            img = Image.open(file).convert("RGB")
            images_to_process.append(img)
            st.image(img, caption=f"Uploaded Image {idx+1}", use_column_width=True)
        
    if images_to_process:
        if st.button("🧠 Detect Ingredients", key="detect_button"):
            all_detected = []
            with st.spinner("Analyzing all images..."):
                for img in images_to_process:
                    detected = predict_ingredients(img)
                    all_detected.extend(detected)

            unique_detected = sorted(set(all_detected))
            st.session_state.detected_ingredients = unique_detected
            st.success(f"Detected ingredients: {', '.join(unique_detected)}")
    
# Display the last detected ingredients (if any)
if st.session_state.get("detected_ingredients"):
    default_input = ", ".join(st.session_state.detected_ingredients)
    custom_input = st.text_input("Confirm or edit ingredients (comma-separated):", default_input)

if st.button("🍳 Generate Recipe Recommendations"):
    with st.spinner("Generating recipe..."):
        recipes = generate_recipe_from_ingredients([i.strip() for i in custom_input.split(",")])

    for ingredient, recipe_text in recipes:
        st.markdown(f"## 🍽️ Recipes for **{ingredient.capitalize()}**")

        # Extract user ingredients again for checking
        user_ingredients = set(i.strip().lower() for i in custom_input.split(","))
        used_ingredients = set()

        for line in recipe_text.splitlines():
            if "-" in line and any(char.isalpha() for char in line):
                line_lower = line.lower()
                for item in user_ingredients:
                    if item in line_lower:
                        used_ingredients.add(item)

        missing_ingredients = user_ingredients - used_ingredients

        st.text(recipe_text)

        if missing_ingredients:
            st.warning(f"This recipe may also require other ingredients not detected: {', '.join(missing_ingredients)}")

# ---- OPTION 2: Weekly Meal Plan ----
if option == "🗓️ Get 1-Week Healthy Meal Plan":
    if st.button("📅 Generate Weekly Plan"):
        with st.spinner("Planning meals..."):
            st.session_state.weekly_plan = generate_weekly_plan()

    # Show and download the weekly plan if it exists
    if "weekly_plan" in st.session_state:
        weekly_plan = st.session_state.weekly_plan

        for day, meals in weekly_plan.items():
            st.markdown(f"### 📆 {day}")
            for meal_type, meal in meals.items():
                st.write(f"🍽️ **{meal['title']} ({meal_type})**")
                st.write("**Ingredients:**")
                st.markdown("\n".join(meal['ingredients']))
                st.write("**Instructions:**")
                st.markdown(meal['instructions'])
                st.write(f"**Calories:** {meal['calories']} kcal")
                st.markdown("---")

        # Format text for download
        def format_weekly_plan_text(plan):
            import io
            output = io.StringIO()
            for day, meals in plan.items():
                output.write(f"{day}\n")
                for meal_type, meal in meals.items():
                    output.write(f"\n{meal_type} - {meal['title']}\n")
                    output.write("Ingredients:\n")
                    for ing in meal['ingredients']:
                        output.write(f"- {ing}\n")
                    output.write("Instructions:\n")
                    output.write(f"{meal['instructions']}\n")
                    output.write(f"Calories: {meal['calories']} kcal\n")
                    output.write("\n" + "-"*40 + "\n\n")
            return output.getvalue()

        formatted_text = format_weekly_plan_text(weekly_plan)

        st.download_button(
            label="⬇️ Download Weekly Meal Plan",
            data=formatted_text,
            file_name="weekly_meal_plan.txt",
            mime="text/plain"
        )