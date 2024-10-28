from django.shortcuts import render
from django.conf import settings
from django.db import connections
from django.http import HttpResponse
import psycopg2

# Create your views here.
def index_view(request):
     return render(request,'index.html')



def connect_to_cluster(request, host_ip):
    connection = None
    message = ''
    try:
        # Establish connection to the PostgreSQL server
        connection = psycopg2.connect(
            host=host_ip,
            user="postgres",        # Replace with your PostgreSQL username
            password="potgres",    # Replace with your PostgreSQL password
            port="5432",
            dbname="postgres",     # Adjust port if needed
        )
        cursor = connection.cursor()

        # Check connection status
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        message = f"Connected to PostgreSQL Cluster on {host_ip}. Version: {version[0]}"

    except Exception as e:
        message = f"Error connecting to PostgreSQL cluster on {host_ip}: {e}"
    finally:
        if connection:
            connection.close()

    # Return a response (you can redirect or render a template)
    return render(request, 'options.html',{'message':message})

def db_size(request, host_ip):
    database_sizes=[]
    connection = None
    message = ''
    try:
        # Establish connection to the PostgreSQL server
        connection = psycopg2.connect(
            host=host_ip,
            user="postgres",        # Replace with your PostgreSQL username
            password="potgres",    # Replace with your PostgreSQL password
            port="5432",
            dbname="postgres",   # Adjust port if needed
        )
        cursor = connection.cursor()

        cursor.execute("SELECT datname, pg_size_pretty(pg_database_size(datname)) as size FROM pg_database;")
        database_sizes=cursor.fetchall()

        if not database_sizes:
            message="No databses Found."
        else:
            message="Databases Sizes:"
    except Exception as e:
        message = f"Erroe fetching database sizes: {e}"
    finally:
        if connection:
            connection.close()

    # Return a response (you can redirect or render a template)
    return render(request, 'db_size.html',{'message':message,'database_sizes':database_sizes})

def user_access(request, host_ip):
    access_details=[]
    connection= None
    message=''
    try:
        connection=psycopg2.connect(
                host=host_ip,
                user="postgres",
                password="postgres",
                port="5432",
                dbname="postgres",
            )
        cursor = connection.cursor()

        query="""
        SELECT
            rol.rolname AS role_name,
            rol.rolsuper AS is_superuser,
            rol.rolcreaterole AS can_create_roles,
            rol.rolcreatedb AS can_create_db,
            rol.rolcanlogin AS can_login,
            rol.rolreplication AS can_replicate,
            perm.grantee AS grantee,
            perm.table_catalog AS database,
            perm.table_schema AS schema,
            perm.table_name AS table_name,
            perm.privilege_type AS privilege
        FROM
            pg_roles AS rol
        LEFT JOIN
            information_schema.role_table_grants AS perm
        ON
            rol.rolname = perm.grantee
        ORDER BY
            rol.rolname, perm.table_name;
        """

        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]  # Get column names
        access_details = [dict(zip(columns, row)) for row in cursor.fetchall()]
        #access_details=cursor.fetchall()
        if not access_details:
            message="Unable to detch User Access Details Please check the query"
        else:
            message= f"{len(access_details)} Use Access Details."
    except Exception as e:
            message="Error fetching User Access Details: {e}"
    finally:
        if connection:
            connection.close()

    # Return a response (you can redirect or render a template)
    return render(request, 'user_access.html',{'message':message,'access_details':access_details})

