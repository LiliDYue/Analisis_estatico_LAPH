from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# =========================
# DRIVER
# =========================
def create_driver():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)

    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )

    return driver


# =========================
# GOOGLE
# =========================
@given("I open Google")
def step_open_google(context):
    context.driver = create_driver()
    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, 10)
    context.driver.get("https://www.google.com")


@when('I search for "{query}"')
def step_search_google(context, query):
    search_box = context.wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)


@when("I click on the first result")
def step_click_first_result(context):
    wait = context.wait

    results = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3"))
    )

    if not results:
        results = context.driver.find_elements(By.XPATH, "//a//h3")

    for result in results:
        try:
            result.click()
            return
        except Exception:
            continue

    raise AssertionError("No clickable search results found")


# =========================
# VALIDAR DOMINIO
# =========================
@then('I should be on "{domain}"')
def step_verify_domain(context, domain):
    context.wait.until(lambda d: domain in d.current_url)
    assert domain in context.driver.current_url


# =========================
# BUSQUEDA EN SITIO
# =========================
@when('I search inside the site for "{query}"')
def step_search_inside_site(context, query):
    driver = context.driver
    wait = context.wait
    current_url = driver.current_url.lower()

    # ITESO
    if "iteso.mx" in current_url:
        try:
            search_input = wait.until(
                EC.presence_of_element_located((By.NAME, "icon-search"))
            )
            search_input.clear()
            search_input.send_keys(query)
            search_input.send_keys(Keys.RETURN)
            return
        except Exception:
            pass

    # UDG
    if "udg.mx" in current_url:
        try:
            button = wait.until(
                EC.element_to_be_clickable((By.NAME, "keys"))
            )
            button.click()

            modal_input = wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "input[type='search'], input[type='text']")
                )
            )

            modal_input.click()
            modal_input.clear()
            modal_input.send_keys(query)
            modal_input.send_keys(Keys.RETURN)
            return
        except Exception:
            pass

    # UNAM
    if "unam.mx" in current_url:
        try:
            search_input = wait.until(
                EC.presence_of_element_located((By.NAME, "search"))
            )
            search_input.clear()
            search_input.send_keys(query)
            search_input.send_keys(Keys.RETURN)
            return
        except Exception:
            pass

    # FALLBACK
    inputs = driver.find_elements(By.CSS_SELECTOR, "input")

    for inp in inputs:
        try:
            inp.clear()
            inp.send_keys(query)
            inp.send_keys(Keys.RETURN)
            return
        except Exception:
            continue


# =========================
# VALIDACION FINAL
# =========================
@then('I should see results related to "{query}"')
def step_validate_results(context, query):
    body = context.driver.page_source.lower()
    url = context.driver.current_url.lower()

    keywords = {
        "carreras": ["carrera", "licenciatura", "oferta", "programa"],
        "admisiones": ["admisión", "ingreso", "aspirante"],
        "posgrados": ["posgrado", "maestría", "doctorado"],
        "investigación": ["investigación", "centro"],
        "convocatoria": ["convocatoria", "registro", "ingreso"],
        "licenciaturas": ["licenciatura", "carrera"],
        "posgrado": ["posgrado", "maestría", "doctorado"],
    }

    if query in keywords:
        found = any(word in body for word in keywords[query]) or \
                any(word in url for word in keywords[query])

        assert found, f"No related content for '{query}'"
    else:
        assert query.lower() in body or query.lower() in url

    context.driver.quit()