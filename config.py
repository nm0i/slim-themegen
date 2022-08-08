bg_color: str = "#191919"
ipt_color: str = "#2f2f2f"

font_name: str = "Terminus"
font_size: int = 16

panel_size: int = 256
input_height: int = 36
input_margin: int = 16

input_x_offset: int = 8
input_y_offset: int = 4


SLIM_THEMEFILE: str = """
msg_color               #ffffff
msg_font                {font_name}:{font_size}:bold
msg_x                   20
msg_y                   20

# valid values: stretch, tile, center
background_style        tile

# Login Name
username_color		#ffffff

password_x		50%
password_y		88%

username_x		50%
username_y		88%
username_font           {font_name}:{font_size}:bold

username_msg		Login
password_msg		Password

# Input controls
input_font          	{font_name}:{font_size}
input_panel_x           50%
input_panel_y           50%

input_name_x            {input_x}
input_name_y            {input_y}
input_pass_x            {input_x}
input_pass_y            {input_y}

input_color		#eaeaea"""
