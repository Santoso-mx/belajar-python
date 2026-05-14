import time

def pengingat_minum():
    print("--- Pengingat Minum Air ---")
    print("Halo! Jangan lupa minum air ya biar fokus coding.")
    
    # Program ini akan ngingetin tiap 1 jam (3600 detik)
    try:
        while True:
            print(f"Waktunya minum! {time.ctime()}")
            time.sleep(3600) 
    except KeyboardInterrupt:
        print("\nProgram dihentikan.")

if __name__ == "__main__":
    pengingat_minum()