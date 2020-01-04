from tkinter import *
from operator import itemgetter
import math


def calc_collage():
    global num_rows
    global num_max_photos
    global photo_height
    global photo_width
    global collage_aspect_ratio_list
    global desired_collage_h_to_w_ratio
    global canvas_widget
    try:
        num_min_photos = float(num_min_photos_input.get())
    except ValueError:
        popup_window_input = Tk()
        Label(popup_window_input, text="Please enter a valid minimum number of photos.").grid(row=0, column=0)
        popup_window_input.mainloop()

    try:
        num_max_photos = float(num_max_photos_input.get())
    except ValueError:
        popup_window_input = Tk()
        Label(popup_window_input, text="Please enter a valid maximum number of photos.").grid(row=0, column=0)
        popup_window_input.mainloop()

    try:
        photo_height = float(photo_height_input.get())
    except ValueError:
        popup_window_input = Tk()
        Label(popup_window_input, text="Please enter a valid number for the height of the photos.").grid(row=0, column=0)
        popup_window_input.mainloop()

    try:
        photo_width = float(photo_width_input.get())
    except ValueError:
        popup_window_input = Tk()
        Label(popup_window_input, text="Please enter a valid number for the width of the photos.").grid(row=0, column=0)
        popup_window_input.mainloop()

    try:
        desire_collage_aspect_ratio_height = float(desire_collage_aspect_ratio_height_input.get())
    except ValueError:
        popup_window_input = Tk()
        Label(popup_window_input, text="Please enter a valid number for the aspect height of the collage.").grid(row=0, column=0)
        popup_window_input.mainloop()

    try:
        desire_collage_aspect_ratio_width = float(desire_collage_aspect_ratio_width_input.get())
    except ValueError:
        popup_window_input = Tk()
        Label(popup_window_input, text="Please enter a valid number for the aspect height of the collage.").grid(row=0, column=0)
        popup_window_input.mainloop()

    desired_collage_h_to_w_ratio = desire_collage_aspect_ratio_height / desire_collage_aspect_ratio_width

    collage_aspect_ratio_list = []

    for num_rows in range(2, math.floor(num_max_photos / 2)):
        num_photos_width = math.floor(num_max_photos / num_rows)

        collage_height = num_rows * photo_height
        collage_width = num_photos_width * photo_width

        collage_aspect_ratio_list.append(collage_height / collage_width)

    collage_aspect_ratio_delta_list = []
    for collage_aspect_ratio in collage_aspect_ratio_list:
        collage_aspect_ratio_delta_list.append(abs(collage_aspect_ratio - desired_collage_h_to_w_ratio))

    num_rows = 2 + min(enumerate(collage_aspect_ratio_delta_list), key=itemgetter(1))[0]
    num_photos_width = math.floor(num_max_photos / num_rows)
    collage_height = num_rows * photo_height
    collage_width = num_photos_width * photo_width
    collage_aspect_ratio_list.append(collage_height / collage_width)

    output_text_line_1 = "Organizing the photos into %i rows of %i photos utilizes %i of the maximum %i photos.\n" % (
        num_rows, num_photos_width, num_max_photos - (num_max_photos % num_rows), num_max_photos)
    output_text_line_2 = "The resulting collage is %.2f\" high %.2f\" wide.\n" % (collage_height, collage_width)
    output_text_line_3 = "Actual aspect ratio of %.2f compared to the desired %.2f." % (
        collage_height / collage_width, desired_collage_h_to_w_ratio)

    output_text_all_lines = output_text_line_1 + output_text_line_2 + output_text_line_3

    output_text = Text(window, width=85, height=3)
    output_text.insert(END, output_text_all_lines)
    output_text.grid(row=3, column=0, columnspan=100)

    Button(window, text="Add row", command=add_row).grid(row=4, column=0)
    Button(window, text="Subtract row", command=subtract_row).grid(row=4, column=1)

    vis_scale = 10
    vis_padding = vis_scale
    canvas_widget = Canvas(window, width=int(2 * vis_padding + vis_scale * collage_width),
                           height=int(2 * vis_padding + vis_scale * collage_height))
    canvas_widget.grid(row=5, column=0, columnspan=100)
    # w.create_rectangle(0, 0, int(2*vis_padding+vis_scale*collage_width), int(2*vis_padding+vis_scale*collage_height), fill="aqua")

    # w.create_rectangle(x1, y1, x2, y2, fill="")

    for row in range(num_rows):
        for col in range(num_photos_width):
            start_x = 1 + (photo_width * col)
            start_y = 1 + (photo_height * row)
            end_x = start_x + photo_width
            end_y = start_y + photo_height

            canvas_widget.create_rectangle(vis_scale * start_x, vis_scale * start_y, vis_scale * end_x,
                                           vis_scale * end_y, fill="")


def recalc_collage():
    global num_max_photos
    global photo_height
    global photo_width
    global collage_aspect_ratio_list
    global desired_collage_h_to_w_ratio
    global canvas_widget
    num_photos_width = math.floor(num_max_photos / num_rows)
    collage_height = num_rows * photo_height
    collage_width = num_photos_width * photo_width
    collage_aspect_ratio_list.append(collage_height / collage_width)

    output_text_line_1 = "Organizing the photos into %i rows of %i photos utilizes %i of the maximum %i photos.\n" % (
        num_rows, num_photos_width, num_max_photos - (num_max_photos % num_rows), num_max_photos)
    output_text_line_2 = "The resulting collage is %.2f\" high %.2f\" wide.\n" % (collage_height, collage_width)
    output_text_line_3 = "Actual aspect ratio of %.2f compared to the desired %.2f." % (
        collage_height / collage_width, desired_collage_h_to_w_ratio)

    output_text_all_lines = output_text_line_1 + output_text_line_2 + output_text_line_3

    output_text = Text(window, width=85, height=3)
    output_text.insert(END, output_text_all_lines)
    output_text.grid(row=3, column=0, columnspan=100)

    Button(window, text="Add row", command=add_row).grid(row=4, column=0)
    Button(window, text="Subtract row", command=subtract_row).grid(row=4, column=1)

    vis_scale = 10
    vis_padding = vis_scale
    canvas_widget.delete("all")
    canvas_widget = Canvas(window, width=int(2 * vis_padding + vis_scale * collage_width),
                           height=int(2 * vis_padding + vis_scale * collage_height))
    canvas_widget.grid(row=5, column=0, columnspan=100)

    for row in range(num_rows):
        for col in range(num_photos_width):
            start_x = 1 + (photo_width * col)
            start_y = 1 + (photo_height * row)
            end_x = start_x + photo_width
            end_y = start_y + photo_height

            canvas_widget.create_rectangle(vis_scale * start_x, vis_scale * start_y, vis_scale * end_x,
                                           vis_scale * end_y, fill="")


def add_row():
    global num_rows
    if num_rows != num_max_photos - 1:
        num_rows += 1
        recalc_collage()


def subtract_row():
    global num_rows
    if num_rows != 1:
        num_rows -= 1
        recalc_collage()


window = Tk()
window.wm_title("Collage Optimizer")  # name window

Label(window, text="Minimum number of photos").grid(row=0, column=0)
num_min_photos_input = Entry(window, width=6)
num_min_photos_input.grid(row=0, column=1)

Label(window, text="Maximum number of photos").grid(row=1, column=0)
num_max_photos_input = Entry(window, width=6)
num_max_photos_input.grid(row=1, column=1)

Label(window, text="Photo aspect ratio (h:w)").grid(row=0, column=2)
photo_height_input = Entry(window, width=6)
photo_height_input.grid(row=0, column=3)
Label(window, text=":").grid(row=0, column=4)
photo_width_input = Entry(window, width=6)
photo_width_input.grid(row=0, column=5)

Label(window, text="Collage aspect ratio (h:w)").grid(row=1, column=2)
desire_collage_aspect_ratio_height_input = Entry(window, width=6)
desire_collage_aspect_ratio_height_input.grid(row=1, column=3)
Label(window, text=":").grid(row=1, column=4)
desire_collage_aspect_ratio_width_input = Entry(window, width=6)
desire_collage_aspect_ratio_width_input.grid(row=1, column=5)

# create calculate button
Button(window, text="Calculate", command=calc_collage).grid(row=2, column=0)

mainloop()
