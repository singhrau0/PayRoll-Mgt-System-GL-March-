import sqlite3

class Employee:
    def empinsert(self,**k):
        conn = sqlite3.connect('pms.db')
        cur = conn.cursor()
        cur.execute(f''' INSERT INTO EMPLOYEE_DETAILS
                    VALUES({k['eid']},"{k['ename']}",{k['dptid']},
                    "{k['designation']}","{k['email']}",{k['contact']},
                    "{k['address']}")
            ''')
        conn.commit()