# SPDX-FileCopyrightText: Copyright (c) 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
"""
Simpletest demo for MacroPad. Prints the key pressed, the relative position of the rotary
encoder, and the state of the rotary encoder switch to the serial console.
"""
import time
from adafruit_macropad import MacroPad

macropad = MacroPad()
encoderValue = macropad.encoder
buttonValue = macropad.encoder_switch
brightness = 100

apps = ["Figma", "OnShape", "Numpad"]
currApp = "Figma"
macropad.display_image("sd/{}.bmp".format(currApp))
key = macropad.Keycode

figmaBindings = [
    (key.OPTION, key.EIGHT), (key.OPTION, key.NINE,), (key.SHIFT, key.A),
    (key.ENTER, ), (key.OPTION, key.W), (key.BACKSLASH, ),
    (key.OPTION, key.A), (key.OPTION, key.H), (key.OPTION, key.D),
    (key.COMMAND, key.FORWARD_SLASH), (key.OPTION, key.S), (key.COMMAND, )
]

colors = [
    (242,78,30), (225, 114, 98),
    (162, 89, 255), (26, 188, 254),
    (10, 207, 80), (255, 255, 255)
]

figmaColors = [
    colors[0], colors[0], colors[1],
    colors[2], colors[3], colors[2],
    colors[3], colors[3], colors[3],
    colors[4], colors[3], colors[4],
]

onShapeBindings = [
    (key.Q, ), (key.L, ), (key.R,),
    (key.C, ), (key.U, ), (key.M, ),
    (key.D, ), (key.SHIFT, key.L, ), (key.SHIFT, key.O ),
    (key.T, ), (key.E, ), (key.OPTION, key.C),
]

onShapeColors = [
    colors[5], colors[5], colors[5],
    colors[5], colors[5], colors[5],
    colors[3], colors[3], colors[3],
    colors[3], colors[3], colors[3],
]

numpadBindings = [
    (key.KEYPAD_SEVEN, ), (key.KEYPAD_EIGHT, ), (key.KEYPAD_NINE, ),
    (key.KEYPAD_FOUR, ), (key.KEYPAD_FIVE, ), (key.KEYPAD_SIX, ),
    (key.KEYPAD_ONE, ), (key.KEYPAD_TWO, ), (key.KEYPAD_THREE, ),
    (key.KEYPAD_ZERO, ), (key.KEYPAD_PERIOD, ), (key.KEYPAD_ENTER, ),
]

numPadColors = [
    colors[3], colors[3], colors[3],
    colors[3], colors[3], colors[3],
    colors[3], colors[3], colors[3],
    colors[3], colors[2], colors[4],
]

keyBindings = [
    figmaBindings,
    onShapeBindings,
    numpadBindings
]

colors = [
    figmaColors,
    onShapeColors,
    numPadColors
]

def runKey(key):
    print("{} {}".format(apps.index(currApp), key))
    print(keyBindings[apps.index(currApp)][key])
    macropad.keyboard.press(*keyBindings[apps.index(currApp)][key])

def updateApp():
    global currApp
    currApp = apps[encoderValue % len(apps)]
    for i in range(12):
        macropad.pixels[i] = tuple(value * (brightness / 255) for value in colors[apps.index(currApp)][i])
    macropad.display_image("sd/{}.bmp".format(currApp))

updateApp()

while True:
    lastEncoderValue = encoderValue
    lastEncoderButtonValue = buttonValue
    encoderValue = macropad.encoder
    buttonValue = macropad.encoder_switch
    
    key_event = macropad.keys.events.get()
    if key_event and key_event.pressed:
        runKey(key_event.key_number)
    if key_event and key_event.released:
        macropad.keyboard.release_all()

    if lastEncoderValue != encoderValue:
        updateApp()

    # displayText.show()
    time.sleep(0.1)
