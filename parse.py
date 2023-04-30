import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# launch the webdriver
driver = webdriver.Chrome()
driver.get("http://orar.usarb.md/")

# select the date, semester, and week
date_select = Select(driver.find_element(By.ID, 'daySelector'))
date_select.select_by_visible_text('Luni')
semester_select = Select(driver.find_element(By.ID, 'semesterSelector'))
semester_select.select_by_visible_text('2')
week_select = Select(driver.find_element(By.ID, 'weekSelector'))
week_select.select_by_value('11')
group_select = driver.find_element(By.ID, "53")

# get the table rows containing schedule data
table = driver.find_elements(By.ID, 'tableForLesssons')
rows = table[0].find_elements(By.TAG_NAME, 'tr')

# iterate over the rows and extract schedule data
schedule = []
for row in rows:
    cols = row.find_elements(By.TAG_NAME, 'td')
    if len(cols) >= 2:
        time = cols[0].text
        lesson_div = cols[1].find_element(By.CLASS_NAME, 'simple')
        lesson = lesson_div.find_element(By.TAG_NAME, 'strong').text
        p_tags = lesson_div.find_elements(By.TAG_NAME, 'p')
        if len(p_tags) >= 2:
            lesson_type = p_tags[0].text
            teacher = p_tags[1].text
        else:
            lesson_type = ''
            teacher = ''
        location = cols[1].text
        schedule.append({
            'time': time,
            'lesson': lesson,
            'lesson_type': lesson_type,
            'teacher': teacher,
            'location': location
        })

# convert schedule to JSON and print
schedule_json = json.dumps(schedule, ensure_ascii=False, indent=4)
print(schedule_json)

# close the webdriver
driver.quit()
