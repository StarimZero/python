from dao import db

def list():
  try:
    with db.connection.cursor() as cursor:
      sql = "select *, date_format(bbs_regDate, '%Y-%m-%d %T') fmtdate from bbs order by bbs_id desc"
      cursor.execute(sql)
      rows = cursor.fetchall()
      return rows
  except Exception as err:
    print('목록오류:', err)
  finally:
    cursor.close()


def insert(bbs):
    try:
      with db.connection.cursor() as cursor:
        sql = "insert into bbs (bbs_title, bbs_contents, bbs_writer) \
                values(%s, %s, %s)"
        cursor.execute(sql, (bbs.get('title'), bbs.get('contents'), bbs.get('uid')))
        db.connection.commit()
        return 'success'
    except Exception as err:
      print('글쓰기오류 : ', err)
      return 'fail'
    finally:
      cursor.close()
  

def read(bbs_id):
  try:
    with db.connection.cursor() as cursor:
      sql="select *, date_format(bbs_regDate, '%%Y-%%m-%%d %%T') fmtdate from bbs where bbs_id = '%s' order by bbs_id desc "
      cursor.execute(sql, bbs_id)
      row = cursor.fetchone()
      return row
  except Exception as err:
    print("읽기오류: ", err)
  finally:
    cursor.close();
  

def delete(bid):
    try:
        with db.connection.cursor() as cursor:
            sql ="delete from bbs where bbs_id='%s'"
            cursor.execute(sql, bid)
            db.connection.commit()
            return 'success'
    except Exception as err:
        print('글삭제오류 : ', err)
        return 'fail'
    finally:
        cursor.close()