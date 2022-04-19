

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TraverseSite:
<<<<<<< HEAD
    def __init__(self, loginLink, libraryLink):
        self.l1 = loginLink
        self.l2 = libraryLink
        self.smallRooms=['311', '317', '318', '319', '327', '348', '349', '383', '384', '385', '386', '389', '390', '391', '392', '403', '404', '411', '412', '413', '414', '415', '416', '417', '418', '422', '424', '426', '427']
        self.largeRooms=['387', '402', '405', '425']
=======
    """
    Traverses the library's website

    . . .

    Attributes
    ----------
    link: str
        The URL to the library website
    driver: selenium.webdriver
        A Chrome webdriver instance

    Methods
    ----------
    bookRoom(dateStringPath: str, userN: str, passW: str)
        Attempts to book the requested room with the credentials provided

    findRoom(dateTime: str)
        Goes to the charles website and see what rooms are available and return one for the booking.
        Usually first room available at the specified time/date

    """
    def __init__(self, link: str):
        """
        Creates an instance of the TraverseSite class

        . . .

        Parameters
        ----------
        link: str
            The URL to the library website
        """
        self.link = link
>>>>>>> main
        self.service = Service(executable_path=ChromeDriverManager().install())
        chromeOptions = Options()
        chromeOptions.headless = True
        self.driver = webdriver.Chrome(service=self.service, options = chromeOptions)

<<<<<<< HEAD
    def bookRoom(self, bookings, userN, passW):
        successfulBookings=[]
        self.login(userN, passW)

        for i in bookings:
            dateTime, size = i.split('+')
            newLink = f"{self.l2}{size}"
            self.driver.get(newLink)
            rooms = self.smallRooms if size=='small' else self.largeRooms
            j=0
            foundRoom=False
            while(j<len(rooms) and not foundRoom):
                try: 
                    currentRoom = rooms[j]
                    dateString = (f"//a[@aria-label='{dateTime} - {currentRoom} - Available']")
                    timeOption = self.driver.find_element(By.XPATH, dateString)
                    print(f"\nAttempting to book room {currentRoom}.")

                    foundRoom = self.firstAvailable(dateString)
                except:
                    pass
                j+=1

            if(foundRoom):
                print(f"\nSUCCESS : Booked a {size} room for {dateTime}")
                successfulBookings.append(i)
            else:
                print(f"\nFAILURE : Couldn't book a {size} room for {dateTime}")

        return successfulBookings
    
                    

    def firstAvailable(self,dateStringPath):
=======
    def bookRoom(self, dateStringPath, userN, passW):
        """
        Attempts to book the requested room with the credentials provided

        . . .

        Parameters
        ----------
        dateStringPath: str
            The date of the booking as a string
        userN: str
            The username of the person booking the room
        passW: str
            The password of the user booking the room

        Returns
        ----------
        True if successful, otherwise False
        """
        self.driver.get(self.link)
>>>>>>> main
        try:
            timeOption = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, dateStringPath)))
            timeOption.click()
        except:
            print("Room Unavailable/Doesn't Exist")
            return False

        # Continue Booking
        try:
            continueButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='submit_times']")))
            continueButton.click()
        except:
            print("Couldn't continue booking")
            return False

        try:
            # Submit Booking
            submitButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='s-lc-eq-bform-submit']")))
            submitButton.click()
        except:
            print("Booking Failure")
            return False
        
        try:
            errorPopUp = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='submit-errors']")))
            # submit-errors
            print("Booking Couldn't be made. Another booking was already made for this day.")
            return False
        except:
            print("Booking Success")
            
        return True

    def login(self,userN, passW):
        self.driver.get(self.l1)
        try:
            # Log in  
            userInput = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='username']")))
            userInput.click()
            userInput.send_keys(userN)

            passInput =  WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
            passInput.click()
            passInput.send_keys(passW)
            
            logInButton = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default btn-login']")))
            logInButton.click()
        except:
            print("Login Failure")
            return False

        return True

<<<<<<< HEAD
=======
    def findRoom(self, dateTime):
        """
        Go to the charles website and see what rooms are available and return one for the booking.
        Usually first room available at the specified time/date

        . . .

        Parameters
        ----------
        dateTime: str
            The date of the booking as a string

        Returns
        ----------
        A string with room information if it exists, else None
        """

        rooms = []
        grabRoom = False
        roomIndex = 0
        currentRoom = ""

        self.driver.get(self.link)
        try:
            error = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[@class='fc-cell-text']")))
        except:
            print("ERROR NO ELEMENTS LOADED OR DONT EXIST")

        # Fetch all elements with the XPATH "//span..." -> Retrieve all the room numbers, stored in rooms list
        elements = self.driver.find_elements(by=By.XPATH, value="//span[@class='fc-cell-text']")
        for i in elements:
            rooms.append(i.text[0:3])


        # Loop through rooms list and find a room that is 'available'
        while(not grabRoom and roomIndex < len(rooms)):
            try:
                currentRoom = rooms[roomIndex]
                dateString = (f"//a[@aria-label='{dateTime} - {currentRoom} - Available']")
                timeOption = self.driver.find_element(By.XPATH, dateString)
                print("Room " + currentRoom + " is available")
                grabRoom = True
                return dateString
            
            except:
                print("Room " + currentRoom + " is not available")
                roomIndex = roomIndex + 1
        return None

>>>>>>> main
