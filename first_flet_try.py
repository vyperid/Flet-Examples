import flet as ft

def main(page: ft.Page):
    
    page.title = "Music Recommender" #sets the window name
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    txt = ft.TextField(value="Link of your playlist.", text_align=ft.TextAlign.RIGHT, width=500) #creates a text field called txt
    page.update() #this is a very necessary function, we call it when we make a new change
    
    
    
    def save_link(e): #when a value is entered to the txt field, we set it's value to the txt value
        
        txt.value = str(txt.value)
        print(txt.value)
    
    page.add( #getting used when we want to put rows or columns 
        ft.Row( #creating a new row
            [
                txt, #our previously created txt field
                ft.IconButton(ft.icons.GRASS_OUTLINED, on_click=save_link), #a button next to our txt field
            
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    
    
    
ft.app(target=main) 
