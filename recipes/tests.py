from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from recipes.models import Recipe


# Create your tests here.
class RecipeModelTests(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
                title= "CHICKEN INN RECIPE",
                description="classic kfc copied baked chicken",
                ingredents="Chicken, cooking oil, spices, baking flour, breadcumbs",
                instructions="1. boil the chicken. 2. Marinate the chicken 3. Dip it in mixed flour with breadcrumbs. 4. fry the chicken"
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.title, "CHICKEN INN RECIPE")
        self.assertEqual(self.recipe.description, "classic kfc copied baked chicken")
        self.assertEqual(self.recipe.ingredents, "Chicken, cooking oil, spices, baking flour, breadcumbs")
        self.assertEqual(self.recipe.instructions, "1. boil the chicken. 2. Marinate the chicken 3. Dip it in mixed flour with breadcrumbs. 4. fry the chicken")


class RecipeAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="chalie", password="@Password101")
        self.client.force_authenticate(user=self.user)
        self.recipe = Recipe.objects.create(
            title="CHICKEN INN RECIPE",
            description="classic kfc copied baked chicken",
            ingredents="Chicken, cooking oil, spices, baking flour, breadcumbs",
            instructions="1. boil the chicken. 2. Marinate the chicken 3. Dip it in mixed flour with breadcrumbs. 4. fry the chicken"
        )

        self.valid_payload = {
            "title":"GRILLS INN RECIPE",
            "description": "classic grills copied baked chicken",
            "ingredents": "Chicken, cooking oil, spices, baking flour, breadcumbs, vinegar",
            "instructions": "1. boil the chicken. 2. Marinate the chicken 3. Dip it in mixed flour with breadcrumbs. 4. fry the chicken 5. eat"
        }

        self.invalid_payload = {
            "title": "",
            "description": "classic grills copied baked chicken",
            "ingredents": "Chicken, cooking oil, spices, baking flour, breadcumbs, vinegar",
            "instructions": "1. boil the chicken. 2. Marinate the chicken 3. Dip it in mixed flour with breadcrumbs. 4. fry the chicken 5. eat"
        }

    def test_get_all_recipes(self):
        response = self.client.get('/api/v1/recipes')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_recipe(self):
        response = self.client.post('/api/v1/recipes', self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_recipe(self):
        response = self.client.post('/api/v1/recipes', self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_recipe_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/v1/recipes')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



