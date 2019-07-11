import temperature_program

def get_preheating_instructions(fahrenheit: float) -> str:
    """Return instructions for preheating oven in F degrees and C degrees

    >>> get_preheating_instructions(500)
    'Preheat oven to 500 degrees F (260.0 degrees C).'
    """

    cels = str(temperature_program.convert_to_celsius(fahrenheit))
    fahr = str(fahrenheit)
    return 'Preheat oven to ' + fahr + ' degrees F (' + cels + ' degrees C).'

fahr = float(input("Enter baking temperature in F degrees: "))
print(get_preheating_instructions(fahr))
