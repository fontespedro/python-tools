import speedtest

def testar_banda():
    st = speedtest.Speedtest()
    print("Testando a velocidade de download...")
    download_speed = st.download() / 1_000_000 
    print(f"Velocidade de download: {download_speed:.2f} Mbps")

    print("\nTestando a velocidade de upload...")
    upload_speed = st.upload() / 1_000_000 
    print(f"Velocidade de upload: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    testar_banda()

# Lembre-se de instalar o speedtest-cli com pip para utilizar esta biblioteca
