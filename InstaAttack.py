#python 3.7.1

# w = write mode / mode menulis dan menghapus file Lama, jika file tidak ada maka akan dibuat file baru
# r read mode only / hanya bisa baca
# a = appending mode / menambahkan data di akhir baris
# r = write and read mode

try :
  import subprocess
  import os
  import time

  def main() :
    try :
      print ("Running ...")
      time.sleep (4)
      print ("Copyright (c) 2019 Todidiang@gmail.com, Ruben A.Y.")
      time.sleep (3)
      print ("Hai\nWelcome to InstaHack")
      time.sleep (3)
      fir = input("Kamu hanya boleh menggunakan tool ini untuk menyerang Cracker/Black hat (Hacker Jahat) [y/n]\n")
      if fir == "y" or fir == "Y" :
        time.sleep (2)
        try :
          nama = input("Masukkan nama Cracker :\n")
          if nama == "Chadompy" or nama == "chadompy" :
            os.system("clear")
            print ("Processing\n")
            time.sleep (3)
            print ("Passwordnya adalah :\nStkGhianza")
            os.system("exit")
          elif nama == "hosea.nath" or nama == "Hosea.nath" or nama == "hosea.Nath" :
              os.system("clear")
              print ("Processing\n")
              time.sleep (3)
              print ("Maaf sepertinya nama yg Anda masukkan salah")
              print ("Connection time out")                                                                                                            
              time.sleep (3)
              os.system("clear")
              time.sleep (1)
              os.system("exit")
          else :
              print ("BrokenSystem")
              time.sleep (2)
              os.system("exit")
        except KeyboardInterrupt :
              print ("Gagal keluar\nKarena kamu langsung control c")
              main()
        except PermissionError :
              print ("File ini tidak memiliki izin")
              main()
        except IndentationError :
              print ("Tidak dapat mengidentifikasi")
              main()
        except SyntaxError :
              print ("Kesalahan Syntax")
              main()
        except EOFError :
              print ("Terjadi kesalahan EOFError\nMungkin terjadi karena kamu melakukan control + d")
              main()
      elif fir == "N" or fir == "n" :
          print ("Ok bye\n")
          time.sleep (0.5)
          os.system("exit")
      elif fir == "keluar" or fir == "Keluar" :
          file = open("code.sh", "w")
          file.write("echo Sedang Memulai Untuk Keluar")
          file.close()
          os.system("sh code.sh")
          time.sleep (3)
          os.system("rm -r code.sh")
          time.sleep (3)
          print ("Bye bye ya ...")
          time.sleep (2)
          os.system("clear")
          time.sleep (2)
          os.system("exit")
      else :
          print ("Ketik yg bener")
          main()
    except KeyboardInterrupt :
          print ("Gagal keluar\nKarena kamu langsung control c")
          main()
    except PermissionError :
          print ("File ini tidak memiliki izin")
          main()
    except IndentationError :
          print ("Tidak dapat mengidentifikasi")
          main()
    except SyntaxError :
          print ("Kesalahan Syntax")
          main()
    except EOFError :
          print ("Terjadi kesalahan EOFError\nMungkin terjadi karena kamu melakukan control + d")
          main()
except KeyboardInterrupt :
      print ("Gagal keluar\nKarena kamu langsung control c")
      main()
except PermissionError :
      print ("File ini tidak memiliki izin")
      main()
except IndentationError :
      print ("Tidak dapat mengidentifikasi")
      main()
except SyntaxError :
      print ("Kesalahan Syntax")
      main()
except EOFError :
      print ("Terjadi kesalahan EOFError\nMungkin terjadi karena kamu melakukan control + d")
      main()
main()
