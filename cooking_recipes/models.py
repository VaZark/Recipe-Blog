from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=60)
    # images (3)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=60)
    username = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Cuisine(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type

class CookingType(models.Model):
    # Types : Saute, Baking, Frying, Steaming, Grilling, Roasting, boiling, bbqing, smoking,curing,puree, braising
    name = models.CharField(max_length=20)
    uses = models.TextField()

    def __str__(self):
        return self.name

# Wire up to a remote Amazon S3 instance for storage
# class RemoteImage(models.Model)

class Recipe(models.Model):
    title = models.CharField(max_length=60)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    cook_type = models.ForeignKey(CookingType, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, through='IngredientDetail')
    # cover_photo
    # suppl_photos 

    def __str__(self):
        return self.title

class Direction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step = models.PositiveIntegerField()
    desc = models.TextField(unique=True)

class Measure(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size

class IngredientDetail(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    size = models.PositiveIntegerField()
    size_type = models.ForeignKey(Measure, on_delete=models.CASCADE)

