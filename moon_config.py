def construct_svg(moon_data, day, size=150, light_color="rgb(255,255,210)", shade_color="black"):
    moon_phase_data = moon_data['phase'].get(str(day), {})
    svg_content = moon_phase_data.get("svg", "")
    
    path_start = svg_content.find('<path d="')
    path_start += len('<path d="') if path_start != -1 else 0
    path_end = svg_content.find('"', path_start)
    path_description = svg_content[path_start:path_end] if path_end != -1 else "M 50 1 A 49,49 0 1,0 49,99 A 40.18,49 0 0,1 50,1"

    svg_content = f"""
    <svg class="moon-svg" width="{size}" height="{size}" viewBox="0 0 100 100">
    <g>
        <circle cx="50" cy="50" r="49" stroke="none" fill="{shade_color}"/>
        <path d="{path_description}" stroke-width="0" stroke="none" fill="{light_color}" />
    </g>
    </svg>
    """
    
    return svg_content

def get_waning_value(moon_data, day):
    moon_phase_data = moon_data['phase'].get(str(day), {})
    phase_name = moon_phase_data.get('phaseName', '')
    np_widget_value = moon_phase_data.get('npWidget', '')

    if '(' in np_widget_value and ')' in np_widget_value:
        start = np_widget_value.find('(') + 1
        end = np_widget_value.find(')')
        percentage = np_widget_value[start:end]
    else:
        percentage = '' 

    waning_value = f"{phase_name} {percentage}" if percentage else phase_name
    
    return waning_value

def generate_html(svg_content):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Moon Phase</title>
        <style>
            #ex1 {{
                display: table;
                margin: 20px auto;
                text-align: center;
                color: black;
                padding: 5px 30px;
                background-color: white; /* Optional: set a background color if needed */
                box-shadow: none; /* Remove any shadow effect */
            }}
            .moon-svg {{
                filter: drop-shadow(0 0 25px rgb(0,50,50));
                padding: 15px 0;
            }}
        </style>
    </head>
    <body>
        <div id="ex1">
            {svg_content}
        </div>
    </body>
    </html>
    """
    
    return html_content

def save_html_to_file(html_content, drive_letter, filename="moon_phase.html"):
    file_path = f"{drive_letter}:/{filename}"
    with open(file_path, "w") as file:
        file.write(html_content)