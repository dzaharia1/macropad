import time
from adafruit_macropad import MacroPad
import os

macropad = MacroPad()
encoderValue = macropad.encoder
buttonValue = macropad.encoder_switch

fullBrightness = 1
midBrightness = .25
lowBrightness = .1
brightness = fullBrightness
macropad.pixels.brightness = brightness

layers = ["Figma", 
        "Arc", 
        "OnShape",
        "Game", 
        "Numpad", 
        "off"]
currLayer = "Figma"
startingLayer = 0
macropad.display_image("sd/{}.bmp".format(currLayer))
key = macropad.Keycode

colors = [
    (242,45,40), (242,78,30),
    (162, 89, 255), (26, 188, 254),
    (10, 207, 80), (255, 255, 255),
    (0, 0, 0)
]

figmaBindings = [
    (key.OPTION, key.EIGHT), (key.OPTION, key.NINE,), (key.SHIFT, key.A),
    (key.ENTER, ), (key.OPTION, key.W), (key.BACKSLASH, ),
    (key.OPTION, key.A), (key.OPTION, key.H), (key.OPTION, key.D),
    (key.COMMAND, key.FORWARD_SLASH), (key.OPTION, key.S), (key.COMMAND, )
]

figmaColors = [
    colors[0], colors[0], colors[1],
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
    (key.SHIFT, ), (key.COMMAND, ), (key.SPACE, )
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
    colors[3], colors[3], colors[3],
    colors[3], colors[3], colors[3],
    colors[3], colors[3], colors[3],
    colors[3], colors[2], colors[4],
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
    colors[6], colors[6], colors[6],
]

keyBindings = [
    figmaBindings,
    arcBindings,
    onShapeBindings,
    gameBindings,
    numpadBindings,
    offBindings,
]

colors = [
    figmaColors,
    arcColors,
    onShapeColors,
    gameColors,
    numPadColors,
    offColors,
]

def runKey(key):
    print("{} {}".format(layers.index(currLayer), key))
    print(keyBindings[layers.index(currLayer)][key])
    macropad.keyboard.press(*keyBindings[layers.index(currLayer)][key])

def save_mode_to_file(mode):
    with open("/sd/layer.txt", "w") as file:
        file.write(mode)

def read_mode_from_file():
    global currLayer
    global startingLayer
    
    try:
        with open("/sd/layer.txt", "r") as file:
            currLayer = file.read().strip()
            startingLayer = layers.index(currLayer)
            print(startingLayer)
            updateLayer()
            return file.read().strip()
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

    save_mode_to_file(currLayer)

read_mode_from_file()
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
    if key_event and key_event.released:
        macropad.keyboard.release_all()

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




