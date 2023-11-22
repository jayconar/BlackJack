from PIL import Image, ImageTk

BG = "#35654d"
image_list = []


def interface(root, *canvases):
    root.configure(bg=BG)
    for i, canvas in enumerate(canvases):
        canvas.grid(row=i, column=0, columnspan=3, sticky="ew")


def display(canvas, image_path, x, y):
    image = Image.open(image_path)
    tk_image = ImageTk.PhotoImage(image)
    # Adding the image to the canvas at the specified coordinates (x, y)
    canvas.create_image(x, y, image=tk_image)
    # Appending the tk_image to the image_list to keep a reference to it
    image_list.append(tk_image)
