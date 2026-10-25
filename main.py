import os
import sys
import webview

def main():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    html_path = os.path.join(base_path, 'index.html')
    webview.create_window('MPC-HC Media Player', html_path, width=980, height=640)
    webview.start()

if __name__ == '__main__':
    main()