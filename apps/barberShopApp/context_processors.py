def add_variable_to_context(request):

    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    return {
        'user': user
    }