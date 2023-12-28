from django.shortcuts import render

# def Home(request):
#     if request.method == "POST":
#         try:
#             print('1')
#             text = request.POST.get('textarea')
#             print(text)

#             cnt = request.POST.get('cnt')
#             rev = request.POST.get('rev')
#             wrd = request.POST.get('wrd')

#             if cnt == 'count':
#                 total_char = sum(1 for char in text if char != ' ')
#                 return render(request, 'core/index.html', {'count': total_char})

#             elif rev == 'reverse':
#                 reversed_text = text[::-1]
#                 return render(request, 'core/index.html', {'reverse': reversed_text})
            
#             elif wrd == 'words':
#                 word_list = text.split()
#                 return render(request, 'core/index.html', {'words': len(word_list), 'words_count': word_list})

#         except Exception as e:
#             print(e.__str__())

#     return render(request, 'core/index.html')

def Home(request):
    if request.method == "POST":
        try:
            text = request.POST.get('textarea')

            action = request.POST.get('action')

            if action == 'count':
                total_char = sum(1 for char in text if char != ' ')
                return render(request, 'core/index.html', {'count': total_char})

            elif action == 'reverse':
                reversed_text = text[::-1]
                return render(request, 'core/index.html', {'reverse': reversed_text})
            
            elif action == 'words':
                word_list = text.split()
                return render(request, 'core/index.html', {'words': len(word_list), 'words_count': word_list})

        except Exception as e:
            print(e.__str__())

    return render(request, 'core/index.html')
