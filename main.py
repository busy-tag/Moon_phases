from api_operations import load_moon_phases
from moon_config import construct_svg, generate_html, save_html_to_file, get_waning_value
from image_operations import convert_html_to_png, crop_image, place_image_center, add_text_to_image
from utility_operations import get_user_or_system_date, get_drive_letter
from datetime import datetime

def get_system_date(input_date):
    day_of_week = input_date.strftime("%A")
    date_str = input_date.strftime("%d %B %Y")
    return day_of_week, date_str

def main():
    drive_letter = get_drive_letter()
    input_date = get_user_or_system_date()
    today = input_date 
    current_month = today.month
    current_year = today.year
    current_day = today.day

    config_moon = {
        'lang': 'en',
        'month': current_month,  
        'year': current_year,   
        'size': 150,
        'lightColor': "rgb(255,255,210)",
        'shadeColor': "black",
        'texturize': False,
    }

    moon_data = load_moon_phases(config_moon)
    svg_content = construct_svg(
        moon_data,
        day=current_day,
        size=config_moon['size'],
        light_color=config_moon['lightColor'],
        shade_color=config_moon['shadeColor']
    )
    html_content = generate_html(svg_content)
    save_html_to_file(html_content, drive_letter)
    convert_html_to_png(drive_letter)

    crop_image(drive_letter)
    
    background_size = (240, 280)
    final_image_path = 'moon_phase.png'
    overlay_path = 'moon_phase.png'
    desired_width = 180
    place_image_center(drive_letter, background_size, overlay_path, final_image_path, desired_width)
    
    day_of_week, date_str = get_system_date(input_date)
    waning_value = get_waning_value(moon_data, day=current_day)

    font_path = "MontserratBlack-3zOvZ.ttf" 
    add_text_to_image(drive_letter, final_image_path, "moon_phase.png", waning_value, day_of_week, date_str, font_path)

    print("Process completed successfully.")

if __name__ == "__main__":
    main()