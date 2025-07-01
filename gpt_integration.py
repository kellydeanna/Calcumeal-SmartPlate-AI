from openai import OpenAI

client = OpenAI(api_key="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")  # 🔒 Replace with your actual key securely

def generate_recipe_from_ingredients(ingredients):
    all_recipes = []

    for item in ingredients:
        prompt = f"""
You are a healthy cooking assistant.
Suggest 2 healthy recipes that use "{item}" as the main ingredient.
Each recipe should include: title, list of ingredients, instructions, and estimated calories.
"""
        try:
            response = client.chat.completions.create(  # ✅ This is correct for OpenAI SDK v1.x
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            recipe_text = response.choices[0].message.content
            all_recipes.append((item, recipe_text))
        except Exception as e:
            all_recipes.append((item, f"Error generating recipes: {e}"))

    return all_recipes

import re

def parse_recipe_text(text):
    title_match = re.search(r"Title:\s*(.+)", text)
    ingredients_match = re.search(r"Ingredients:\s*(.*?)\n\n", text, re.DOTALL)
    instructions_match = re.search(r"Instructions:\s*(.*?)\n\n", text, re.DOTALL)
    calories_match = re.search(r"Calories:\s*(.+)", text)

    title = title_match.group(1).strip() if title_match else "Untitled"
    
    if ingredients_match:
        ingredients_raw = ingredients_match.group(1).strip()
        ingredients = [line.strip("- ").strip() for line in ingredients_raw.splitlines() if line.strip()]
    else:
        ingredients = []

    instructions = instructions_match.group(1).strip() if instructions_match else "Not provided."
    calories = calories_match.group(1).strip() if calories_match else "Unknown"

    return {
        "title": title,
        "ingredients": ingredients,
        "instructions": instructions,
        "calories": calories
    }

def generate_weekly_plan():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    meal_types = ["Breakfast", "Lunch", "Dinner"]
    plan = {}

    for day in days:
        plan[day] = {}
        for meal in meal_types:
            prompt = f"""
You are a healthy meal planner. 
Provide a healthy {meal.lower()} recipe for {day} in the following format:

Title: ...
Ingredients:
- ...
- ...
Instructions:
1. ...
2. ...
Calories: ...
"""

            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a healthy meal planner."},
                        {"role": "user", "content": prompt}
                    ]
                )
                result = response.choices[0].message.content
                parsed = parse_recipe_text(result)

            except Exception as e:
                parsed = {
                    "title": f"{meal} Error",
                    "ingredients": [],
                    "instructions": f"Error generating recipe: {str(e)}",
                    "calories": "N/A"
                }

            plan[day][meal] = {
                "title": parsed["title"],
                "ingredients": parsed["ingredients"],
                "instructions": parsed["instructions"],
                "calories": parsed["calories"]
            }

    return plan