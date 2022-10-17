def get_formatted_name(first, last, middle): #Gera um nome completo formatado de modo elegante.
    """ if(middle): """     
    full_name = '%s %s %s'%(first, middle, last)
    """ else:
        full_name = '%s %s'%(first, last) """
    return full_name.title()