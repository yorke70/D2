from django import template


register = template.Library()

BAD_WORDS = "редиска жопа писька"

def is_int(text):
    try:
        int(text)
        return True
    except ValueError:
        return False

def is_float(text):
    try:
        float(text)
        return True
    except ValueError:
        return False

@register.filter()
def censor(text):
    temp_text = text.split()
    for i, txt in enumerate(temp_text):
        if not is_int(txt) and not is_float(txt):
            if len(txt.lower()[:-1]) > 2 and txt.lower()[:-1] in BAD_WORDS:
                temp_text[i] = f'{txt[0]}{"*" * (len(txt) - 1)}'
    return " ".join(temp_text)
