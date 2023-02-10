tablename="Bikes"
attribute="ID"
domain="INT"
contraints="PRIMARY KEY (ID)"

print("CREATE TABLE %s"%tablename+"(%s"%attribute+" "+"%s"%domain+" "+"%s)"%contraints)