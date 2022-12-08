import dbm

photo_category = dbm.open("captions", "c")

photo_category["animals.png"] = "this is a picture of a group of animals"
photo_category["taylor.png"] = "this is a picture of taylor swift"
photo_category["harry.png"] = "this is a picture of harry styles"
photo_category["animals.png"] = "this is a picture of some zoo animals"
photo_category["taylor.png"] = "this is taylor swift at the 2022 VMAs"
photo_category["harry.png"] = "this is harry styles on tour performing"

for item in photo_category.keys():
    print(item)
    print(photo_category[item])
