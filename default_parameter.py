def greet4(first_name="John", last_name="Doe"):
    """
    Greet again
    :param first_name: first name of the person, default=John
    :param last_name: last_name, default=Doe
    :return: None
    """
    print(f"Hello {first_name} {last_name}, this is pretty cool, right?")


greet4("Lucas", "Baptiste")
greet4()  # returns default
greet4("James")  # returns default last_name
greet4(last_name="Jordan")  # returns default first name

greet4("Michael", "Jordan")
greet4(last_name="Jordan", first_name="Michael")  # to alter position of the parameters by specifying it