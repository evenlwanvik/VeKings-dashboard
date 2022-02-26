from sqlalchemy import create_engine


def connection_uri():
    '''
        Get postgresql connection URI
    :return:
    '''
    return "blabla"


def create_table(query):
    '''
        Function used to create an SQL table for inserting our
        veking sales into.
    :return:
    '''

    URI = connection_uri()
    my_connection = None
    
    try:
        engine = create_engine(URI, echo=False)
        my_connection = engine.connect()
        my_connection.execute(query)

        return "Table created successfully"

    except exc.SQLAlchemyError as error:
        return 'Error trying to create table: {}'.format(error)

    finally:
        my_connection.close()
        engine.dispose()