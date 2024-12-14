import time
from adafruit_macropad import MacroPad
import os
import json

macropad = MacroPad()
encoderValue = macropad.encoder
buttonValue = macropad.encoder_switch

fullBrightness = 1
midBrightness = .4
lowBrightness = .1
brightness = fullBrightness
macropad.pixels.brightness = brightness

key = macropad.Keycode
print(dir(key))

colors = [
    (242,45,40), (242,78,30),
    (162, 89, 255), (26, 188, 254),
    (10, 207, 80), (255, 255, 255),
    (0, 0, 0)
]

figmaBindings = [
    (key.SHIFT, key.A), (key.OPTION, key.EIGHT), (key.OPTION, key.NINE,),
    (key.COMMAND, key.SHIFT, key.R ), (key.OPTION, key.W), (key.BACKSLASH, ),
    (key.OPTION, key.A), (key.OPTION, key.H, key.V), (key.OPTION, key.D),
    (key.COMMAND, key.OPTION, key.C), (key.OPTION, key.S), (key.COMMAND, key.OPTION, key.V)
]

figmaColors = [
    colors[1], colors[0], colors[0],
    colors[2], colors[3], colors[2],
    colors[3], colors[3], colors[3],
    colors[4], colors[3], colors[4],
]

onShapeBindings = [
    (key.Q, ), (key.L, ), (key.G,),
    (key.C, ), (key.U, ), (key.O, ),
    (key.D, ), (key.SHIFT, key.O, ), (key.T, ),
    (key.E, ), (key.I, ), (key.ESCAPE, ),
]

onShapeColors = [
    colors[4], colors[4], colors[4],
    colors[4], colors[4], colors[4],
    colors[3], colors[3], colors[3],
    colors[3], colors[3], colors[0],
]

arcBindings = [
    (key.CONTROL, key.ONE), (key.CONTROL, key.TWO), (key.CONTROL, key.THREE),
    (key.CONTROL, key.FOUR), (key.CONTROL, key.FIVE), (key.CONTROL, key.SIX),
    (key.COMMAND, key.SHIFT, key.C), (key.COMMAND, key.S), (key.CONTROL, key.TAB),
    (key.COMMAND, key.N ), (key.COMMAND, key.W), (key.COMMAND, key.T)
]

arcColors = [
    colors[2], colors[2], colors[2],
    colors[2], colors[2], colors[2],
    colors[3], colors[3], colors[3],
    colors[4], colors[0], colors[4],
]

gameBindings = [
    (key.TAB, ), (key.ONE, ), (key.TWO, ),
    (key.Q, ), (key.W, ), (key.E, ),
    (key.A, ), (key.S, ), (key.D, ),
    (key.SHIFT, ), (key.OPTION, ), (key.SPACE, )
]

gameColors = [
    colors[4], colors[4], colors[4], 
    colors[2], colors[3], colors[2],
    colors[3], colors[3], colors[3],
    colors[0], colors[0], colors[1],
]

numpadBindings = [
    (key.KEYPAD_ONE, ), (key.KEYPAD_TWO, ), (key.KEYPAD_THREE, ),
    (key.KEYPAD_FOUR, ), (key.KEYPAD_FIVE, ), (key.KEYPAD_SIX, ),
    (key.KEYPAD_SEVEN, ), (key.KEYPAD_EIGHT, ), (key.KEYPAD_NINE, ),
    (key.KEYPAD_ZERO, ), (key.KEYPAD_PERIOD, ), (key.KEYPAD_ENTER, ),
]

numPadColors = [
    colors[4], colors[4], colors[4],
    colors[4], colors[4], colors[4],
    colors[4], colors[4], colors[4],
    colors[4], colors[0], colors[1],
]

clipBoardBindings = [
    (key.COMMAND, key.V), (key.COMMAND, ), (key.COMMAND, ),
]

offBindings = [
    (key.SHIFT, ), (key.SHIFT, ), (key.SHIFT, ),
    (key.SHIFT, ), (key.SHIFT, ), (key.SHIFT, ),
    (key.SHIFT, ), (key.SHIFT, ), (key.SHIFT, ),
    (key.SHIFT, ), (key.SHIFT, ), (key.SHIFT, ),
]

offColors = [
    colors[6], colors[6], colors[6],
    colors[6], colors[6], colors[6],
    colors[6], colors[6], colors[6],
    colors[6], colors[3], colors[1],
]

clipboardColors = [
    colors[0], colors[0], colors[0],
    colors[4], colors[4], colors[4],
    colors[4], colors[4], colors[4],
    colors[4], colors[4], colors[4],
]

layers = [
        "OnShape",
        "Arc", 
        "Clipboard",
        "Figma", 
        "Numpad", 
        "off"]
currLayer = "Clipboard"
startingLayer = 0
macropad.display_image("sd/{}.bmp".format(currLayer))

keyBindings = [
    onShapeBindings,
    arcBindings,
    [],
    figmaBindings,
    numpadBindings,
    offBindings,
]

colors = [
    onShapeColors,
    arcColors,
    clipboardColors,
    figmaColors,
    numPadColors,
    offColors,
]

def runKey(keyIndex):
    if currLayer == "Clipboard":
        runClipBoard(keyIndex)
    else:
        macropad.keyboard.press(*keyBindings[layers.index(currLayer)][keyIndex])

def release(keyIndex):
    macropad.keyboard.release(*keyBindings[layers.index(currLayer)][keyIndex])

def runClipBoard(keyIndex):
    easeDuration = 0.1
    macropad.keyboard.send(*(key.COMMAND, key.C))
    time.sleep(easeDuration)

    if keyIndex == 0:
        macropad.keyboard.send(*(key.COMMAND, key.SHIFT, key.V))
        time.sleep(easeDuration)
        macropad.keyboard.send(*(key.SHIFT, key.ENTER))
    if keyIndex == 1:
        macropad.keyboard.send(*(key.COMMAND, key.V))
    if keyIndex == 2:
        macropad.keyboard.send(*(key.COMMAND, key.SHIFT, key.V))
    if keyIndex == 3:
        macropad.keyboard.send(*(key.LEFT_BRACKET, ))
        macropad.keyboard.send(*(key.COMMAND, key.V))
        time.sleep(easeDuration)
        macropad.keyboard.send(*(key.RIGHT_BRACKET, ))
    if keyIndex == 4:
        macropad.keyboard.send(*(key.SHIFT, key.NINE, ))
        macropad.keyboard.send(*(key.COMMAND, key.V))
        time.sleep(easeDuration)
        macropad.keyboard.send(*(key.SHIFT, key.ZERO, ))
    if keyIndex == 5:
        macropad.keyboard.send(*(key.SHIFT, key.LEFT_BRACKET, ))
        macropad.keyboard.send(*(key.COMMAND, key.V))
        time.sleep(easeDuration)
        macropad.keyboard.send(*(key.SHIFT, key.RIGHT_BRACKET, ))
    if keyIndex == 6:
        macropad.keyboard.send(*(key.SHIFT, key.QUOTE))
        macropad.keyboard.send(*(key.COMMAND, key.V))
        time.sleep(easeDuration)
        macropad.keyboard.send(*(key.SHIFT, key.QUOTE))
    if keyIndex == 7:
        macropad.keyboard.send(*(key.QUOTE, ))
        macropad.keyboard.send(*(key.COMMAND, key.V))
        time.sleep(easeDuration)
        macropad.keyboard.send(*(key.QUOTE, ))
    if keyIndex == 8:
        macropad.keyboard_layout.write("`")
        macropad.keyboard.send(*(key.COMMAND, key.V))
        time.sleep(easeDuration)
        macropad.keyboard_layout.write("`")
    if keyIndex == 9:
        macropad.keyboard.send(*(key.SHIFT, key.EIGHT))
        macropad.keyboard.send(*(key.COMMAND, key.V))
        time.sleep(easeDuration)
        macropad.keyboard.send(*(key.SHIFT, key.EIGHT))
    if keyIndex == 10:
        macropad.keyboard.send(*(key.SHIFT, key.EIGHT))
        macropad.keyboard.send(*(key.SHIFT, key.EIGHT))
        macropad.keyboard.send(*(key.COMMAND, key.V))
        time.sleep(easeDuration)
        macropad.keyboard.send(*(key.SHIFT, key.EIGHT))
        macropad.keyboard.send(*(key.SHIFT, key.EIGHT))
    if keyIndex == 11:
        macropad.keyboard_layout.write("```")
        macropad.keyboard.send(*(key.RETURN, ))
        macropad.keyboard.send(*(key.COMMAND, key.V))
        time.sleep(easeDuration)
        macropad.keyboard.send(*(key.RETURN, ))
        macropad.keyboard_layout.write("```")

def save_settings_to_file():
    global currLayer
    global brightness

    settings = {
        "layer": currLayer,
        "brightness": brightness
    }
    
    with open("/sd/layer.txt", "w") as file:
        json.dump(settings, file)

def read_settings_from_file():
    global currLayer
    global startingLayer
    global brightness
    
    try:
        with open("/sd/layer.txt", "r") as file:
            settings = json.load(file)
            currLayer = settings["layer"]
            brightness = settings["brightness"]
            startingLayer = layers.index(currLayer)
            print(startingLayer)
            print(brightness)
            updateLayer()
            return settings
    except:
        print("File not found")
        return None
    
def updateLayer():
    global currLayer
    for i in range(12):
        # macropad.pixels[i] = tuple(value * (brightness / 255) for value in colors[layers.index(currLayer)][i])
        macropad.pixels[i] = colors[layers.index(currLayer)][i]
    if currLayer == "off":
        macropad.pixels.brightness = 0
        macropad.display_sleep = True
    else:
        macropad.display_sleep = False
        macropad.pixels.brightness = brightness
        macropad.display_image("sd/{}.bmp".format(currLayer))

    save_settings_to_file()

read_settings_from_file()
# time.sleep(.2)
# print(currLayer)
# updateLayer()

while True:
    lastEncoderValue = encoderValue
    lastEncoderButtonValue = buttonValue
    encoderValue = macropad.encoder
    buttonValue = macropad.encoder_switch
    
    key_event = macropad.keys.events.get()
    if key_event and key_event.pressed and currLayer != "off":
        runKey(key_event.key_number)
    if key_event and key_event.released and currLayer != "Clipboard":
        release(key_event.key_number)

    if lastEncoderValue != encoderValue:
        currLayer = layers[(encoderValue + startingLayer) % len(layers)]
        updateLayer()
    
    if lastEncoderButtonValue != buttonValue and buttonValue:
        if brightness == fullBrightness:
            brightness = midBrightness
        elif brightness == midBrightness:
            brightness = lowBrightness
        else:
            brightness = fullBrightness
        updateLayer()
            

    # displayText.show()
    time.sleep(0.1)




