from PIL import Image
import customtkinter


my_image = customtkinter.CTkImage(light_image=Image.open("<path to light mode image>"),
                                  dark_image=Image.open("<path to dark mode image>"),
                                  size=(30, 30))

image_label = customtkinter.CTkLabel(app, image=my_image, text="")  # display image with a CTkLabel