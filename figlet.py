import sys
import pyfiglet
from pyfiglet import Figlet

figlet = Figlet()

figlet.getFonts()

figlet.setFont(font=figlet.getFonts()[0])


def main():
    if len(sys.argv) == 1:
        str = input("Input: ")
        figlet = pyfiglet.Figlet()
        print(figlet.renderText(str))
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font = sys.argv[2]
        figlet = pyfiglet.Figlet(font=font)
        str = input("Input: ")
        print(figlet.renderText(str))
    else:
        sys.exit("Invalid usage")

if __name__ == "__main__":
    main()