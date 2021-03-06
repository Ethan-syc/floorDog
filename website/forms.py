from django import forms
from upload.models import UploadFile
from website.models import *


GENDER = (("W", "Women"), ("M", "Men"))

CATEGORY = (
    ("All", "All"),
    ("blazer", "blazer"),
    ("blouse", "blouse"),
    ("bodysuit", "bodysuit"),
    ("bomber", "bomber"),
    ("bustier", "bustier"),
    ("camisole", "camisole"),
    ("cape", "cape"),
    ("cardigan", "cardigan"),
    ("catsuit", "catsuit"),
    ("coat", "coat"),
    ("corset", "corset"),
    ("crewneck", "crewneck"),
    ("denim", "denim"),
    ("dickie", "dickie"),
    ("dress", "dress"),
    ("genius", "genius"),
    ("harrington", "harrington"),
    ("hoodie", "hoodie"),
    ("jacket", "jacket"),
    ("jean", "jean"),
    ("jumper", "jumper"),
    ("jumpsuit", "jumpsuit"),
    ("kilt", "kilt"),
    ("leggings", "leggings"),
    ("miniskirt", "miniskirt"),
    ("outerwear", "outerwear"),
    ("overalls", "overalls"),
    ("overcoat", "overcoat"),
    ("overshirt", "overshirt"),
    ("pant", "pant"),
    ("parka", "parka"),
    ("peacoat", "peacoat"),
    ("polo", "polo"),
    ("poncho", "poncho"),
    ("puffer", "puffer"),
    ("pullover", "pullover"),
    ("raincoat", "raincoat"),
    ("set", "set"),
    ("shirt", "shirt"),
    ("short", "short"),
    ("skirt", "skirt"),
    ("stole", "stole"),
    ("suit", "suit"),
    ("sweater", "sweater"),
    ("sweatpants", "sweatpants"),
    ("sweatshirt", "sweatshirt"),
    ("tights", "tights"),
    ("top", "top"),
    ("trenchcoat", "trenchcoat"),
    ("trouser", "trouser"),
    ("tunic", "tunic"),
    ("turtleneck", "turtleneck"),
    ("vest", "vest"),
    ("waistcoat", "waistcoat"),
)

MATERIAL = (
    ("All", "All"),
    ("cotton", "cotton"),
    ("polyester", "polyester"),
    ("wool", "wool"),
    ("elastane", "elastane"),
    ("polyamide", "polyamide"),
    ("leather", "leather"),
    ("silk", "silk"),
    ("polyurethane", "polyurethane"),
    ("acrylic", "acrylic"),
    ("cashmere", "cashmere"),
    ("cupro", "cupro"),
    ("mohair", "mohair"),
    ("spandex", "spandex"),
    ("acetate", "acetate"),
    ("alpaca", "alpaca"),
    ("rayon", "rayon"),
    ("leather", "leather"),
    ("merino", "merino"),
    ("linen", "linen"),
    ("lamb", "lamb"),
    ("lyocell", "lyocell"),
    ("calfskin", "calfskin"),
    ("modal", "modal"),
    ("lycra", "lycra"),
    ("fiber", "fiber"),
    ("cupra", "cupra"),
    ("angora", "angora"),
    ("triacetate", "triacetate"),
    ("camel", "camel"),
    ("recycled", "recycled"),
    ("pima", "pima"),
    ("modacrylic", "modacrylic"),
    ("lambswool", "lambswool"),
)

DESIGN = (
    ("All", "All"),
    ("Collar", "Collar"),
    ("Long sleeve", "Long sleeve"),
    ("Short sleeve", "Short sleeve"),
    ("Slim-fit", "Slim-fit"),
    ("Relaxed-fit", "Relaxed-fit"),
    ("Skinny-fit", "Skinny-fit"),
    ("Button closure", "Button closure"),
    ("Zip closure", "Zip closure"),
    ("Mid-rise", "Mid-rise"),
    ("logo", "Logo"),
    ("Spread collar", "Spread collar"),
    ("Four-pocket", "Four-pocket"),
    ("embroidered", "Embroidered"),
    ("Five-pocket", "Five-pocket"),
    ("Three-pocket", "Three-pocket"),
    ("Straight-leg", "Straight-leg"),
    ("lapel collar", "Lapel collar"),
    ("stand collar", "Stand collar"),
)

COLOR = (
    ("All", "All"),
    ("beige", "Beige"),
    ("blue", "Blue"),
    ("black", "Black"),
    ("brown", "Brown"),
    ("green", "Green"),
    ("grey", "Grey"),
    ("gold", "Gold"),
    ("indigo", "Indigo"),
    ("khaki", "Khaki"),
    ("lime", "Lime"),
    ("magenta", "Magenta"),
    ("navy", "Navy"),
    ("orange", "Orange"),
    ("pink", "Pink"),
    ("purple", "Purple"),
    ("red", "Red"),
    ("silver", "Silver"),
    ("tan", "Tan"),
    ("white", "White"),
    ("yellow", "Yellow")
)


class GenderForm(forms.Form):
    gender = forms.ChoiceField(widget=forms.Select(), choices=GENDER)


class FilterForm(forms.Form):
    category = forms.ChoiceField(widget=forms.Select(), choices=CATEGORY)


class MaterialForm(forms.Form):
    material = forms.ChoiceField(widget=forms.Select(), choices=MATERIAL)


class DesignForm(forms.Form):
    design = forms.ChoiceField(widget=forms.Select(), choices=DESIGN)


class ColorForm(forms.Form):
    color = forms.ChoiceField(widget=forms.Select(), choices=COLOR)


class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        exclude = ()


