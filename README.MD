# QA automation
## Final Diploma Project

This is final project on TeachMeSkills QA automation on Python courses for getting
diploma.This project contains UI tests of login, personal cabinet, catalog, cart, comparison page, footer and header
elements. Project can be run with two browsers Chrome and Edge. The design pattern of
this project is Page Object Model. 
and contains the following:

This project is the final assignment for the TeachMeSkills QA Automation course on Python. 
The project contains not only UI-test, but also API tests integration and API tests for https://jsonplaceholder.typicode.com/. The project can be launched in the Chrome browser.The design pattern of this project is Page Object Model and contains the following:

* python package that contains the files with base url and assertions
* python package with locators for pages
* python package with pages (base_page, main_page, basket_page, favorites_page, account_page)
* package test which contains tests for each page
* conftest - file with project settings (pytest fixtures for driver)
* README file with information about the project
* Makefile for easy launch

## A step-by-step guide to installing all the necessary requirements and launching the project.
### 1. Installation

**Clone the repository**:
```bash
git clone https://github.com/parchinskayay/diplom
```
**Go to the project folder**:
```bash
cd diplom
```
**Install the requirements**:
```bash
pip install -r requirements.txt
```

### 2. Running tests

**Run all tests**:
```bash
make test_all
```
**To run tests for a specific page, e.g., the main page**:
```bash
make test_<name_page>
```



Author:<br>
Yuliya Parchynskaya, AQA (Python) Engineer.

Contacts:<br>
email: parchinskayay@gmail.com





 