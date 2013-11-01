"""Settings for emoticons app"""
import re

from django.conf import settings

try:
    unicode = unicode
except NameError:  # Python 3
    unicode = str
    basestring = (str, bytes)


emoticons_default_list = (
    ((':)', ':-)', ':=)', '(smile)'), 'smile.gif'),
    ((':(', ':-(', ':=(', '(sad)'), 'sadsmile.gif'),
    ((':D', ':-D', ':=D', ':d', ':-d', ':=d', '(laugh)'), 'bigsmile.gif'),
    (('8)', '8-)', '8=)', 'B)', 'B-)', 'B=)', '(cool)'), 'cool.gif'),
    ((':O', ':-O', ':=O', ':o', ':-o', ':=o', '(surprised)'), 'surprised.gif'),
    ((';)', ';-)', ';=)', '(wink)'), 'wink.gif'),
    ((';(', ';-(', ';=(', '(cry)'), 'crying.gif'),
    (('(:|', '(sweat)'), 'sweating.gif'),
    ((':|', ':-|', ':=|', '(speechless)'), 'speechless.gif'),
    ((':*', ':-*', ':=*', '(kiss)'), 'kiss.gif'),
    ((':P', ':-P', ':=P', ':p', ':-p', ':=p', '(tongueout)'), 'tongueout.gif'),
    ((':$', ':-$', ':=$', ':">', '(blush)'), 'blush.gif'),
    ((':^)', '(wonder)'), 'wondering.gif'),
    (('|-)', 'I-)', 'I=)', '(snooze)'), 'sleepy.gif'),
    (('|-(', '|(', '|=(', '(dull)'), 'dull.gif'),
    ('(inlove)', 'inlove.gif'),
    ((']=)', '>=)', '(grin)'), 'evilgrin.gif'),
    ('(talk)', 'talking.gif'),
    (('|-()', '(yawn)'), 'yawn.gif'),
    ((':&', ':-&', ':=&', '(puke)'), 'puke.gif'),
    ('(doh)', 'doh.gif'),
    ((':@', ':-@', ':=@', 'x(', 'x-(', 'X(', 'X-(',
      'x=(', 'X=(', '(angry)'), 'angry.gif'),
    ('(wasntme)', 'itwasntme.gif'),
    ('(party)', 'party.gif'),
    ((':S', ':s', ':-s', ':-S', ':=s', ':=S', '(worry)'), 'worried.gif'),
    (('(mm)', '(mmm)', '(mmmm)'), 'mmm.gif'),
    (('8-|', 'B-|', '8|', 'B|', '8=|', 'B=|', '(nerd)'), 'nerd.gif'),
    ((':x', ':-x', ':X', ':-X', ':#', ':-#',
      ':=x', ':=X', ':=#'), 'lipssealed.gif'),
    ('(hi)', 'hi.gif'),
    ('(call)', 'call.gif'),
    ('(devil)', 'devil.gif'),
    ('(angel)', 'angel.gif'),
    ('(envy)', 'envy.gif'),
    ('(wait)', 'wait.gif'),
    (('(hug)', '(bear)'), 'bear.gif'),
    (('(makeup)', '(kate)'), 'makeup.gif'),
    (('(chuckle)', '(giggle)'), 'giggle.gif'),
    ('(clap)', 'clapping.gif'),
    ((':-?', ':?', ':=?', '(think)'), 'thinking.gif'),
    ('(bow)', 'bow.gif'),
    ('(rofl)', 'rofl.gif'),
    ('(whew)', 'whew.gif'),
    ('(happy)', 'happy.gif'),
    ('(smirk)', 'smirk.gif'),
    ('(nod)', 'nod.gif'),
    ('(shake)', 'shake.gif'),
    ('(punch)', 'punch.gif'),
    ('(emo)', 'emo.gif'),
    (('(y)', '(Y)', '(ok)', '(yes)'), 'yes.gif'),
    (('(n)', '(N)', '(no)'), 'no.gif'),
    ('(handshake)', 'handshake.gif'),
    (('(h)', '(H)', '(l)', '(L)', '(heart)', '(love)'), 'heart.gif'),
    (('(u)', '(U)', '(brokenheart)'), 'brokenheart.gif'),
    (('(e)', '(m)', '(mail)'), 'mail.gif'),
    (('(F)', '(f)', '(flower)'), 'flower.gif'),
    (('(rain)', '(st)', '(london)'), 'rain.gif'),
    ('(sun)', 'sun.gif'),
    (('(o)', '(O)', '(time)', '(clock)'), 'time.gif'),
    ('(music)', 'music.gif'),
    (('(~)', '(film)', '(movie)'), 'movie.gif'),
    (('(mp)', '(ph)', '(phone)'), 'phone.gif'),
    ('(coffee)', 'coffee.gif'),
    (('(pi)', '(pizza)'), 'pizza.gif'),
    (('(cash)', '(mo)', '($)'), 'cash.gif'),
    (('(flex)', '(muscle)'), 'muscle.gif'),
    (('(^)', '(cake)'), 'cake.gif'),
    ('(beer)', 'beer.gif'),
    (('(d)', '(D)', '(drink)'), 'drink.gif'),
    (('\o/', '\:D/', '\:d/', '(dance)'), 'dance.gif'),
    ('(ninja)', 'ninja.gif'),
    (('(*)', '(star)'), 'star.gif'),
    ('(mooning)', 'mooning.gif'),
    ('(finger)', 'middlefinger.gif'),
    ('(bandit)', 'bandit.gif'),
    ('(drunk)', 'drunk.gif'),
    (('(smoking)', '(smoke)', '(ci)'), 'smoke.gif'),
    ('(toivo)', 'toivo.gif'),
    ('(rock)', 'rock.gif'),
    (('(headbang)', '(banghead)'), 'headbang.gif'),
    (('(poolparty)', '(hrv)'), 'poolparty.gif'),
    ('(swear)', 'swear.gif'),
    ('(bug)', 'bug.gif'),
    ('(fubar)', 'fubar.gif'),
    ('(tmi)', 'tmi.gif'),
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


def build_emoticons_regexp(emoticons_list):
    """
    Build a new list of emoticon tuples.
    Each tuple contains a regexp of the emoticon,
    the original name and the image associated.
    """
    emoticons_regexp = []
    for emoticons, image in emoticons_list:
        for emoticon in emoticons:
            emoticons_regexp.append(
                (re.compile(re.escape(emoticon)),
                 emoticon, image))
    return emoticons_regexp


EMOTICONS_LIST = getattr(settings, 'EMOTICONS_LIST',
                         emoticons_default_list)

EMOTICONS_LIST = cast_to_list(EMOTICONS_LIST)

EMOTICONS_REGEXP = build_emoticons_regexp(EMOTICONS_LIST)

EMOTICONS_DIRECTORY = getattr(settings, 'EMOTICONS_DIRECTORY', 'emoticons')
