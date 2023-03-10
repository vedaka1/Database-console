import psycopg2
from psycopg2.extensions import register_type, UNICODE


elephant = "host='tyke.db.elephantsql.com' port='5432' dbname='zraipbcj' user='zraipbcj' password='UKhLBec43xcfm_dKAqwAGyRN-WVUBR-V'"
rpr = "host='10.163.31.218' port='5432' dbname='rpr' user='kuleshov_v' password='kuleshov_v'"

CONN_STR = elephant
conn = ''
cur = ''

def connection():
    global cur, conn
    try:
        register_type(UNICODE)
        conn = psycopg2.connect(CONN_STR)
        cur = conn.cursor()
    except:
        print('Connection Error')

def print_discipline():
    connection()
    cur.execute('select * from kuleshov_v.discipline')
    dis = cur.fetchall()

    for row in dis:
        print("#--id:", row[0])
        print("#--discipline_name:", row[1])
        print("#--department_name:", row[2])
        print("#--hours_amount:", row[3])
        print("#--control_type:", row[4], "\n")

    cur.close()
    conn.close()


def print_register(text):
    connection()
    cur.execute('select * from kuleshov_v.register')
    text = cur.fetchall()
    cur.close()
    conn.close()
    return text


def add_discipline(discipline_name, department_name, hours_amount,
                   control_type):
    connection()
    cur.callproc(
        'kuleshov_v.add_discipline',
        [discipline_name, department_name, hours_amount, control_type])
    conn.commit()
    cur.close()
    conn.close()


def delete_register(register_id):
    connection()
    cur.callproc('kuleshov_v.delete_register', [register_id])
    conn.commit()
    cur.close()
    conn.close()


def update_register(register_id, mark):
    connection()
    cur.callproc('kuleshov_v.update_register', [register_id, mark])
    conn.commit()
    cur.close()
    conn.close()


def add_register(student_id, discipline_name, teacher_id, mark):
    connection()
    cur.callproc('kuleshov_v.add_register', [student_id, discipline_name, teacher_id, mark])
    conn.commit()
    cur.close()
    conn.close()


def add_custom_query(text):
    conn = psycopg2.connect(CONN_STR)
    cur = conn.cursor()
    cur.execute('%s', (text))
    conn.commit()
    cur.close()
    conn.close()


def run():
    choice = 0
    choices = {
        1:
        lambda: print_discipline(),
        2:
        lambda: add_discipline(
            input('enter discipline_name: '), input('enter department_name: '),
            input('enter amount of hours: '), input('enter control type: ')),
        3:
        lambda: delete_register(input('enter register id: ')),
        4:
        lambda: update_register(input('enter register id: '),
                                input('enter new mark: ')),
        5:
        lambda: print_register(),
        6:
        lambda: add_custom_query(input('enter query: '))
    }
    while (choice != 7):
        print('1. print discipline')
        print('2. add discipline')
        print('3. delete register')
        print('4. update register')
        print('5. print register')
        print('6. add custom query')
        print('7. EXIT')
        print('choose: ')
        choice = int(input())
        if choice in choices:
            choices[choice]()


if __name__ == '__main__':
    run()