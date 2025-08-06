class TextEditor:

    def __init__(self):
        self.left_stack = []
        self.right_stack = []

    def addText(self, text: str) -> None:
        for ch in text:
            self.left_stack.append(ch);

    def deleteText(self, k: int) -> int:
        deleted = 0
        while k > 0 and self.left_stack:
            self.left_stack.pop()
            deleted += 1
            k -= 1
        return deleted

    def cursorLeft(self, k: int) -> str:
        while k > 0 and self.left_stack:
            self.right_stack.append(self.left_stack.pop())
            k -= 1
        return ''.join(self.left_stack[-10:])

    def cursorRight(self, k: int) -> str:
        while k > 0 and self.right_stack:
            self.left_stack.append(self.right_stack.pop())
            k -= 1
        return ''.join(self.left_stack[-10:])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)