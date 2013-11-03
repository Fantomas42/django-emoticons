"""Settings for emoticons app"""
import re
import os
import binascii

from django.conf import settings

try:
    unicode = unicode
except NameError:  # Python 3
    unicode = str
    basestring = (str, bytes)


emoticons_default_list = (
    ((':)', ':-)', ':=)', '(smile)'), 'smile.gif'),
    ((':(', ':-(', ':=(', '(sad)'), 'sadsmile.gif'),
    ((';)', ';-)', ';=)', '(wink)'), 'wink.gif'),
    ((';(', ';-(', ';=(', '(cry)'), 'crying.gif'),
    ((':*', ':-*', ':=*', '(kiss)'), 'kiss.gif'),
    ((':|', ':-|', ':=|', '(speechless)'), 'speechless.gif'),
    ((':&', ':-&', ':=&', '(puke)'), 'puke.gif'),
    ((':-?', ':?', ':=?', '(think)'), 'thinking.gif'),
    (('|(', '|-(', '|=(', '(dull)'), 'dull.gif'),
    (('|-)', 'I-)', 'I=)', '(snooze)'), 'sleepy.gif'),
    (('])', '>)', ']=)', '>=)', '(grin)'), 'evilgrin.gif'),
    ((':$', ':-$', ':=$', ':">', '(blush)'), 'blush.gif'),
    ((':D', ':-D', ':=D', ':d', ':-d', ':=d', '(laugh)'), 'bigsmile.gif'),
    ((':O', ':-O', ':=O', ':o', ':-o', ':=o', '(surprised)'), 'surprised.gif'),
    (('8)', '8-)', '8=)', 'B)', 'B-)', 'B=)', '(cool)'), 'cool.gif'),
    (('8-|', 'B-|', '8|', 'B|', '8=|', 'B=|', '(nerd)'), 'nerd.gif'),
    ((':P', ':-P', ':=P', ':p', ':-p', ':=p', '(tongueout)'), 'tongueout.gif'),
    ((':S', ':s', ':-s', ':-S', ':=s', ':=S', '(worry)'), 'worried.gif'),
    ((':@', ':-@', ':=@', 'x(', 'x-(', 'X(', 'X-(', 'x=(', 'X=('),
     'angry.gif'),
    ((':x', ':-x', ':X', ':-X', ':#', ':-#', ':=x', ':=X', ':=#'),
     'lipssealed.gif'),
    ((':^)', '(wonder)'), 'wondering.gif'),
    (('\o/', '\:D/', '\:d/', '(dance)'), 'dance.gif'),
    (('(mm)', '(mmm)', '(mmmm)'), 'mmm.gif'),
    ('(hi)', 'hi.gif'),
    ('(call)', 'call.gif'),
    ('(devil)', 'devil.gif'),
    ('(angel)', 'angel.gif'),
    ('(envy)', 'envy.gif'),
    ('(wait)', 'wait.gif'),
    ('(yawn)', 'yawn.gif'),
    ('(sweat)', 'sweating.gif'),
    ('(doh)', 'doh.gif'),
    ('(talk)', 'talking.gif'),
    ('(inlove)', 'inlove.gif'),
    ('(party)', 'party.gif'),
    ('(wasntme)', 'itwasntme.gif'),
    ('(clap)', 'clapping.gif'),
    ('(rofl)', 'rofl.gif'),
    ('(whew)', 'whew.gif'),
    ('(happy)', 'happy.gif'),
    ('(smirk)', 'smirk.gif'),
    ('(nod)', 'nod.gif'),
    ('(shake)', 'shake.gif'),
    ('(punch)', 'punch.gif'),
    ('(emo)', 'emo.gif'),
    ('(sun)', 'sun.gif'),
    ('(music)', 'music.gif'),
    ('(coffee)', 'coffee.gif'),
    ('(beer)', 'beer.gif'),
    ('(ninja)', 'ninja.gif'),
    ('(bow)', 'bow.gif'),
    ('(mooning)', 'mooning.gif'),
    ('(finger)', 'middlefinger.gif'),
    ('(bandit)', 'bandit.gif'),
    ('(drunk)', 'drunk.gif'),
    ('(toivo)', 'toivo.gif'),
    ('(rock)', 'rock.gif'),
    ('(swear)', 'swear.gif'),
    ('(bug)', 'bug.gif'),
    ('(fubar)', 'fubar.gif'),
    ('(tmi)', 'tmi.gif'),
    ('(handshake)', 'handshake.gif'),
    (('(^)', '(cake)'), 'cake.gif'),
    (('(*)', '(star)'), 'star.gif'),
    (('(hug)', '(bear)'), 'bear.gif'),
    (('(makeup)', '(kate)'), 'makeup.gif'),
    (('(smoking)', '(smoke)'), 'smoke.gif'),
    (('(chuckle)', '(giggle)'), 'giggle.gif'),
    (('(headbang)', '(banghead)'), 'headbang.gif'),
    (('(pi)', '(pizza)'), 'pizza.gif'),
    (('(flex)', '(muscle)'), 'muscle.gif'),
    (('(cash)', '(mo)', '($)'), 'cash.gif'),
    (('(d)', '(D)', '(drink)'), 'drink.gif'),
    (('(e)', '(m)', '(mail)'), 'mail.gif'),
    (('(mp)', '(ph)', '(phone)'), 'phone.gif'),
    (('(poolparty)', '(hrv)'), 'poolparty.gif'),
    (('(F)', '(f)', '(flower)'), 'flower.gif'),
    (('(~)', '(film)', '(movie)'), 'movie.gif'),
    (('(rain)', '(st)', '(london)'), 'rain.gif'),
    (('(o)', '(O)', '(time)', '(clock)'), 'time.gif'),
    (('(y)', '(Y)', '(ok)', '(yes)'), 'yes.gif'),
    (('(n)', '(N)', '(ko)', '(no)'), 'no.gif'),
    (('(u)', '(U)', '(brokenheart)'), 'brokenheart.gif'),
    (('(h)', '(H)', '(l)', '(L)', '(heart)', '(love)'), 'heart.gif'),
)


def cast_to_list(emoticons_list):
    """
    Fix list of emoticons with a single name
    to a list for easier future iterations,
    and cast iterables to list.
    """
    emoticons_tuple = []
    for emoticons, image in emoticons_list:
        if isinstance(emoticons, basestring):
            emoticons = [emoticons]
        else:
            emoticons = list(emoticons)
        emoticons_tuple.append((emoticons, image))
    return emoticons_tuple


def compile_emoticons(emoticons_list):
    """
    Compile a new list of emoticon tuples.
    Each tuple contains the name of the emoticon,
    the image path concatened with EMOTICONS_DIRECTORY,
    the hexadecimal code of the emoticon and a
    compiled regular expression of the emoticon.
    """
    emoticons_compiled = []
    for emoticons, image in emoticons_list:
        for emoticon in emoticons:
            emoticons_compiled.append(
                (emoticon,
                 os.path.join(EMOTICONS_DIRECTORY, image),
                 binascii.hexlify(emoticon.encode('utf-8')),
                 re.compile(re.escape(emoticon)))
            )
    return emoticons_compiled


EMOTICONS_LIST = getattr(settings, 'EMOTICONS_LIST',
                         emoticons_default_list)

EMOTICONS_LIST = cast_to_list(EMOTICONS_LIST)

EMOTICONS_DIRECTORY = getattr(settings, 'EMOTICONS_DIRECTORY',
                              'emoticons')

EMOTICONS_COMPILED = compile_emoticons(EMOTICONS_LIST)
