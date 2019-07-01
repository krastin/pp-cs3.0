def convert_temperatures(t, source, target):
    celsius = 0.0
    #convert to celsius
    if source == "Kelvin":
        celsius = t - 273.15
    elif source == "Fahrenheit":
        celsius = (t - 32.0) * 5/9
    elif source == "Rankine":
        celsius = (t - 491.67) * 5/9
    elif source == "Delisle":
        celsius = 100 - (t * 5/9)
    elif source == "Newton":
        celsius = t * 100/33
    elif source == "Reaumur":
        celsius = t * 5/4
    elif source == "Romer":
        celsius = (t - 7.5) * 40/21
    else:
        celsius = t
    #now covert to $target
    if target == "Kelvin":
        return celsius + 273.15
    elif target == "Fahrenheit":
        return celsius * 9/5 + 32
    elif target == "Rankine":
        return (celsius + 273.15) * 9/5
    elif target == "Delisle":
        return (100 - celsius) * 3/2
    elif target == "Newton":
        return celsius * 33/100
    elif target == "Reaumur":
        return celsius * 4/5
    elif target == "Romer":
        return celsius * 21/40 + 7.5
    else:
        return celsius
    # adding another temperature scale would add 2 IFs