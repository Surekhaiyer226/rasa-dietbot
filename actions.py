# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


#This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_core_sdk.events import SlotSet
import requests

# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import SlotSet, EventType
# from rasa_sdk.executor import CollectingDispatcher
# from db_sqlite import insert_data
import random



class ActionMealPlan(Action):

    def name(self) -> Text:
        return "action_meal_plan"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        diets = str(tracker.get_slot('diet related'))
        intolerance = str(tracker.get_slot('allergy related'))
        calories = str(tracker.get_slot('calorie related'))

        api_address = "https://api.spoonacular.com/mealplanner/generate?timeFrame=day&apiKey=a6245dfac411424dac6a89860fa9c179&cuisine=Indian&diet="+ diets+"&intolerances="+intolerance+"&targetCalories="+calories+""
        response = requests.get(api_address)
        data = response.json()
        breakfast_name = data['meals'][0]['title']
        breakfast_url = data['meals'][0]['sourceUrl']
        breakfast_readyinminutes = data['meals'][0]['readyInMinutes']
        lunch_name = data['meals'][1]['title']
        lunch_url = data['meals'][1]['sourceUrl']

        lunch_readyinminutes = data['meals'][1]['readyInMinutes']

        dinner_name = data['meals'][2]['title']


        dinner_url = data['meals'][2]['sourceUrl']

        dinner_readyinminutes = data['meals'][2]['readyInMinutes']

        calories = data['nutrients']['calories']

        protein = data['nutrients']['protein']

        fat = data['nutrients']['fat']

        carbs = data['nutrients']['carbohydrates']


        mealplan_data = "BREAKFAST: \n Name:{} \n  URL:{} \n  Ready In Minutes:{} \n LUNCH: \n Name:{} \n URL:{} \n Ready In Minutes:{} \n DINNER: \n Name:{} \n  URL:{} \n  Ready In Minutes:{} \n NUTRITIONAL INFORMATION: \n  Calories:{} \n Proteins:{} \n Fats:{} \n Carbs:{} ".format(breakfast_name,breakfast_url,breakfast_readyinminutes,lunch_name ,lunch_url,lunch_readyinminutes, dinner_name,dinner_url,dinner_readyinminutes,calories,protein,fat,carbs)

        dispatcher.utter_message(mealplan_data)

        return[]


# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_core_sdk.events import SlotSet
# import requests


class ActionNutrition(Action):

    def name(self) -> Text:
        return "action_nutrition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ingrs = str(tracker.get_slot('Ingredients and Quantity'))
        api_address = "https://api.edamam.com/api/nutrition-data?app_id=7ede9cec&app_key=b0d237446a453b0b9d232561bc93bf1d&ingr= "+ ingrs +""
        response = requests.get(api_address)
        data=response.json()
        calories = round(data['calories'])
        fat = round(data['totalNutrients']['FAT']['quantity'],2)
        carbs = round(data['totalNutrients']['CHOCDF']['quantity'],2)
        sugar = round(data['totalNutrients']['SUGAR']['quantity'],3)
        protein = round(data['totalNutrients']['PROCNT']['quantity'],4)
        Cholesterol = round(data['totalNutrients']['CHOLE']['quantity'],3)
        Iron = round(data['totalNutrients']['FE']['quantity'],2)
        Water = round(data['totalNutrients']['WATER']['quantity'],3)
        Fibre = round(data['totalNutrients']['FIBTG']['quantity'],2)
        VitaminB12 = round(data['totalNutrients']['VITB12']['quantity'],3)
        VitaminD = round(data['totalNutrients']['VITD']['quantity'],2)
        VitaminE = round(data['totalNutrients']['TOCPHA']['quantity'],3)
        VitaminK = round(data['totalNutrients']['VITK1']['quantity'],2)
        VitaminB6 = round(data['totalNutrients']['VITB6A']['quantity'],3)
        VitaminA = round(data['totalNutrients']['VITA_RAE']['quantity'],3)
        VitaminC = round(data['totalNutrients']['VITC']['quantity'],2)

        nutrition_data = "Calories:{} \n Fat:{} \n Carbs:{} \n Sugar:{} \n Protein:{} \n Cholesterol:{} \n Iron:{} \n Water:{} \n Fibre:{} \n VITAMINS: \n Vitamin B12:{} \n Vitamin D:{} \n Vitamin E:{} \n Vitamin K:{} \n Vitamin B6:{} \n Vitamin A:{} \n Vitamin C:{} ".format(calories,fat,carbs,sugar,protein,Cholesterol,Iron,Water,Fibre,VitaminB12, VitaminD,VitaminE,VitaminK,VitaminB6,VitaminA,VitaminC )
        dispatcher.utter_message(nutrition_data)

        return [SlotSet("Ingredient and Quantity",ingrs)]


class ActionAnswer(Action):

    def name(self) -> Text:
        return "action_recipe_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        query = str(tracker.get_slot('recipe related'))
        api_address = "https://api.edamam.com/search?app_id=cc2cfdbb&app_key=5a29d3d7bfcca324cfe6beeca753500e&from=0&to=3&cuisineType=Indian&cuisineType=American&q="+query+""
        response = requests.get(api_address)
        data = response.json()
        name = data['hits'][0]['recipe']['label']
        image= data['hits'][0]['recipe']['image']
        url= data['hits'][0]['recipe']['url']
        ingredientlines= data['hits'][0]['recipe']['ingredientLines']
        mealtype = data['hits'][0]['recipe']['mealType']
        name1= data['hits'][1]['recipe']['label']
        image1 = data['hits'][1]['recipe']['image']
        url1 = data['hits'][1]['recipe']['url']
        ingredientlines1 = data['hits'][1]['recipe']['ingredientLines']
        mealtype1 = data['hits'][1]['recipe']['mealType']
        name2 = data['hits'][2]['recipe']['label']
        image2 = data['hits'][2]['recipe']['image']
        url2 = data['hits'][2]['recipe']['url']
        ingredientlines2 = data['hits'][2]['recipe']['ingredientLines']
        mealtype2 = data['hits'][2]['recipe']['mealType']


        food_answer_data ="RECIPE 1 \n  NAME : {} \n  IMAGE :{}  \n  URL:{}  \n   INGREDIENTS :{} \n Meal Type:{} \n RECIPE 2 \n  NAME: {} \n  IMAGE :{}  \n  URL:{}  \n   INGREDIENTS :{} \n Meal Type:{} \n RECIPE 3 \n NAME: {} \n  IMAGE :{}  \n  URL:{}  \n   INGREDIENTS :{} \n Meal Type:{}  ".format(name,image,url,ingredientlines,mealtype,name1,image1,url1,ingredientlines1,mealtype1,name2,image2,url2,ingredientlines2,mealtype2)

        dispatcher.utter_message(food_answer_data)

        return [SlotSet("recipe related",query)]


# class ActionVideo(Action):
#
#     def name(self) -> Text:
#         return "action_video"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         q = str(tracker.get_slot('video related'))
#         api_address = "https://api.spoonacular.com/food/videos/search?number=2&apiKey=a6245dfac411424dac6a89860fa9c179&query= "+q+""
#         response = requests.get(api_address)
#         data=response.json()
#         title = data['videos'][0]['title']
#         rating = data['videos'][0]['rating']
#         views = data['videos'][0]['views']
#         thumbnail = data['videos'][0]['thumbnail']
#         youtubeid = data['videos'][0]['youTubeId']
#         title1 = data['videos'][1]['title']
#         rating1 = data['videos'][1]['rating']
#         views1 = data['videos'][1]['views']
#         thumbnail1 = data['videos'][1]['thumbnail']
#         youtubeid1 = data['videos'][1]['youTubeId']
#
#
#
#         video_data = "VIDEO 1 \n Title:{} \n Rating:{} \n Views:{} \n Thumbnail:{} \n YOUTUBEID:{} \n VIDEO 2 \n Title:{} \n Rating:{} \n Views:{} \n Thumbnail:{} \n YOUTUBEID:{} ".format(title,rating,views,thumbnail,youtubeid,title1,rating1,views1,thumbnail1,youtubeid1)
#         dispatcher.utter_message(video_data)
#
#         return [SlotSet("video related",q)]

class ActionFood(Action):

    def name(self) -> Text:
        return "action_food_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        food = str(tracker.get_slot('food related'))
        api_address="https://api.spoonacular.com/recipes/quickAnswer?apiKey=a6245dfac411424dac6a89860fa9c179&q="+food+""
        response = requests.get(api_address)
        data = response.json()
        Images = data['image']
        Answers = data['answer']
        food_data =  "Image:{} \n Answer:{}".format(Images,Answers)
        dispatcher.utter_message(food_data)

        return [SlotSet("food related", food)]

# class DietForm(FormAction):
#     def name(self) -> Text:
#         return "diet_plan_form"
#
#     @staticmethod
#     def required_slots(tracker:Tracker) -> List[Text]:
#         """A list of required slots"""
#         print("required_slots(tracker:Tracker)")
#         return["name","age"]
#
#
#     def submit(
#             self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any],
#          ) -> List[Dict]:
#         dispatcher.utter_message("thank you")
#         # insert_data(tracker.get_slot("name"),tracker.get_slot("age"))
#         return[]

# class ValidateDietForm(Action):
#     def name(self) -> Text:
#         return "user_details_form"
#
#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
#     ) -> List[EventType]:
#         required_slots = ["name", "age"]
#
#         for slot_name in required_slots:
#             if tracker.slots.get(slot_name) is None:
#                 # The slot is not filled yet. Request the user to fill this slot next.
#                 return [SlotSet("requested_slot", slot_name)]
#
#         # All slots are filled.
#         return [SlotSet("requested_slot", None)]
#
# class ActionSubmit(Action):
#     def name(self) -> Text:
#         return "action_submit"
#
#     def run(
#         self,
#         dispatcher,
#         tracker: Tracker,
#         domain: "DomainDict",
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(template="utter_details_thanks",
#                                  Name=tracker.get_slot("name"),
#                                  Age=tracker.get_slot("age"))
# class ActionMealPlan1(Action):
#
#     def name(self) -> Text:
#         return "action_meal_plan1"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         diets1 = str(tracker.get_slot('diet related1'))
#         intolerance1 = str(tracker.get_slot('allergy related1'))
#         calories1 = str(tracker.get_slot('calorie related1'))
#
#         api_address = "https://api.spoonacular.com/mealplanner/generate?timeFrame=week&apiKey=a6245dfac411424dac6a89860fa9c179&cuisine=Indian&diet="+ diets1+"&intolerances="+intolerance1+"&targetCalories="+calories1+""
#         response = requests.get(api_address)
#         data = response.json()
#         Breakfast = data['week']['monday']['meals'][0]['title']
#         Breakfast_URL = data['week']['monday']['meals'][0]['sourceUrl']
#         Ready_In_Minutes1= data['week']['monday']['meals'][0]['readyInMinutes']
#
#         Lunch = data['week']['monday']['meals'][1]['title']
#         Lunch_URL= data['week']['monday']['meals'][1]['sourceUrl']
#         Ready_In_Minutes2= data['week']['monday']['meals'][1]['readyInMinutes']
#
#         Dinner = data['week']['monday']['meals'][2]['title']
#         Dinner_URL = data['week']['monday']['meals'][2]['sourceUrl']
#         Ready_In_Minutes3= data['week']['monday']['meals'][2]['readyInMinutes']
#
#         calories = data['week']['monday']['nutrients']['calories']    #Nutritional info
#
#         Breakfast1 = data['week']['tuesday']['meals'][0]['title']                #tuesday
#         Breakfast_URL1 = data['week']['tuesday']['meals'][0]['sourceUrl']
#         Ready_In_Minutes4 = data['week']['tuesday']['meals'][0]['readyInMinutes']
#
#         Lunch1 = data['week']['tuesday']['meals'][1]['title']
#         Lunch_URL1 = data['week']['tuesday']['meals'][1]['sourceUrl']
#         Ready_In_Minutes5= data['week']['tuesday']['meals'][1]['readyInMinutes']
#
#         Dinner1 = data['week']['tuesday']['meals'][2]['title']
#         Dinner_URL1 = data['week']['tuesday']['meals'][2]['sourceUrl']
#         Ready_In_Minutes6 = data['week']['tuesday']['meals'][2]['readyInMinutes']
#    #Nutritional info
#
#
#
#         mealplan1_data = "Monday \n BREAKFAST: \n Name:{} \n  URL:{} \n  Ready In Minutes:{} \n LUNCH: \n Name:{} \n URL:{} \n Ready In Minutes:{} \n DINNER: \n Name:{} \n  URL:{} \n  Ready In Minutes:{} \n NUTRITIONAL INFORMATION: \n  Calories:{} \n Tuesday \n BREAKFAST: \n Name:{} \n  URL:{} \n  Ready In Minutes:{} \n LUNCH: \n Name:{} \n URL:{} \n Ready In Minutes:{} \n DINNER: \n Name:{} \n  URL:{} \n  Ready In Minutes:{} ".format(Breakfast,Breakfast_URL,Ready_In_Minutes1,Lunch,Lunch_URL,Ready_In_Minutes2, Dinner,Dinner_URL,Ready_In_Minutes3,calories,Breakfast1,Breakfast_URL1,Ready_In_Minutes4,Lunch1,Lunch_URL1,Ready_In_Minutes5,Dinner1,Dinner_URL1,Ready_In_Minutes6)
#
#         dispatcher.utter_message(mealplan1_data)
#
#         return[SlotSet("calorie related1",calories1)]

