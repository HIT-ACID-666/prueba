from colorama import Fore, init
init()


# Terminal color definitions

class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE   = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

class bg:
    BLACK   = '\033[40m'
    RED     = '\033[41m'
    GREEN   = '\033[42m'
    YELLOW  = '\033[43m'
    BLUE    = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN    = '\033[46m'
    WHITE   = '\033[47m'
    RESET   = '\033[49m'

class style:
    BRIGHT    = '\033[1m'
    DIM       = '\033[2m'
    NORMAL    = '\033[22m'
    RESET_ALL = '\033[0m'
    
    
   
# portada

print(f"""
\033[32m┏━┳┳┳━┳┳┓
\033[32m┃━┫┃┃┏┫━┫┏┓ \033[31m [ 1 ] RECOLECTING INFO OF IP 
\033[32m┃┏┫┃┃┗┫┃┃┃┃ \033[31m [ 2 ] PHISHING NGROK
\033[32m┗┛┗━┻━┻┻┛┃┃
\033[32m┏┳┳━┳┳┳┓┏┫┣┳┓   \033[30m @hit_acid666
\033[32m┃┃┃┃┃┃┃┃┣┻┫┃┃
\033[32m┣┓┃┃┃┃┣┫┃┏┻┻┫
\033[32m┗━┻━┻━┻""")
