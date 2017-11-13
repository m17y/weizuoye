import os
from url import Application
import concurrent.futures
from tornado.options import define, options


define("port", default=9878, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="blog database host")
define("mysql_database", default="blog", help="blog database name")
define("mysql_user", default="blog", help="blog database user")
define("mysql_password", default="blog", help="blog database password")
executor = concurrent.futures.ThreadPoolExecutor(2)

class SetApplication(Application):
    def __init__(self):
        settings = dict(
            blog_title=u"Tornado Blog",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            # ui_modules={"Entry": EntryModule},
            # xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/auth/login",
            debug=True,
        )
        super(Application, self).__init__(self.handlers, **settings)
        # Have one global connection to the blog DB across all handlers
        # self.db = torndb.Connection(
        #     host=options.mysql_host, database=options.mysql_database,
        #     user=options.mysql_user, password=options.mysql_password)

        # self.maybe_create_tables()
# A thread pool to be used for password hashing with bcrypt.

    # def maybe_create_tables(self):
    #     try:
    #         self.db.get("SELECT COUNT(*) from entries;")
    #     except MySQLdb.ProgrammingError:
    #         subprocess.check_call(['mysql',
    #                                '--host=' + options.mysql_host,
    #                                '--database=' + options.mysql_database,
    #                                '--user=' + options.mysql_user,
    #                                '--password=' + options.mysql_password],
    #                               stdin=open('schema.sql'))