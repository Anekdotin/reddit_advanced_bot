


# Database connections

# databases info
MYSQL_USERNAME = 'root'
MYSQL_PW = 'password'


MYSQL_SERVER = '127.0.0.1:3306'

MYSQL_DBNAME0 = 'reddit_database_comments'
MYSQL_DBNAME1 = 'reddit_database_users'

# Users
SQLALCHEMY_DATABASE_URI_0 = "mysql+pymysql://{}:{}@{}/{}".format(MYSQL_USERNAME,
                                                               MYSQL_PW,
                                                               MYSQL_SERVER,
                                                               MYSQL_DBNAME0)
#  Comments
SQLALCHEMY_DATABASE_URI_1 = "mysql+pymysql://{}:{}@{}/{}".format(MYSQL_USERNAME,
                                                                 MYSQL_PW,
                                                                 MYSQL_SERVER,
                                                                 MYSQL_DBNAME1)


SQLALCHEMY_BINDS = {
    'reddit_database_comments': SQLALCHEMY_DATABASE_URI_0,
    'reddit_database_users': SQLALCHEMY_DATABASE_URI_1,

}

#-------------------------------------------------------------#
customlog = '/home/logs/'
SQLALCHEMY_TRACK_MODIFICATIONS = False
