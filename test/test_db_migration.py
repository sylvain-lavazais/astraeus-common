from astraeus_common.io.database import Database

if __name__ == '__main__':
    Database('localhost', '5432', 'astraeus', 'astraeus-db', 'astraeus')
