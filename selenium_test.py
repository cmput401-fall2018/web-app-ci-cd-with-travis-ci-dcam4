from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def test_home():
    options = Options()
    options.add_argument("--no--sandbox")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("http://162.246.157.152:8000")
    
    name = driver.find_element_by_id("name")
    about = driver.find_element_by_id("about")
    education = driver.find_element_by_id("education")
    skills = driver.find_element_by_id("skills")
    work = driver.find_element_by_id("work")
    contact = driver.find_element_by_id("contact")
    

    assert name != None
    assert about != None
    assert education != None
    assert skills != None
    assert work != None
    assert contact != None
    
    # assert name.text == "Dan Cam"
    # assert about.text == "I like coding and I like video games"
    # assert education.text == "University of Alberta"
    # assert skills.text == "Immaculate hand-eye coordination and obscure trivia"
    # assert work.text == "University of Alberta Hospital"
    # assert contact.text == "dcam@ualberta.ca"
    
    #asdasd
    
    driver.close()

    
test_home()
