def print_(text,color,highlight,words):
  font_ = {'p':'0','bold':'1','italic':'3','flashing':'5','flashingfast':'6'}
  color_ = {'p':'29','red':'31','green':'32','yellow':'33','blue':'34','violet':'35','lightBlue':'36','white':'37'}
  highlight_ = {'p':'','hred':';41',';hgreen':';42',';hyellow':';43','hblue':';44',';hviolet':';45',';hlightBlue':';46',';hwhite':';47'}
  if text in font_:
    if color in color_:
      if highlight in highlight_:
        print ('\x1b['+font_[text]+';'+color_[color]+highlight_[highlight]+'m'+words+'\x1b[0m')
      else:
        print('One of the fonts/colors/highlights you entered didnt work, try again.')
    else:
      print('One of the fonts/colors/highlights you entered didnt work, try again.')
  else:
    print('One of the fonts/colors/highlights you entered didnt work, try again.')

print_('italic','violet','p','this is proof that two nukes wasnt enough')
print('\x1b[3;35;39m'+'this is proof that two nukes wasnt enough'+'\x1b[0m')
