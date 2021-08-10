import datetime

# Store the next available id for all new notes
last_id = 0


class Note:
    """Represent a note in the notebook. Match against a
    string in searches and store tags for each note."""

    def __init__(self, memo, tags=""):
        """initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags."""
        return filter in self.memo or filter in self.tags


class Notebook:
    """Represent a collection of notes that can be tagged,
    modified, and searched."""

    def __init__(self):
        """Initialize a notebook with an empty list."""
        self.notes = []

    def new_note(self, memo, tags=""):
        """Create a new note and add it to the list."""
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """Locate the note with the given id."""
        for note in self.notes:
            if note.id == int(note_id):
                return note

    def modify_memo(self, note_id, memo):
        """Find the note with the given id and change its
        memo to the given value."""
        n = self._find_note(note_id)
        if n:
            n.memo = memo

    def modify_tags(self, note_id, tags):
        """Find the note with the given id and change its
        tags to the given value."""
        n = self._find_note(note_id)
        if n:
            n.tags = tags

    def search(self, filter):
        """Find all notes that match the given filter
        string."""
        return [note for note in self.notes if note.match(filter)]


def main():
    n1 = Note("hello first")
    n2 = Note('Hello again', 'hi')
    print(n1.id, n1.memo)
    print(n2.id, n2.memo)
    print(n1.match('hello'))
    print(n2.match("hi"))

    book = Notebook()
    book.new_note('first memo', 'tag1')
    book.new_note('second memo', "tag2")
    book.new_note('third memo', 'tag3')
    book.new_note('fourth memo', 'tag4')
    print(book.notes[0].memo)
    # print(lambda i: i.memo in book.search("memo"))
    # print(n3)

    book.modify_memo(4, 'modified!')
    for n in book.notes:
        print(n.tags)


if __name__ == '__main__':
    main()
