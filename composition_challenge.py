class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag= ""


class Head(Tag):

    def __init__(self):
        super().__init__('head', '')
        self._head_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._head_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._head_contents:
            self.contents = str(tag)

        super().display(file=file)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')  # body contents build up separately
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)


class HtmlDoc(object):

    def __init__(self, title=None):
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()

    def add_tag(self, name, contents):
        self._head.add_tag(name= 'title', contents='Demo HTML Document')
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    my_page = HtmlDoc('Demo HTML Document')
    my_page.add_tag('h1','main heading')
    my_page.add_tag('h2','sub-heading')
    my_page.add_tag('p', 'This is a paragraph that will appear on the page')
    # with open('test.html', 'w') as test_doc:
    my_page.display()
