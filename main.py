import os
"""
---  This is for MacOS ---
"""


# if __name__ == '__main__':
#     print("Welcome to RoboSpeaker created by Dev")
#     while True:
#         x = input("Enter what you want me to speak")
#         if x == "q":
#             os.system("say 'bye bye friend'")
#             break
#         command = f"say {x}"
#         os.system(command)

"""
---  This is for Windows ---
"""

if __name__ == '__main__':
    print("Welcome to RoboSpeaker created by Dev")
    while True:
        x = input("Enter what you want me to speak")
        if x == "q":
            os.system("PowerShell -Command \"Add-Type –AssemblyName System.Speech; "
                      "(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('bye bye friend')\"")
            break
        command = f"PowerShell -Command \"Add-Type –AssemblyName System.Speech; " \
                  f"(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')\""
        os.system(command)
