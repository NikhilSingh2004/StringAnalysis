from django.shortcuts import render

def Home(request):
    '''
        The Home function is the only and main functin that handles all the requests.
        If request is POST then the action variable is checked for certain values, values are the type of action to be prtformed ont the text.
        For instance if the value of the action is count, the if condition of with count will be executed, result will be again populated to the index.html.
        The DTL in index.html is then responsible to dynamically display the content.
    '''

    if request.method == "POST":
        try:
            text = request.POST.get('textarea')

            action = request.POST.get('action')

            # Condition for Count value of action
            if action == 'count':
                total_char = sum(1 for char in text if char != ' ')
                return render(request, 'core/index.html', {'count': total_char})

            # Condition for Reverse value of action
            elif action == 'reverse':
                reversed_text = text[::-1]
                return render(request, 'core/index.html', {'reverse': reversed_text})
            
            # Condition for Count Words value of action
            elif action == 'words':
                word_list = text.split()
                return render(request, 'core/index.html', {'words': len(word_list), 'words_count': word_list})
            
            # Condition for Upper Case value of action
            elif action == 'upper':
                upper_text = text.upper()
                return render(request, 'core/index.html', {'upper': upper_text})
            
            # Condition for Lower Case value of action
            elif action == 'lower':
                lower_text = text.lower()
                return render(request, 'core/index.html', {'lower': lower_text})

        except Exception as e:
            print(e.__str__())

    return render(request, 'core/index.html')
