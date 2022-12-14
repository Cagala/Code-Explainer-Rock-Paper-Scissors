# with hex = \033[{38:foreground, 48:background};2;{r};{g};{b}m
# \033[38;2;255;204;102m

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    IMORANGE = '\033[38;2;252;145;50m'
    STRINGG = '\033[38;2;93;219;50m'
    CODEGREY = '\u001b[38;5;244m'
    BOOLS = '\u001b[38;5;209m'
    OPERATORS = '\033[38;2;240;74;83m'
    YELLOW = '\u001b[38;5;220m'
    MODULES = '\033[38;2;247;197;57m'
    WARNING = '\033[38;2;240;240;26m'
    FAIL = '\u001b[38;5;1m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BG_GREEN = '\u001b[42;1m'
    BG_RED = '\u001b[41;1m'
    BG_GREY = '\u001b[48;5;240m'
    ENDBG = '\u001b[0m'
