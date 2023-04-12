import flet as ft

from flet import (
    Container,
    Icon,
    Page,
    Text,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    colors,
    icons,
    margin,
    Column,
)

def main(page: ft.Page):
    
    page.title = "Music Recommender" #sets the window name
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    txt1 = ft.TextField(value="Enter a song:", text_align=ft.TextAlign.RIGHT, width=200) #creates a text field called txt
    txt2 = ft.TextField(value="Enter a song:", text_align=ft.TextAlign.RIGHT, width=200)
    txt3 = ft.TextField(value="Enter a song:", text_align=ft.TextAlign.RIGHT, width=200)
    page.update() #this is a very necessary function, we call it when we make a new change
    
    
    
    def save_link(e): 
        
        txt1.value = str(txt1.value)
        print(txt1.value)
    
    page.add(
             
            ft.Row( 
                [
                    txt1,
                    txt2,
                    txt3,
                    ft.IconButton(ft.icons.GRASS_OUTLINED, on_click=save_link), 
                
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            
            ft.AppBar(
                leading=Icon(icons.APPS),
                leading_width=100,
                title=Text("Music Recommender",size=32, text_align="start"),
                center_title=False,
                toolbar_height=75,
                bgcolor=colors.DEEP_PURPLE_ACCENT,
                ),
                
        
  )
    

    
    
    
ft.app(target=main) 
