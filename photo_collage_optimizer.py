import math

num_min_photos = float(input("Input the minimum number of photos: "))
num_max_photos = float(input("Input the maximum number of photos: "))
photo_height = float(input("Input the photo height (in): "))
photo_width = float(input("Input the photo width (in): "))
desire_collage_aspect_ratio_height = float(input("Input the collage height (in): "))
desire_collage_aspect_ratio_width = float(input("Input the collage width (in): "))

desired_collage_h_to_w_ratio = desire_collage_aspect_ratio_height/desire_collage_aspect_ratio_width

print(desired_collage_h_to_w_ratio)
print()

# num_rows = 3


for num_rows in range(2, math.floor(num_max_photos/2)):

    num_columns = math.floor(num_max_photos / num_rows)

    collage_height = num_rows * photo_height
    collage_width = num_columns * photo_width

    print("Organizing the photos into %i rows of %i photos utilizes %i of the maximum %i photos." % (num_rows, num_columns, num_max_photos - (num_max_photos % num_rows), num_max_photos))
    print("The resulting collage is %.2f\" high %.2f\" wide." % (collage_height, collage_width))
    print("Aspect ratio: %.2f" % (collage_height/collage_width))

    print()


