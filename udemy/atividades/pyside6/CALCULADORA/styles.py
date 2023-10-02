import qdarktheme
from padroes import PRIMARY_COLOR,DARKER_PRIMARY_COLOR,DARKEST_PRIMARY_COLOR


qss = f"""
    PushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}"""#obs : ele esta usando dockstring com f strig , so da certo isso qudno tem chame dentro de chave , que é o caso.





def setupthema():
    qdarktheme.setup_theme(       
        theme='dark',
        corner_shape='rounded',
        custom_colors={
            "[dark]": {
                "primary": f"{PRIMARY_COLOR}",
            },
            "[light]": {
                "primary": f"{PRIMARY_COLOR}",
            },
        },
        additional_qss=qss
    )