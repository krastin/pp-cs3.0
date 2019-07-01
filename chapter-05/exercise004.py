light = 0.001
temperature = 1

if (light < 0.01) or (temperature > 0.0):
    if not ((light < 0.01) and (temperature > 0.0)):
        print("turn_camera_on() - my function")
# this was indeed a XOR and can be more easily written as:
if (light < 0.01) != (temperature > 0.0):
    print("turn_camera_on() - friend function")