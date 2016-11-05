def read_text_as_item (filename) :

    import codecs
    
    text_file = codecs.open( filename, "r", "utf-8" )
    new_item = text_file.read()

    return new_item
