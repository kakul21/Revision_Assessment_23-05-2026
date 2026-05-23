from selenium.webdriver.common.by import By
from Pages.Base_page import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def close_popup(self):
        try:
            from selenium.webdriver.common.action_chains import ActionChains
            ActionChains(self.driver).move_by_offset(0, 0).click().perform()
        except:
            pass

    from_dest = (By.XPATH,"//span[.='From']")
    from_city = (By.XPATH,"(//p[.='Mumbai Chhatrapati Shivaji International Airport'])[1]")
    # from_city = (By.XPATH,"(//div[@class='flex flex-grow items-center']//input)[1]")
    from_airport = (By.XPATH,"(//p[.='Jaipur International Airport'])[1]")
    to_dest = (By.XPATH,"//span[.='To']")
    to_city = (By.XPATH,"(//span[.='GOI'])[2]")
    date = (By.XPATH,"(//button[@class='react-calendar__tile react-calendar__month-view__days__day'])[30]")
    travellers = (By.XPATH,"//p[.='Travellers & Class']")
    no_of_travellers_adult = (By.XPATH,"(//button[@data-testid='3'])[1]")
    select_class = (By.XPATH,"//span[.='Premium Economy']")
    done = (By.XPATH,"//button[.='Done']")
    search_button = (By.XPATH,"//button[.='Search']")

    ## Booking Page
    book_button = (By.XPATH,"//button[.='Book']")
    free_booking_cancellation = (By.XPATH,"(//input[@name='fare-type-selection'])[2]")


    def from_destination(self):
        self.click(self.from_dest)

    def select_from_city(self):
        self.click(self.from_city)
        # self.enter_text(self.from_city,city)
        # self.click(self.from_airport)

    def to_destination(self):
        self.click(self.to_dest)

    def select_to_city(self):
        self.click(self.to_city)

    def select_date(self):
        self.click(self.date)

    def travellers_click(self):
        self.click(self.travellers)
        self.click(self.no_of_travellers_adult)
        self.click(self.select_class)
        self.click(self.done)

    def click_search(self):
        self.click(self.search_button)

    ## Booking Page

    def click_book(self):
        self.click(self.book_button)

    def select_free_booking_cancellation(self):
        self.scroll_to_element(self.free_booking_cancellation)
        self.click(self.free_booking_cancellation)













