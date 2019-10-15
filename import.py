# Nama file: import.py

# mengimpor modul intensitas
import intensitas

def main():
    # jarak kecepatan
    v = 2
    t = 6

    jarak = intensitas.jarak(v,t)

    print("jarak kecepatan")
    print("volume\t: ", v)
    print("waktu\t: ", t)
    print("jarak\t= ", jarak)

if __name__ == "__main__":
    main()
    
