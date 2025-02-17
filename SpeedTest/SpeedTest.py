import speedtest

def convert_bytes(bytes):
    KB = bytes / 1024
    MB = KB / 1024
    return round(MB, 2)  # rounding to 2 decimal places for better readability

def SPEEStestFunction(): 
    try:
        st = speedtest.Speedtest()
        option = int(input('''What speed do you want to test:   
                           
1) Download Speed   
2) Upload Speed   
3) ALL 

Your Choice: ''')) 
        if option == 1:
            download_speed = st.download()
            MB = convert_bytes(download_speed)
           
            print(f"Download Speed: {MB} MB\n")
        elif option == 2:
            upload_speed = st.upload()
            MB  = convert_bytes(upload_speed)
            print(f"Upload Speed: {MB} MB\n")
        elif option == 3:
            download_speed = st.download()
            upload_speed = st.upload()
            DL_MB = convert_bytes(download_speed)
            UL_MB = convert_bytes(upload_speed)
            print(f"Download Speed: {DL_MB} MB\n")
            print(f"Upload Speed: {UL_MB} MB\n")
            print("ENJOY....☕")
        else:
            print("Invalid Option")
    except speedtest.ConfigRetrievalError:
        print("Error retrieving speedtest configuration. Please check your internet connection or try again later.")
    except Exception as e:
        print(f"An error occurred: {e}")

SPEEStestFunction()
