class MyFile:
    def __init__(self, filename, mode, encoding='utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, mode=self.mode, encoding=self.encoding)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with MyFile('text.txt', 'w') as f:
    f.write('Hello Maximum!')

with MyFile('text.txt', 'r') as f:
    print(f.read())