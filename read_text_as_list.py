def read_text_as_list (filename, seperator):

    import codecs
    
    text_file = codecs.open( filename, "r", "utf-8" )
    new_list = text_file.read().split(seperator)
    
    #text_file = open (filename, "r")
    #text_file.encode('utf-8', "ignore")
    #new_list = text_file.read().split(seperator)

    return new_list
