#!/usr/bin/python
import mysql.connector
import traceback
host = 'localhost'
user = 'root'
password = 'password'
database = 'devpiin'
try:
    mydb = mysql.connector.connect(
      host=host,
      user=user,
      password=password,
      database=database
    )
except Exception, e:
    print(e)
mydb.autocommit = True
#logic
#Flirt and Love -> Date, 168 and 167 -> 166
Flirt = 168
Love = 167
Date = 166
Hangout = 169
flirtnlove = set([Love, Flirt])
datenflirt = set([Date, Flirt])
datenlove = set([Date, Love])
hangoutnflirt = set([Hangout, Flirt])
hangoutnlove = set([Hangout, Love])
table_name = 'preferenceforuser'
def mysql_command(command):
    print(command)
    try:
        cursor = mydb.cursor()
        cursor.execute(command)
    except Exception, e:
        print(e)

def fetch_unique_userids():
    sql = 'select distinct(userid) from ' + table_name
    cursor = mydb.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    return res
def fetch_userinterest_data(userid):
    sql = 'select * from {0} where userid={1}'.format(table_name, userid)
    # print(sql)
    cursor = mydb.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    # for row in cursor:
    #     print(type(row))
    return res

def delete_entry_userinterest(userinterest_pk):
    # print(type(userinterest_pk))
    # if(type(userinterest_pk) == 'int'):
    sql = 'delete from {0} where id = {1} LIMIT 1'.format(table_name, userinterest_pk)
    # else:
    #     sql = 'delete from userinterest where id IN {0} LIMIT {1}'.format(str(userinterest_pk), len(userinterest_pk))
    # print(sql)
    cursor = mydb.cursor()
    cursor.execute(sql)

def update_user_interest(userinterest_pk, staticdataid):
    sql = 'update {0} set staticdataid={1} where id={2} LIMIT 1'.format(table_name, staticdataid, userinterest_pk)
    # print(sql)
    cursor = mydb.cursor()
    cursor.execute(sql)

def add_userinterest(userid, staticdataid):
    sql = 'insert into {0}(userid, staticdataid) values({1}, {2})'.format(table_name, userid, staticdataid)
    cursor = mydb.cursor()
    cursor.execute(sql)

def existing_users_query(userid):
    user_interest = fetch_userinterest_data(userid)
    len_user_interest = len(user_interest)
    to_be_deleted = False
    to_be_updated = False
    if(len_user_interest > 4):
        # staticdataid1 = user_interest[0][2]
        # staticdataid2 = user_interest[1][2]
        # staticdataid3 = user_interest[2][2]
        # staticdataid4 = user_interest[3][2]
        staticdataids = []
        for user_inte in user_interest:
            staticdataids.append(user_inte[2])
        # staticdataids = [staticdataid1, staticdataid2, staticdataid3, staticdataid4]
        if(Date in staticdataids):
            #delete flirt and love
            if(Flirt in staticdataids):
                pkflirt = user_interest[staticdataids.index(Flirt)][0]
                delete_entry_userinterest(pkflirt)

            if(Love in staticdataids):
                pklove = user_interest[staticdataids.index(Love)][0]
                delete_entry_userinterest(pklove)
        else:
            if((Love in staticdataids) and (Flirt in staticdataids)):
                #update one and delete other
                pkflirt = user_interest[staticdataids.index(Flirt)][0]
                pklove = user_interest[staticdataids.index(Love)][0]
                update_user_interest(pkflirt, Date)
                delete_entry_userinterest(pklove)
            elif(Love in staticdataids):
                #update to date
                pklove = user_interest[staticdataids.index(Love)][0]
                update_user_interest(pklove, Date)
            elif(Flirt in staticdataids):
                #update to date
                pkflirt = user_interest[staticdataids.index(Flirt)][0]
                update_user_interest(pkflirt, Date)
            else:
                return
    elif(len_user_interest == 3):
        staticdataid1 = user_interest[0][2]
        staticdataid2 = user_interest[1][2]
        staticdataid3 = user_interest[2][2]
        staticdataids = [staticdataid1, staticdataid2, staticdataid3]
        if(Date in staticdataids):
            #delete flirt and love
            if(Flirt in staticdataids):
                pkflirt = user_interest[staticdataids.index(Flirt)][0]
                delete_entry_userinterest(pkflirt)

            if(Love in staticdataids):
                pklove = user_interest[staticdataids.index(Love)][0]
                delete_entry_userinterest(pklove)
        else:
            if((Love in staticdataids) and (Flirt in staticdataids)):
                #update one and delete other
                pkflirt = user_interest[staticdataids.index(Flirt)][0]
                pklove = user_interest[staticdataids.index(Love)][0]
                update_user_interest(pkflirt, Date)
                delete_entry_userinterest(pklove)
            elif(Love in staticdataids):
                #update to date
                pklove = user_interest[staticdataids.index(Love)][0]
                update_user_interest(pklove, Date)
            elif(Flirt in staticdataids):
                #update to date
                pkflirt = user_interest[staticdataids.index(Flirt)][0]
                update_user_interest(pkflirt, Date)
            else:
                return
    elif(len_user_interest == 4):
        staticdataid1 = user_interest[0][2]
        staticdataid2 = user_interest[1][2]
        staticdataid3 = user_interest[2][2]
        staticdataid4 = user_interest[3][2]
        staticdataids = [staticdataid1, staticdataid2, staticdataid3, staticdataid4]
        if(Date in staticdataids):
            #delete flirt and love
            if(Flirt in staticdataids):
                pkflirt = user_interest[staticdataids.index(Flirt)][0]
                delete_entry_userinterest(pkflirt)

            if(Love in staticdataids):
                pklove = user_interest[staticdataids.index(Love)][0]
                delete_entry_userinterest(pklove)
        else:
            if((Love in staticdataids) and (Flirt in staticdataids)):
                #update one and delete other
                pkflirt = user_interest[staticdataids.index(Flirt)][0]
                pklove = user_interest[staticdataids.index(Love)][0]
                update_user_interest(pkflirt, Date)
                delete_entry_userinterest(pklove)
            elif(Love in staticdataids):
                #update to date
                pklove = user_interest[staticdataids.index(Love)][0]
                update_user_interest(pklove, Date)
            elif(Flirt in staticdataids):
                #update to date
                pkflirt = user_interest[staticdataids.index(Flirt)][0]
                update_user_interest(pkflirt, Date)
            else:
                return


    elif(len_user_interest == 1):# 1 interest
        pk = user_interest[0][0]
        staticdataid = user_interest[0][2]
        if(staticdataid in flirtnlove):
            update_user_interest(pk, Date)
    elif(len_user_interest == 2):# 2 interests
        staticdataid1 = user_interest[0][2]
        staticdataid2 = user_interest[1][2]
        pk1 = user_interest[0][0]
        pk2 = user_interest[1][0]
        userid = user_interest[0][1]
        userinterestids = set([staticdataid1, staticdataid2])

        if(userinterestids == flirtnlove):
            # #delete flirt and love and add date
            # delete_entry_userinterest((pk1, pk2))
            # #create new entry date
            # add_userinterest(userid, Date)
            to_be_deleted = [pk1]
            to_be_updated = [pk2, Date]
        elif(userinterestids == datenflirt):
            if(staticdataid1 == Date):
                to_be_deleted = [pk2]
            else:
                to_be_deleted = [pk1]

        elif(userinterestids == datenlove):
            if(staticdataid1 == Date):
                to_be_deleted = [pk2]
            else:
                to_be_deleted = [pk1]

        elif(userinterestids in [hangoutnlove, hangoutnflirt]):
            #hangout will remain, love/flirt will be updated to date
            if(staticdataid1 == Hangout):
                to_be_updated = [pk2, Date]
            else:
                to_be_updated = [pk1, Date]
        else:
            if(staticdataid1 in flirtnlove):
                to_be_updated = [pk1, Date]
            elif(staticdataid2 in flirtnlove):
                to_be_updated = [pk2, Date]
    if(to_be_deleted != False):
        delete_entry_userinterest(to_be_deleted[0])
    if(to_be_updated != False):
        update_user_interest(to_be_updated[0], to_be_updated[1])

# existing_users_query(6079)

def run_flirtlove_to_date_update():
    userids = fetch_unique_userids()
    for userid in userids:
        existing_users_query(userid[0])
# run_flirtlove_to_date_update()
# table_name = 'userinterest'
# run_flirtlove_to_date_update()

def queries_run():
    try:
        sql1 = "UPDATE `userdetails` SET `job` = ' ' WHERE `job` is null"
        mysql_command(sql1)
        sql2 = "ALTER TABLE `userdetails`CHANGE COLUMN `sexualid` `sexualid` INT(11) NULL DEFAULT NULL ,CHANGE COLUMN `sexualityvisibility` `sexualityvisibility` TINYINT(1) NULL DEFAULT NULL ,CHANGE COLUMN `bodytypeid` `bodytypeid` INT(11) NULL DEFAULT NULL ,CHANGE COLUMN `familyplanid` `familyplanid` INT(11) NULL DEFAULT NULL ,CHANGE COLUMN `kidid` `kidid` INT(11) NULL DEFAULT NULL ,CHANGE COLUMN `job` `job` VARCHAR(128) CHARACTER SET 'utf8mb4' NOT NULL ,CHANGE COLUMN `ethnicityid` `ethnicityid` INT(11) NULL DEFAULT NULL ,CHANGE COLUMN `religionid` `religionid` INT(11) NULL DEFAULT NULL ,CHANGE COLUMN `religionvisibility` `religionvisibility` TINYINT(1) NULL DEFAULT NULL ,CHANGE COLUMN `educationid` `educationid` INT(11) NULL DEFAULT NULL ,CHANGE COLUMN `hairid` `hairid` INT(11) NULL DEFAULT NULL"
        mysql_command(sql2)

        run_flirtlove_to_date_update()
        global table_name
        table_name = 'userinterest'
        run_flirtlove_to_date_update()

        sql3 = "SET FOREIGN_KEY_CHECKS=0"
        sql4 = "Insert into staticdata values(249,20,'Network')"
        sql5 = "SET FOREIGN_KEY_CHECKS=1"
        sql6 = "Delete from staticdata where id=167"
        sql7 = "Delete from staticdata where id=168"
        mysql_command(sql3)
        mysql_command(sql4)
        mysql_command(sql5)
        mysql_command(sql6)
        mysql_command(sql7)
    except Exception, e:
        print(e)

queries_run()

