from flask import Flask, render_template, url_for, request

app = Flask(__name__)

pref = ["art", "arp", "ast", "apt", "att", "aro", "atu", "abb", "ant", "aw", "bat", "boo", "bu", "bap", "bul", "ber", "beth", "bar", "boll", "box", "bux", "buzz", "biz", "buck", "car", "cat", "cha", "choo", "cur", "co", "coll", "cow", "cab", "cash", "copp", "datt", "deo", "doo", "du", "dul", "dat", "dox", "dek", "dash", "dish", "dart", "ett", "each", "eon", "ell", "ess", "ex", "emo", "ew", "fu", "fa", "fact", "gyu", "gu", "gap", "gan", "gum", "giv", "gow", "han", "hoo", "hatt", "hand", "hut", "hall", "how", "haw", "hox", "hux", "io", "ir", "iss", "ix", "ion", "ish", "ist", "ire", "ite", "i", "izz", "ino", "ill", "ju", "joo", "jan", "jam", "jaw", "jott", "koo", "ku", "kat", "kom", "kaw", "ko", "kew", "kio", "kall", "kon", "lar", "lay", "lop", "lish", "list", "lan", "lew", "lly", "lash", "learn", "lore", "lu", "loo", "mar", "moo", "mo", "mat", "mit", "mart", "mill", "mio", "mee", "mane", "morn", "more", "mash", "mosh", "my", "non", "norm", "nass", "ny", "no", "nu", "na", "now", "nott", "nore", "note", "neo", "noll", "oo", "ott", "ore", "osha", "ona", "oa", "or", "one", "ost", "ope", "ode", "ou", "part", "pu", "pio", "per","pall", "po", "pu", "pit", "push", "poll", "pow", "pew", "pax", "ro", "rat", "row", "ra", "rill", "rox", "ron", "ry", "ree", "ri", "reo", "rich", "rest", "rew", "rech", "so", "soy", "sare", "san", "son", "seek", "saw", "sort", "say", "sh", "sho", "shee", "shea", "sha", "shi", "show", "shot", "to", "tu", "ti", "ta", "ter", "tra", "tro", "ton", "tin", "tow", "taw", "tea", "th", "tha", "tho", "toll", "teo", "tio", "tok", "tax", "u", "uo", "ua", "uno", "una", "une", "ute", "uto", "utu", "ulo", "ula", "uwo", "uvo", "upo", "upa", "uja", "ux", "vo", "vu", "var", "ver", "vi", "va", "vow", "vox", "vat", "voss", "via", "voo", "vue", "wow", "ware", "wash", "wish", "wa", "wu", "wo", "war", "wer", "won", "wall", "win", "wed", "xo", "xi", "xy", "xa", "ya", "yo", "yi", "yar", "yer", "zo", "zi", "za", "zow"]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        suggested_name = request.form['suggested']
        ingredient_used = request.form['ingred']
        country_name = request.form['country']
        number = int(request.form['number'])

        data = [number, suggested_name, ingredient_used]

        return render_template('result.html', data = data, pref=pref)

    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    suggested_name = request.form['suggested']
    ingredient_used = request.form['ingred']
    country_name = request.form['country']
    number = int(request.form['number'])

    data = [number, suggested_name, ingredient_used]

    return render_template('result.html', data=data, pref=pref)



app.run(debug=True)