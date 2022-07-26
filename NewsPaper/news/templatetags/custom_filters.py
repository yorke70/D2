from django import template

register = template.Library()

BAD_WORDS = "редиска жопа писька"

@register.filter()
def censor(text):
    temp_text = text.split()
    for i, txt in enumerate(temp_text):
        if isinstance(txt, str):
            if txt.lower()[:-1] in BAD_WORDS:
                temp_text[i] = f'{txt[0]}{"*" * (len(txt) - 1)}'
    return " ".join(temp_text)
