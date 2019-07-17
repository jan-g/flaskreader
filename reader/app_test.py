from textwrap import dedent
from reader.app import highlight_phrases, replace_single_phrase


def test_first():
    # This is my first test
    words = [('find me', 'replacement'),
             ('and adjust me too', 'replacement'),
             ]

    text = dedent("""
    Line one
    
    line two and three and find me maybe and also
    and adjust me too and find me also
    """)

    expected = dedent("""
    Line one
    
    line two and three and <b>find me</b> maybe and also
    <b>and adjust me too</b> and <b>find me</b> also
    """)

    output = highlight_phrases(text, words)
    assert expected == output


def test_line_wrap():
    # This is my first test
    words = [('find me', 'replacement'),
             ]

    text = dedent("""
    I would like you to find
    me wrapped text
    """)

    expected = dedent("""
    I would like you to <b>find
    me</b> wrapped text
    """)

    output = highlight_phrases(text, words)
    assert expected == output


def test_single_highlight():
    orig = "some text to find and replace on and find another and find one more"
    phrase = "find"
    expected = "some text to <b>find</b> and replace on and <b>find</b> another and <b>find</b> one more"

    assert expected == replace_single_phrase(orig, phrase)