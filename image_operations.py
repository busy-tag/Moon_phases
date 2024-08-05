from PIL import Image, ImageDraw, ImageFont
from html2image import Html2Image

def convert_html_to_png(drive_letter, html_file="moon_phase.html", png_file="moon_phase.png"):
    html_file_path = f"{drive_letter}:/{html_file}"    
    output_directory = f"{drive_letter}:/"
    hti = Html2Image(output_path=output_directory)
    hti.screenshot(html_file=html_file_path, save_as=png_file)

def crop_image(drive_letter, image_path="moon_phase.png", output_path='moon_phase.png', left_margin=854, upper_margin=20, right_margin=854, lower_margin=864):
    input_path = f"{drive_letter}:/{image_path}"
    output_path = f"{drive_letter}:/{output_path}"
    with Image.open(input_path) as img:
        img_width, img_height = img.size

        left = left_margin
        upper = upper_margin
        right = img_width - right_margin
        lower = img_height - lower_margin
        
        left = max(left, 0)
        upper = max(upper, 0)
        right = min(right, img_width)
        lower = min(lower, img_height)
        
        cropped_img = img.crop((left, upper, right, lower))
        cropped_img.save(output_path)

def configure_overlay(drive_letter, overlay_path, desired_width):
    overlay_path = f"{drive_letter}:/{overlay_path}"
    overlay = Image.open(overlay_path)
    
    if overlay.mode != 'RGBA':
        overlay = overlay.convert('RGBA')
    
    original_width, original_height = overlay.size
    aspect_ratio = original_height / original_width
    desired_height = int(desired_width * aspect_ratio)
    
    overlay = overlay.resize((desired_width, desired_height), Image.LANCZOS)
    
    return overlay

def place_image_center(drive_letter, background_size, overlay_path, output_path, desired_width):
    overlay = configure_overlay(drive_letter, overlay_path, desired_width)
    output_path = f"{drive_letter}:/{output_path}"
    background = Image.new('RGBA', background_size, (255, 255, 255, 255))
    overlay_width, overlay_height = overlay.size
    bg_width, bg_height = background_size
    
    x = (bg_width - overlay_width) // 2
    y = (bg_height - overlay_height) // 2
    
    background.paste(overlay, (x, y), overlay)
    
    background.save(output_path)

def add_text_to_image(drive_letter, image_path, output_path, waning_value, day_of_week, date, font_path="MontserratBlack-3zOvZ.ttf"):
    image_path = f"{drive_letter}:/{image_path}"
    output_path = f"{drive_letter}:/{output_path}"
    font_path = f"{drive_letter}:/{font_path}"
    with Image.open(image_path) as img:
        draw = ImageDraw.Draw(img)
        
        try:
            font = ImageFont.truetype(font_path, 20)
        except IOError:
            print(f"Font file '{font_path}' not found. Using default font.")
            font = ImageFont.load_default()

        image_width, image_height = img.size
        
        def get_text_size(text, font):
            bbox = draw.textbbox((0, 0), text, font=font)
            return bbox[2] - bbox[0], bbox[3] - bbox[1] 

        text_y_day = (image_height // 2) -130
        text_y_date = (image_height // 2)  -105
        text_y_waning = (image_height // 2) + 80

        day_size = get_text_size(day_of_week, font)
        date_size = get_text_size(date, font)
        draw.text(((image_width - day_size[0]) / 2, text_y_day), day_of_week, font=font, fill="black")
        draw.text(((image_width - date_size[0]) / 2, text_y_date), date, font=font, fill="black")
        
        waning_size = get_text_size(f"{waning_value}", font)
        draw.text(((image_width - waning_size[0]) / 2, text_y_waning), f"{waning_value}", font=font, fill="black")
        
        img.save(output_path)