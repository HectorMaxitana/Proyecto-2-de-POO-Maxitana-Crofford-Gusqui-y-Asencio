import sys

import pyodbc as bd

# --INTEGRANTES--
# CROFFORD VILLAO FREDDY DARWIN
# ASENCIO MADESCO CARLOS ALEXIS
# GUSQUI PALLO MELANIE ANABEL
# MAXITANA MOREIRA HECTOR ALFREDO

class Conexion:
    """
    Clase que permite abrir conexion a la BBDD y abrir cursor.
    """
    _SERVIDOR = 'AlFREDO-MAXI'
    _BBDD = 'APP_POO_C2'
    _USUARIO = 'MAXIALF'
    _PASSWORD = 'sa'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        """
        Obtiene la conexion a la BBDD con los parametros de conexion pasados como constantes
        :return:
        """
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                           cls._SERVIDOR + ';DATABASE=' + cls._BBDD + ';UID=' + cls._USUARIO + ';PWD=' + cls._PASSWORD)
                # log.debug(f'Conexión exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                # log.error(f'Ocurrió una excepción al obtener la conexión: {e}')
                print(e)
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        """
        Obtiene el cursor que
        :return:
        """
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                # log.debug(f'Se abrió correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                # log.error(f'Ocurrió una excepción al obtener el cursor: {e}')
                print(e)
                sys.exit()
        else:
            return cls._cursor

if __name__ == '__main__':
    print(Conexion.obtenerConexion())
    print(Conexion.obtenerCursor())