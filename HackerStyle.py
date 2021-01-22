import webbrowser
import termcolor
import pyfiglet

# print(dir(pyfiglet))
print(termcolor.colored(pyfiglet.figlet_format("Soon Ahmed"), color='green'))
# import pyfiglet module
result = termcolor.colored(pyfiglet.figlet_format("Geeks", font="isometric1"), color='red')
print(result)




###---- power by 
url = 'https://github.com/AhmedAlamoudi7'

# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

webbrowser.get(chrome_path).open(url)
