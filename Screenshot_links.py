from selenium import webdriver

def find_link(url_file):
    list_links = []
    for tupp in url_file:
        #print(tupp)
        stt = tupp[2:-2].split()
        linkk = stt[0]
        link=linkk[:-2]
        #if link:
        list_links.append(link)

    return list_links


if __name__ == '__main__':
    with open("C:\\Users\\sidharth.m\\Desktop\\Files\\VB  Analysis\\Dido Events.txt", 'r') as f:
        file = f.readlines()
    #print(file)

    nnn = find_link(file)
    print(nnn)

    i = 1

    for link in range(len(nnn)):

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.binary_location = "C:\\Users\\sidharth.m\\Desktop"
        driver = webdriver.Chrome(executable_path='C:\\Users\\sidharth.m\\Desktop\\chromedriver.exe')

        driver.get(nnn[link])
        driver.save_screenshot("C:\\Users\\sidharth.m\\Desktop\\screenshot"+str(i)+".png")

        driver.close()

        i = i+1
