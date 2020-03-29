new_name=''
def fun(name):

    if len(name)>3:
        return name[:3].capitalize() + name[3:].capitalize()

    else:
        return 'name is too short'
