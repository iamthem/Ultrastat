# Change the names of teams depending on which database 
# we are working with 
def renameWrapper(f, league, name):
    if f == 'goals' and league == 'bundes':
            return renameBundes(name)
    elif f == 'goals' and league == 'serie A':
        return renameSerieA(name)
    elif f == 'goals' and league == 'liga':
        return renameLiga(name)
    elif f == 'goals' and league == 'prem':
        return renamePrem(name)
    elif f == 'players' and league == 'bundes':
        return renameBundesPlayers(name)
    elif f == 'players' and league == 'serie A':
        return renameSerieAPlayers(name)
    elif f == 'players' and  league == 'liga':
        return renameLigaPlayers(name)
    elif f == 'players' and league  == 'prem':
        return renamePremPlayers(name)
    

def renamePrem(name):
    if name == 'Manchester United':
        return 'Man United'
    elif name == 'Brighton & Hove Albion':
        return 'Brighton'
    elif name == 'Newcastle United':
        return 'Newcastle'
    elif name == 'Huddersfield Town':
        return 'Huddersfield'
    elif name == 'Leicester City':
        return 'Leicester'
    elif name == 'Manchester City':
        return 'Man City'
    elif name == 'West Ham United':
        return 'West Ham'
    elif name == 'Stoke City':
        return 'Stoke'
    elif name == 'Swansea City':
        return 'Swansea'
    elif name == 'Tottenham Hotspur':
        return 'Tottenham'
    elif name == 'West Bromwich Albion':
        return 'West Brom'
    else:
        return name


def renameLiga(name):
    if name == 'Deportivo Alaves':
        return 'Alaves'
    elif name == 'Celta Vigo':
        return 'Celta'
    elif name == 'Real Sociedad':
        return 'Sociedad'
    elif name == 'Atletico Madrid':
        return 'Ath Madrid'
    elif name == 'Real CD Espanyol':
        return 'Espanol'
    elif name == 'Athletic Bilbao':
        return 'Ath Bilbao'
    elif name == 'Dep. La Coruna':
        return 'La Coruna'
    elif name == 'FC Barcelona':
        return 'Barcelona'
    elif name == 'Swansea City':
        return 'Swansea'
    elif name == 'Malaga CF':
        return 'Malaga'
    else:
        return name


def renameSerieA(name):
    if name == 'FC Torino':
        return 'Torino'
    elif name == 'SPAL 1907':
        return 'Spal'
    elif name == 'AC milan':
        return 'Milan'
    elif name == 'Bologna FC':
        return 'Bologna'
    else:
        return name


def renameBundes(name):
    if name == 'Bayer Leverkusen':
        return 'Leverkusen'
    elif name == '1899 Hoffenheim':
        return 'Hoffenheim'
    elif name == 'FSV Mainz 05':
        return 'Mainz'
    elif name == 'Hannover 96':
        return 'Hannover'
    elif name == 'Hamburger SV':
        return 'Hamburg'
    elif name == 'FC Augsburg':
        return 'Augsburg'
    elif name == 'Hertha BSC Berlin':
        return 'Hertha'
    elif name == 'VfB Stuttgart':
        return 'Stuttgart'
    elif name == 'VfL Wolfsburg':
        return 'Wolfsburg'
    elif name == 'Borussia Dortmund':
        return 'Dortmund'
    elif name == 'Bor. Monchengladbach':
        return "M'gladbach"
    elif name == 'FC Schalke 04':
        return 'Schalke 04'
    elif name == 'SC Freiburg':
        return 'Freiburg'
    elif name == 'Eintracht Frankfurt':
        return 'Ein Frankfurt'
    else:
        return name

def renameBundesPlayers(name):
    if name == "M'gladbach":
        return "Borussia Mönchengladbach"
    elif name == 'Dortmund':
        return 'Borussia Dortmund'
    elif name == 'Bayern Munich':
        return 'FC Bayern Munich'
    elif name == 'Leverkusen':
        return 'Bayer 04 Leverkusen'
    elif name == 'Hamburg':
        return 'Hamburger SV'
    elif name == 'Augsburg':
        return 'FC Augsburg'
    elif name == 'Hertha':
        return 'Hertha BSC Berlin'
    elif name == 'Stuttgart':
        return 'VfB Stuttgart'
    elif name == 'Hoffenheim':
        return 'TSG 1899 Hoffenheim'
    elif name == 'Werder Bremen':
        return 'SV Werder Bremen'
    elif name == 'Mainz':
        return '1. FSV Mainz 05'
    elif name == 'Hannover':
        return 'Hannover 96'
    elif name == 'Schalke 04':
        return 'FC Schalke 04'
    elif name == 'Wolfsburg':
        return 'VfL Wolfsburg'
    elif name == 'Freiburg':
        return 'SC Freiburg'
    elif name == 'Ein Frankfurt':
        return 'Eintracht Frankfurt'
    elif name == 'FC Koln':
        return '1. FC Köln'
    else: return name 

def renameSerieAPlayers(name):
    if name == 'Verona':
        return 'Hellas Verona'
    elif name == 'Spal':
        return 'Ferrara (SPAL)'
    elif name == 'Benevento':
        return 'Benevento Calcio'
    elif name == 'Chievo':
        return 'Chievo Verona'
    else: return name 

def renamePremPlayers(name):
    if name == 'Leicester':
        return 'Leicester City'
    elif name == 'Brighton':
        return 'Brighton & Hove Albion'
    elif name == 'Man City':
        return 'Manchester City'
    elif name == 'Man United':
        return 'Manchester United' 
    elif name == 'Huddersfield':
        return 'Huddersfield Town'
    elif name == 'Stoke':
        return 'Stoke City'
    elif name == 'Swansea':
        return 'Swansea City'
    elif name == 'West Brom':
        return 'West Bromwich Albion' 
    elif name == 'West Ham':
        return 'West Ham United'
    elif name == 'Newcastle':
        return 'Newcastle United'
    elif name == 'Tottenham':
        return 'Tottenham Hotspur'
    else: return name 

def renameLigaPlayers(name):
    if name == 'Leganes':
        return 'CD Leganés'
    elif name == 'Alaves':
        return 'Deportivo Alavés'
    elif name == 'Valencia':
        return 'Valencia CF'
    elif name == 'Las Palmas':
        return 'UD Las Palmas'
    elif name == 'Celta':
        return 'RC Celta de Vigo'
    elif name == 'Sociedad':
        return 'Real Sociedad'
    elif name == 'Girona':
        return 'Girona CF'
    elif name == 'Ath Madrid':
        return 'Atlético Madrid'
    elif name == 'Sevilla':
        return 'Sevilla FC'
    elif name == 'Espanol':
        return 'RCD Espanyol'
    elif name == 'Ath Bilbao':
        return 'Athletic Club de Bilbao'
    elif name == 'Getafe':
        return 'Getafe CF'
    elif name == 'Barcelona':
        return 'FC Barcelona'
    elif name == 'Betis':
        return 'Real Betis Balompié'
    elif name == 'La Coruna':
        return 'RC Deportivo de La Coruña'
    elif name == 'Real Madrid':
        return 'Real Madrid CF'
    elif name == 'Levante':
        return 'Levante UD'
    elif name == 'Villarreal':
        return 'Villarreal CF'
    elif name == 'Malaga':
        return 'Málaga CF'
    elif name == 'Eibar':
        return 'SD Eibar'
    else: return name 


