import customtkinter
from PIL import Image, ImageTk 




class Panel(customtkinter.CTk):
    def __init__(self,apariencia,color,tamaño):
            super().__init__()
            self.apariencia = customtkinter.set_appearance_mode(apariencia)
            self.color = customtkinter.set_default_color_theme(color)
            self.geometry(tamaño)

            self.FrameRemeras = Frame(self,0,0)  
            self.botonRemera = Boton(self.FrameRemeras,"Lista de Remeras",0.5,0.5)
            
            self.FramePantalones = Frame(self,0,1)

            self.botonPantalon = Boton(self.FramePantalones, "Lista de Pantalones",0.5,0.5)
            
       


class Boton(customtkinter.CTkButton):
      def __init__(self,app,nombre,ubicacionX,ubicacionY,**kwargs):
            super().__init__(master=app , text=nombre)
            self.boton = self.place(relx=ubicacionX,rely=ubicacionY,anchor=customtkinter.CENTER)
    
    
class Frame(customtkinter.CTkFrame):
      def __init__(self,master,posicionX , posicionY):
            super().__init__(master,width=200,height=400,)
            self.grid(row=posicionX,column=posicionY,padx=40,pady=40,sticky="nsew")
            

   



primer = Panel("System","blue","1360x1024")

primer.mainloop()