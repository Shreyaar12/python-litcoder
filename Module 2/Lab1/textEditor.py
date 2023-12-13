class CustomStack:
    def __init__(self):
        self.text = ""
        self.history = []

    def insert(self, value):
        self.history.append((1, self.text[-len(value):]))  # Save the part of the text to be deleted for undo
        self.text += value

    def delete(self, value):
        value = int(value)
        deleted = self.text[-value:]
        self.history.append((2, deleted))  # Save the deleted text for undo
        self.text = self.text[:-value]

    def get(self, value):
        value = int(value) - 1  # Convert to zero-based index
        if 0 <= value < len(self.text):
            return self.text[value]
        return ""

    def undo(self):
        if self.history:
            command, value = self.history.pop()
            if command == 1:  # Insert operation was done, need to delete
                self.text = self.text[:-len(value)]
            elif command == 2:  # Delete operation was done, need to insert
                self.text += value

def text_editor(commands):
    editor = CustomStack()
    output = []

    for command in commands:
        cmd, value = command.split()
        if cmd == '1':
            editor.insert(value)
        elif cmd == '2':
            editor.delete(value)
        elif cmd == '3':
            output.append(editor.get(value))
        elif cmd == '4':
            editor.undo()

    return output

# User input handling
if __name__ == "__main__":
    commands_input = input("Enter commands, separated by commas: ").split(',')
    result = text_editor(commands_input)
    print("\n".join(result))

