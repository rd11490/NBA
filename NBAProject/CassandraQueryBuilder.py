__author__ = 'Ryan'


class CassandraQueryBuilder:
    @staticmethod
    def selectFrom(table, columnNames, conditions):
        return CassandraQueryBuilder.selectQueryBuilder(table, columnNames, conditions)

    @staticmethod
    def selectQueryBuilder(table, columnNames, conditions):
        select = "SELECT "
        if columnNames is None:
            select += "*"
        else:
            for c in columnNames:
                select += c + ","
            select = select[:-1]
        select += " FROM {0}".format(table)
        if conditions is None:
            return select + " ALLOW FILTERING"
        else:
            select += " WHERE "
            for c in conditions:
                select += c + " AND "
            return select[:-5] + " ALLOW FILTERING"

    @staticmethod
    def insertInto(table, columns, data):
        return CassandraQueryBuilder.insertQueryBuilder(table, columns, data)

    @staticmethod
    def insertQueryBuilder(table, columns, data):
        insert = "INSERT INTO {0} (".format(table)
        for c in columns:
            insert = insert + c + ", "
        insert = insert[:-2] + ") VALUES ("
        for d in data:
            if isinstance(d, str):
                insert = insert + "$$" + str(d) + "$$, "
            else:
                insert = insert + str(d) + ", "
        insert = insert[:-2] + ")"
        return insert

    @staticmethod
    def insertBatch(table, columns, data):
        insert = 'BEGIN BATCH'
        for d in data:
            insert += " "+CassandraQueryBuilder.insertInto(table, columns, d)
        insert += " APPLY BATCH"
        return insert

    @staticmethod
    def updateQueryBuilder(table, setClause, conditions):
        update = "UPDATE {0} SET {1}".format(table, setClause)
        if conditions is None:
            return update
        else:
            update += " WHERE "
            for c in conditions:
                update += c + " AND "
            return update[:-5]


    @staticmethod
    def checkRowInTable(table, conditions):
        """
        SELECT count(*) FROM TABLE WHERE primary_keys = blah
        :param conditions:
        :param table:
        """
        select = "SELECT COUNT(*) FROM {0}".format(table)
        if conditions is None:
            return select
        else:
            select += " WHERE "
            for c in conditions:
                select += "{0}=\'{1}\' AND ".format(c[0], c[1])
            return select[:-5] + " ALLOW FILTERING"

    @staticmethod
    def inClause(column, list):
        s = "{0} in (".format(column)
        for i in list:
            s += "'{0}',".format(i)
        return s[:-1] + ")"









