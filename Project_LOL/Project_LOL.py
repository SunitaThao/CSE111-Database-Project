import sqlite3
from sqlite3 import Error
from decimal import Decimal


def openConnection(_dbFile): 
    conn = None
    conn = sqlite3.connect(_dbFile)
    return conn

def closeConnection(_conn, _dbFile):
    _conn.close()

def PrintTables(table, _conn):
    print(table)
    if table == 'champion':
        sql = (f"""SELECT *
                From champion ;""")
    if table == 'type':
        sql = (f"""SELECT *
                From type ;""")
    if table == 'matchups':
        sql = (f"""SELECT *
                From matchups ;""")
    if table == 'skins':
        sql = (f"""SELECT *
                From skins ;""")
    if table == 'abilities':
        sql = (f"""SELECT *
                From abilities ;""")
    if table == 'stats':
        sql = (f"""SELECT *
                From stats ;""")
    
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    rows = cursor.fetchall()
    for row in rows:
        if table == 'champion' or table == 'type' or table == 'matchups':
            l = '{:20} {:<30} {:20}\n'.format(row[0], row[1], row[2])
            print(l)
        elif table == 'skins':
            l = '{:20} {:<30} {:20} {:10}\n'.format(row[0], row[1], row[2], row[3])
            print(l)
        elif table == 'abilities':
            l = '{:20} {:<30} {:20} {:10} {:20} {:10}\n'.format(row[0], row[1], row[2], row[3], row[4], row[5])
            print(l)
        elif table == 'stats':
            l = '{:20} {:<30} {:20} {:10} {:20} {:10} {:20} {:10}\n'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            print(l)
    Start(_conn)

def Champion(_conn, _use):
    if _use == 'add':
        cname = input("Please enter the champion name: ")
        cnkname = input("Please enter champion nickname: ")
        cdifficulty = input("Please enter champion difficulty: ")

        sql = (f"""INSERT INTO champion VALUES (?, ?, ?);""")
        args = [cname, cnkname, cdifficulty]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('champion', _conn)
    if _use == 'remove':
        cname = input("Please enter the champion name: ")
        cnkname = input("Please enter champion nickname: ")
        cdifficulty = input("Please enter champion difficulty: ")

        sql = (f"""Delete From champion Where c_name = ? and c_nickname = ? and c_difficulty = ?;""")
        args = [cname, cnkname, cdifficulty]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('champion', _conn)
    if _use == 'update':
        col = input("Enter the attribute you wish to update(c_name, c_nickname, c_difficulty): ")
        data = input("Enter the data you wish to update it with: ")
        col2 = input("Specify where that update will happen by entering another attribute(c_name, c_nickname, c_difficulty): ")
        data2 = input("Specify the value for that attribute: ")

        if col == 'c_name':
            if col2 == 'c_nickname':
                sql = (f"""UPDATE champion SET c_name = ? WHERE c_nickname = ?;""")
            elif col2 == 'c_difficulty':
                sql = (f"""UPDATE champion SET c_name = ? WHERE c_difficulty = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'c_nickname':
            if col2 == 'c_name':
                sql = (f"""UPDATE champion SET c_nickname = ? WHERE c_name = ?;""")
            elif col2 == 'c_difficulty':
                sql = (f"""UPDATE champion SET c_nickname = ? WHERE c_difficulty = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'c_difficulty':
            if col2 == 'c_name':
                sql = (f"""UPDATE champion SET c_difficulty = ? WHERE c_name = ?;""")
            elif col2 == 'c_nickname':
                sql = (f"""UPDATE champion SET c_difficulty = ? WHERE c_nickname = ?;""")
            else:
                Type(_conn, 'update')
        else:
            Type(_conn, 'update')

        args = [data, data2]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('champion', _conn)

def Type(_conn, _use):
    if _use == 'add':
        tchamp = input("Please enter the champion name: ")
        tname = input("Please enter champion type name: ")
        trole = input("Please enter champion role: ")

        sql = (f"""INSERT INTO type VALUES (?, ?, ?);""")
        args = [tchamp, tname, trole]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('type', _conn)
    if _use == 'remove':
        tchamp = input("Please enter the champion name: ")
        tname = input("Please enter champion type name: ")
        trole = input("Please enter champion role: ")

        sql = (f"""Delete From type Where t_champ_name = ? and t_name = ? and t_role = ?;""")
        args = [tchamp, tname, trole]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('type', _conn)
    if _use == 'update':
        col = input("Enter the attribute you wish to update(t_champ_name, t_name, t_role): ")
        data = input("Enter the data you wish to update it with: ")
        col2 = input("Specify where that update will happen by entering another attribute(t_champ_name, t_name, t_role): ")
        data2 = input("Specify the value for that attribute: ")
        
        if col == 't_champ_name':
            if col2 == 't_name':
                sql = (f"""UPDATE type SET t_champ_name = ? WHERE t_name = ?;""")
            elif col2 == 't_role':
                sql = (f"""UPDATE type SET t_champ_name = ? WHERE t_role = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 't_name':
            if col2 == 't_champ_name':
                sql = (f"""UPDATE type SET t_name = ? WHERE t_champ_name = ?;""")
            elif col2 == 't_role':
                sql = (f"""UPDATE type SET t_name = ? WHERE t_role = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 't_role':
            if col2 == 't_champ_name':
                sql = (f"""UPDATE type SET t_role = ? WHERE t_champ_name = ?;""")
            elif col2 == 't_name':
                sql = (f"""UPDATE type SET t_role = ? WHERE t_name = ?;""")
            else:
                Type(_conn, 'update')
        else:
            Type(_conn, 'update')
        
        args = [data, data2]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('type', _conn)

def Matchups(_conn, _use):
    if _use == 'add':
        muchamp = input("Please enter the champion name: ")
        badmu = input("Please enter champion bad match up: ")
        goodmu = input("Please enter champion good match up: ")

        sql = (f"""INSERT INTO matchups VALUES (?, ?, ?);""")
        args = [muchamp, badmu, goodmu]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('matchups', _conn)
    if _use == 'remove':
        muchamp = input("Please enter the champion name: ")
        badmu = input("Please enter champion bad match up: ")
        goodmu = input("Please enter champion good match up: ")

        sql = (f"""Delete From matchups Where mu_champ_name = ? and bad_mu_name = ? and good_mu_name = ?;""")
        args = [muchamp, badmu, goodmu]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('matchups', _conn)
    if _use == 'update':
        col = input("Enter the attribute you wish to update(mu_champ_name, bad_mu_name, good_mu_name): ")
        data = input("Enter the data you wish to update it with: ")
        col2 = input("Specify where that update will happen by entering another attribute(mu_champ_name, bad_mu_name, good_mu_name): ")
        data2 = input("Specify the value for that attribute: ")
        
        if col == 'mu_champ_name':
            if col2 == 'bad_mu_name':
                sql = (f"""UPDATE matchups SET mu_champ_name = ? WHERE bad_mu_name = ?;""")
            elif col2 == 'good_mu_name':
                sql = (f"""UPDATE matchups SET mu_champ_name = ? WHERE good_mu_name = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'bad_mu_name':
            if col2 == 'mu_champ_name':
                sql = (f"""UPDATE matchups SET bad_mu_name = ? WHERE mu_champ_name = ?;""")
            elif col2 == 'good_mu_name':
                sql = (f"""UPDATE matchups SET bad_mu_name = ? WHERE good_mu_name = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'good_mu_name':
            if col2 == 'mu_champ_name':
                sql = (f"""UPDATE matchups SET good_mu_name = ? WHERE mu_champ_name = ?;""")
            elif col2 == 'bad_mu_name':
                sql = (f"""UPDATE matchups SET good_mu_name = ? WHERE bad_mu_name = ?;""")
            else:
                Type(_conn, 'update')
        else:
            Type(_conn, 'update')

        args = [data, data2]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('matchups', _conn)

def Skins(_conn, _use):
    if _use == 'add':
        skchamp = input("Please enter the champion name: ")
        skname = input("Please enter skin name: ")
        skcost = input("Please enter skin cost: ")
        sktype = input("Please enter skin type: ")

        sql = (f"""INSERT INTO skins VALUES (?, ?, ?, ?);""")
        args = [skchamp, skname, skcost, sktype]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('skins', _conn)
    if _use == 'remove':
        skchamp = input("Please enter the champion name: ")
        skname = input("Please enter skin name: ")
        skcost = input("Please enter skin cost: ")
        sktype = input("Please enter skin type: ")

        sql = (f"""Delete From skins Where sk_champ_name = ? and sk_name = ? and sk_cost = ? and sk_skin_kind = ?;""")
        args = [skchamp, skname, skcost, sktype]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('skins', _conn)
    if _use == 'update':
        col = input("Enter the attribute you wish to update(sk_champ_name, sk_name, sk_cost, sk_skin_kind): ")
        data = input("Enter the data you wish to update it with: ")
        col2 = input("Specify where that update will happen by entering another attribute(sk_champ_name, sk_name, sk_cost, sk_skin_kind): ")
        data2 = input("Specify the value for that attribute: ")

        if col == 'sk_champ_name':
            if col2 == 'sk_name':
                sql = (f"""UPDATE skins SET sk_champ_name = ? WHERE sk_name = ?;""")
            elif col2 == 'sk_cost':
                sql = (f"""UPDATE skins SET sk_champ_name = ? WHERE sk_cost = ?;""")
            elif col2 == 'sk_skin_kind':
                sql = (f"""UPDATE skins SET sk_champ_name = ? WHERE sk_skin_kind = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'sk_name':
            if col2 == 'sk_champ_name':
                sql = (f"""UPDATE skins SET sk_name = ? WHERE sk_champ_name = ?;""")
            elif col2 == 'sk_cost':
                sql = (f"""UPDATE skins SET sk_name = ? WHERE sk_cost = ?;""")
            elif col2 == 'sk_skin_kind':
                sql = (f"""UPDATE skins SET sk_name = ? WHERE sk_skin_kind = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'sk_cost':
            if col2 == 'sk_champ_name':
                sql = (f"""UPDATE skins SET sk_cost = ? WHERE sk_champ_name = ?;""")
            elif col2 == 'sk_name':
                sql = (f"""UPDATE skins SET sk_cost = ? WHERE sk_name = ?;""")
            elif col2 == 'sk_skin_kind':
                sql = (f"""UPDATE skins SET sk_cost = ? WHERE sk_skin_kind = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'sk_skin_kind':
            if col2 == 'sk_champ_name':
                sql = (f"""UPDATE skins SET sk_skin_kind = ? WHERE sk_champ_name = ?;""")
            elif col2 == 'sk_name':
                sql = (f"""UPDATE skins SET sk_skin_kind = ? WHERE sk_name = ?;""")
            elif col2 == 'sk_cost':
                sql = (f"""UPDATE skins SET sk_skin_kind = ? WHERE sk_cost = ?;""")
            else:
                Type(_conn, 'update')
        else:
            Type(_conn, 'update')

        args = [data, data2]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('skins', _conn)

def Abilities(_conn, _use):
    if _use == 'add':
        achamp = input("Please enter the champion name: ")
        apassive = input("Please enter champion passive: ")
        aq = input("Please enter champion q ability: ")
        aw = input("Please enter champion w ability: ")
        ae = input("Please enter champion e ability: ")
        ar = input("Please enter champion r ability: ")

        sql = (f"""INSERT INTO abilities VALUES (?, ?, ?, ?, ?, ?);""")
        args = [achamp, apassive, aq, aw, ae, ar]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('abilities', _conn)
    if _use == 'remove':
        achamp = input("Please enter the champion name: ")
        apassive = input("Please enter champion passive: ")
        aq = input("Please enter champion q ability: ")
        aw = input("Please enter champion w ability: ")
        ae = input("Please enter champion e ability: ")
        ar = input("Please enter champion r ability: ")

        sql = (f"""Delete From abilities Where a_champ_name = ? and a_passive = ? and a_qability = ? and a_wability = ? and a_eability = ? and a_rability = ?;""")
        args = [achamp, apassive, aq, aw, ae, ar]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('abilities', _conn)
    if _use == 'update':
        col = input("Enter the attribute you wish to update(a_champ_name, a_passive, a_qability, a_wability, a_eability, a_rability): ")
        data = input("Enter the data you wish to update it with: ")
        col2 = input("Specify where that update will happen by entering another attribute(a_champ_name, a_passive, a_qability, a_wability, a_eability, a_rability): ")
        data2 = input("Specify the value for that attribute: ")
        
        if col == 'a_champ_name':
            if col2 == 'a_passive':
                sql = (f"""UPDATE abilities SET a_champ_name = ? WHERE a_passive = ?;""")
            elif col2 == 'a_qability':
                sql = (f"""UPDATE abilities SET a_champ_name = ? WHERE a_qability = ?;""")
            elif col2 == 'a_wability':
                sql = (f"""UPDATE abilities SET a_champ_name = ? WHERE a_wability = ?;""")
            elif col2 == 'a_eability':
                sql = (f"""UPDATE abilities SET a_champ_name = ? WHERE a_eability = ?;""")
            elif col2 == 'a_rability':
                sql = (f"""UPDATE abilities SET a_champ_name = ? WHERE a_rability = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'a_passive':
            if col2 == 'a_champ_name':
                sql = (f"""UPDATE abilities SET a_passive = ? WHERE a_champ_name = ?;""")
            elif col2 == 'a_qability':
                sql = (f"""UPDATE abilities SET a_passive = ? WHERE a_qability = ?;""")
            elif col2 == 'a_wability':
                sql = (f"""UPDATE abilities SET a_passive = ? WHERE a_wability = ?;""")
            elif col2 == 'a_eability':
                sql = (f"""UPDATE abilities SET a_passive = ? WHERE a_eability = ?;""")
            elif col2 == 'a_rability':
                sql = (f"""UPDATE abilities SET a_passive = ? WHERE a_rability = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'a_qability':
            if col2 == 'a_champ_name':
                sql = (f"""UPDATE abilities SET a_qability = ? WHERE a_champ_name = ?;""")
            elif col2 == 'a_passive':
                sql = (f"""UPDATE abilities SET a_qability = ? WHERE a_passive = ?;""")
            elif col2 == 'a_wability':
                sql = (f"""UPDATE abilities SET a_qability = ? WHERE a_wability = ?;""")
            elif col2 == 'a_eability':
                sql = (f"""UPDATE abilities SET a_qability = ? WHERE a_eability = ?;""")
            elif col2 == 'a_rability':
                sql = (f"""UPDATE abilities SET a_qability = ? WHERE a_rability = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'a_wability':
            if col2 == 'a_champ_name':
                sql = (f"""UPDATE abilities SET a_wability = ? WHERE a_champ_name = ?;""")
            elif col2 == 'a_passive':
                sql = (f"""UPDATE abilities SET a_wability = ? WHERE a_passive = ?;""")
            elif col2 == 'a_qability':
                sql = (f"""UPDATE abilities SET a_wability = ? WHERE a_qability = ?;""")
            elif col2 == 'a_eability':
                sql = (f"""UPDATE abilities SET a_wability = ? WHERE a_eability = ?;""")
            elif col2 == 'a_rability':
                sql = (f"""UPDATE abilities SET a_wability = ? WHERE a_rability = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'a_eability':
            if col2 == 'a_champ_name':
                sql = (f"""UPDATE abilities SET a_eability = ? WHERE a_champ_name = ?;""")
            elif col2 == 'a_passive':
                sql = (f"""UPDATE abilities SET a_eability = ? WHERE a_passive = ?;""")
            elif col2 == 'a_qability':
                sql = (f"""UPDATE abilities SET a_eability = ? WHERE a_qability = ?;""")
            elif col2 == 'a_wability':
                sql = (f"""UPDATE abilities SET a_eability = ? WHERE a_wability = ?;""")
            elif col2 == 'a_rability':
                sql = (f"""UPDATE abilities SET a_eability = ? WHERE a_rability = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'a_rability':
            if col2 == 'a_champ_name':
                sql = (f"""UPDATE abilities SET a_rability = ? WHERE a_champ_name = ?;""")
            elif col2 == 'a_passive':
                sql = (f"""UPDATE abilities SET a_rability = ? WHERE a_passive = ?;""")
            elif col2 == 'a_qability':
                sql = (f"""UPDATE abilities SET a_rability = ? WHERE a_qability = ?;""")
            elif col2 == 'a_wability':
                sql = (f"""UPDATE abilities SET a_rability = ? WHERE a_wability = ?;""")
            elif col2 == 'a_eability':
                sql = (f"""UPDATE abilities SET a_rability = ? WHERE a_eability = ?;""")
            else:
                Type(_conn, 'update')
        else:
            Type(_conn, 'update')

        args = [data, data2]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('abilities', _conn)

def Stats(_conn, _use):
    if _use == 'add':
        stchamp = input("Please enter the champion name: ")
        strole = input("Please enter champion role: ")
        tier = input("Please enter champion tier: ")
        pickrate = input("Please enter champion pickrate: ")
        matches = input("Please enter champion number of matches: ")
        rank = input("Please enter champion rank: ")
        banrate = input("Please enter champion banrate: ")
        winrate = input("Please enter champion winrate: ")

        sql = (f"""INSERT INTO stats VALUES (?, ?, ?, ?, ?, ?, ?, ?);""")
        args = [stchamp, strole, tier, pickrate, matches, rank, banrate, winrate]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('stats', _conn)
    if _use == 'remove':
        stchamp = input("Please enter the champion name: ")
        strole = input("Please enter champion role: ")
        tier = input("Please enter champion tier: ")
        pickrate = input("Please enter champion pickrate: ")
        matches = input("Please enter champion number of matches: ")
        rank = input("Please enter champion rank: ")
        banrate = input("Please enter champion banrate: ")
        winrate = input("Please enter champion winrate: ")

        sql = (f"""Delete From stats Where st_champ_name = ? and st_role = ? and st_tier = ? and st_pickrate = ? and st_matches = ? and st_rank = ? and st_banrate = ? and st_winrate = ?;""")
        args = [stchamp, strole, tier, pickrate, matches, rank, banrate, winrate]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('stats', _conn)
    if _use == 'update':
        col = input("Enter the attribute you wish to update(st_champ_name, st_role, st_tier, st_pickrate, st_matches, st_rank, st_banrate, st_winrate): ")
        data = input("Enter the data you wish to update it with: ")
        col2 = input("Specify where that update will happen by entering another attribute(st_champ_name, st_role, st_tier, st_pickrate, st_matches, st_rank, st_banrate, st_winrate): ")
        data2 = input("Specify the value for that attribute: ")
        
        if col == 'st_champ_name':
            if col2 == 'st_role':
                sql = (f"""UPDATE stats SET st_champ_name = ? WHERE st_role = ?;""")
            elif col2 == 'st_tier':
                sql = (f"""UPDATE stats SET st_champ_name = ? WHERE st_tier = ?;""")
            elif col2 == 'st_pickrate':
                sql = (f"""UPDATE stats SET st_champ_name = ? WHERE st_pickrate = ?;""")
            elif col2 == 'st_matches':
                sql = (f"""UPDATE stats SET st_champ_name = ? WHERE st_matches = ?;""")
            elif col2 == 'st_rank':
                sql = (f"""UPDATE stats SET st_champ_name = ? WHERE st_rank = ?;""")
            elif col2 == 'st_banrate':
                sql = (f"""UPDATE stats SET st_champ_name = ? WHERE st_banrate = ?;""")
            elif col2 == 'st_winrate':
                sql = (f"""UPDATE stats SET st_champ_name = ? WHERE st_winrate = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'st_role':
            if col2 == 'st_champ_name':
                sql = (f"""UPDATE stats SET st_role = ? WHERE st_champ_name = ?;""")
            elif col2 == 'st_tier':
                sql = (f"""UPDATE stats SET st_role = ? WHERE st_tier = ?;""")
            elif col2 == 'st_pickrate':
                sql = (f"""UPDATE stats SET st_role = ? WHERE st_pickrate = ?;""")
            elif col2 == 'st_matches':
                sql = (f"""UPDATE stats SET st_role = ? WHERE st_matches = ?;""")
            elif col2 == 'st_rank':
                sql = (f"""UPDATE stats SET st_role = ? WHERE st_rank = ?;""")
            elif col2 == 'st_banrate':
                sql = (f"""UPDATE stats SET st_role = ? WHERE st_banrate = ?;""")
            elif col2 == 'st_winrate':
                sql = (f"""UPDATE stats SET st_role = ? WHERE st_winrate = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'st_tier':
            if col2 == 'st_champ_name':
                sql = (f"""UPDATE stats SET st_tier = ? WHERE st_champ_name = ?;""")
            elif col2 == 'st_role':
                sql = (f"""UPDATE stats SET st_tier = ? WHERE st_role = ?;""")
            elif col2 == 'st_pickrate':
                sql = (f"""UPDATE stats SET st_tier = ? WHERE st_pickrate = ?;""")
            elif col2 == 'st_matches':
                sql = (f"""UPDATE stats SET st_tier = ? WHERE st_matches = ?;""")
            elif col2 == 'st_rank':
                sql = (f"""UPDATE stats SET st_tier = ? WHERE st_rank = ?;""")
            elif col2 == 'st_banrate':
                sql = (f"""UPDATE stats SET st_tier = ? WHERE st_banrate = ?;""")
            elif col2 == 'st_winrate':
                sql = (f"""UPDATE stats SET st_tier = ? WHERE st_winrate = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'st_pickrate':
            if col2 == 'st_champ_name':
                sql = (f"""UPDATE stats SET st_pickrate = ? WHERE st_champ_name = ?;""")
            elif col2 == 'st_role':
                sql = (f"""UPDATE stats SET st_pickrate = ? WHERE st_role = ?;""")
            elif col2 == 'st_tier':
                sql = (f"""UPDATE stats SET st_pickrate = ? WHERE st_tier = ?;""")
            elif col2 == 'st_matches':
                sql = (f"""UPDATE stats SET st_pickrate = ? WHERE st_matches = ?;""")
            elif col2 == 'st_rank':
                sql = (f"""UPDATE stats SET st_pickrate = ? WHERE st_rank = ?;""")
            elif col2 == 'st_banrate':
                sql = (f"""UPDATE stats SET st_pickrate = ? WHERE st_banrate = ?;""")
            elif col2 == 'st_winrate':
                sql = (f"""UPDATE stats SET st_pickrate = ? WHERE st_winrate = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'st_matches':
            if col2 == 'st_champ_name':
                sql = (f"""UPDATE stats SET st_matches = ? WHERE st_champ_name = ?;""")
            elif col2 == 'st_role':
                sql = (f"""UPDATE stats SET st_matches = ? WHERE st_role = ?;""")
            elif col2 == 'st_tier':
                sql = (f"""UPDATE stats SET st_matches = ? WHERE st_tier = ?;""")
            elif col2 == 'st_pickrate':
                sql = (f"""UPDATE stats SET st_matches = ? WHERE st_pickrate = ?;""")
            elif col2 == 'st_rank':
                sql = (f"""UPDATE stats SET st_matches = ? WHERE st_rank = ?;""")
            elif col2 == 'st_banrate':
                sql = (f"""UPDATE stats SET st_matches = ? WHERE st_banrate = ?;""")
            elif col2 == 'st_winrate':
                sql = (f"""UPDATE stats SET st_matches = ? WHERE st_winrate = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'st_rank':
            if col2 == 'st_champ_name':
                sql = (f"""UPDATE stats SET st_rank = ? WHERE st_champ_name = ?;""")
            elif col2 == 'st_role':
                sql = (f"""UPDATE stats SET st_rank = ? WHERE st_role = ?;""")
            elif col2 == 'st_tier':
                sql = (f"""UPDATE stats SET st_rank = ? WHERE st_tier = ?;""")
            elif col2 == 'st_pickrate':
                sql = (f"""UPDATE stats SET st_rank = ? WHERE st_pickrate = ?;""")
            elif col2 == 'st_matches':
                sql = (f"""UPDATE stats SET st_rank = ? WHERE st_matches = ?;""")
            elif col2 == 'st_banrate':
                sql = (f"""UPDATE stats SET st_rank = ? WHERE st_banrate = ?;""")
            elif col2 == 'st_winrate':
                sql = (f"""UPDATE stats SET st_rank = ? WHERE st_winrate = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'st_banrate':
            if col2 == 'st_champ_name':
                sql = (f"""UPDATE stats SET st_banrate = ? WHERE st_champ_name = ?;""")
            elif col2 == 'st_role':
                sql = (f"""UPDATE stats SET st_banrate = ? WHERE st_role = ?;""")
            elif col2 == 'st_tier':
                sql = (f"""UPDATE stats SET st_banrate = ? WHERE st_tier = ?;""")
            elif col2 == 'st_pickrate':
                sql = (f"""UPDATE stats SET st_banrate = ? WHERE st_pickrate = ?;""")
            elif col2 == 'st_matches':
                sql = (f"""UPDATE stats SET st_banrate = ? WHERE st_matches = ?;""")
            elif col2 == 'st_rank':
                sql = (f"""UPDATE stats SET st_banrate = ? WHERE st_rank = ?;""")
            elif col2 == 'st_winrate':
                sql = (f"""UPDATE stats SET st_banrate = ? WHERE st_winrate = ?;""")
            else:
                Type(_conn, 'update')
        elif col == 'st_winrate':
            if col2 == 'st_champ_name':
                sql = (f"""UPDATE stats SET st_winrate = ? WHERE st_champ_name = ?;""")
            elif col2 == 'st_role':
                sql = (f"""UPDATE stats SET st_winrate = ? WHERE st_role = ?;""")
            elif col2 == 'st_tier':
                sql = (f"""UPDATE stats SET st_winrate = ? WHERE st_tier = ?;""")
            elif col2 == 'st_pickrate':
                sql = (f"""UPDATE stats SET st_winrate = ? WHERE st_pickrate = ?;""")
            elif col2 == 'st_matches':
                sql = (f"""UPDATE stats SET st_winrate = ? WHERE st_matches = ?;""")
            elif col2 == 'st_rank':
                sql = (f"""UPDATE stats SET st_winrate = ? WHERE st_rank = ?;""")
            elif col2 == 'st_banrate':
                sql = (f"""UPDATE stats SET st_winrate = ? WHERE st_banrate = ?;""")
            else:
                Type(_conn, 'update')
        else:
            Type(_conn, 'update')
        
        args = [data, data2]
        cursor = _conn.cursor()
        cursor.execute(sql, args)
        _conn.commit()
        PrintTables('stats', _conn)

def add(_conn):
    table = input("Enter which table you would like to add to(champion, type, skins, abilities, stats, matchups): ")
    if table == 'champion':
        Champion(_conn, 'add')
    elif table == 'type':
        Type(_conn, 'add')
    elif table == 'matchups':
        Matchups(_conn, 'add')
    elif table == 'skins':
        Skins(_conn, 'add')
    elif table == 'abilities':
        Abilities(_conn, 'add')
    elif table == 'stats':
        Stats(_conn, 'add')
    else:
        add(_conn)

def remove(_conn):
    table = input("Enter which table you would like to remove data from(champion, type, skins, abilities, stats, matchups): ")
    if table == 'champion':
        Champion(_conn, 'remove')
    elif table == 'type':
        Type(_conn, 'remove')
    elif table == 'matchups':
        Matchups(_conn, 'remove')
    elif table == 'skins':
        Skins(_conn, 'remove')
    elif table == 'abilities':
        Abilities(_conn, 'remove')
    elif table == 'stats':
        Stats(_conn, 'remove')
    else:
        remove(_conn)

def update(_conn):
    table = input("Enter which table you would like to update data from(champion, type, skins, abilities, stats, matchups): ")
    if table == 'champion':
        Champion(_conn, 'update')
    elif table == 'type':
        Type(_conn, 'update')
    elif table == 'matchups':
        Matchups(_conn, 'update')
    elif table == 'skins':
        Skins(_conn, 'update')
    elif table == 'abilities':
        Abilities(_conn, 'update')
    elif table == 'stats':
        Stats(_conn, 'update')
    else:
        update(_conn)

def Admin(_conn):
    password = input("Enter password: ")
    if password == 'CSE111':
        use = input("Enter 'u' to update data, 'a' to add data, or 'r' to remove data: ")
        if use == 'a':
            add(_conn)
        if use == 'r':
            remove(_conn)
        if use == 'u':
            update(_conn)
    else:
        Admin(_conn)

def Q1(_conn):
    
    sql = (f"""SELECT st_champ_name, max(st_banrate)
                FROM stats;"""
        )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20} {:<30}\n'.format(row[0], row[1])
        print(l)
    Start(_conn)

def Q2(_conn):
    
    sql = (f"""SELECT sk_champ_name, sk_name
                From skins;"""
        )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20} {:<30}\n'.format(row[0], row[1])
        print(l)
    Start(_conn)

def Q3(_conn):
    
    sql = (f"""SELECT c_name, c_difficulty
                FROM champion;"""
        )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20} {:<30}\n'.format(row[0], row[1])
        print(l)
    Start(_conn)

def Q4(_conn):
    
    sql = (f"""SELECT t_champ_name, t_name
                FROM type;"""
        )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20} {:<30}\n'.format(row[0], row[1])
        print(l)
    Start(_conn)

def Q5(_conn):
    
    sql = (f"""SELECT a_champ_name, a_passive
                FROM abilities;"""
        )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20} {:<30}\n'.format(row[0], row[1])
        print(l)
    Start(_conn)

def Q6(_conn):
    
    sql = (f"""SELECT mu_champ_name, good_mu_name
                FROM matchups;"""
        )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20} {:<30}\n'.format(row[0], row[1])
        print(l)
    Start(_conn)

def Q7(_conn):
    
    sql = (f"""SELECT st_champ_name, st_winrate
                FROM stats;"""
        )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20} {:<30}\n'.format(row[0], row[1])
        print(l)
    Start(_conn)

def Q8(_conn):
    
    sql = (f"""SELECT c_name
                FROM champion
                WHERE c_difficulty = 'high';"""
            )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20}\n'.format(row[0])
        print(l)
    Start(_conn)

def Q9(_conn):
    
    sql = (f"""SELECT sk_champ_name
                FROM skins
                WHERE sk_name = 'Star Guardian';"""
        )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20}\n'.format(row[0])
        print(l)
    Start(_conn)

def Q10(_conn):
    
    sql = (f"""SELECT mu_champ_name
                FROM matchups
                WHERE bad_mu_name = 'Seraphine';"""
        )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20}\n'.format(row[0])
        print(l)
    Start(_conn)

def Q11(_conn):
    
    sql = (f"""SELECT distinct a_champ_name, a_rability
                FROM abilities, skins
                WHERE a_champ_name = sk_champ_name
                    AND sk_skin_kind = 'legendary' or sk_skin_kind = 'ultimate';"""
        )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20} {:<30}\n'.format(row[0], row[1])
        print(l)
    Start(_conn)

def Q12(_conn):
    
    sql = (f"""SELECT sk_champ_name, max(sk_cost)
                FROM skins
                GROUP by sk_champ_name;"""
        )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20} {:<30}\n'.format(row[0], row[1])
        print(l)
    Start(_conn)

def Q13(_conn):
    
    sql = (f"""SELECT c_nickname
            FROM champion, stats, matchups
            WHERE c_name = st_champ_name
                AND c_name = mu_champ_name
                AND st_tier = 'S'
                AND good_mu_name = 'Miss Fortune';"""
        )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20}\n'.format(row[0])
        print(l)
    Start(_conn)

def Q14(_conn):
    
    sql = (f"""SELECT t_champ_name, t_role, a_qability, bad_mu_name, st_pickrate
                FROM type, abilities, matchups, stats
                WHERE t_champ_name = a_champ_name
                    AND a_champ_name = mu_champ_name
                    AND mu_champ_name = st_champ_name
                    AND st_pickrate > '3.0'
                Order by st_pickrate DESC;"""
        )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:10} {:10} {:10} {:10} {:10}\n'.format(row[0], row[1], row[2], row[3], row[4])
        print(l)
    Start(_conn)

def Q15(_conn):
    
    sql = (f"""SELECT a_wability
                FROM abilities
                WHERE substr(a_champ_name, 1, 1) = 'B';"""
        )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20}\n'.format(row[0])
        print(l)
    Start(_conn)

def Q16(_conn):
    
    sql = (f"""SELECT distinct c_name
                FROM champion, stats, type, skins
                WHERE c_name = sk_champ_name
                    AND sk_champ_name = t_champ_name
                    AND t_champ_name = st_champ_name
                    AND st_winrate > '50'
                    AND st_matches > '20000'
                    AND t_name = 'Fighter'
                    AND substr(sk_name, 1, 6) = 'SKT T1'
                    AND c_difficulty = 'moderate';"""
            )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20}\n'.format(row[0])
        print(l)
    Start(_conn)

def Q17(_conn):
    
    sql = (f"""SELECT count(sk_champ_name)
                FROM skins, stats
                WHERE sk_champ_name = st_champ_name
                    AND sk_name = 'Dark Star'
                    AND st_banrate < '2';"""
        )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:10}\n'.format(row[0])
        print(l)
    Start(_conn)

def Q18(_conn):
    
    sql = (f"""SELECT distinct t_champ_name
                FROM type
                WHERE t_name = 'Mage';"""
        )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20}\n'.format(row[0])
        print(l)
    Start(_conn)

def Q19(_conn):
    
    sql = (f"""SELECT mu_champ_name, c_nickname, a_eability
                FROM matchups, champion, abilities, skins
                WHERE mu_champ_name = c_name
                    AND c_name = sk_champ_name 
                    AND sk_champ_name = a_champ_name
                    AND good_mu_name = 'Azir'
                GRoup by mu_champ_name, c_nickname;"""
            )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20} {:<30} {:20}\n'.format(row[0], row[1], row[2])
        print(l)
    Start(_conn)

def Q20(_conn):
    
    sql = (f"""SELECT c_name
                FROM champion, type
                WHERE c_name = t_champ_name
                    AND c_difficulty = 'low'
                    AND t_role = 'jungle';"""
        )
    cursor = _conn.cursor()
    cursor.execute(sql)
    _conn.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        l = '{:20}\n'.format(row[0])
        print(l)
    Start(_conn)

def User(_conn):
    print("Here is a list of statistics you can view from (1-20):\n1. What Champion has the highest banrate?\n2. List all the champions and their skins.\n3. Print out each champion and their difficulty.\n4. Print out each champion and their type.")
    print("5. Print out each champion and their passive.\n6. Print out each champion and their good match up.\n7. Print out each champion and their winrate.\n8. Print out the champions with high difficulty.")
    print("9. Print out all the champions that have Star Guardian skins.\n10. Print out all the champions that have a bad match up against Seraphine.\n11. Print the champion and it's r ability if it has a a legendary or ultimate skin.\n12. Print the highest cost of each champion's skins.")
    print("13. Print the nickname of the champions who have a tier S and a good match up with Miss Fortune.\n14. Print the champion name, its role, its q ability, its bad match up, and its pickrate if it's over 3.0 in descending order of the pickrate.")
    print("15. Print out the w ability of all champions whose names start with 'B'.\n16. Print out the champion name of those who has a winrate higher than 50, over 20,000 matches, is a Fighter, has a SKT T1 skin, and is moderate difficulty.")
    print("17. Print how many champions have a Dark Star skin and has a banrate lower than 2.\n18. Print out all the champions who are mages.\n19. Print out the champions that have a good match up against Azir, their nickname, and their e ability.\n20. Print out easiest champions to play that are also junglers.")
    i = input("\nEnter a number(1-20) for which statistic you would like to see: ")

    if i == '1':
        print("What Champion has the highest banrate?\n")
        Q1(_conn)
    elif i == '2':
        print("List all the champions and their skins.\n")
        Q2(_conn)
    elif i == '3':
        print("Print out each champion and their difficulty.\n")
        Q3(_conn)
    elif i == '4':
        print("Print out each champion and their type.\n")
        Q4(_conn)
    elif i == '5':
        print("Print out each champion and their passive.\n")
        Q5(_conn)
    elif i == '6':
        print("Print out each champion and their best match up.\n")
        Q6(_conn)
    elif i == '7':
        print("Print out each champion and their winrate.\n")
        Q7(_conn)
    elif i == '8':
        print("Print out the champions with high difficulty.\n")
        Q8(_conn)
    elif i == '9':
        print("Print out all the champions that have Star Guardian skins.\n")
        Q9(_conn)
    elif i == '10':
        print("Print out all the champions that have a bad match up against Seraphine.\n")
        Q10(_conn)
    elif i == '11':
        print("Print the champion and it's r ability if it has a a legendary or ultimate skin.\n")
        Q11(_conn)
    elif i == '12':
        print("Print the highest cost of each champion's skins.\n")
        Q12(_conn)
    elif i == '13':
        print("Print the nickname of the champions who have a tier S and a good match up with Miss Fortune.\n")
        Q13(_conn)
    elif i == '14':
        print("Print the champion name, its role, its q ability, its bad match up, and its pickrate if it's over 3.0 in descending order of the pickrate.\n")
        Q14(_conn)
    elif i == '15':
        print("Print out the w ability of all champions whose names start with 'B'.\n")
        Q15(_conn)
    elif i == '16':
        print("Print out the champion name of those who has a winrate higher than 50, over 20,000 matches, is a Fighter, has a SKT T1 skin, and is moderate difficulty.\n")
        Q16(_conn)
    elif i == '17':
        print("Print how many champions have a Dark Star skin and has a banrate lower than 2.\n")
        Q17(_conn)
    elif i == '18':
        print("Print out all the champions who are mages.\n")
        Q18(_conn)
    elif i == '19':
        print("Print out the champions that have a good match up against Azir, their nickname, and their e ability.\n")
        Q19(_conn)
    elif i == '20':
        print("Print out easiest champions to play that are also junglers.\n")
        Q20(_conn)
    else:
        User(_conn)

def Start(_conn):
    print("League of Legends Data\n")
    user = input("Enter 'U' for User or 'A' for Admin 'q' to quit: ")
    if user == 'A':
        Admin(_conn)
    elif user == 'U':
        User(_conn)
    elif user == 'q':
        quit()
    else:
        Start(_conn)

def main():
    database = r"LOL.sqlite"

    conn = openConnection(database)
    with conn:
        Start(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
