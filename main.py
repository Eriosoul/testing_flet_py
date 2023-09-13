import flet
from flet import *
# import requests
# import datetime

# La API no es mi es de una web de metorologia

days = [
    "Mon",
    "Mun",
    "Wed",
    "The",
    "Fri",
    "Sat",
    "Sun"
]

def main(page: Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    # animacion
    def _expand(e):
        if e.data == "true":
            _c.content.controls[0].height = 560
            _c.content.controls[0].update()
        else:
            _c.content.controls[0].height = 660 * 0.4
            _c.content.controls[0].update()

    # el tiempo actual
    def _current_temp():
        _current_temp = [-3]
        return [_current_temp]
    # top del contenedor
    def _top():
        _today = _current_temp

        top = Container(
            width=310,
            height= 660 * 0.40,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=["lightblue600", "lightblue900"],
            ),
            border_radius=35,
            animate=animation.Animation(duration=450,
            curve="decelerate"),
            on_hover=lambda e: _expand(e),
            padding=15,
            content=Column(
                alignment='start',
                spacing=10,
                controls=[
                    Row(
                        alignment='center',
                        controls=[
                            Text(
                                "Costel vs Andrei",
                                size=16,
                                width="w500",
                            )
                        ],
                    ),
                    Container(padding=padding.only(
                        bottom=5
                    )),
                    Row(
                        alignment='center',
                        spacing=30,
                        controls=[
                            Column(
                                controls=[
                                    Container(
                                        width=90,
                                        height=90,
                                        image_src="./assets/storm.png"
                                    ),
                                ],
                            ),
                            Column(
                                spacing=5,
                                horizontal_alignment='center',
                                controls=[
                                    Text(
                                        "Today",
                                        size=12,
                                        text_align='center',
                                    ),
                                    Row(
                                        vertical_alignment='start',
                                        spacing=0,
                                        controls=[
                                            Container(
                                                content=Text(
                                                    "-3",
                                                    size=52,
                                                ),
                                            )
                                        ]
                                    )
                                ]
                            ),
                        ],
                    )
                ],
            ),
        )
        return top

    # Contenedor principal
    _c = Container(
        width=310,
        height=660,
        border_radius=35,
        bgcolor='black',
        padding=10,
        content=Stack(width=300, height=550,
                      controls=[
                          _top(),
                      ],
                      ),
    )
    page.add(_c)
if __name__ == '__main__':
    flet.app(target=main, assets_dir='assets')