from enum import Enum

class ColorType(Enum):
    Black = 0x000000
    Brown = 0x002AA5
    Dark_Olive_Green = 0x404000
    Dark_Green = 0x005500
    Dark_Teal = 0x5E0000
    Dark_Blue = 0x8B0000
    Indigo = 0x82004B
    Dark_Grey = 0x282828

    Dark_Red = 0x00008B
    Orange = 0x2068FF
    Dark_Yellow = 0x008B8B
    Green = 0x009300
    Teal = 0x8E8E38
    Blue = 0xFF0000
    Blue_Grey = 0xC07B7B
    Grey_40 = 0x666666

    Red = 0x0000FF
    Light_Orange = 0x5BADFF
    Lime = 0x32CD32
    Sea_Green = 0x71B33C
    Aqua = 0xD4FF7F
    Light_Blue = 0xC09E7D
    Violet = 0x800080
    Grey_50 = 0x7F7F7F

    Pink = 0xCBC0FF
    Gold = 0x00D7FF
    Yellow = 0x00FFFF
    Bright_Green = 0x00FF00
    Turquoise = 0xD0E040
    Skyblue = 0xFFFFC0
    Plum = 0x480048
    Light_Grey = 0xC0C0C0

    Rose = 0xE1E4FF
    Tan = 0x8CB4D2
    Light_Yellow = 0xE0FFFF
    Pale_Green = 0x98FB98
    Pale_Turquoise = 0xEEEEAF
    Pale_Blue = 0x8B8368
    Lavender = 0xFAE6E6
    White = 0xFFFFFF
    
class ColorPicker():
    def getRGBFromColor(color: int):
        """
        Returns the RGB representation of a color from its int value

        Parameters:
            color (int) : int representing the color

        Returns: 
            tuple containing red, green and blue values of the color. Each of red, green and blue are between 0 and 255 inclusive
                    
        """
        # Internally MSFT COLORREF stores the byte ordering of RGB Color as BGR: 0x00bbggrr
        blue = (color >> 16) & 0xFF
        green = (color >> 8) & 0xFF
        red = color & 0xFF

        return (red, green, blue)
    
    def getColorFromRGB(red: int, green: int, blue: int):
        """
        Returns the int representation of a color from its R, G, B values
        
        Parameters:
                red (int) : int representing red value of the color. Must be between 0 and 255 inclusive
                green (int) : int representing green value of the color. Must be between 0 and 255 inclusive
                blue (int) : int representing blue value of the color. Must be between 0 and 255 inclusive

            Returns: int representation of color formed combining rgb values
        """
        if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
                raise ValueError("Red, Green, and Blue values must be between 0 and 255, inclusive")
        
        # Internally MSFT COLORREF stores the byte ordering of RGB Color as BGR: 0x00bbggrr
        return (blue << 16) | (green << 8) | red
    
    def _setColorValidation(*args):
        if len(args) == 1:
            color_input = args[0]

            if isinstance(color_input, str):
                # Hex string case
                hex_color = color_input.lstrip('#')
                if len(hex_color) not in (6, 8):
                    raise ValueError("Hex string must be 6 or 8 characters long.")
                red = int(hex_color[0:2], 16)
                green = int(hex_color[2:4], 16)
                blue = int(hex_color[4:6], 16)
                alpha = int(hex_color[6:8], 16) if len(hex_color) == 8 else 255

            elif isinstance(color_input, ColorType):
                red, green, blue = ColorPicker.getRGBFromColor(color_input.value)
                alpha = 255

            elif isinstance(color_input, int):
                red, green, blue = ColorPicker.getRGBFromColor(color_input)
                alpha = 255

            else:
                raise ValueError("Unsupported single-argument input type.")

        elif 3 <= len(args) <= 4 and all(isinstance(a, int) for a in args):
            red, green, blue = args[0], args[1], args[2]
            alpha = args[3] if len(args) == 4 else 255

        else:
            raise ValueError("Invalid arguments. Provide RGB[A] ints, hex string, ColorType, or int.")

        # Validate
        for value, name in zip((red, green, blue, alpha), ['R', 'G', 'B', 'A']):
            if not (0 <= value <= 255):
                raise ValueError(f"{name} value must be between 0 and 255.")
            
        color_bytes = bytes([red, green, blue, alpha])
        return color_bytes