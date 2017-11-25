from selenium import webdriver
import unittest


CNT_OF_TASKS = 5
WAITING_TIME = 30
JQ_URL = "http://code.jquery.com/jquery-1.11.2.min.js"

class AtomicBoard(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.get("http://atomicboard.devman.org/create_test_user/")
        self.driver.find_element_by_css_selector(
                                                 'button[type="submit"]').click()
        self.driver.get("http://atomicboard.devman.org/#/")


    def test_load_and_display_tasks(self):
        driver = self.driver
        driver.implicitly_wait(WAITING_TIME)
        tasks = driver.find_elements_by_css_selector('span.'
                                                     'panel-heading_text.js-panel-heading_text.ng-scope.ng-binding.editable')
        self.assertEqual(CNT_OF_TASKS, len(tasks))


    def test_updated_one_of_current_task(self):
        driver = self.driver
        driver.implicitly_wait(WAITING_TIME)
        target_task = driver.find_element_by_css_selector('span.'
                                                          'panel-heading_text.js-panel-heading_text.ng-scope.ng-binding.editable')
        target_task.click()
        current_task = driver.find_element_by_css_selector('input.'
                                                           'editable-has-buttons.editable-input.form-control.ng-pristine.ng-valid')
        current_task.clear()
        current_task.send_keys("Updated_task")
        driver.find_element_by_css_selector('button.btn.btn-primary').click()
        self.assertEqual(u'Updated_task', target_task.text)


    def test_close_a_task(self):
        driver = self.driver
        driver.implicitly_wait(WAITING_TIME)
        closed_task = driver.find_element_by_css_selector('span.'
                                                          'badge.ticket_status.ng-binding')
        self.assertEqual(u'open', closed_task.text)
        closed_task.click()
        driver.find_element_by_css_selector('button.'
                                            'btn.btn-lg.btn-primary.change-status-form__button').click()
        self.assertEqual(u'closed', closed_task.text)


    def test_add_a_new_task(self):
        driver = self.driver
        driver.implicitly_wait(WAITING_TIME)
        driver.find_element_by_css_selector('div.'
                                            'well.well-sm.add-ticket-block').click()
        driver.find_element_by_css_selector('span.add-ticket-block_button.'
                                            'ng-scope.ng-pristine.ng-valid.editable.editable-empty').click()
        driver.find_element_by_css_selector('input.editable-has-buttons.'
                                            'editable-input.form-control.ng-pristine.ng-valid').send_keys("A_new_tesk")
        driver.find_element_by_css_selector('button.btn.btn-primary').click()
        new_task = driver.find_elements_by_css_selector('span.panel-heading_text.'
                                                        'js-panel-heading_text.ng-scope.ng-binding.editable')[1]
        self.assertEqual(u'A_new_tesk', notify_text.text)


    def test_drag_and_drop(self):
        """
        How to simulate HTML5 drag_and_drop in selenium.
        HTML5 "drag&drop" is not currently supported by Selenium
        One of the suggested workarounds is to simulate HTML5 drag and 
        drop via JavaScript:
        1)download drag_and_drop_helper.js
        2)execute the script via execute_script() calling simulateDragDrop()
        function on a source element passing the target element as a dropTarget
        3)It requires dynamically load jQuery for this  purpose we will use
         jquery_load_helper.js
        """
        driver = self.driver
        driver.implicitly_wait(WAITING_TIME)
        week_tasks=driver.find_elements_by_css_selector('span.'
                                                        'col-md-4.tickets-column.js-tickets-column.ng-scope')[1]
        count_tasks = len(week_tasks.find_elements_by_css_selector('span.'
                                                                   'badge.ticket_status.ng-binding'))
        # The jquery_load_helper.js was taken from source https://sqa.stackexchange.com/questions/2921/
        with open("jquery_load_helper.js") as f:
            load_jquery_js = f.read()
        # The drag_and_drop_helper.js was taken from source https://gist.github.com/rcorreia/2362544  
        with open("drag_and_drop_helper.js") as f:
            drag_and_drop_js = f.read()
        driver.execute_async_script(load_jquery_js, JQ_URL)
        driver.execute_script(drag_and_drop_js + ('$("div.js-ticket:eq(0)").'
                                                  'simulateDragDrop(''{dropTarget: "span.tickets-column:eq(1)"});'))
        updated_week_tasks = driver.find_elements_by_css_selector('span.'
                                                                  'col-md-4.tickets-column.js-tickets-column.ng-scope')[1]
        updated_count_tasks = len(updated_week_tasks.find_elements_by_css_selector(
                                                                          'span.badge.ticket_status.ng-binding'))
        self.assertEqual(count_tasks+1, updated_count_tasks)


if __name__ == '__main__':
    unittest.main()