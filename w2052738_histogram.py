# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20220957
# Date: 11/26/2023

from graphics import *

# Draw bar function
def draw_bar(x1, x2, height, color, win):
    bar = Rectangle(Point(x1, 550 - height), Point(x2, 550))
    bar.setFill(color)
    bar.setOutline(color)
    bar.draw(win)

# Draw label function
def draw_label(x, y, text, size, win):
    text_colour = color_rgb(100,98,96)

    label = Text(Point(x, y), text)
    label.setStyle('bold')
    label.setTextColor(text_colour)
    label.setSize(size)
    label.draw(win)

# Create the histogram
def histogram(progress_count, trailing_count, retriever_count, exclude_count):
    # Define the graphics window
    win = GraphWin("My graph", 700, 650)

    # Define colors
    color_1 = color_rgb(153,170,119)
    color_2 = color_rgb(120,153,119)
    color_3 = color_rgb(204,204,136)
    color_4 = color_rgb(200,150,140)

    # Calculate total number of outcomes
    total_count = progress_count + trailing_count + retriever_count + exclude_count

    # Calculate the height of each bar based on the counts and the total outcomes
    progress_height = (progress_count / total_count) * 400
    trailing_height = (trailing_count / total_count) * 400
    retriever_height = (retriever_count / total_count) * 400
    exclude_height = (exclude_count / total_count) * 400

    # Draw the bars
    draw_bar(100, 220, progress_height, color_2, win)
    draw_bar(230, 350, trailing_height, color_1, win)
    draw_bar(360, 480, retriever_height, color_3, win)
    draw_bar(490, 610, exclude_height, color_4, win)

    # Draw count labels
    draw_label(160, (540 - progress_height), progress_count, 12, win)
    draw_label(290, (540 - trailing_height), trailing_count, 12, win)
    draw_label(420, (540 - retriever_height), retriever_count, 12, win)
    draw_label(550, (540 - exclude_height), exclude_count, 12, win)

    # Draw other labels
    draw_label(350, 110, "Histogram Results", 20, win)
    draw_label(160, 565, "Progress", 13, win)
    draw_label(290, 565, "Trailing", 13, win)
    draw_label(420, 565, "Retriever", 13, win)
    draw_label(550, 565, "Exclude", 13, win)
    draw_label(350, 610, f"{total_count} Outcomes in Total", 14, win)

    # Draw the line
    l = Line(Point(60,550), Point(650,550))
    l.draw(win)

    # Pause to view the result and close the window
    try:
        win.getMouse()
        win.close()

    except GraphicsError:
        win.close()