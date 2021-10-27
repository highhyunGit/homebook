'''
Created on 2021. 7. 22.

@author: pc358
'''
import sqlite3
print(sqlite3.version) #버전 확인
#1단계 - connection 획득단계
#isolation_level = None을 지정하는 이유 - 데이터베이스에 커밋없이 반영하기 위해(자동 커밋)
conn = sqlite3.connect("homebook.db")#isolation_level = None
#2단계 - cursor 획득단계
cursor = conn.cursor()
#3단계 - 테이블 만들기
#TEXT,NUMERIC,INTEGER,REAL,BLOB(대용량 바이너리 넣을 때) 등
cursor.execute('''
    CREATE TABLE IF NOT EXISTS HOMEBOOK
        (NO INTEGER PRIMARY KEY AUTOINCREMENT,
        DAY TEXT,
        SECTION TEXT,
        ACCOUNTTITLE TEXT,
        REMARK TEXT,
        REVENUE NUMBER,
        EXPENSE NUMBER)
''')
conn.commit() #isolation_level=None추가하면 이줄 커밋할 필요없음
cursor.close()
conn.close()