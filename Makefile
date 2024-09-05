PYTEST=pytest

ALLURE_DIR=allure-results
ALLURE_ALL=allure_all
ALLURE_UI=allure_ui
ALLURE_API=allure_api
ALLURE_ACCOUNT_PAGE=allure_account_page
ALLURE_BASKET_PAGE=allure_basket_page
ALLURE_FAVORITES_PAGE=allure_favorites_page
ALLURE_MAIN_PAGE=allure_main_page

TESTS_API=tests/tests_API
TESTS_UI=tests/tests_UI
TESTS_ACCOUNT=tests/tests_UI/test_account_page.py
TESTS_BASKET=tests/tests_UI/test_basket_page.py
TESTS_FAVORITES=tests/tests_UI/test_favorites_page.py
TEST_MAIN_PAGE=tests/tests_UI/test_main_page.py

test_all:
	@echo Run all tests
	$(PYTEST)

test_api:
	@echo Run all API tests
	$(PYTEST) $(TESTS_API)

test_ui:
	@echo Run all UI tests
	$(PYTEST) $(TESTS_UI)

test_account:
	@echo Run all account page tests
	$(PYTEST) $(TESTS_ACCOUNT)

test_basket:
	@echo Run all basket page tests
	$(PYTEST) $(TESTS_BASKET)

test_favorites:
	@echo Run all favorites page tests
	$(PYTEST) $(TESTS_FAVORITES)

test_main_page:
	@echo Run all main page tests
	$(PYTEST) $(TESTS_MAIN_PAGE)

test_allure_all:
	@echo Run all tests and create allure report
	$(PYTEST) --alluredir=$(ALLURE_DIR)/$(ALLURE_ALL)

test_allure_api:
	@echo Run all API tests and create allure report
	$(PYTEST) --alluredir=$(ALLURE_DIR)/$(ALLURE_API) $(TESTS_API)

test_allure_ui:
	@echo Run all UI tests and create allure report
	$(PYTEST) --alluredir=$(ALLURE_DIR)/$(ALLURE_UI) $(TESTS_UI)

test_allure_account:
	@echo Run all account page tests and create allure report
	$(PYTEST) --alluredir=$(ALLURE_DIR)/$(ALLURE_ACCOUNT_PAGE) $(TESTS_ACCOUNT)

test_allure_basket:
	@echo Run all basket page tests and create allure report
	$(PYTEST) --alluredir=$(ALLURE_DIR)/$(ALLURE_BASKET_PAGE) $(TESTS_BASKET)

test_allure_favorites:
	@echo Run all favorites page tests and create allure report
	$(PYTEST) --alluredir=$(ALLURE_DIR)/$(ALLURE_FAVORITES_PAGE) $(TESTS_FAVORITES)

test_allure_main_page:
	@echo Run all main page tests and create allure report
	$(PYTEST) --alluredir=$(ALLURE_DIR)/$(ALLURE_MAIN_PAGE) $(TESTS_MAIN_PAGE)

report_all:
	@echo Show report all tests
	allure serve $(ALLURE_DIR)/$(ALLURE_ALL)

report_api:
	@echo Show report API tests
	allure serve $(ALLURE_DIR)/$(ALLURE_API)

report_ui:
	@echo Show report UI tests
	allure serve $(ALLURE_DIR)/$(ALLURE_UI)

report_account:
	@echo Show report account page tests
	allure serve $(ALLURE_DIR)/$(ALLURE_ACCOUNT_PAGE)

report_basket:
	@echo Show report basket page tests
	allure serve $(ALLURE_DIR)/$(ALLURE_BASKET_PAGE)

report_favorites:
	@echo Show report favorires page tests
	allure serve $(ALLURE_DIR)/$(ALLURE_FAVORITES_PAGE)

report_main_page:
	@echo Show report main page tests
	allure serve $(ALLURE_DIR)/$(ALLURE_MAIN_PAGE)

clean:
	@echo Clean all allure reports
	rm -rf $(ALLURE_DIR)
