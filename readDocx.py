#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import docx

def getText(filename):
    """TODO: Docstring for getText.

    :filename: TODO
    :returns: TODO

    """
    doc = docx.Document(filename)
    fullText = []

    for para in doc.paragraphs:
        fullText.append(para.text)

    return '\n'.join(fullText)

