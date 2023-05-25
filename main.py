from __init__ import *

from bar_search import BarSearch
from body_main import BodyCenter


def main(page: Page) -> None:
    def set_page():
        page.window_width = 800
        page.window_height = 500
        
        page.bgcolor = 'black100'
        page.theme_mode = 'dark'

        page.vertical_alignment = 'start'
        page.horizontal_alignment = 'center'
        
        page.window_min_width = page.window_width
        page.window_min_height = page.window_height
        
        page.title = 'Emprega Campinas (Automatizador de busca de empregos)'

        page.on_keyboard_event = debug_keyboard
        page.update()
        
    def debug_keyboard(e):
        if e.key.lower() == 's' and e.ctrl:
            page.show_semantics_debugger = not page.show_semantics_debugger
            page.update()
                
    set_page()
    body_center = BodyCenter(page)
    bar_search = BarSearch(body_center.table.add_data_table)
    
    page.add(
        bar_search,
        body_center,
    )    


if '__main__' == __name__:
    app(target=main, assets_dir='assets')