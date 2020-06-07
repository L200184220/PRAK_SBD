import mysql.connector

cnx = mysql.connector.connect(user="root", database="perbankan")
cursor = cnx.cursor()

hapus_nasabah = ("DELETE FROM nasabah WHERE nama_nasabah LIKE 'Putri Febiana'")
cursor.execute(hapus_nasabah)

tambah_nasabah = ("INSERT INTO nasabah(id_nasabah, nama_nasabah, alamat_nasabah)"
                  "VALUES (%s, %s, %s)")
data_nasabah = (21, "Putri Febiana", "Jl. Cendrawasih 18")
cursor.execute(tambah_nasabah, data_nasabah)

update_nasabah = ("UPDATE nasabah SET alamat_nasabah = %s WHERE nama_nasabah = %s")
data_nasabah = ("Jl. Elang 12", "Putri Febiana")
cursor.execute(update_nasabah, data_nasabah)

cnx.commit()
cursor.close()
cnx.close()
