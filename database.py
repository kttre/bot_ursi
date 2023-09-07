import sqlite3


def register_db(id_client, isu_number, role):
    with sqlite3.connect("Bot_ursi.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""INSERT or REPLACE INTO tClient VALUES (?, ?, ?)""", (id_client, isu_number, role))
        cursor.close()
        connection.commit()


#что-то, что не работает и уже не нужно, но пусть останется
def get_markup(id_client):
    with sqlite3.connect("Bot_ursi.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT RoleMember FROM tMemberShip WHERE idСlient = {id_client}')
        record = cursor.fetchone()
        cursor.close()
        connection.commit()
    return record


def get_id_club(isu_num):
    with sqlite3.connect("Bot_ursi.db") as connection:
        cursor = connection.cursor()
        final = True
        record = [0]
        try:
            cursor.execute(f'SELECT idClient FROM tClient WHERE ISUNumber = {isu_num}')
            id_lead = cursor.fetchone()
            cursor.execute(f"SELECT idClub FROM tMemberShip WHERE idClient = ? AND RoleMember = ?", (id_lead[0], "руководитель"))
            record = cursor.fetchone()
            cursor.execute("UPDATE tMemberShip SET RoleMember = ? WHERE idClient = ?", ("участник", id_lead[0]))
        except Exception:
            final = False
        finally:
            cursor.close()
            connection.commit()
        return record[0], final


def change_lead_club(isu_num, id_club):
    with sqlite3.connect("Bot_ursi.db") as connection:
        cursor = connection.cursor()
        final = True
        try:
            cursor.execute(f'SELECT idClient FROM tClient WHERE ISUNumber = {isu_num}')
            id_new_lead = cursor.fetchone()
            cursor.execute("UPDATE tMemberShip SET RoleMember = ? WHERE idClient = ? AND idClub = ?",
                       ("руководитель", id_new_lead[0], id_club))
        except Exception:
            final = False
        finally:
            cursor.close()
            connection.commit()
        return final


def close_club(club_name):
    with sqlite3.connect("Bot_ursi.db") as connection:
        cursor = connection.cursor()
        final = True
        try:
            cursor.execute(f"SELECT idClub FROM tClub WHERE NameClub = '{club_name}'")
            id_club = cursor.fetchone()
            cursor.execute("UPDATE tClub SET OpenClub = ? WHERE idClub = ?",
                            (0, id_club[0]))
        except Exception:
            final = False
        finally:
            cursor.close()
            connection.commit()
        return final


def admin_of_clubs(id_client):
    with sqlite3.connect("Bot_ursi.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f'SELECT idClub FROM tMemberShip WHERE idClient = {id_client} AND RoleMember = "руководитель"')
        record = cursor.fetchall()
        club_names = []
        for id_club in record:
            cursor.execute(f'SELECT NameClub FROM tClub WHERE idClub = {id_club[0]} AND OpenClub = 1')
            club_names.append((cursor.fetchone())[0])
        cursor.close()
        connection.commit()
    return club_names
