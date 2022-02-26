from sqlalchemy import create_engine
from lib import (
    connection_uri,
    create_table
)

def create_sales_table():
    '''
        Function used to create an SQL table for inserting our
        veking sales into.
    :return:
    '''
    TABLE_NAME = "sales"

    CREATE_TABLE_QUERY = f"""
                    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                        id INT NOT NULL UNIQUE,
                        price INT NOT NULL,
                        collection INT NOT NULL,
                        buyer VARCHAR (255) NOT NULL,
                        seller VARCHAR (255) NOT NULL,
                        date DATE NOT NULL DEFAULT CURRENT_DATE,
                        nativeid INT NOT NULL UNIQUE
                    )"""

    create_table(CREATE_TABLE_QUERY)

def create_collection_table():
    '''
        Create table for holding full collection with attributes and rank
    :return:
    '''
    TABLE_NAME = "collection"

    CREATE_TABLE_QUERY = f"""
                    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                        nativeid INT NOT NULL UNIQUE,
                        collection INT NOT NULL,
                        background VARCHAR (255) NOT NULL,
                        rune VARCHAR (255) NOT NULL,
                        type VARCHAR (255) NOT NULL,
                        clothes VARCHAR (255) NOT NULL,
                        hair VARCHAR (255) NOT NULL,
                        mouth VARCHAR (255) NOT NULL,
                        headwear VARCHAR (255) NOT NULL,
                        prop VARCHAR (255) NOT NULL
                    )"""

    create_table(CREATE_TABLE_QUERY)
    

def insert_calculation(firstNum, secondNum, answer):
    '''
    Function used to insert our calculation into the DB.
    :param firstNum: first operand of calculation
    :param secondNum: second operand of calculation
    :param answer: calculation answer
    :return: error or success strings for inserting into DB.
    '''
    URI = connection_uri()
    my_connection = None

    try:
        engine = create_engine(URI, echo=True)
        my_connection = engine.connect()

        my_connection.execute('INSERT INTO calculations VALUES (%s, %s, %s)', (firstNum, secondNum, answer))
        return "Insertion successful"

    except exc.SQLAlchemyError as err:
        return 'Error occured inserting into table {}. Exception: {}'.format("calculations", err)

    finally:
        my_connection.close()
        engine.dispose()

