import inspect
from objprint import op

def print_current_frame():
    frame = inspect.currentframe()
    op(frame, honor_existing=False, depth=2)
    print("===== Last Instruction =====")
    print(frame.f_lasti, end="\n\n")       # Last instruction

    print("===== Current Line Number =====")
    print(frame.f_lineno, end="\n\n")      # Current line number

    print("===== Local Variables =====")
    print(frame.f_locals, end="\n\n")      # Local variables

    print("===== Code Object =====")
    print(frame.f_code, end="\n\n")        # Code object

    print("===== Previous Frame =====")
    print(frame.f_back, end="\n\n")        # Previous frame

    print("===== Built-in Namespace =====")
    print(frame.f_builtins, end="\n\n")    # Built-in namespace

    print("===== Global Namespace =====")
    print(frame.f_globals, end="\n\n")     # Global namespace

def called_by_who():
    frame = inspect.currentframe()
    print("===== Caller File Name =====")
    print(frame.f_back.f_code.co_filename, end="\n\n")

    print("===== Caller Function Name =====")
    print(frame.f_back.f_code.co_name, end="\n\n")

    print("===== Caller Line Number =====")
    print(frame.f_back.f_lineno, end="\n\n")

def caller():
    called_by_who()

if __name__ == "__main__":
    print_current_frame()
    caller()